from .utils import Model


class OHLC(Model):
    symbol: str
    volume: int
    timestamp: int
    open: float
    high: float
    low: float
    close: float
