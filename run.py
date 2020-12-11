from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from sitemap import siteMap
from store import Store
import random
import time

class Run:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def iterate(self):
        for store in siteMap:
            parser: Store = siteMap[store]["parser"]
            for product in siteMap[store]["products"]:
                print("opening", product)
                jitter()
                self.driver.get(product)
                parser.prettyReport(self.driver)


def jitter(min = 1, max = 10):
    print("sleeping...")
    time.sleep(random.randint(min, max))
    print("ready...")