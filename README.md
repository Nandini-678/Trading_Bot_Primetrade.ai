# Binance Futures Testnet Trading Bot

A simplified Python trading bot for **Binance Futures Testnet (USDT-M)** that supports **MARKET**, **LIMIT**, and **STOP-LIMIT** orders through both a **Command Line Interface (CLI)** and a **lightweight Streamlit UI**.

This project focuses on clean API integration, structured code organization, reusable backend logic, input validation, logging, and error handling. It is designed for **testnet order placement**, not for real-money trading or strategy automation.

---

## Table of Contents

- [Introduction](#introduction)
- [Project Objective](#project-objective)
- [Features Implemented](#features-implemented)
- [Why These Features Were Added](#why-these-features-were-added)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [File Responsibilities](#file-responsibilities)
- [Application Flow](#application-flow)
- [UI Features](#ui-features)
- [UI Screenshots](#ui-screenshots)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [Security Note](#security-note)
- [Assumptions](#assumptions)
- [How to Run the Project on Your Device](#how-to-run-the-project-on-your-device)
- [CLI Usage](#cli-usage)
- [UI Usage](#ui-usage)
- [Sample Output Details](#sample-output-details)
- [Possible Future Improvements](#possible-future-improvements)
- [Submission Contents](#submission-contents)
- [Conclusion](#conclusion)

---

## Introduction

This project is a simplified trading bot built in Python for **Binance Futures Testnet (USDT-M)**. It allows users to place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders using either a **CLI** or a **Streamlit-based UI**.

The project is not intended to implement a trading strategy, generate profit, or manage a full trading lifecycle. Its purpose is to demonstrate:

- clean integration with Binance Futures Testnet
- reusable and structured code
- proper validation before API calls
- graceful error handling
- useful runtime logging
- both command-line and UI-based usage

All orders are placed on **Binance Futures Testnet**, so no real funds are used.

---

## Project Objective

The objective of this project is to build a clean and reusable Python application that can:

- connect to Binance Futures Testnet
- place futures orders programmatically
- validate user input before sending API requests
- handle API errors and unexpected failures clearly
- log important application events
- support both terminal-based and UI-based interaction

---

## Features Implemented

### 1. MARKET Order Support
A MARKET order executes immediately at the best available price.

**Why it is useful:**  
It is the simplest order type for immediate execution and was one of the core assignment requirements.

---

### 2. LIMIT Order Support
A LIMIT order allows the user to specify the price at which the order should be placed.

**Why it is useful:**  
It gives the user price control instead of immediately executing at market price.

---

### 3. STOP-LIMIT Order Support
A STOP-LIMIT order requires:
- a **stop price** to trigger the order
- a **limit price** for the actual placed order

**Why it is useful:**  
This was added as a bonus feature to demonstrate support for a more advanced order type beyond the minimum requirements.

---

### 4. BUY and SELL Support
The bot supports both:
- `BUY`
- `SELL`

**Why it is useful:**  
This is required to support both major futures order directions.

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
It prevents invalid requests from being sent to Binance and provides immediate user feedback.

---

### 6. Structured Logging
The application logs:
- client initialization
- order request data
- payload generation
- API responses
- API errors
- unexpected exceptions

**Why it is useful:**  
This improves debugging, traceability, and submission quality.

---

### 7. CLI Interface
A command-line interface is provided using **Typer** and **Rich**.

**Why it is useful:**  
It allows users to place orders quickly from the terminal with clean output formatting.

---

### 8. Lightweight Streamlit UI
A lightweight web interface is provided using **Streamlit**.

**Why it is useful:**  
It makes the application easier to use for users who prefer a visual workflow over terminal commands.

---

## Why These Features Were Added

The goal was not just to place an order, but to build a small application that is structured and usable.

- **MARKET and LIMIT orders** were required by the assignment.
- **STOP-LIMIT** was added as a bonus feature to show extended functionality.
- **Validation** was added to catch user errors early.
- **Logging** was added to make request flow and failures visible.
- **CLI** was added for direct terminal usage.
- **UI** was added to improve usability and demonstrate a better user experience.

---

## Tech Stack

- **Python 3.x**
- **python-binance**
- **python-dotenv**
- **Typer**
- **Rich**
- **Streamlit**
- **pandas**
- **requests**

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
├── sample_logs/
│   ├── market_order.log
│   └── limit_order.log
│
├── screenshots/
│   ├── ui_home.png
│   ├── market_order_success.png
│   ├── limit_order_success.png
│   └── stop_limit_order_form.png
│
├── cli.py
├── ui.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
