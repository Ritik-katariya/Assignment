from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import uuid
import os
from src.database.mongo_utils import insert_record
from src.selenium.config import TWITTER_USERNAME, TWITTER_PASSWORD, PROXYMESH_URL

def scrape_trending_topics():
    options = webdriver.ChromeOptions()
    
    # Set up ProxyMesh if available
    # if PROXYMESH_URL:
    #     options.add_argument(f'--proxy-server={PROXYMESH_URL}')
    
    driver = webdriver.Chrome()

    try:
        # Log in to Twitter
        driver.get("https://x.com/login")
        driver.implicitly_wait(10)  # Adjust as needed

        try:
            # Enter username
            username = driver.find_element(By.NAME, "text")
            username.send_keys(TWITTER_USERNAME)
            username.send_keys(Keys.RETURN)
            driver.implicitly_wait(5)

            # Enter password
            password = driver.find_element(By.NAME, "password")
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.RETURN)
            driver.implicitly_wait(5)
        except NoSuchElementException as e:
            print(f"Error during login: {e}")
            return {"status": "error", "message": "Login failed."}

        # Scrape trending topics
        try:
            trends = driver.find_elements(By.CLASS_NAME, "css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3")
            for trend in trends:
                print(trend.text)
            trend_names = [trend.text for trend in trends]
        except NoSuchElementException as e:
            print(f"Error scraping trends: {e}")
            return {"status": "error", "message": "Failed to scrape trends."}

        # Generate unique ID and add metadata
        unique_id = str(uuid.uuid4())
        record = {
            "_id": unique_id,
            "trends": trend_names,
            "datetime": datetime.now(),
            "ip_address": PROXYMESH_URL.split("//")[-1] if PROXYMESH_URL else "localhost"
        }

        # Insert into MongoDB
        insert_record(record)
        return {"status": "success", "data": record}

    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"status": "error", "message": str(e)}
    finally:
        driver.quit()
