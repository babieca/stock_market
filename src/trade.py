# -*- coding: utf-8 -*-

import enum
from datetime import datetime

# custom modules
from .tickers import TickerSymbol

@enum.unique
class TransactionType(enum.Enum):

    """Indicator to buy or sell that accompanies each trade"""

    BUY = 1
    SELL = -1


class Trade:

    """A change of ownership of a collection of shares at a definite price per share"""

    def __init__(self,
                 ticker_symbol: TickerSymbol,
                 timestamp: datetime,
                 quantity: int,
                 price: float,
                 trans_type: TransactionType):
        """
        :param timestamp: The moment when the transaction has taken place
        :param quantity: The amount of shares exchanged
        :param price: Price for each share
        :param trans_type: Indication to buy or sell
        """

        self.ticker_symbol = ticker_symbol
        self.timestamp = timestamp

        if quantity > 0:
            self.quantity = quantity
        else:
            msg = "The quantity of shares has to be positive."
            raise ValueError(msg)

        if price >= 0.0:
            self.price = price
        else:
            msg = "The price per share can not be negative."
            raise ValueError(msg)

        self.trans_type = trans_type


