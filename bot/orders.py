from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs
from bot.logging_config import setup_logger


logger = setup_logger("orders")


def place_order(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
) -> dict:
    """
    Main function to place an order.
    Steps:
    1. Converts inputs to correct format
    2. Validates all inputs
    3. Builds order parameters
    4. Sends order to Binance
    5. Returns response
    """

    # ── Step 1: Format Inputs ─────────────────────
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    # ── Step 2: Validate Inputs ───────────────────
    validate_inputs(symbol, side, order_type, quantity, price)

    # ── Step 3: Build Order Parameters ───────────
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    # LIMIT orders need price and timeInForce
    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"  # Good Till Cancelled

    # STOP_MARKET orders need stopPrice
    if order_type == "STOP_MARKET":
        params["stopPrice"] = price

    logger.info(f"Final order parameters: {params}")

    # ── Step 4: Send Order ────────────────────────
    client = BinanceFuturesClient()
    response = client.place_order(**params)

    # ── Step 5: Return Response ───────────────────
    return response