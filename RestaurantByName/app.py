from flask import Flask, jsonify
from pymongo import MongoClient, ReturnDocument
from bson import ObjectId
from bson.json_util import dumps, loads

# Connect to MongoDB
client = MongoClient("localhost", 27017)
db = client["restaurant"]  # Replace 'restaurant' with your database name

app = Flask(__name__)


def jsonify_with_objectid(data):
    data['_id'] = str(data['_id'])
    return jsonify(data)


# API Endpoint for listing all the restaurants on the basis of 
# Name.
@app.route('/api/restaurants/<string:Name>', methods=['GET'])
def get_restaurants_seats_available(Name):
    global restaurant
    try:
        restaurant = db['restaurants'].find_one({"Name": Name})
    except:
        print("Error while retrieving a restaurant")
    if restaurant == None:
        return jsonify({"message": f"Restaurant is not available. Please try another restaurant"})
    else:
        return jsonify_with_objectid(restaurant)


if __name__ == '__main__':
    app.run(debug=True)
