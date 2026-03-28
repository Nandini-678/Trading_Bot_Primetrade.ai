class TradingBotError(Exception):
    """Base exception for the trading bot."""


class ConfigurationError(TradingBotError):
    """Raised when required configuration is missing or invalid."""


class ValidationError(TradingBotError):
    """Raised when user input is invalid."""


class APIError(TradingBotError):
    """Raised when an external API request fails."""