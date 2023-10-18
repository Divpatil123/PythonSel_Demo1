from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://the-internet.herokuapp.com/upload')
driver.maximize_window()
driver.find_element(By.ID, 'file-upload').send_keys("C:\\Users\\Lenov\\Desktop\\File1.docx")
driver.find_element(By.XPATH,'//*[@id="file-submit"]').click()