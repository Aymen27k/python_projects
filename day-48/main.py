from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "/usr/local/bin/chromedriver"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
xpath = driver.find_element(By.XPATH, "/html/body/div/footer/div[1]/div/ul/li[4]/ul/li[9]/a")
print(xpath.text)

""" search_box = driver.find_element(By.ID, "searchbox_input")
print("Found the search box")
search_box.send_keys("do a barrel roll")
search_box.send_keys(Keys.ENTER)
time.sleep(5)
 """

driver.quit()
