from pymongo import MongoClient
client = MongoClient("mongodb+srv://foodlover:CDOG2CI3GApYWkJv@foodlover.xagchl4.mongodb.net/")
db = client['users']

test_data = [
        {
        "name": "Pizza Margherita",
        "description": "Italian pizza with tomatoes, mozzarella, and basil.",
        "keywords": ["Italian", "Pizza", "Margherita"],
        "averageRating": 4.4
    },
    {

        "name": "Beef Pho",
        "description": "Vietnamese soup with beef and rice noodles.",
        "keywords": ["Vietnamese", "Soup", "Pho"],
        "averageRating": 4.6
    },
    {

        "name": "Falafel",
        "description": "Middle Eastern dish of spiced mashed chickpeas.",
        "keywords": ["Middle Eastern", "Vegetarian", "Falafel"],
        "averageRating": 4.5
    }
]

# Insert test data into the collection
db['food'].insert_many(test_data)
