import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logger


# Load API keys from .env file
load_dotenv()

# Setup logger for this module
logger = setup_logger("client")


class BinanceFuturesClient:
    """
    Wrapper around the Binance API client.
    Handles connection to Binance Futures Testnet.
    """

    def __init__(self):
        # ── Read Keys from .env ───────────────────
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        # ── Validate Keys Exist ───────────────────
        if not api_key or not api_secret:
            raise ValueError(
                "API Key or Secret not found.\n"
                "Please check your .env file has:\n"
                "BINANCE_API_KEY=your_key\n"
                "BINANCE_API_SECRET=your_secret"
            )

        # ── Connect to Testnet ────────────────────
        self.client = Client(
            api_key,
            api_secret,
            testnet=True   # This points to testnet.binancefuture.com
        )
        logger.info("Binance Futures Testnet client initialized successfully.")

    def place_order(self, **kwargs) -> dict:
        """
        Places an order on Binance Futures Testnet.
        Returns the full order response as a dictionary.
        """

        # Log the request before sending
        logger.info(f"Sending order request: {kwargs}")

        try:
            # ── Send Order to Binance ─────────────
            response = self.client.futures_create_order(**kwargs)

            # Log the full response
            logger.info(f"Order response received: {response}")

            return response

        except BinanceAPIException as e:
            # Binance specific errors (wrong symbol, insufficient balance etc)
            logger.error(
                f"Binance API Error | "
                f"Code: {e.status_code} | "
                f"Message: {e.message}"
            )
            raise

        except ConnectionError as e:
            # Internet/network problems
            logger.error(f"Network connection error: {str(e)}")
            raise

        except Exception as e:
            # Any other unexpected errors
            logger.error(f"Unexpected error while placing order: {str(e)}")
            raise