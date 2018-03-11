#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

sys.path.append("..")

# custom
from data import TRADES, STOCKS

from src.GBCE import GlobalBeverageCorporationExchange as GBCE
from src.tickers import TickerSymbol
from config.config_trade import ConfigTrade
from config.config_stock import ConfigStock


class GBCEInitTestCase(unittest.TestCase):

    def test_checks_empty_stocks(self):
        with self.assertRaises(ValueError):
            gbce = GBCE([])


class GBCERecordAllShareIndexTestCase(unittest.TestCase):

    def test_not_enough_significant_trades_returns_none(self):
        stocks = ConfigStock(STOCKS).get_stocks()
        gbce = GBCE(stocks)
        index = gbce.all_share_index()
        self.assertEqual(index, 0)

    def test_index_value(self):

        tea_stock = ConfigStock(STOCKS).get_stock_by_ticker_symbol(TickerSymbol.TEA)
        gin_stock = ConfigStock(STOCKS).get_stock_by_ticker_symbol(TickerSymbol.GIN)
        gbce = GBCE([tea_stock, gin_stock])

        tea_stock_trades = ConfigTrade(TRADES).get_trades_for_stock(TickerSymbol.TEA)
        gin_stock_trades = ConfigTrade(TRADES).get_trades_for_stock(TickerSymbol.GIN)

        for trade in tea_stock_trades + gin_stock_trades:
            gbce.record_trade(trade)

        last_tea_stock_trade = sorted(tea_stock_trades,
                                      key=lambda t: t.timestamp,
                                      reverse=True)[0]
        last_gin_stock_trade = sorted(gin_stock_trades,
                                      key=lambda t: t.timestamp,
                                      reverse=True)[0]

        current_time = max([last_tea_stock_trade.timestamp,
                            last_gin_stock_trade.timestamp])
        tea_stock_price = tea_stock.vwap(current_time)
        gin_stock_price = gin_stock.vwap(current_time)
        expected_value = (tea_stock_price * gin_stock_price)**(1/2)

        self.assertEqual(gbce.all_share_index(current_time), expected_value)



if __name__ == '__main__':
    
    unittest.main()
    





