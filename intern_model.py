from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

# MongoDB Connection
client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

# Collections
intern_collection = db['interns']
admin_collection = db['admins']