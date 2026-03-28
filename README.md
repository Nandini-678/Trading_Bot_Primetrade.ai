
# Binance Futures Testnet Trading Bot

A Python-based trading bot for **Binance Futures Testnet (USDT-M)** that supports **MARKET**, **LIMIT**, and **STOP-LIMIT** orders through both a **Command Line Interface (CLI)** and a **Streamlit UI**.

This project focuses on clean code structure, input validation, logging, and error handling for safe testnet order placement.

---

## Features

- Place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders
- Support for both **BUY** and **SELL**
- Input validation before sending requests
- Structured logging for requests, responses, and errors
- CLI-based interaction using **Typer**
- Simple web UI using **Streamlit**
- Works with **Binance Futures Testnet**, not live trading

---

## Tech Stack

- Python
- python-binance
- Typer
- Rich
- Streamlit
- python-dotenv

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── sample_logs/
├── screenshots/
├── cli.py
├── ui.py
├── requirements.txt
├── README.md
└── .env
````

---

## How It Works

1. The user enters order details through the CLI or UI.
2. Inputs are validated before sending the request.
3. The bot builds the correct Binance Futures payload.
4. The request is sent to Binance Futures Testnet.
5. The response is displayed and logged.

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

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd trading_bot
```

### 2. Create and activate a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
BINANCE_BASE_URL=https://testnet.binancefuture.com
```

---

## Run the Project

### CLI

**MARKET order**

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.002
```

**LIMIT order**

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.002 --price 120000
```

**STOP-LIMIT order**

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type STOP_LIMIT --quantity 0.002 --price 69000 --stop-price 69500
```

### UI

```bash
streamlit run ui.py
```

---

## Logging and Error Handling

The project includes logging for:

* client initialization
* order requests
* API responses
* validation failures
* runtime errors

It also handles invalid inputs and Binance API errors gracefully instead of crashing with unclear messages.

---

## Notes

* This project uses **Binance Futures Testnet** only.
* It is built for **order placement**, not trading strategy automation.
* Do **not** use live API keys.
* Make sure the screenshot filenames match the files in your repository.

---

## Future Improvements

* Fetch final order status after placement
* Cancel open orders
* View order history
* Add symbol precision validation
* Add unit tests
* Add Docker support


Everything else was fluff. If you want, I can trim it even further into a **clean GitHub-style README with only 6 sections**.
```
