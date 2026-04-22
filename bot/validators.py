from bot.logging_config import setup_logger


logger = setup_logger("validators")

# ── Allowed Values ─────────────────────────────────────
VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT", "STOP_MARKET"]
MIN_QUANTITY = 0.001   # Minimum order size for BTCUSDT


def validate_inputs(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    """
    Validates all user inputs before placing an order.
    Raises ValueError with clear messages if anything is wrong.
    """

    errors = []

    # ── Validate Symbol ───────────────────────────
    if not symbol or len(symbol) < 3:
        errors.append(
            f"Invalid symbol '{symbol}'. "
            f"Example of valid symbol: BTCUSDT"
        )

    # ── Validate Side ─────────────────────────────
    if side.upper() not in VALID_SIDES:
        errors.append(
            f"Invalid side '{side}'. "
            f"Must be one of: {', '.join(VALID_SIDES)}"
        )

    # ── Validate Order Type ───────────────────────
    if order_type.upper() not in VALID_ORDER_TYPES:
        errors.append(
            f"Invalid order type '{order_type}'. "
            f"Must be one of: {', '.join(VALID_ORDER_TYPES)}"
        )

    # ── Validate Quantity ─────────────────────────
    if quantity <= 0:
        errors.append(
            f"Quantity must be greater than 0. "
            f"You entered: {quantity}"
        )

    if quantity < MIN_QUANTITY:
        errors.append(
            f"Quantity too small. "
            f"Minimum is {MIN_QUANTITY}. "
            f"You entered: {quantity}"
        )

    # ── Validate Price (only for LIMIT orders) ────
    if order_type.upper() == "LIMIT":
        if price is None:
            errors.append(
                "Price is required for LIMIT orders. "
                "Add --price flag e.g. --price 50000"
            )
        elif price <= 0:
            errors.append(
                f"Price must be greater than 0. "
                f"You entered: {price}"
            )

    # ── Validate Stop Price (for STOP_MARKET) ─────
    if order_type.upper() == "STOP_MARKET":
        if price is None or price <= 0:
            errors.append(
                "Stop price is required for STOP_MARKET orders. "
                "Add --price flag e.g. --price 45000"
            )

    # ── Raise All Errors Together ─────────────────
    if errors:
        for error in errors:
            logger.warning(f"Validation failed: {error}")
        raise ValueError("\n".join(errors))

    logger.info(
        f"Validation passed for: {symbol} {side} "
        f"{order_type} qty={quantity}"
        + (f" price={price}" if price else "")
    )