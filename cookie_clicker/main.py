import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


is_clicking = True
last_check_time = time.time()

chrome_driver_path = "/usr/local/bin/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
print("Website opened successfully")

cookie = driver.find_element(By.ID, "cookie")

def check_prices():
    for item in items:
        item_id = item.get_attribute("id")
        try:
            b_element = item.find_element(By.TAG_NAME, "b")
            raw = b_element.text
            item_price = raw.split("-")[-1].strip()
        except:
            item_price = ("N/A")
        upgrades_price.append((item_id, item_price))
    return upgrades_price

upgrades_price = []
expensive_item = 0

while is_clicking:
    cookie.click()
    current_time = time.time()
    money = driver.find_element(By.ID, "money").text
    store = driver.find_element(By.ID, "store")
    if current_time - last_check_time >= 5:
        items = store.find_elements(By.XPATH, "./div")
        print("5 seconds have Passed! Checking upgrades...")
        print(money)
        store_list = check_prices()
        for item in store_list:
            if item[1] != "":
                item_cost = item[1].replace("," , ".").replace(".", "")
                item_cost = float(item_cost)
                actual_money = float(money.replace(",", ""))
                if (item_cost > expensive_item) and (float(actual_money) >= item_cost):
                    expensive_item = item_cost
                    affordable_item = item[0]
                    print(f"The name of the affordable item : {affordable_item}")
                    item_to_buy = driver.find_element(By.ID, affordable_item)
                    item_to_buy.click()
        last_check_time = time.time()
""" for item_id, item_price in upgrades_price:
            print(f"{item_id}: {item_price}") """