from stocks import Polygon
from scrapping import Scrapper

# IF YOU ARE A RECRUITER AND ARE NOT FAMILIAR WITH PYTHON, SHOW THIS TO A SOFTWARE DEVELOPER AND THEY CAN RUN IT


stocks = Polygon()
stocks.percent_change()

scrapping = Scrapper(stocks.stocks_ticker)
scrapping.news()
