import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from bot.exceptions import TradingBotError, ValidationError
from bot.orders import OrderService
from bot.validators import validate_order_inputs


app = typer.Typer(
    help="Binance Futures Testnet Trading Bot CLI",
    no_args_is_help=True,
)
console = Console()


@app.callback()
def main() -> None:
    """Trading bot CLI."""
    pass


def print_order_summary(validated_data: dict) -> None:
    table = Table(title="Order Request Summary")
    table.add_column("Field", style="bold")
    table.add_column("Value")

    for key, value in validated_data.items():
        table.add_row(str(key), str(value))

    console.print(table)


def print_order_response(result: dict) -> None:
    table = Table(title="Order Response Details")
    table.add_column("Field", style="bold")
    table.add_column("Value")

    fields_to_show = [
        "orderId",
        "symbol",
        "status",
        "side",
        "type",
        "price",
        "avgPrice",
        "origQty",
        "executedQty",
        "timeInForce",
        "stopPrice",
        "updateTime",
    ]

    for field in fields_to_show:
        table.add_row(field, str(result.get(field)))

    console.print(table)


@app.command("place-order")
def place_order(
    symbol: str = typer.Option(..., help="Trading symbol, e.g. BTCUSDT"),
    side: str = typer.Option(..., help="Order side: BUY or SELL"),
    order_type: str = typer.Option(..., "--order-type", help="Order type: MARKET, LIMIT, STOP_LIMIT"),
    quantity: str = typer.Option(..., help="Order quantity"),
    price: str = typer.Option(None, help="Price required for LIMIT and STOP_LIMIT"),
    stop_price: str = typer.Option(None, "--stop-price", help="Stop price required for STOP_LIMIT"),
) -> None:
    try:
        validated_data = validate_order_inputs(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price,
        )

        print_order_summary(validated_data)

        order_service = OrderService()
        result = order_service.place_order(validated_data)

        print_order_response(result)

        console.print(Panel.fit("Order placed successfully.", title="Success"))

    except ValidationError as exc:
        console.print(Panel.fit(str(exc), title="Validation Error"))

    except TradingBotError as exc:
        console.print(Panel.fit(str(exc), title="Application Error"))

    except Exception as exc:
        console.print(Panel.fit(f"Unexpected error: {exc}", title="Unexpected Error"))


if __name__ == "__main__":
    app()