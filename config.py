import os
from dotenv import load_dotenv

load_dotenv()

# mongodb config 
mongo_url = os.getenv('mongo_url')
db_name = os.getenv('mongo_db_name')
collection_name = os.getenv('energy_indicator')

