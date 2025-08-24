import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

load_dotenv()
LOGIN = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")

chrome_driver_path = "/usr/local/bin/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

def main():
    """Get the To-do From me and then add it to my website automatically
    """
    try:
        #Get Users To-do Input
        task = input("Hey Aymen !\nWhat task would you like to add ?: ")
    # 1. Navigate to the main page and then to the login page
        driver.get("http://localhost:5173/")
        print("Website accessed successfully!")

        # Wait for the link to the To-Do list to be clickable before we click it
        wait = WebDriverWait(driver, 10)
        to_do_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/header/nav/a[4]")))
        to_do_link.click()
        print("Reached the To-Do login Page!")

        # 2. Add a simple sleep to give the page time to load and render the elements
        time.sleep(2)

        # 3. Find the username and password input fields and the login button
        username_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

        # 4. Use the send_keys() method to type the credentials
        username_input.send_keys(LOGIN)
        password_input.send_keys(PASSWORD)

        # 5. Click the login button to submit the form
        login_button.click()
        print("Login successful!")

        time.sleep(2)

        task_input = driver.find_element(By.CLASS_NAME, "new-task-input")
        task_input.click()
        task_input.send_keys(task)
        driver.find_element(By.CLASS_NAME, "add-todo-button").click()
    except Exception as e:
        print(f"Something went wrong - {e}")
    finally:
        time.sleep(5)




if __name__ == "__main__":
    main()