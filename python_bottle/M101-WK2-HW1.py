import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students

grades = db.grades

query = {'score': {'$gt': 65.0}}

cursor = grades.find(query)
cursor.sort('score', pymongo.ASCENDING)
cursor.limit(1)

for doc in cursor:
	print(doc)






