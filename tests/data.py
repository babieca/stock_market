# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

# custom
from src.tickers import TickerSymbol
from src.stock import CommonStock, PreferredStock
from src.trade import TransactionType


''' Format: Stock Symbol, Stock Type, Last Dividend, Fixed Dividend, Par Value
'''
STOCKS = (
    (TickerSymbol.TEA, CommonStock, 0.0, None, 100.0),
    (TickerSymbol.POP, CommonStock, 8.0, None, 100.0),
    (TickerSymbol.ALE, CommonStock, 23.0, None, 60.0),
    (TickerSymbol.GIN, PreferredStock, 8.0, 0.02, 100.0),
    (TickerSymbol.JOE, CommonStock, 13.0, None, 250.0)
)

''' Format: Stock Symbol, Timestamp, Quantity, Price, Transaction Type
'''
TRADES = (
    (TickerSymbol.TEA, '2018-03-09T08:30:01', 100, 80.0, TransactionType.BUY),
    (TickerSymbol.TEA, '2018-03-09T08:30:02', 200, 72.0, TransactionType.BUY),
    (TickerSymbol.TEA, '2018-03-09T08:30:03', 50, 78.0, TransactionType.SELL),
    (TickerSymbol.TEA, '2018-03-09T08:30:04', 60, 77.5, TransactionType.SELL),
    (TickerSymbol.TEA, '2018-03-09T08:30:05', 100, 81.0, TransactionType.SELL),
    
    (TickerSymbol.POP, '2018-03-09T08:30:06', 5000, 102.0, TransactionType.BUY),
    (TickerSymbol.POP, '2018-03-09T08:30:07', 6000, 101.0, TransactionType.SELL),
    (TickerSymbol.POP, '2018-03-09T08:30:08', 2000, 98.0, TransactionType.BUY),
    (TickerSymbol.POP, '2018-03-09T08:30:09', 5000, 100.0, TransactionType.SELL),
    (TickerSymbol.POP, '2018-03-09T08:30:10', 1000, 105.0, TransactionType.BUY),
    
    (TickerSymbol.ALE, '2018-03-09T08:30:11', 20, 500.5, TransactionType.SELL),
    (TickerSymbol.ALE, '2018-03-09T08:30:12', 30, 501.0, TransactionType.SELL),
    (TickerSymbol.ALE, '2018-03-09T08:30:13', 50, 503.2, TransactionType.SELL),
    (TickerSymbol.ALE, '2018-03-09T08:30:14', 50, 507.6, TransactionType.BUY),
    (TickerSymbol.ALE, '2018-03-09T08:30:15', 50, 514.0, TransactionType.BUY),
    
    (TickerSymbol.GIN, '2018-03-09T08:30:16', 10, 20.0, TransactionType.BUY),
    (TickerSymbol.GIN, '2018-03-09T08:30:17', 10, 24.75, TransactionType.BUY),
    (TickerSymbol.GIN, '2018-03-09T08:30:18', 10, 16.5, TransactionType.BUY),
    (TickerSymbol.GIN, '2018-03-09T08:30:19', 10, 19.0, TransactionType.BUY),
    (TickerSymbol.GIN, '2018-03-09T08:30:20', 10, 15.4, TransactionType.BUY),
    
    (TickerSymbol.JOE, '2018-03-09T08:30:21', 20, 60.2, TransactionType.SELL),
    (TickerSymbol.JOE, '2018-03-09T08:30:22', 20, 59.0, TransactionType.SELL),
    (TickerSymbol.JOE, '2018-03-09T08:30:23', 20, 64.9, TransactionType.SELL),
    (TickerSymbol.JOE, '2018-03-09T08:30:24', 20, 64.4, TransactionType.SELL),
    (TickerSymbol.JOE, '2018-03-09T08:30:25', 20, 58.3, TransactionType.SELL),
)






