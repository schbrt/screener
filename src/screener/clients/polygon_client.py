from polygon import RESTClient
import pyarrow as pa
import pyarrow.parquet as pq
from screener.models import Quote, OHLC


class PolygonClient:
    def __init__(self):
        self.client = RESTClient()

    def fetch_previous_close(self, ticker: str) -> Quote:
        quote = self.client.get_previous_close_agg(ticker)[0]
        return OHLC(
            ticker=quote.ticker,
            open=quote.open,
            high=quote.high,
            low=quote.low,
            close=quote.close,
            timestamp=quote.timestamp,
            volume=quote.volume,
        )

    def fetch_full_market_data(self, date: str) -> list[OHLC]:
        """
        @param date: date of the form "2024-01-01"
        Return list of closes for the entire market
        """

        ohlcs = self.client.get_grouped_daily_aggs(date)
        output_fname = f"{date}_ohlc_data.parquet"
        ohlc_list = [ohlc.__dict__ for ohlc in ohlcs]
        ohlc_table = pa.Table.from_pylist(ohlc_list)
        pq.write_table(ohlc_table, output_fname)
