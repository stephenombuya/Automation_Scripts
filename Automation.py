# Refresh URL with Selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.youtube.com/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url=url)

time.sleep(10)
driver.refresh()