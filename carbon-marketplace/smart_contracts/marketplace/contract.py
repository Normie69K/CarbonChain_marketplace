from algopy import (
    ARC4Contract,
    Asset,
    GlobalState,
    UInt64,
    Account,
    Txn,
    Global,
    arc4,
    itxn,
    op,
    gtxn,
)


class CarbonMarketplace(ARC4Contract):
    """
    Contract 2 — Carbon Credit Marketplace
    NGOs list their NFTs for sale. Companies buy them with ALGO.
    Atomic swap: payment + NFT transfer happen in the same transaction group.
    Platform fee automatically split between seller and admin.
    """

    def __init__(self) -> None:
        self.admin                  = GlobalState(Account)
        self.platform_fee_bps       = GlobalState(UInt64)   # 250 = 2.5%
        self.total_volume_microalgo = GlobalState(UInt64)
        self.total_trades           = GlobalState(UInt64)


    @arc4.abimethod(allow_actions=["NoOp"], create="require")
    def create_marketplace(self, fee_bps: arc4.UInt64) -> None:
        """
        Deploy the marketplace.
        fee_bps: platform fee in basis points. 250 = 2.5%
        """
        self.admin.value                  = Txn.sender
        self.platform_fee_bps.value       = fee_bps.native
        self.total_volume_microalgo.value = UInt64(0)
        self.total_trades.value           = UInt64(0)


    @arc4.abimethod
    def list_credit(
        self,
        asset_id:        arc4.UInt64,
        price_microalgo: arc4.UInt64,
        co2_tonnes:      arc4.UInt64,
        vintage_year:    arc4.UInt64,
        project_type:    arc4.String,
    ) -> None:
        """
        NGO lists a carbon credit NFT for sale.

        Call as atomic group:
            [0] AssetTransfer — seller sends NFT to this contract (amount = 1)
            [1] AppCall       — this method

        Contract holds NFT in escrow until sold or cancelled.
        """
        assert price_microalgo.native > UInt64(0), "Price must be > 0"
        assert Txn.group_index > UInt64(0), "Must be in atomic group"

        # Verify the previous txn sent the NFT to this contract
        prev = gtxn.AssetTransferTransaction(Txn.group_index - UInt64(1))
        assert prev.asset_receiver == Global.current_application_address, "NFT must go to contract"
        assert prev.xfer_asset.id  == asset_id.native, "Wrong asset ID"
        assert prev.asset_amount   == UInt64(1), "Must send exactly 1 NFT"
        assert prev.sender         == Txn.sender, "Sender mismatch"

        # Box layout:
        # asset_id(8) | seller(32) | price(8) | co2(8) | vintage(8) | timestamp(8) | active(8)
        # Total: 80 bytes
        op.Box.put(
            op.itob(asset_id.native),
            op.itob(asset_id.native)         +   # offset 0  — 8 bytes
            Txn.sender.bytes                 +   # offset 8  — 32 bytes
            op.itob(price_microalgo.native)  +   # offset 40 — 8 bytes
            op.itob(co2_tonnes.native)       +   # offset 48 — 8 bytes
            op.itob(vintage_year.native)     +   # offset 56 — 8 bytes
            op.itob(Global.latest_timestamp) +   # offset 64 — 8 bytes
            op.itob(UInt64(1)),                  # offset 72 — 8 bytes (active=1)
        )


    @arc4.abimethod
    def buy_credit(self, asset_id: arc4.UInt64) -> None:
        """
        Company purchases a listed carbon credit.

        Call as atomic group:
            [0] Payment  — buyer pays exact listing price to this contract
            [1] AppCall  — this method

        Contract automatically:
            1. Pays seller  (price minus platform fee)
            2. Pays admin   (platform fee)
            3. Transfers NFT to buyer
        """
        assert Txn.group_index > UInt64(0), "Must be in atomic group"

        # Load listing from box — Box.get returns (value, exists)
        box_value, box_exists = op.Box.get(op.itob(asset_id.native))
        assert box_exists, "Listing not found"

        seller = Account(op.extract(box_value, 8,  32))
        price  = op.btoi(op.extract(box_value, 40, 8))
        active = op.btoi(op.extract(box_value, 72, 8))

        assert active == UInt64(1), "Listing is not active"

        # Verify the payment transaction
        pay = gtxn.PaymentTransaction(Txn.group_index - UInt64(1))
        assert pay.sender   == Txn.sender,                              "Payment sender mismatch"
        assert pay.receiver == Global.current_application_address,      "Payment must go to contract"
        assert pay.amount   == price,                                   "Payment must match listing price"

        # Calculate fee split
        platform_fee  = (price * self.platform_fee_bps.value) // UInt64(10000)
        seller_payout = price - platform_fee

        # Pay seller
        itxn.Payment(
            receiver = seller,
            amount   = seller_payout,
            fee      = Global.min_txn_fee,
        ).submit()

        # Pay platform fee to admin
        if platform_fee > UInt64(0):
            itxn.Payment(
                receiver = self.admin.value,
                amount   = platform_fee,
                fee      = Global.min_txn_fee,
            ).submit()

        # Transfer NFT to buyer
        itxn.AssetTransfer(
            xfer_asset     = Asset(asset_id.native),
            asset_receiver = Txn.sender,
            asset_amount   = 1,
            fee            = Global.min_txn_fee,
        ).submit()

        # Mark listing as sold — keep first 72 bytes, set active = 0
        op.Box.put(
            op.itob(asset_id.native),
            op.extract(box_value, 0, 72) + op.itob(UInt64(0)),
        )

        self.total_volume_microalgo.value = self.total_volume_microalgo.value + price
        self.total_trades.value           = self.total_trades.value + UInt64(1)


    @arc4.abimethod
    def cancel_listing(self, asset_id: arc4.UInt64) -> None:
        """
        Seller cancels their listing and retrieves the NFT.
        Only the original seller can cancel.
        """
        box_value, box_exists = op.Box.get(op.itob(asset_id.native))
        assert box_exists, "Listing not found"

        seller = Account(op.extract(box_value, 8,  32))
        active = op.btoi(op.extract(box_value, 72, 8))

        assert Txn.sender == seller, "Only seller can cancel"
        assert active     == UInt64(1), "Listing not active"

        # Return NFT to seller
        itxn.AssetTransfer(
            xfer_asset     = Asset(asset_id.native),
            asset_receiver = seller,
            asset_amount   = 1,
            fee            = Global.min_txn_fee,
        ).submit()

        # Mark inactive
        op.Box.put(
            op.itob(asset_id.native),
            op.extract(box_value, 0, 72) + op.itob(UInt64(0)),
        )


    @arc4.abimethod(readonly=True)
    def get_listing(
        self,
        asset_id: arc4.UInt64,
    ) -> tuple[arc4.Address, arc4.UInt64, arc4.UInt64, arc4.UInt64]:
        """
        Get details of a listing.
        Returns: (seller, price_microalgo, co2_tonnes, active)
        active: 1 = for sale, 0 = sold or cancelled
        """
        box_value, box_exists = op.Box.get(op.itob(asset_id.native))
        assert box_exists, "Listing not found"

        return (
            arc4.Address(op.extract(box_value, 8,  32)),
            arc4.UInt64(op.btoi(op.extract(box_value, 40, 8))),
            arc4.UInt64(op.btoi(op.extract(box_value, 48, 8))),
            arc4.UInt64(op.btoi(op.extract(box_value, 72, 8))),
        )


    @arc4.abimethod(readonly=True)
    def get_stats(self) -> tuple[arc4.UInt64, arc4.UInt64]:
        """Returns (total_volume_algo, total_trades)."""
        return (
            arc4.UInt64(self.total_volume_microalgo.value // UInt64(1_000_000)),
            arc4.UInt64(self.total_trades.value),
        )