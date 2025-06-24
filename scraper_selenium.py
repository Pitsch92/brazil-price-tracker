import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time
import random

# Automatically install and use the correct ChromeDriver
chromedriver_autoinstaller.install()


def selenium_scraper(url):
    
    # Start the browser
    driver = webdriver.Chrome()
    
    # Automatically install and use the correct ChromeDriver
    chromedriver_autoinstaller.install()

    # Start the browser
    driver = webdriver.Chrome()
    
    # Go to the target page
    driver.get(url)

    # Wait for the page to load (adjust as needed)
    time.sleep(random.randint(5, 15))  # Random sleep between 5 and 10 seconds

    # Get the full rendered HTML
    html = driver.page_source

    # Parse with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    driver.quit()
    return soup


