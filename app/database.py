from pymongo import MongoClient
import certifi
import os

# Connect to the MongoDB cluster with the CA certificate from certifi
MONGODB_URL = os.environ.get("MONGO_URL",
                           "mongodb+srv://rajeshupadhayaya:Umy6ELZmWN2kYqCV@universal-sandbox.84fqpe6.mongodb.net/?retryWrites=true&w=majority&appName=Universal-sandbox")
client = MongoClient(MONGODB_URL, tlsCAFile=certifi.where()
                     )

# Access the 'universal-sandbox' database
database = client['universal-sandbox']
