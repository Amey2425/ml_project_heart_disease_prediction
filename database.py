# d:\ml_project_heart_dieases prediction\project\database.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
print("database.py loaded successfully")
uri = "mongodb+srv://Amey:Ameypict26@cluster0.ojxcbas.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
