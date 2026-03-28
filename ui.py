import streamlit as st
import pandas as pd
from datetime import datetime

from bot.exceptions import TradingBotError, ValidationError
from bot.orders import OrderService
from bot.validators import validate_order_inputs


st.set_page_config(
    page_title="Trading Bot UI",
    page_icon="📈",
    layout="centered",
)

st.title("📈 Binance Futures Testnet Trading Bot")
st.caption("Place MARKET, LIMIT, and STOP_LIMIT orders on Binance Futures Testnet.")

st.markdown("---")


def format_timestamp(value):
    if value in (None, "", "N/A"):
        return "N/A"
    try:
        ts = int(value)
        return datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return str(value)


def display_request_summary(validated_data: dict) -> None:
    st.subheader("Order Request Summary")
    rows = [{"Field": key, "Value": str(value)} for key, value in validated_data.items()]
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)


def display_response_summary(result: dict) -> None:
    st.subheader("Order Response Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Order ID", result.get("orderId", "N/A"))
    col2.metric("Status", result.get("status", "N/A"))
    col3.metric("Executed Qty", result.get("executedQty", "N/A"))

    col4, col5, col6 = st.columns(3)
    col4.metric("Symbol", result.get("symbol", "N/A"))
    col5.metric("Side", result.get("side", "N/A"))
    col6.metric("Type", result.get("type", "N/A"))


def display_response_details(result: dict) -> None:
    st.subheader("Order Response Details")

    left, right = st.columns(2)

    with left:
        st.markdown("**Core Details**")
        st.write(f"**Price:** {result.get('price', 'N/A')}")
        st.write(f"**Average Price:** {result.get('avgPrice', 'N/A')}")
        st.write(f"**Original Quantity:** {result.get('origQty', 'N/A')}")
        st.write(f"**Executed Quantity:** {result.get('executedQty', 'N/A')}")

    with right:
        st.markdown("**Execution Details**")
        st.write(f"**Time in Force:** {result.get('timeInForce', 'N/A')}")
        st.write(f"**Stop Price:** {result.get('stopPrice', 'N/A')}")
        st.write(f"**Updated At:** {format_timestamp(result.get('updateTime'))}")

    with st.expander("View Raw API Response"):
        st.json(result.get("raw", {}))


with st.container(border=True):
    st.subheader("Place an Order")

    with st.form("order_form"):
        common_symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "XRPUSDT", "CUSTOM"]
        symbol_choice = st.selectbox("Symbol", options=common_symbols)

        if symbol_choice == "CUSTOM":
            symbol = st.text_input(
                "Custom Symbol",
                value="",
                placeholder="e.g. ADAUSDT",
                help="Enter any valid Binance Futures symbol",
            )
        else:
            symbol = symbol_choice

        side = st.selectbox("Side", options=["BUY", "SELL"])
        order_type = st.selectbox("Order Type", options=["MARKET", "LIMIT", "STOP_LIMIT"])
        quantity = st.text_input("Quantity", value="0.002")

        price = None
        stop_price = None

        if order_type in ["LIMIT", "STOP_LIMIT"]:
            price = st.text_input(
                "Price",
                value="",
                help="Required for LIMIT and STOP_LIMIT orders",
                placeholder="e.g. 120000",
            )

        if order_type == "STOP_LIMIT":
            stop_price = st.text_input(
                "Stop Price",
                value="",
                help="Required for STOP_LIMIT orders",
                placeholder="e.g. 69500",
            )

        submitted = st.form_submit_button("Place Order", use_container_width=True)


if order_type == "MARKET":
    st.info("MARKET orders execute immediately at the best available price.")
elif order_type == "LIMIT":
    st.info("LIMIT orders require a price and are placed at that price or better.")
elif order_type == "STOP_LIMIT":
    st.info("STOP_LIMIT orders require both a trigger price and a limit price.")

st.caption("Note: The initial Binance create-order response may not always reflect the final filled state immediately.")


if submitted:
    try:
        validated_data = validate_order_inputs(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price,
        )

        display_request_summary(validated_data)

        order_service = OrderService()
        result = order_service.place_order(validated_data)

        st.success("Order placed successfully.")
        display_response_summary(result)
        display_response_details(result)

    except ValidationError as exc:
        st.error(f"Validation Error: {exc}")

    except TradingBotError as exc:
        st.error(f"Application Error: {exc}")

    except Exception as exc:
        st.error(f"Unexpected Error: {exc}")