from typing import Any, Dict

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.config import get_settings
from bot.exceptions import APIError
from bot.logging_config import setup_logger


logger = setup_logger()


class BinanceFuturesClient:
    def __init__(self) -> None:
        settings = get_settings()

        self.client = Client(settings.api_key, settings.api_secret)
        self.client.FUTURES_URL = f"{settings.base_url}/fapi"

        logger.info("Binance Futures client initialized for testnet.")

    def place_order(self, order_params: Dict[str, Any]) -> Dict[str, Any]:
        try:
            safe_log_data = {k: str(v) for k, v in order_params.items()}
            logger.info(f"Sending futures order request: {safe_log_data}")

            response = self.client.futures_create_order(**order_params)

            logger.info(
                f"Futures order created successfully. "
                f"Order ID: {response.get('orderId')} | Status: {response.get('status')}"
            )

            return response

        except BinanceAPIException as exc:
            logger.error(f"Binance API error: {exc.message}")
            raise APIError(f"Binance API error: {exc.message}") from exc

        except BinanceRequestException as exc:
            logger.error(f"Binance request error: {str(exc)}")
            raise APIError(f"Binance request error: {str(exc)}") from exc

        except Exception as exc:
            logger.exception("Unexpected error while placing futures order.")
            raise APIError(f"Unexpected API error: {str(exc)}") from exc