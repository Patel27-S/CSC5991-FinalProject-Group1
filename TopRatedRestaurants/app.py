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

@app.route("/FiveStarList", methods=["GET"])
def five_star_list():
    # pull all 5 star restaurant from table and display
    top_five_restaurants = dict(db['restaurant'].find({"Rating": "5"}))
    return jsonify_with_objectid(top_five_restaurants)


@app.route("/TopThreeRestaurants", methods=["GET"])
def top_three():
    # pull first 3 restaurants from table and display
    top_three_restaurants = dict(db['restaurant'].find().sort('Rating',-1).limit(3))
    return jsonify_with_objectid(top_three_restaurants)


if __name__ == "__main__":
    app.run(debug=True)