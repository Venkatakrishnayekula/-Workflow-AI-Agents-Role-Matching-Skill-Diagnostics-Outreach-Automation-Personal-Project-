import json
from selenium import webdriver
from selenium.webdriver.common.by import By

def load_user_settings():
    with open("user_settings.json") as f:
        return json.load(f)

def fill_form(url, user_data):
    driver = webdriver.Chrome()
    driver.get(url) 
    # Basic field autofill logic
    for key, value in user_data.items():
        try:
            field = driver.find_element(By.NAME, key)
            field.clear()
            field.send_keys(value)
        except Exception as e:
            print(f"Error with field {key}: {str(e)}")
    driver.quit()

def auto_apply():
    with open("userdata.json") as f:
        user_data = json.load(f)
    with open("../dashboard/job_queue.json") as f:
        jobs = json.load(f)
    for job in jobs:
        fill_form(job['link'], user_data)