from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://142.93.131.22:27017/')
db = client['test-database']
collection = db['test-collection']


posts = db.posts


post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}


post_id = posts.insert_one(post).inserted_id
print(post_id)