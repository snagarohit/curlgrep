from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from abc import ABC, abstractmethod

class Store(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def isOutOfStock(self, driver: webdriver.Chrome):
        return False

    @abstractmethod
    def getPrice(self, driver: webdriver.Chrome):
        return 0

    @abstractmethod
    def getTitle(self, driver: webdriver.Chrome):
        return "Title"

    def prettyReport(self, driver: webdriver.Chrome):
        print(self.getTitle(driver), "is Out of stock" if self.isOutOfStock(driver) else "is In stock", "for", self.getPrice(driver))