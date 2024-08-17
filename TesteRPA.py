from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


driver = webdriver.Chrome()
driver.get("https://rpachallenge.com/")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Start')]"))
)
start_button = driver.find_element(By.XPATH, "//button[contains(text(),'Start')]")
start_button.click()


df = pd.read_excel('challenge.xlsx')



WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelPhone']"))
)

for index, row in df.iterrows():
    data = {
        "First Name": row['First Name'],
        "Last Name": row['Last Name '],
        "Company Name": row['Company Name'],
        "Role": row['Role in Company'],
        "Address": row['Address'],
        "Email": row['Email'],
        "Phone": row['Phone Number']
    }

    for field, value in data.items():
        input_element = driver.find_element(By.XPATH, f"//input[@ng-reflect-name='label{field.replace(' ', '')}']")
        input_element.clear()
        input_element.send_keys(str(value))

    submit_button = driver.find_element(By.XPATH, "//input[@value='Submit']")
    submit_button.click()
    time.sleep(2)


