from stocks import Polygon
from scrapping import Scrapper

stocks = Polygon()
stocks.percent_change()

scrapping = Scrapper(stocks.stocks_ticker)
scrapping.news()
