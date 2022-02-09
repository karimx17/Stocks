import requests
import datetime as dt


class Polygon:
    def __init__(self):
        # POLYGON API CALL
        self.stocks_ticker = input("What stock would you like to see?\nExample:'TSLA'\n").upper()
        api_key = "CakcO4loX4fU6bL78tHmrzOtop5dL_ZB"

        current_day_info = f"https://api.polygon.io/v1/open-close/{self.stocks_ticker}/{self.day_of_week(dt.date.today())}?apiKey={api_key}"

        previous_day_info = f"https://api.polygon.io/v1/open-close/{self.stocks_ticker}/{self.day_of_week(self.yesterday())}?apiKey={api_key}"

        self.response_current = requests.get(current_day_info)
        self.response_previous = requests.get(previous_day_info)

        # CHECKING WHAT DAY WE ARE CURRENTLY ON, IF MONDAY: GRAB FRIDAY AS PREVIOUS DAY, ELSE CURRENT DAY - 1
    def day_of_week(self, today):
        if int(today.strftime('%w')) == 1:
            today -= dt.timedelta(days=3)
            return today

        elif int(today.strftime('%w')) == 0:
            today -= dt.timedelta(days=2)
            return today

        elif int(today.strftime('%w')) == 6:
            today -= dt.timedelta(days=1)
            return today
        else:
            today -= dt.timedelta(days=1)
            return today

    def yesterday(self):
        before_yes = dt.date.today() - dt.timedelta(days=1)
        return before_yes

    # CALCULATING AND RETURNING THE PERCENT CHANGE FOR A GIVEN STOCK
    def percent_change(self):
        current_day_close = float(self.response_current.json()["close"])
        previous_day_close = float(self.response_previous.json()["close"])
        change = round(((current_day_close - previous_day_close) / previous_day_close) * 100, 2)
        print(f"{self.stocks_ticker} is", "Up" if change > 0 else "down", f"{change}%")
