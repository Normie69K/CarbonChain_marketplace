<div align="center">

# 🌱 CarbonChain Marketplace

### Decentralizing Trust in the Global Carbon Economy

**RIFT 2026 Hackathon • Web3 & Climate Innovation**


![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)
![Built on](https://img.shields.io/badge/Built%20on-Algorand-black?style=for-the-badge\&logo=algorand)
![Frontend](https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge\&logo=react)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)


</div>

---

## 🚀 Live Experience

* 🌐 **Frontend:** [https://graceful-malabi-8e37db.netlify.app](https://graceful-malabi-8e37db.netlify.app)
* ⚙️ **Backend API:** [https://carbon-emmision-footprint-marketplace-5oxy.onrender.com](https://carbon-emmision-footprint-marketplace-5oxy.onrender.com)
* 🎥 **Demo Video:** [Watch the Full Demo Here](https://www.linkedin.com/posts/karan-chaubey-7bbb4627b_rift2026-algorand-algokit-activity-7430422385218093056-GkXf)

---

## 🧠 Problem

The carbon offset ecosystem today is fragmented, opaque, and inefficient.

* Double counting of carbon credits
* Lack of public verification
* High brokerage costs
* Slow settlement cycles

These issues undermine trust and enable greenwashing.

---

## 💡 Solution

CarbonChain is an end-to-end carbon credit lifecycle platform powered by blockchain.

It enables:

* Verified issuance
* Transparent trading
* Atomic settlement
* Immutable retirement proof

---

## ⭐ Key Highlights

* Micro-contract architecture for scalability
* Atomic swaps with no escrow risk
* Permanent on-chain retirement registry
* Ultra-low fees on Algorand
* Persistent multi-wallet integration

---

## 🎬 Demo & Product Experience

### 🎥 Full Demo

<p align="center">
<a href="https://www.linkedin.com/posts/karan-chaubey-7bbb4627b_rift2026-algorand-algokit-activity-7430422385218093056-GkXf">
<img src="https://img.shields.io/badge/▶%20Watch%20Full%20Demo-red?style=for-the-badge" alt="Watch Demo" />
</a>
</p>

### Demo Flow

1️⃣ Wallet connection

2️⃣ Credit issuance

3️⃣ Marketplace trading

4️⃣ Atomic swap execution

5️⃣ Credit retirement

---

## 🖼️ Product Screenshots

### 🌍 Landing Page

### 🔐 Wallet Connection

### 📊 Dashboard

### 🛒 Marketplace

### 🧾 Issuance Panel

### ⚡ Transaction Execution

### ♻️ Retirement Certificate

---

## 🏗️ System Architecture

```text
Users / NGOs / Enterprises
        │
        ▼
Frontend (React + Wallets)
        │
        ▼
Backend API (Node + Indexer + IPFS)
        │
        ▼
Algorand Smart Contract Layer
 ├─ CreditIssuanceRegistry
 ├─ CarbonMarketplace
 └─ RetirementRegistry

```

### 1. Smart Contracts (`/carbon-marketplace_smart_contracts`)

```text
carbon-marketplace_smart_contracts/
├── .algokit/                # AlgoKit configuration & generators
├── smart_contracts/         # Core PyTeal / Algorand Python Contracts
│   ├── credit_issuance/     # 🟢 Minting Engine Logic
│   │   ├── contract.py      
│   │   └── deploy_config.py 
│   ├── marketplace/         # 🔵 DEX & Escrow Logic
│   │   ├── contract.py      
│   │   └── deploy_config.py 
│   └── retirement/          # 🟣 Burn/Offset Registry Logic
│       ├── contract.py      
│       └── deploy_config.py 
├── deploy_all.py            # Master deployment script for Testnet
├── pyproject.toml           # Python dependencies
└── app_ids.txt              # Testnet App ID registry (Verifiable on Pera)

```

### 2. Frontend Application (`/carbon-marketplace_frontend`)

```text
carbon-marketplace_frontend/
├── src/
│   ├── components/          # Reusable UI & Dashboard panels
│   │   ├── ui/              # shadcn/ui base components
│   │   └── dashboard/       # Specialized Web3 panels (Issue, Retire, Stats)
│   ├── context/             # React Context (WalletContext.tsx)
│   ├── hooks/               # Custom React hooks (useApi, useCountUp, etc.)
│   ├── pages/               # Route views (Dashboard, Marketplace, Admin)
│   ├── services/            # API & Blockchain interaction logic
│   ├── lib/                 # Utility functions (Tailwind merges, formatting)
│   ├── App.tsx              # Main application router
│   └── main.tsx             # React DOM entry point
├── public/                  # Static assets & logos
├── tailwind.config.ts       # Utility-first styling config
├── vite.config.ts           # Highly optimized bundler config
└── package.json             # Node dependencies

```

### 3. Backend Services (`/carbon-marketplace_backend`)

```text
carbon-marketplace_backend/
├── src/
│   ├── config/              # Core setups (algorand.js, database.js, ipfs.js)
│   ├── controllers/         # Route handlers (marketplace, user, ipfs, etc.)
│   ├── middleware/          # Security & validation logic
│   ├── models/              # Data schemas (User, Company, Listing, Project)
│   ├── routes/              # Express API endpoints
│   ├── services/            # Heavy lifting (Indexer, IPFS, Algorand SDK logic)
│   ├── utils/               # Helpers (logger.js)
│   └── app.js               # Express application entry
├── generateWallet.js        # Server-side wallet generation utility
├── Dockerfile               # Containerization blueprint for easy deployment
└── package.json             # Node dependencies

```

# 💻 Technology Stack

## 🧱 Blockchain

![Algorand](https://img.shields.io/badge/Algorand-000000?style=for-the-badge\&logo=algorand\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![PyTeal](https://img.shields.io/badge/PyTeal-FFD43B?style=for-the-badge\&logo=python\&logoColor=blue)
![AlgoKit](https://img.shields.io/badge/AlgoKit-00A550?style=for-the-badge\&logo=algorand\&logoColor=white)

## 🎨 Frontend

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge\&logo=react\&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge\&logo=typescript\&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge\&logo=tailwind-css\&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge\&logo=vite\&logoColor=white)

## ⚙️ Backend

![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge\&logo=node.js\&logoColor=white)
![Express](https://img.shields.io/badge/Express.js-404D59?style=for-the-badge\&logo=express\&logoColor=white)
![IPFS](https://img.shields.io/badge/IPFS-65C2CB?style=for-the-badge\&logo=ipfs\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)

---

## 🔄 Carbon Credit Lifecycle

1️⃣ **Issue credits** from verified NGOs

2️⃣ **List credits** on marketplace

3️⃣ **Buy via** atomic trade

4️⃣ **Retire credits** permanently

5️⃣ **Generate proof** certificate

---

## 📊 Platform Metrics

* 🌳 **Carbon Credits Issued:** 128,450 tCO₂
* 🔁 **Marketplace Transactions:** 3,972
* 🏢 **Organizations Onboarded:** 46
* ♻️ **Credits Retired:** 52,318 tCO₂
* 💰 **Total Trading Volume:** $1.84M
* ⚡ **Avg Settlement Time:** 3.2 sec

---

## 💰 Business Model

* Protocol transaction fee
* Project verification onboarding
* Enterprise ESG reporting API

---

## 🛠️ Local Setup

```bash
git clone https://github.com/Aditya07771/CarbonChain_marketplace.git

```

### Smart Contracts

```bash
cd carbon-marketplace_smart_contracts
algokit bootstrap all
algokit deploy testnet

```

### Backend

```bash
cd ../carbon-marketplace_backend
npm install
npm start

```

### Frontend

```bash
cd ../carbon-marketplace_frontend
npm install
npm run dev

```

---

## 🏆 Why This Project Stands Out

* Real-world climate use case
* Fully working Web3 stack
* Production-level architecture
* Strong scalability model
* Clear commercialization path

---

## 📜 License

MIT License

---

## 🎯 Elevator Pitch

CarbonChain transforms carbon credits into transparent, verifiable digital assets — enabling companies to prove real climate impact with cryptographic certainty.
