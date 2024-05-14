from pymongo import MongoClient

client = MongoClient("mongodb+srv://foodlover:CDOG2CI3GApYWkJv@foodlover.xagchl4.mongodb.net/")
db = client['users']
menu = db['food']

cursor = menu.find()

first_doc = list(cursor)[0]
print(first_doc)