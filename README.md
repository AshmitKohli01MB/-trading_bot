# Binance Futures Testnet Trading Bot

A Python command-line trading bot that places orders on
Binance Futures Testnet (USDT-M).

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
│   └── trading_bot.log
├── cli.py
├── .env.example
├── README.md
└── requirements.txt
```

---

## Setup Steps

### Step 1: Clone the Repository
```
git clone https://github.com/YOUR_USERNAME/trading_bot.git
cd trading_bot
```

### Step 2: Create Virtual Environment
```
python -m venv venv
```

### Step 3: Activate Virtual Environment
```
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Step 4: Install Dependencies
```
pip install -r requirements.txt
```

### Step 5: Create .env File
```
copy .env.example .env
```
Open .env and add your Binance Futures Testnet API keys:
```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```
Get free API keys from: https://testnet.binancefuture.com

---

## How to Run

### See All Options
```
python cli.py --help
```

### Place a Market BUY Order
```
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### Place a Market SELL Order
```
python cli.py --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
```

### Place a Limit BUY Order
```
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 93000
```

### Place a Limit SELL Order
```
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 96000
```

---

## Example Output

### Market Order
```
──────────── Order Request Summary ────────────
  Symbol      : BTCUSDT
  Side        : BUY
  Order Type  : MARKET
  Quantity    : 0.001

──────────── Order Placed Successfully ✅ ──────
┌─────────────┬──────────────┐
│ Field       │ Value        │
├─────────────┼──────────────┤
│ orderId     │ 123456789    │
│ symbol      │ BTCUSDT      │
│ status      │ FILLED       │
│ side        │ BUY          │
│ type        │ MARKET       │
│ origQty     │ 0.001        │
│ executedQty │ 0.001        │
│ avgPrice    │ 94500.00     │
└─────────────┴──────────────┘
```

---

## Assumptions

- Uses Binance Futures Testnet (USDT-M) only
- Minimum order quantity for BTCUSDT is 0.001
- LIMIT orders use GTC (Good Till Cancelled) by default
- All logs are saved to logs/trading_bot.log
- Tested on Windows 11 with Python 3.11

---

## Logging

All API requests, responses and errors are saved to:
```
logs/trading_bot.log
```

---

## Error Handling

The bot handles these errors:
- Invalid symbol
- Invalid side
- Invalid order type
- Zero or negative quantity
- Missing price for LIMIT orders
- Insufficient margin
- Network failures
- Invalid API credentials

---

## Dependencies

- python-binance
- python-dotenv
- typer
- rich