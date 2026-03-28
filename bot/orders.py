from decimal import Decimal
from typing import Any, Dict

from bot.client import BinanceFuturesClient
from bot.exceptions import ValidationError
from bot.logging_config import setup_logger


logger = setup_logger()


class OrderService:
    def __init__(self) -> None:
        self.client = BinanceFuturesClient()

    def build_order_payload(self, validated_data: Dict[str, Any]) -> Dict[str, Any]:
        order_type = validated_data["order_type"]

        payload: Dict[str, Any] = {
            "symbol": validated_data["symbol"],
            "side": validated_data["side"],
            "quantity": self._decimal_to_string(validated_data["quantity"]),
        }

        if order_type == "MARKET":
            payload["type"] = "MARKET"

        elif order_type == "LIMIT":
            payload["type"] = "LIMIT"
            payload["price"] = self._decimal_to_string(validated_data["price"])
            payload["timeInForce"] = "GTC"

        elif order_type == "STOP_LIMIT":
            payload["type"] = "STOP"
            payload["price"] = self._decimal_to_string(validated_data["price"])
            payload["stopPrice"] = self._decimal_to_string(validated_data["stop_price"])
            payload["timeInForce"] = "GTC"

        else:
            raise ValidationError(f"Unsupported order type: {order_type}")

        return payload

    def place_order(self, validated_data: Dict[str, Any]) -> Dict[str, Any]:
        payload = self.build_order_payload(validated_data)

        logger.info(f"Built order payload: {payload}")

        response = self.client.place_order(payload)

        return self.format_order_response(response)

    @staticmethod
    def format_order_response(response: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "orderId": response.get("orderId"),
            "symbol": response.get("symbol"),
            "status": response.get("status"),
            "side": response.get("side"),
            "type": response.get("type"),
            "price": response.get("price"),
            "avgPrice": response.get("avgPrice"),
            "origQty": response.get("origQty"),
            "executedQty": response.get("executedQty"),
            "timeInForce": response.get("timeInForce"),
            "stopPrice": response.get("stopPrice"),
            "updateTime": response.get("updateTime"),
            "raw": response,
        }

    @staticmethod
    def _decimal_to_string(value: Decimal) -> str:
        return format(value.normalize(), "f")