# 🎰 Gameka Lottery DApp

Demo Link: https://tkani.github.io/ethpop/

A decentralized lottery game built with **Solidity**, integrated into a web interface using **Flask**, **HTML**, **CSS**, and **JavaScript**.

## 🔍 Overview

Gameka Lottery allows users to place bets using ETH by selecting up to 18 unique numbers between **0 and 36**. If the drawn number matches any guess, users win a calculated payout.

### 💰 Bet Distribution:
- **70%** stays in the contract as the **Liquidity Pool**
- **30%** goes to a designated **Gameka Pool**

Winners are automatically paid from the liquidity pool. If funds are insufficient, they are added to a **waiting list** and paid later when liquidity is restored.

---

## ⚙️ Technologies Used

- **Solidity** — Smart Contract logic
- **Flask** — Backend API & server
- **HTML/CSS/JS** — Frontend UI
- **Web3.py / Web3.js** — Smart contract integration

---

## 🧪 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/gameka-lottery.git
cd gameka-lottery

2. Setup Flask Backend
cd app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py


3. Deploy Smart Contract
Use Remix, Hardhat, or Truffle to deploy GamekaLottery.sol.
After deployment, copy the contract address and update your frontend integration code (JS or Flask config).


4. Access the Web App
http://localhost:5000


Connect your MetaMask wallet and start playing!

🗂 Project Structure
gameka-lottery/
├── contracts/
│   └── GamekaLottery.sol
├── app/
│   ├── static/
│   ├── templates/
│   └── app.py
├── requirements.txt
└── README.md


🎯 Features
✅ Fair random number draw (0–36)

✅ Max 18 unique guesses per bet

✅ Winner auto-payout or waitlist if funds low

✅ Contract & pool balance views

✅ Owner-only withdrawals & waitlist controls


🔐 Security Note
This project is for educational and demonstration purposes.
It has not been audited — use with caution and avoid real funds in production.



📜 License
MIT License


License

👨‍💻 Author
Built with ❤️ by Thamaraikani Chandrasooden


![Gameka UI](https://i.ibb.co/RpRxFdkR/ethpop.png)



