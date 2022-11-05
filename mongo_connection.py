#from gc import collect
#from typing import Collection
#from flask import Flask
#app = Flask(__name__)
from cgitb import text
import pymongo
from pymongo import MongoClient
import certifi
from sklearn import cluster
text = 'hello kese ho aap . this is the test data . Ye data testing ke kam me ane wala hai. Ise aap haat na lagaye'

cluster = MongoClient("mongodb+srv://new_user_7:584nYp9q17XE5VrR@cluster77.yfqtoem.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)

db = cluster["user_database"]
#collection = db["user_collection"]
user_collection = db.get_collection("user_collection")

#collection.insert_one({"_id":10000, "user_name":"Sukhi"})
#user_collection.insert_one('text')
#user_collection.insert_one({"_id":70000, "user_name":"Yes its working"})
user_collection.insert_one({"user_data":text})

#refer commentator main.py
#try accept blog

#serverSelectionTimeoutMS=50000)