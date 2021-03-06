<br /><br />

## Stock Market

<br /><br />

This code is submitted as an answer to the assignment Super Simple Stocks Market
included in the hiring process at J.P.Morgan.
The full details of the assignment are in the document `doc/Homework Assignment - Super Simple Stocks.pdf`.

<br /><br />

## Requirements

<br /><br />

Application developed using Python 3.6.4.<br />
No non-standard packages are needed.<br />

<br /><br />

## Tested on   

<br /><br />

ARCH Linux version 4.15.6-1 x86_84<br />
BASH shell version 4.4.19(1)-release<br />
Eclipse IDE for C/C++ Developers; Version: Oxygen.2 Release (4.7.2)<br />
PyDev version 6.3.1<br />
   
<br /><br />

## Code structure and usage

<br /><br />

All the application is fully contained in the module `src`. <br /><br />
  - **Tickers file:** contains the universe of tickers (future improvements: store the list of tickers in a database). <br /><br />
  - **Stock file:** define a stock (common/preferred) and its attributes (ticker, dividend, par value, fixed dividend).
       `Stock` itself is an abstract objects. It can be created either calling `CommonStock` or `PreferredStock`. <br /><br />
  - **Trade file:** define a trade with its attributes (ticker, transaction type, price, quantity, timestamp). <br /><br />
  - **GBCE file:** records new transactions and calculates the GBCE All Share Index.

<br /><br />

##### The calculations requested in the assignment instructions can be accessed by the following properties or methods:

<br />

- For a given instance of `Stock`: <br /><br />
  1. Calculate the **dividend yield**: `Stock.dividend_yield` <br /><br />
  2. Calculate the **Price/Dividend ratio**(*): `Stock.price_dividend_ratio` <br /><br />
  3. Record a **trade, with timestamp, quantity of shares, buy or sell indicator and price**. <br /><br />
  4. Calculate the **VWAP (Volume Weighted Stock Price)** on trades recorded in past 5 minutes: `Stock.vwap` <br /><br />
  5. Calculate the **GBCE All Share Index** using the geometric mean of prices for all stocks: `GBCE.all_share_index`. <br /><br />


<br />

(*) *Note: The assignment requests to calculate PE as Price/Dividend.<br /> 
         The standard definition of PE is Price/Earnings Per Share and not Price/Dividend.
         For more details:<br /><br />
        - [P/E - Wikipedia](https://en.wikipedia.org/wiki/Price%E2%80%93earnings_ratio) <br />
        - [P/D - Wikipedia](https://en.wikipedia.org/wiki/Dividend_yield)* <br />

<br /><br />

## Installation

<br /><br />
Run the following command:
<br /><br />

```

$ git clone https://github.com/babieca/stock_market.git

$ cd stock_market/

$ python setup.py install  (it may require root access)


```

<br /><br />

## Tests

<br /><br />

A moderately extensive (although by no means exhaustive) suite of tests is included in `tests/`.
The structure of the `tests` folder is as follow: <br /><br />
  - **Data file**: contains the stocks and trades used for the tests files. <br /> <br /><br />
  - **Config folder**: contains the stock and trade configuration file. <br /><br />
       These files can be completely customised to meet the structure of the `data` file.
       If future improvements are done (i.e. using a database instead of a file with tuples as input),
       the config_xxx.py files could be adjusted accordingly to reflect those changes. <br /><br />
  - **Test_stock file**: a serie of tests of a stock using unittest module. The file reads the `data` file and perform the test. <br /><br />
  - **Test_trade file**: a serie of tests of a trades using unittest module. The file reads the `data` file and perform the test. <br /><br />
  - **Test_GBCE file**: a serie of tests of GBCE using unittest module. The file reads the `data` file and perform the test. <br /><br />

<br />

You can run each test from a text editor or using the following commands:

<br /><br />
```

$ cd ./tests/

$ python -m unittest -v test_stock.py

$ python -m unittest -v test_trade.py

$ python -m unittest -v test_GBCE.py

```

<br /><br />
