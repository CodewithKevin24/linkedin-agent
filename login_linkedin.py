import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv, find_dotenv

# Load .env if present, then environment variables (override with actual secrets)
load_dotenv(find_dotenv(), override=True)

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

if not USERNAME or not PASSWORD:
    raise ValueError("USERNAME and PASSWORD must be set in environment variables")

# Configure Chrome for headless execution
toptions = Options()
toptions.add_argument('--headless')
toptions.add_argument('--no-sandbox')
toptions.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=toptions)

try:
    driver.get('https://www.linkedin.com/login')

    # Input credentials
tusername = driver.find_element(By.ID, 'username')
tpassword = driver.find_element(By.ID, 'password')

tusername.send_keys(USERNAME)
tpassword.send_keys(PASSWORD)
tpassword.send_keys(Keys.RETURN)

    # Wait for login to complete
time.sleep(5)

    # Verify login
ttry:
        driver.find_element(By.ID, 'profile-nav-item')
        print("Login successful!")
    except NoSuchElementException:
        print("Login failed. Check credentials.")
finally:
    driver.quit()
