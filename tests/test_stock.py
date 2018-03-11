#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from datetime import timedelta

sys.path.append("..")

# custom
from data import TRADES, STOCKS

from src.tickers import TickerSymbol
from src.stock import Stock, CommonStock, PreferredStock
from config.config_trade import ConfigTrade
from config.config_stock import ConfigStock


class StockInitTestCase(unittest.TestCase):

    
    def test_not_instantiable(self):
        ''' Test if CommonStock or PreferredStocks are created accordingly.
        The test will rise an error (pass) if CommonStock or PreferredStock
        contain a missing argument. The test will also rise an error (pass)
        if we access Stock() directly without previously defining the dividend 
        property (abstract method)
        '''
        with self.assertRaises(TypeError):
            ''' Correct way to create a new CommonStock:
                    stock = CommonStock(ticker_symbol=TickerSymbol.TEA, par_value=100, last_dividend=1)
            '''
            stock1 = Stock(ticker_symbol=TickerSymbol.TEA, par_value=100)
            stock2 = CommonStock(ticker_symbol=TickerSymbol.TEA, par_value=100)


class StockRecordTradeTestCase(unittest.TestCase):

    ''' Set for all the tests in the class the stock
    before running the test
    '''
    def setUp(self):
        self.stock = ConfigStock(STOCKS).get_stock()

    def test_checks_type(self):
        ''' Test if a wrong value for a trade for a particular stock will
        rise an error. If a wrong value raises the error, the test will pass.
        '''
        
        ''' A correct value is (timestamp, quantity, price, buy/sell indicator)
        '''
        wrong_value = ('wrong', 'value')

        with self.assertRaises(TypeError):
            self.stock.record_trade(wrong_value)

    def test_trade_is_recorded(self):

        trade = ConfigTrade(TRADES).get_trade()
        self.stock.record_trade(trade)

        self.assertIn(trade, self.stock.trades)

    def test_checks_ticker_symbol(self):
        ale_stock = ConfigStock(STOCKS).get_stock_by_ticker_symbol(TickerSymbol.ALE)
        tea_trade = ConfigTrade(TRADES).get_trade_for_stock(TickerSymbol.TEA)
        with self.assertRaises(ValueError):
            ale_stock.record_trade(tea_trade)


class StockTickerPriceTestCase(unittest.TestCase):

    def setUp(self):
        self.stock = ConfigStock(STOCKS).get_stock()

    def test_empty_trades_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            ticker_price = self.stock.ticker_price

    def test_price_value(self):
        trade = ConfigTrade(TRADES).get_trade()
        self.stock.record_trade(trade)
        self.assertEqual(trade.price, self.stock.ticker_price)

    def test_price_value_is_last_trades(self):
        trades = ConfigTrade(TRADES).get_trades(3)
        last_trade = trades[-1]
        for trade in trades:
            self.stock.record_trade(trade)
        self.assertEqual(last_trade.price, self.stock.ticker_price)


class StockPriceDividendRatioTestCase(unittest.TestCase):

    def test_zero_dividend_stock_returns_none(self):
        zero_dividend_stock = ConfigStock(STOCKS).get_zero_dividend_stock()
        trade = ConfigTrade(TRADES).get_trade()
        zero_dividend_stock.record_trade(trade)
        pd_ratio = zero_dividend_stock.price_dividend_ratio
        self.assertEqual(pd_ratio, 0)


class StockPriceTestCase(unittest.TestCase):

    def setUp(self):
        self.stock = ConfigStock(STOCKS).get_stock()

    def test_not_enough_significant_trades_returns_none(self):
        trade = ConfigTrade(TRADES).get_trade()
        self.stock.record_trade(trade)

        stock_price = self.stock.vwap()
        self.assertEqual(stock_price, 0)

    def test_price_value_for_one_trade(self):
        trade = ConfigTrade(TRADES).get_trade()
        self.stock.record_trade(trade)
        current_time = trade.timestamp + timedelta(minutes=5)

        expected_value = trade.price
        self.assertEqual(self.stock.vwap(current_time), expected_value)

    def test_price_value_for_multiple_trades(self):
        trades = ConfigTrade(TRADES).get_trades_for_stock(TickerSymbol.TEA)
        for trade in trades:
            self.stock.record_trade(trade)

        # Set the most recent trade timestamp as current_time.
        by_timestamp = sorted(trades,
                              key=lambda t: t.timestamp,
                              reverse=True)

        last_trade = by_timestamp[0]
        selected_trades = [trade for trade in trades
                              if trade.timestamp >=
                              last_trade.timestamp - self.stock.price_time_interval]
        pxvol = shares = 0
        for trade in selected_trades:
            pxvol= pxvol + (trade.price * trade.quantity)
            shares = shares + trade.quantity
        expected_value = 0 if shares==0 else (pxvol / shares)

        self.assertEqual(self.stock.vwap(last_trade.timestamp), expected_value)


class CommonStockDividendTestCase(unittest.TestCase):

    def setUp(self):
        self.stock = ConfigStock(STOCKS).get_common_stock()

    def test_dividend_value(self):
        expected_value = self.stock.last_dividend
        self.assertEqual(self.stock.dividend, expected_value)


class PreferredStockDividendTestCase(unittest.TestCase):

    def setUp(self):
        self.stock = ConfigStock(STOCKS).get_preferred_stock()

    def test_dividend_value(self):
        expected_value = self.stock.fixed_dividend * self.stock.par_value
        self.assertEqual(self.stock.dividend, expected_value)


if __name__ == '__main__':
    
    unittest.main()
    

