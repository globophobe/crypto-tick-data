from datetime import datetime
from typing import Callable

from django.db import models
from pandas import DataFrame

from cryptofeed_werks.constants import SymbolType


class BaseController:
    def __init__(
        self,
        symbol: models.Model,
        timestamp_from: datetime,
        timestamp_to: datetime,
        on_data_frame: Callable,
        retry: bool = False,
        verbose: bool = True,
    ):
        self.symbol = symbol
        self.timestamp_from = timestamp_from
        self.timestamp_to = timestamp_to
        self.on_data_frame = on_data_frame
        self.retry = retry
        self.verbose = verbose

    @property
    def log_format(self):
        symbol = str(self.symbol)
        return f"{symbol}: {{timestamp}}"

    @property
    def columns(self) -> list:
        SINGLE_SYMBOL_COLUMNS = [
            "uid",
            "timestamp",
            "nanoseconds",
            "price",
            "volume",
            "notional",
            "tickRule",
            "index",
        ]
        if self.symbol.symbol_type == SymbolType.FUTURE:
            return SINGLE_SYMBOL_COLUMNS[:-1] + ["expiry", "index"]
        else:
            return SINGLE_SYMBOL_COLUMNS

    def main(self):
        raise NotImplementedError

    def get_candles(
        self, timestamp_from: datetime, timestamp_to: datetime
    ) -> DataFrame:
        """Get candles."""
        raise NotImplementedError
