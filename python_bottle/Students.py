import pymongo

try:
	connection = pymongo.MongoClient("mongodb://localhost")

	db = connection.school

	scores = db.scores

except Exception as e:
	print("Exception occured. ",e)

def find_one():
	try:
		query = {'student_id':2.0}

		doc = scores.find_one('student_id':2.0)

		print(doc)

	except Exception as e:
		print("Exception occured. ", e)

find_one()
