from pymongo import MongoClient 

def connect_to_mongo():
    CONNECTION_STRING = "mongodb+srv://Morgan11235:gg6EZ$$bill@cluster0.q3tm7.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['CMTDataSystems']