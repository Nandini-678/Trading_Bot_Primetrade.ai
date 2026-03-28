# Binance Futures Testnet Trading Bot

## Introduction

This project is a simplified trading bot built in Python for **Binance Futures Testnet (USDT-M)**. It allows users to place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders using either a **Command Line Interface (CLI)** or a **lightweight Streamlit UI**.

The goal of the project is not to build a trading strategy or profit-making system. It is designed to demonstrate clean API integration, structured project organization, input validation, logging, error handling, and reusable backend design.

This project uses the Binance Futures Testnet environment, so all orders are placed in a safe test environment rather than a real-money trading account.

---

## Project Objective

The purpose of this project is to provide a clean and reusable Python application that can:

- Connect to Binance Futures Testnet
- Place futures orders programmatically
- Validate user inputs before sending requests
- Handle API and network errors gracefully
- Log requests, responses, and failures clearly
- Support both CLI and UI-based usage

---

## Features Implemented

### 1. MARKET Order Support
A MARKET order executes immediately at the best available market price.

**Why it is useful:**  
This is the simplest and fastest order type for immediate execution.

---

### 2. LIMIT Order Support
A LIMIT order allows the user to specify the exact price at which the order should be placed.

**Why it is useful:**  
It gives more control over entry or exit price instead of executing immediately.

---

### 3. STOP-LIMIT Order Support
A STOP-LIMIT order uses:
- a **stop price** to trigger the order
- a **limit price** to place the actual order

**Why it is useful:**  
This adds a more advanced order flow and demonstrates support for an additional order type beyond the mandatory requirements.

---

### 4. BUY and SELL Support
The bot supports both:
- `BUY`
- `SELL`

**Why it is useful:**  
This ensures the bot supports both major order directions in futures trading.

---

### 5. Input Validation
The application validates:
- symbol
- side
- order type
- quantity
- price
- stop price

**Why it is useful:**  
This prevents invalid requests from reaching the Binance API and gives users immediate, clear feedback.

---

### 6. Structured Logging
The application logs:
- order requests
- order responses
- API errors
- unexpected exceptions

**Why it is useful:**  
Logging makes debugging easier and provides traceability for testing and review.

---

### 7. CLI Interface
A CLI is provided using **Typer** and **Rich**.

**Why it is useful:**  
It allows quick order placement directly from the terminal with clean formatted output.

---

### 8. Lightweight UI
A lightweight web UI is provided using **Streamlit**.

**Why it is useful:**  
It makes the application easier to use for users who prefer a visual interface instead of terminal commands.

---

## Tech Stack

- **Python 3.x**
- **python-binance**
- **Typer**
- **Rich**
- **Streamlit**
- **python-dotenv**
- **pandas**

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── cli.py
├── ui.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
