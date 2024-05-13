from pymongo import MongoClient
client = MongoClient("mongodb+srv://foodlover:CDOG2CI3GApYWkJv@foodlover.xagchl4.mongodb.net/")
db = client['users']

test_data = [
    {
        "name": "Spaghetti Carbonara",
        "description": "Italian pasta with egg, cheese, and pork.",
        "keywords": ["Italian", "Pasta", "Carbonara"],
        "averageRating": 4.5
    },
    {
        "name": "Chicken Tikka Masala",
        "description": "Roasted chicken chunks in a spiced curry sauce.",
        "keywords": ["Indian", "Chicken", "Curry"],
        "averageRating": 4.7
    },
    {
        "name": "Sushi",
        "description": "Japanese dish of vinegared rice with seafood or vegetables.",
        "keywords": ["Japanese", "Seafood", "Rice"],
        "averageRating": 4.8
    }
]

# Insert test data into the collection
db['users.food'].insert_many(test_data)
