import logging
import os


def setup_logger(name: str) -> logging.Logger:
    """
    Creates and returns a logger that writes to:
    - logs/trading_bot.log (all levels)
    - terminal/console (INFO and above)
    """

    # Create logs folder if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Create logger with given name
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # ── File Handler ──────────────────────────────
    # Saves ALL log messages to file
    fh = logging.FileHandler("logs/trading_bot.log")
    fh.setLevel(logging.DEBUG)

    # ── Console Handler ───────────────────────────
    # Shows INFO and above in terminal
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # ── Formatter ─────────────────────────────────
    # How each log line looks
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Avoid adding duplicate handlers
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger