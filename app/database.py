from pymongo import MongoClient
import certifi

# Connect to the MongoDB cluster with the CA certificate from certifi
client = MongoClient(
    "mongodb+srv://rajeshupadhayaya:Umy6ELZmWN2kYqCV@universal-sandbox.84fqpe6.mongodb.net/?retryWrites=true&w=majority&appName=Universal-sandbox",
    tlsCAFile=certifi.where()
)

# Access the 'universal-sandbox' database
database = client['universal-sandbox']


