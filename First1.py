import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.facebook.com/login.php")
print(driver.title)
driver.maximize_window()
time.sleep(2)
driver.minimize_window()
