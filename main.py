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