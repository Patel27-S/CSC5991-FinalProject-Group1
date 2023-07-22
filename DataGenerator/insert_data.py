import json
from pymongo import MongoClient, errors

def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# MongoDB connection parameters
mongo_host = 'localhost'
mongo_port = 27017

# Connect to MongoDB
try:
    client = MongoClient(mongo_host, mongo_port)
    db = client['restaurant']

    # Read data from JSON files
    restaurant_data = read_json_file('restaurant_list.json')
    user_data = read_json_file('user_list.json')

    # Create collections for 'restaurants' and 'users'
    restaurants_collection = db['restaurants']
    users_collection = db['users']

    # Insert data into the 'restaurants' collection
    restaurants_collection.insert_many(restaurant_data)

    # Insert data into the 'users' collection
    users_collection.insert_many(user_data)

    # Query and print documents from 'restaurants' collection
    for restaurant in restaurants_collection.find():
        print(restaurant)

    # Query and print documents from 'users' collection
    for user in users_collection.find():
        print(user)

    # Close the MongoDB connection
    client.close()
    print("we got to the end")
except errors.ConnectionFailure as e:
    print("Connection to MongoDB failed:", e)
