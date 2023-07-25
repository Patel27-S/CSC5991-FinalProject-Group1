from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['restaurant']  # Replace 'restaurant' with your database name

# Helper function to convert ObjectId to string
def jsonify_with_objectid(data):
    for document in data:
        document['_id'] = str(document['_id'])
    return jsonify(data)

# API Endpoint to fetch all restaurants
@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = list(db['restaurants'].find({}))
    return jsonify_with_objectid(restaurants)

if __name__ == '__main__':
    app.run(debug=True)
