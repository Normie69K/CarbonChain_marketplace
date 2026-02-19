from algopy import (
    ARC4Contract,
    Asset,
    GlobalState,
    LocalState,
    UInt64,
    Bytes,
    Account,
    Txn,
    Global,
    arc4,
    itxn,
    op,
)


class CreditIssuanceRegistry(ARC4Contract):
    """
    Contract 1 — Credit Issuance Registry
    NGOs register here, admin verifies them, then they mint carbon credit NFTs.
    """

    def __init__(self) -> None:
        self.admin                = GlobalState(Account)
        self.total_credits_issued = GlobalState(UInt64)

        self.issuer_verified      = LocalState(UInt64)
        self.issuer_credits       = LocalState(UInt64)
        self.issuer_name          = LocalState(Bytes)
        self.issuer_standard      = LocalState(Bytes)


    @arc4.abimethod(allow_actions=["NoOp"], create="require")
    def create_registry(self) -> None:
        """Deploy the registry. Caller becomes admin."""
        self.admin.value = Txn.sender
        self.total_credits_issued.value = UInt64(0)


    @arc4.abimethod
    def register_issuer(
        self,
        name: arc4.String,
        country: arc4.String,
        verification_standard: arc4.String,
    ) -> None:
        """
        NGO registers as a credit issuer.
        Status starts as unverified (0) until admin approves.
        Caller must opt into this app first.
        """
        self.issuer_name[Txn.sender]     = name.bytes
        self.issuer_standard[Txn.sender] = verification_standard.bytes
        self.issuer_verified[Txn.sender] = UInt64(0)
        self.issuer_credits[Txn.sender]  = UInt64(0)


    @arc4.abimethod
    def verify_issuer(self, issuer: arc4.Address) -> None:
        """Admin approves an NGO so they can mint credits."""
        assert Txn.sender == self.admin.value, "Admin only"
        self.issuer_verified[issuer.native] = UInt64(1)


    @arc4.abimethod
    def mint_carbon_credit(
        self,
        project_id:   arc4.String,
        project_name: arc4.String,
        location:     arc4.String,
        co2_tonnes:   arc4.UInt64,
        vintage_year: arc4.UInt64,
        project_type: arc4.String,
        ipfs_hash:    arc4.String,
    ) -> arc4.UInt64:
        """
        Verified NGO mints a carbon credit as an Algorand NFT (ASA).
        - Total supply = 1  (true NFT)
        - Unit name    = CCT (Carbon Credit Token)
        - Duplicate project IDs are rejected
        Returns: ASA ID of the new NFT
        """
        assert self.issuer_verified[Txn.sender] == UInt64(1), "Issuer not verified"
        assert co2_tonnes.native > UInt64(0), "Must represent CO2"
        assert vintage_year.native >= UInt64(2000), "Invalid vintage year"

        # Reject duplicate project IDs
        # Box.get returns (value, exists)
        box_value, box_exists = op.Box.get(project_id.bytes)
        assert not box_exists, "Project ID already exists"

        # Create the NFT on Algorand
        asset_txn = itxn.AssetConfig(
            total          = 1,
            decimals       = 0,
            unit_name      = b"CCT",
            asset_name     = project_name.bytes,
            url            = b"ipfs://" + ipfs_hash.bytes,
            manager        = Global.current_application_address,
            reserve        = Txn.sender,
            freeze         = Global.current_application_address,
            clawback       = Global.current_application_address,
            default_frozen = False,
            fee            = Global.min_txn_fee,
        ).submit()

        asset_id = asset_txn.created_asset.id

        # Store metadata in box storage
        # Layout: asset_id(8) | co2_tonnes(8) | vintage_year(8) | timestamp(8)
        op.Box.put(
            project_id.bytes,
            op.itob(asset_id)                 +
            op.itob(co2_tonnes.native)         +
            op.itob(vintage_year.native)       +
            op.itob(Global.latest_timestamp),
        )

        self.issuer_credits[Txn.sender]  = self.issuer_credits[Txn.sender] + UInt64(1)
        self.total_credits_issued.value  = self.total_credits_issued.value  + UInt64(1)

        return arc4.UInt64(asset_id)


    @arc4.abimethod(readonly=True)
    def get_credit_asset_id(self, project_id: arc4.String) -> arc4.UInt64:
        """Returns the ASA ID for a given project ID."""
        box_value, box_exists = op.Box.get(project_id.bytes)
        assert box_exists, "Project not found"
        return arc4.UInt64(op.btoi(op.extract(box_value, 0, 8)))


    @arc4.abimethod(readonly=True)
    def get_issuer_stats(
        self,
        issuer: arc4.Address,
    ) -> tuple[arc4.UInt64, arc4.UInt64]:
        """Returns (is_verified, credits_issued) for a given NGO."""
        return (
            arc4.UInt64(self.issuer_verified[issuer.native]),
            arc4.UInt64(self.issuer_credits[issuer.native]),
        )


    @arc4.abimethod(readonly=True)
    def get_total_issued(self) -> arc4.UInt64:
        """Returns total credits ever minted."""
        return arc4.UInt64(self.total_credits_issued.value)