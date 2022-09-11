# pip install "pymongo[srv]"

import pymongo
from pymongo import MongoClient

# connect to cluster
cluster = MongoClient(
    "mongodb+srv://<username>:<password>@<cluster-address>/test?retryWrites=true&w=majority"
)

# access db and collection
db = cluster["company"]
collection = db["employee"]

# insert single document
# into collection
collection.insert_one(
    {
        "name": "Sarah",
        "type": "PT",
        "age": 29,
    }
)

# insert multiple documents
# into collection
doc1 = {
    "name": "Anne",
    "type": "FT",
    "age": 21,
}

doc2 = {
    "name": "Ian",
    "type": "FT",
    "age": 22,
}

collection.insert_many([doc1, doc2])

# search collection for documents
# using name = Anne and type = FT criteria
results = collection.find(
    {"name": "Anne", "type": "FT"}
)
for r in results:
    print(r["name"])

# using age > 21 criteria
results = collection.find(
    {"age": {"$gt": 21}}
)
for r in results:
    print(r["name"])

# using name starting with
# letters "An" criteria
results = collection.find(
    {"name": {"$regex": "An.*"}}
)
for r in results:
    print(r["name"])

# update a single document
# name =  Anne criteria
results = collection.update_one(
    {"name": "Anne"},
    {
        "$set": {
            "type": "PT",
            "age": 30,
            "country": "UK",
        }
    },
)

# delete a single document
# name = Anne criteria
results = collection.delete_one(
    {"name": "Anne"}
)

# delete many documents
# age > 21 criteria
results = collection.delete_many(
    {"age": {"$gt": 21}}
)
