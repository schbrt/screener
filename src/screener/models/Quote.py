from pydantic import BaseModel


class Quote(BaseModel):
    symbol: str
    price: float
    timestamp: int
