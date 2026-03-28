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

### 2. LIMIT Order Support

A LIMIT order allows the user to specify the price at which the order should be placed.

**Why it is useful:**  
It gives the user price control instead of immediately executing at market price.

### 3. STOP-LIMIT Order Support

A STOP-LIMIT order requires:

- a **stop price** to trigger the order
- a **limit price** for the actual placed order

**Why it is useful:**  
This was added as a bonus feature to demonstrate support for a more advanced order type beyond the minimum requirements.

### 4. BUY and SELL Support

The bot supports both:

- `BUY`
- `SELL`

**Why it is useful:**  
This is required to support both major futures order directions.

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

### 7. CLI Interface

A command-line interface is provided using **Typer** and **Rich**.

**Why it is useful:**  
It allows users to place orders quickly from the terminal with clean output formatting.

### 8. Lightweight Streamlit UI

A lightweight web interface is provided using **Streamlit**.

**Why it is useful:**  
It makes the application easier to use for users who prefer a visual workflow over terminal commands.

---

## Why These Features Were Added

The goal was not just to place an order, but to build a small application that is structured and usable.

- **MARKET** and **LIMIT** orders were required by the assignment.
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
````

---

## File Responsibilities

### `bot/client.py`

Handles Binance Futures Testnet API communication.

### `bot/config.py`

Loads environment variables such as API key, API secret, and base URL.

### `bot/exceptions.py`

Defines custom exception classes used across the project.

### `bot/logging_config.py`

Creates and configures reusable application logging.

### `bot/orders.py`

Builds Binance-ready payloads and manages order placement service logic.

### `bot/validators.py`

Validates and normalizes user input before requests are sent.

### `cli.py`

Provides terminal-based order placement.

### `ui.py`

Provides a lightweight Streamlit-based user interface.

---

## Application Flow

The application follows this flow:

1. User enters order details through CLI or UI
2. Input is validated in `validators.py`
3. `orders.py` builds a Binance-compatible payload
4. `client.py` sends the request to Binance Futures Testnet
5. Response is returned and formatted
6. Logs are written to file and console
7. Success or failure is shown to the user

This separation keeps the code modular and easier to maintain.

---

## UI Features

The UI is built with Streamlit and provides a simple and readable order placement flow.

### UI capabilities

* common symbol dropdown
* custom symbol input option
* BUY / SELL selection
* MARKET / LIMIT / STOP-LIMIT selection
* conditional input fields for:

  * price
  * stop price
* request summary display
* response summary metrics
* detailed response section
* raw API response inside expandable section
* clear success and error messages
* note explaining that initial create-order responses may not always show final fill state immediately

### Why these UI features were added

These features were added to:

* make testing easier without depending only on terminal commands
* improve readability of request and response details
* provide a cleaner experience for reviewers and end users
* make the application understandable even for users new to Binance APIs

---

## UI Screenshots

### Main UI

![Main UI](screenshots/ui_home.png)

### MARKET Order Example

![Market Order Success](screenshots/market_order_success.png)

### LIMIT Order Example

![Limit Order Success](screenshots/limit_order_success.png)

### STOP-LIMIT Order Form

![Stop Limit Order Form](screenshots/stop_limit_order_form.png)

> Replace the screenshot filenames if your actual files use different names.

---

## Logging

The application logs runtime activity to a file in the `logs/` folder.

### Logged events include

* Binance Futures client initialization
* order payload creation
* API request submission
* successful order creation
* validation failures
* Binance API errors
* unexpected exceptions

### Sample logs included for submission

Sample logs are stored in:

```text
sample_logs/
```

Files included:

* `sample_logs/market_order.log`
* `sample_logs/limit_order.log`

These demonstrate successful logging for one MARKET order and one LIMIT order.

---

## Error Handling

The application handles:

* invalid symbol
* invalid side
* unsupported order type
* missing required fields
* invalid quantity
* invalid price
* invalid stop price
* Binance API errors
* request/signature issues
* unexpected runtime errors

Instead of crashing with unreadable output, the application returns controlled and understandable error messages.

---

## Security Note

The `.env` file is excluded from version control and must never be committed.

Only **Binance Futures Testnet** credentials should be used for this project. Live Binance credentials must never be used.

If credentials are exposed during testing, they should be rotated and replaced.

---

## Assumptions

* this project targets **Binance Futures Testnet (USDT-M)** only
* the project focuses on **order placement**, not strategy automation
* leverage configuration is not included
* position monitoring is not included
* open-order cancellation is not included
* symbol support depends on Binance Futures Testnet availability
* the initial create-order response may not always show final execution state immediately

---

## How to Run the Project on Your Device

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd trading_bot
```

Replace the repository URL above with your actual GitHub repository URL.

### 2. Create and activate a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the project root and add:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
BINANCE_BASE_URL=https://testnet.binancefuture.com
```

Use Binance Futures Testnet credentials only.

### 5. Run the application

You can run the application in either CLI mode or UI mode.

---

## CLI Usage

### MARKET order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.002
```

### LIMIT order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.002 --price 120000
```

### STOP-LIMIT order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type STOP_LIMIT --quantity 0.002 --price 69000 --stop-price 69500
```

---

## UI Usage

Run the Streamlit UI with:

```bash
streamlit run ui.py
```

This will open the application in your browser.

---

## Sample Output Details

The application prints or displays:

### Request Summary

* symbol
* side
* order type
* quantity
* price if applicable
* stop price if applicable

### Response Details

* orderId
* status
* symbol
* side
* type
* price
* avgPrice
* origQty
* executedQty
* timeInForce
* stopPrice
* updateTime

---

## Possible Future Improvements

If the project were extended further, the following could be added:

* fetch final order status after placement
* cancel open orders
* retrieve order history
* validate symbol precision and lot size using exchange metadata
* add open positions view
* improve response status visualization
* add automated unit tests
* add Docker support
* make configuration more deployment-ready

---

## Submission Contents

This repository includes:

* source code
* README
* requirements.txt
* CLI support
* Streamlit UI
* input validation
* structured logging
* error handling
* support for MARKET, LIMIT, and STOP-LIMIT orders
* sample log files for MARKET and LIMIT orders

---

## Conclusion

This project demonstrates a clean and structured Binance Futures Testnet trading bot with clear separation of concerns between validation, order building, API communication, CLI handling, and UI rendering.

The focus of the implementation is correctness, readability, usability, logging, and error handling rather than trading strategy complexity.

```

If this breaks again when you paste, the problem is your editor or you’re pasting from inside a code block. Paste it directly into the raw `README.md` file, not into another fenced block.
```
