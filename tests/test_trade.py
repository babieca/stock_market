#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.append("..")

# custom
from data import TRADES, STOCKS

from src.trade import Trade
from config.config_trade import ConfigTrade


class TradeInitTestCase(unittest.TestCase):

    def setUp(self):
        self.trade = ConfigTrade(TRADES).get_trade()

    def test_raises_value_error_on_non_positive_qty(self):
        with self.assertRaises(ValueError):
            bad_trade = Trade(ticker_symbol=self.trade.ticker_symbol,
                              timestamp=self.trade.timestamp,
                              quantity=0,
                              price=self.trade.price,
                              trans_type=self.trade.trans_type)

    def test_raises_value_error_on_negative_price(self):
        with self.assertRaises(ValueError):
            bad_trade = Trade(ticker_symbol=self.trade.ticker_symbol,
                              timestamp=self.trade.timestamp,
                              quantity=self.trade.quantity,
                              price=-25.0,
                              trans_type=self.trade.trans_type)


if __name__ == '__main__':
    
    unittest.main()
    


