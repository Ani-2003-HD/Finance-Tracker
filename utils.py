from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client['finance_tracker']
users_collection = db['users']
expenses_collection = db['expenses']
