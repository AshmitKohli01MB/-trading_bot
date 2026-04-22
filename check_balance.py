from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

print("=== CONNECTING TO TESTNET ===")
client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET"),
    testnet=True
)
print("Connected successfully!")

print("")
print("=== ACCOUNT BALANCE ===")
balance = client.futures_account_balance()
has_balance = False
for asset in balance:
    if float(asset["balance"]) > 0:
        print(asset["asset"] + ": " + asset["balance"])
        has_balance = True

if not has_balance:
    print("No balance found - add USDT on testnet website")

print("")
print("=== CURRENT BTC PRICE ===")
price = client.futures_symbol_ticker(symbol="BTCUSDT")
print("BTCUSDT: " + price["price"])

print("")
print("=== OPEN ORDERS ===")
orders = client.futures_get_open_orders(symbol="BTCUSDT")
print("Open orders: " + str(len(orders)))

print("")
print("=== READY TO TRADE ===")
if has_balance:
    print("YES - You can place orders now!")
else:
    print("NO - Add balance first on testnet website")