# Relative XPath
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rudramtech.in/billing-inventory/index.php")
print(driver.title)

driver.find_element(By.XPATH, "//input[@name='txtregno']").send_keys("9689")
#time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword']").send_keys("billing@2023#(*)")
#time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='Login']").click()
#time.sleep(2)

# Buy Product
driver.find_element(By.XPATH, "//*[@id='accordionSidebar']/li[2]/a/span").click()
driver.find_element(By.XPATH,"//input[@name='txtsbdate']").send_keys("13-09-2023")
driver.find_element(By.XPATH, "//input[@name= 'txtvendn']").send_keys("Divya Patil")
driver.find_element(By.XPATH, "//input[@name='txtvendmobile']").send_keys("9876543210")

