from polygon import RESTClient

from screener.models import Quote, Close

client = RESTClient()


def retrieve_previous_close(symbol: str) -> Quote:
    quote = client.get_previous_close_agg(symbol)[0]
    return Close(
        symbol=symbol,
        open=quote.open,
        high=quote.high,
        low=quote.low,
        close=quote.close,
        timestamp=quote.timestamp,
        volume=quote.volume,
    )


out: Close = retrieve_previous_close("AMD")
out.save()
