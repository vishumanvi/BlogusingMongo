from pymongo import MongoClient

connection = MongoClient('localhost',27017)

db = connection.test

item = db.names.find_one()

print("Item found in Mongo DB is : " + item['name'])

