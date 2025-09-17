# 🪙 BlockchainCat-1_173
## Simple Blockchain Project

A minimal blockchain implementation in Python that demonstrates the **core concepts of blockchain technology**.  
This project is designed for educational use in college-level projects to help students understand how blockchains work internally.

---

## 📘 Project Introduction
This project implements a simple blockchain with the following features:
- Each block stores transactions, proof of work, and hash of the previous block.
- Blocks are linked together to form a chain (immutable ledger).
- A proof-of-work algorithm secures the blockchain by requiring computational effort.
- A lightweight REST API (Flask) provides interaction with the blockchain (mine blocks, add transactions, validate the chain).

---

## ⚙️ Installation Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/BlockchainCat-1_173.git
   cd BlockchainCat-1_173
2.**Install dependencies**
   
   pip install -r requirements.txt

3.**Run the blockchain**
   
   python node.py

## 🚀 Usage Guide

You can interact with the blockchain through API endpoints using a browser, Postman, or command-line tools like curl.

Example Commands:

1.**Mine a new block**

curl http://127.0.0.1:5000/mine_block


2.**View the blockchain**

curl http://127.0.0.1:5000/get_chain


3.**Check if blockchain is valid**

curl http://127.0.0.1:5000/is_valid


4.**Add a transaction**

curl -X POST http://127.0.0.1:5000/add_transaction \
-H "Content-Type: application/json" \
-d '{"sender":"Alice","receiver":"Bob","amount":50}'

## 🌐 API Endpoints

GET /mine_block → Mine a new block

GET /get_chain → View the blockchain

GET /is_valid → Check if the blockchain is valid

POST /add_transaction → Add a new transaction

Example JSON body:

{
  "sender": "Alice",
  "receiver": "Bob",
  "amount": 50
}

## 📖 References

Bitcoin Whitepaper by Satoshi Nakamoto

Flask Documentation

Python hashlib Library


