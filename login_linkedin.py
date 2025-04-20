from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time

# Load credentials from .env
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

if not USERNAME or not PASSWORD:
    raise ValueError("USERNAME and PASSWORD must be set in the .env file")

# Set up Chrome driver in headless mode
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    # Fill in login form
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    # Wait for login to process
    time.sleep(5)

    # Check if login was successful
    try:
        driver.find_element(By.ID, 'profile-nav-item')
        print("Login successful!")
    except NoSuchElementException:
        print("Login may have failed. Please check your credentials.")

finally:
    driver.quit()
