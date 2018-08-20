import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students

grades = db.grades

query = {'type': 'homework'}


cursor = grades.find(query).sort([('student_id', pymongo.ASCENDING),('score',pymongo.DESCENDING)])

count = 1

for doc in cursor:
	if (count%2 == 0):
		#print (doc)
		ID = doc['_id']
		grades.delete_one({'_id': ID})
	count += 1