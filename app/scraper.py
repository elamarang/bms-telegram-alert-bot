from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

SELENIUM_URL = os.getenv("SELENIUM_REMOTE_URL")

def get_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return webdriver.Remote(
        command_executor=SELENIUM_URL,
        options=options
    )

def get_showtimes(url, theatre_filter=None):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)

    elements = driver.find_elements(By.XPATH, "//a[contains(text(),':')]")

    shows = []

    for el in elements:
        text = el.text.strip()

        if theatre_filter:
            parent = el.find_element(By.XPATH, "./ancestor::div")
            if theatre_filter.lower() not in parent.text.lower():
                continue

        shows.append(text)

    driver.quit()
    return list(set(shows))
