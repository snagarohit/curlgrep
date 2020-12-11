
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from store import Store


class Walmart(Store):
    def __init__(self):
        super().__init__()

    def isOutOfStock(self, driver: webdriver.Chrome):
        fullText = driver.find_element_by_tag_name('body').text
        if "Out of stock" in fullText:
            return True
        return False

    def getPrice(self, driver: webdriver.Chrome):
        return int(driver.find_element_by_id('product-overview').find_element_by_class_name('price').find_element_by_class_name('price-characteristic').text)

    def getTitle(self, driver: webdriver.Chrome):
        return driver.find_element_by_class_name('prod-ProductTitle').text

