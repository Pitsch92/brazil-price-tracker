import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install()

def selenium_scraper(url, css_selector_price):
    # Start the browser
    driver = webdriver.Chrome()

    try:
        # Go to the target page
        driver.get(url)

        # Wait up to 15 seconds for price elements to be present
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector_price)))

        # Once elements are loaded, get the full rendered HTML
        html = driver.page_source

        # Parse with BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

    finally:
        driver.quit()

    return soup
