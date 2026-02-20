# 🌿 CarbonChain Marketplace

## 📖 Project Description

CarbonChain Marketplace is a decentralized, transparent, and immutable platform for issuing, trading, and retiring carbon credits, built entirely on the Algorand blockchain. Traditional carbon markets suffer from opacity, double-counting, and high intermediary fees. CarbonChain solves this by leveraging Algorand's high-speed, low-cost infrastructure and the **AlgoKit** development framework to create a trustless ecosystem where businesses can offset their carbon footprint with verifiable on-chain proof.

## 🎯 Problem Statement Selected

**Category:** Carbon credits / sustainability tracking (Open Innovation Track)
**Problem:** The global carbon credit market lacks end-to-end traceability, leading to "greenwashing" and the double-spending of retired credits.
**Solution:** A suite of interconnected Algorand smart contracts that isolate the lifecycle of a carbon credit into three distinct phases: Issuance, Trading (Marketplace), and Retirement. Once a credit is retired, it is permanently burned on-chain, preventing any future resale.

## 🔗 Important Links (MANDATORY RIFT SUBMISSION INFO)

* **Live Demo URL:** `https://graceful-malabi-8e37db.netlify.app`

## 📜 Smart Contract App IDs (Algorand Testnet)

Our application is fully deployed to the Algorand Testnet. The architecture is modular, utilizing three distinct smart contracts:

1. **CreditIssuanceRegistry**
* **App ID:** 755789132
* **Explorer:** [Pera Explorer Link](https://testnet.explorer.perawallet.app/application/755789132/)


2. **CarbonMarketplace**
* **App ID:** 755789142
* **Explorer:** [Pera Explorer Link](https://testnet.explorer.perawallet.app/application/755789142/)


3. **RetirementRegistry**
* **App ID:** 755789143
* **Explorer:** [Pera Explorer Link](https://testnet.explorer.perawallet.app/application/755789143/)



## 🏗️ Architecture Overview

CarbonChain utilizes a micro-contract architecture to ensure security and separation of concerns. The entire smart contract backend was scaffolded, tested, and deployed using **AlgoKit**.

1. **Credit Issuance Registry:** Acts as the minting engine. Authorized environmental NGOs or verification bodies mint verified carbon credits as ASAs (Algorand Standard Assets) or via local state accounting.
2. **Carbon Marketplace:** An escrow-based decentralized exchange (DEX) specifically for carbon assets. Sellers list their verified credits, and buyers send ALGO (or a stablecoin) to the contract. The contract handles the atomic transfer, ensuring zero counterparty risk.
3. **Retirement Registry:** The final destination for a credit. When a company wants to claim the offset, the credits are sent to this contract. The state is permanently updated to reflect the retirement, generating an immutable proof-of-offset for the company's ESG reports.

**Frontend Interaction:** The frontend is built with React and integrates with `@txnlab/use-wallet` (or Pera Wallet Connect) to sign transactions. It uses Algorand's indexer to fetch real-time data from the Testnet.

## 💻 Tech Stack

* **Blockchain Development Framework:** AlgoKit (Primary scaffolding, testing, and deployment pipeline)
* **Smart Contract Language:** Python (Algorand Python / PyTeal) compiled via AlgoKit
* **Network:** Algorand Testnet
* **Frontend Interface:** React.js, TypeScript, Tailwind CSS
* **Wallet Integration:** Pera Wallet (Testnet mode) / Defly Wallet

## ⚙️ Installation & Setup Instructions

### Prerequisites

* [Docker](https://www.docker.com/) (for AlgoKit LocalNet if testing locally)
* [AlgoKit CLI](https://developer.algorand.org/algokit/)
* Node.js (v18+)

### Smart Contract Setup

1. Clone the repository:
```bash
git clone [Your-Repo-Link]
cd carbonchain-marketplace

```


2. Initialize AlgoKit environment:
```bash
algokit bootstrap all

```


3. Deploy to Testnet (Ensure your deployer account is funded via the Algorand Testnet Dispenser):
```bash
algokit deploy testnet

```



### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd carbon-marketplace-frontend

```


2. Install dependencies:
```bash
npm install

```


3. Configure environment variables (`.env`):
```env
VITE_ALGOD_NODE_URL=https://testnet-api.algonode.cloud
VITE_ISSUANCE_APP_ID=755789132
VITE_MARKETPLACE_APP_ID=755789142
VITE_RETIREMENT_APP_ID=755789143

```


4. Start the development server:
```bash
npm run dev

```



## 📖 Usage Guide

*Please refer to the screenshots folder in the repository for visual guidance.*

1. **Connect Wallet:** Open the application and click "Connect Wallet". Approve the connection in your Pera Wallet app (ensure it is set to Testnet).
2. **Minting a Credit (NGO/Admin):** Navigate to the "Issuance" tab. Fill in the carbon project details (e.g., "Amazon Reforestation 2026") and tonnage. Sign the transaction to mint the credits.
3. **Listing on Marketplace:** The credit owner navigates to the "Marketplace" tab, sets a price per ton in ALGO, and signs the listing transaction. The credits are locked in the marketplace smart contract.
4. **Purchasing:** A buyer browses the active listings. Upon clicking "Buy", an atomic transfer is created: the buyer's ALGO is sent to the seller, and the carbon credit is sent to the buyer simultaneously.
5. **Retiring Credits:** To offset their emissions, the buyer navigates to "Dashboard", selects their purchased credits, and clicks "Retire". The transaction interacts with the `RetirementRegistry` (App ID 755789143), permanently locking the assets and generating a retirement certificate on-chain.

## 🚧 Known Limitations

* **Fiat On-Ramping:** Currently, all credits are priced natively in ALGO. Future iterations will support stablecoins (USDC) for easier corporate adoption.
* **Oracle Integration:** We currently rely on manual verification by trusted addresses for credit issuance. V2 will integrate decentralized oracles to automatically verify IoT data from carbon-capture hardware.

## 👥 Team Members and Roles

* **[Your Name / Hacker 1]:** Smart Contract Developer (AlgoKit, PyTeal) & Blockchain Architect
* **[Hacker 2 Name - if applicable]:** Frontend Developer (React, Wallet Integration)
* **[Hacker 3 Name - if applicable]:** UI/UX Design & Project Management
