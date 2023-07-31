from flask import Flask, jsonify
from pymongo import MongoClient, ReturnDocument
from bson import ObjectId
from bson.json_util import dumps, loads

from Restaurants.app import jsonify_with_objectid

# Connect to MongoDB
client = MongoClient("localhost", 27017)
db = client["restaurant"]  # Replace 'restaurant' with your database name

app = Flask(__name__)


@app.route("/addRatings", methods=["POST"])
def add_Ratings(restuarant,rating):
   return (db['restaurant'].db.find_one_and_update({'name':restuarant},
                        { '$set': { "Rating" : rating} },
                        return_document = ReturnDocument.AFTER))


if __name__ == "__main__":
    app.run(debug=True)
