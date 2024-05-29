from abc import ABC, abstractmethod

from screener.models import OHLC


class Client(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    @abstractmethod
    def fetch_previous_close(symbol: str) -> OHLC:
        pass
