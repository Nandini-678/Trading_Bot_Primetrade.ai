from decimal import Decimal, InvalidOperation
from typing import Any, Dict, Optional

from bot.exceptions import ValidationError


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT", "STOP_LIMIT"}


def validate_symbol(symbol: str) -> str:
    if not symbol or not symbol.strip():
        raise ValidationError("Symbol is required.")

    cleaned_symbol = symbol.strip().upper()

    if " " in cleaned_symbol:
        raise ValidationError("Symbol must not contain spaces.")

    return cleaned_symbol


def validate_side(side: str) -> str:
    if not side or not side.strip():
        raise ValidationError("Side is required.")

    cleaned_side = side.strip().upper()

    if cleaned_side not in VALID_SIDES:
        raise ValidationError(f"Side must be one of: {', '.join(sorted(VALID_SIDES))}.")

    return cleaned_side


def validate_order_type(order_type: str) -> str:
    if not order_type or not order_type.strip():
        raise ValidationError("Order type is required.")

    cleaned_order_type = order_type.strip().upper()

    if cleaned_order_type not in VALID_ORDER_TYPES:
        raise ValidationError(
            f"Order type must be one of: {', '.join(sorted(VALID_ORDER_TYPES))}."
        )

    return cleaned_order_type


def validate_positive_decimal(value: Any, field_name: str) -> Decimal:
    if value is None or str(value).strip() == "":
        raise ValidationError(f"{field_name} is required.")

    try:
        decimal_value = Decimal(str(value).strip())
    except (InvalidOperation, ValueError):
        raise ValidationError(f"{field_name} must be a valid number.")

    if decimal_value <= 0:
        raise ValidationError(f"{field_name} must be greater than 0.")

    return decimal_value


def validate_order_inputs(
    symbol: str,
    side: str,
    order_type: str,
    quantity: Any,
    price: Optional[Any] = None,
    stop_price: Optional[Any] = None,
) -> Dict[str, Any]:
    validated_symbol = validate_symbol(symbol)
    validated_side = validate_side(side)
    validated_order_type = validate_order_type(order_type)
    validated_quantity = validate_positive_decimal(quantity, "Quantity")

    validated_data: Dict[str, Any] = {
        "symbol": validated_symbol,
        "side": validated_side,
        "order_type": validated_order_type,
        "quantity": validated_quantity,
    }

    if validated_order_type == "LIMIT":
        validated_price = validate_positive_decimal(price, "Price")
        validated_data["price"] = validated_price

    elif validated_order_type == "STOP_LIMIT":
        validated_price = validate_positive_decimal(price, "Price")
        validated_stop_price = validate_positive_decimal(stop_price, "Stop price")
        validated_data["price"] = validated_price
        validated_data["stop_price"] = validated_stop_price

    return validated_data