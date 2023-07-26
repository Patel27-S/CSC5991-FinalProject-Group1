from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps, loads

from restaurants.app import jsonify_with_objectid

# Connect to MongoDB
client = MongoClient("localhost", 27017)
db = client["restaurant"]  # Replace 'restaurant' with your database name

app = Flask(__name__)


@app.route("/addRatings", methods=["POST"])
def add_Ratings(rating):
    result = int(db['restaurant'].insert_one({}).inserted_id)
    reviewRating = int(db["restaurant"].find_one(result)) ## Storing the rating we just changed
    return jsonify_with_objectid(reviewRating) ## displaying the rating


@app.route("/FiveStarList", methods=["GET"])
def five_star_list():
    # pull all 5 star restaurant from table and display
    top_five_restaurants = dict(db['restaurant'].find({"Rating": "5"}))
    return jsonify_with_objectid(top_five_restaurants)


if __name__ == "__main__":
    app.run(debug=True)
