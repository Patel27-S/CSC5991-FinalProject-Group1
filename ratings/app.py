from flask import Flask, jsonify, request
from pymongo import MongoClient, ReturnDocument
from bson import ObjectId
from bson.json_util import dumps, loads


# Connect to MongoDB
client = MongoClient("localhost", 27017)
db = client["restaurant"]  # Replace 'restaurant' with your database name

app = Flask(__name__)


## Calculate average rating of restaurant
def calculate_Rating(rating, current_Rating):
    return (rating + current_Rating) / 2


@app.route("/addRatings", methods=["POST"])
def add_Ratings():
    input_Restaurant = request.args.get("restaurant")
    input_Rating = request.args.get("rating")
    current_Rating = int(
        db["restaurant"].db.find({"name": input_Restaurant}, {"Ratings: "})
    )  ##Gets the current ratings of that restaurant
    return jsonify(
        db["restaurant"].db.find_one_and_update(
            {"name": input_Restaurant},
            {"$set": {"Rating": calculate_Rating(input_Rating, current_Rating)}},
            return_document=ReturnDocument.AFTER,
        )
    )


@app.route("/FiveStarList", methods=["GET"])
def five_star_list():
    # pull all 5 star restaurant from table and display
    top_five_restaurants = dict(db["restaurant"].find({"Rating": "5"}))
    return jsonify(top_five_restaurants)


app.route("/GetRatings", methods=["GET"])
def get_Ratings():
    input_Restaurant = request.args.get("restaurant")
    current_Rating = int(
        db["restaurant"].db.find({"name": input_Restaurant}, {"Ratings: "})
    )
    return jsonify(current_Rating)


@app.route("/TopThreeRestaurants", methods=["GET"])
def top_three():
    # pull first 3 restaurants from table and display
    top_three_restaurants = dict(db['restaurant'].find().sort('Rating',-1).limit(3))
    return jsonify_with_objectid(top_three_restaurants)


if __name__ == "__main__":
    app.run(debug=True)
