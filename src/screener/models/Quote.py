from .utils import Model


class Quote(Model):
    symbol: str
    price: float
    timestamp: int
