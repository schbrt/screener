from polygon import RESTClient

from screener.models import Quote

client = RESTClient()


def retrieve_previous_close(symbol: str) -> Quote:
    quote = client.get_previous_close_agg(symbol)[0]
    return Quote(symbol=symbol, price=quote.close, timestamp=quote.timestamp)


out: Quote = retrieve_previous_close("AMD")
print(out)
