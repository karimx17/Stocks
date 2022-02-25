from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Scrapper:
    def __init__(self, name_of_stock):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.cnbc.com/")
        self.driver.find_element(By.CLASS_NAME, "icon-search").click()
        self.driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(name_of_stock)
        self.driver.find_element(By.ID, "querySearchButton").click()

    # Grabbing relevant news of stock
    def news(self):
        for i in self.driver.find_elements(By.CLASS_NAME, "LatestNews-headline")[:5]:
            print(i.text)
        self.driver.quit()