import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv

from bot.exceptions import ConfigurationError


load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_key: str
    api_secret: str
    base_url: str


def _get_env_var(name: str, required: bool = True, default: Optional[str] = None) -> str:
    value = os.getenv(name, default)

    if required and (value is None or not value.strip()):
        raise ConfigurationError(f"Missing required environment variable: {name}")

    return value.strip() if value else ""


def get_settings() -> Settings:
    return Settings(
        api_key=_get_env_var("BINANCE_API_KEY"),
        api_secret=_get_env_var("BINANCE_API_SECRET"),
        base_url=_get_env_var("BINANCE_BASE_URL", default="https://testnet.binancefuture.com"),
    )