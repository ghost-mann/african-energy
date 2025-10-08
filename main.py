import os 
import time 
import pandas as pd
import re
from dotenv import load_dotenv
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()
mongo_url = os.getenv('mongo_url')
db_name = os.getenv('mongo_db_name')
collection_name = os.getenv('energy_indicator')

DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)
    
DASHBOARD_URL = "https://africa-energy-portal.org/database"

METADATA_MAP = {
    "Access to electricity, urban (% of urban population)": {
        "metric_name": "Access to electricity, urban", "unit": "% of urban population",
        "sector": "Energy", "sub_sector": "Electricity", "sub_sub_sector": "Access",
        "source": "World Bank", "source_link": DASHBOARD_URL
    },
    "Access to electricity, rural (% of rural population)": {
        "metric_name": "Access to electricity, rural", "unit": "% of rural population",
        "sector": "Energy", "sub_sector": "Electricity", "sub_sub_sector": "Access",
        "source": "World Bank", "source_link": DASHBOARD_URL
    }
}

BASE_COLUMNS = ["country", "country_serial", "metric", "unit", "sector", "sub_sector", "sub_sub_sector", "source_link", "source"]
YEAR_COLUMNS = [str(y) for y in range(2000, 2025)]
FINAL_SCHEMA_COLUMNS = BASE_COLUMNS + YEAR_COLUMNS

def setup_driver():
    # selenium options
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": DOWNLOAD_DIR}
    options.add_experimental_option("prefs",prefs)
    
    # for linux
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # web-driver manager downloads driver
    # selenium uses path to start driver
    service = ChromeService(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

def scrap_and_process_data(driver):
    # telling automated browser to open AEP
    driver.get(DASHBOARD_URL)
    
    # direct the robot browser 
    CONTAINER_SELECTOR = ".visualisation-card"
    TITLE_SELECTOR = ".visualisation-title"
    DOWNLOAD_ICON_SELECTOR = ".download-section"
    CSV_BUTTON_SELECTOR = 'a[data-type="csv"]'
    
    # finding all indicators
    indicator_containers = wait.until(...)
    
    # loop through each indicator one by one 
    # for container in indicator_containers:


def process_downloaded_file(filepath, indicator_name_raw):
    metadata =  METADATA_MAP.get(indicator_name_raw,{})
    df = pd.read_csv(filepath, skiprows=1)
    
    df['metric'] = metadata.get('metric_name', indicator_name_raw)
    
    return df[FINAL_SCHEMA_COLUMNS]

def main():
    
    # setup robot
    driver = setup_driver()
    
    # robot does main job
    final_df = scrap_and_process_data(driver)
    
    # robot quit
    driver.quit()
    
    # prepare data for mongodb
    records = final_df.to_dict('records')
    
    # connect to DB and insert everything
    collection.insert_many(records)
    

