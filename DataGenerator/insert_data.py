import json
from pymongo import MongoClient

def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# Read data from JSON files
restaurant_data = read_json_file('restaurant_list.json')
user_data = read_json_file('user_list.json')

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)

# Create or access the 'restaurant' database
db = client['restaurant']

# Create collections for 'restaurants' and 'users'
restaurants_collection = db['restaurants']
users_collection = db['users']

# Insert data into the 'restaurants' collection
restaurants_collection.insert_many(restaurant_data)

# Insert data into the 'users' collection
users_collection.insert_many(user_data)

# Close the MongoDB connection
client.close()
