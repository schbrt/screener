import requests
from pydantic import BaseModel

class Quote(BaseModel):
    symbol: str
    price: int

def retrieve_symbol_data(symbol: str, start_date: str, end_date: str) -> Quote:

