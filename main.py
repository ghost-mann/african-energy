import os 
import time 
import pandas as pd
import re 
from pymongo import MongoClient
from selenium import webdriver

def setup_driver():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": DOWNLOAD_DIR}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options)
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

