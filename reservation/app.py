from flask import Flask, app, jsonify
from pymongo import MongoClient

#from bson import ObjectId

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['restaurant']  # Replace 'restaurant' with your database name

# Helper function to convert ObjectId to string
def jsonify_with_objectid(data):
    for document in data:
        document['_id'] = str(document['_id'])
    return data

# /reserve API Reasource only
def book_table(restaurant_name, num_of_seats):
    restaurant = db['restaurants'].find_one({"Name": restaurant_name})
    if restaurant is None:
        return jsonify({"message": "Restaurant not found."}), 404

    available_seats = restaurant["Available_Seats"]
    if available_seats >= num_of_seats:
        new_available_seats = available_seats - num_of_seats
        db['restaurants'].update_one({"_id": restaurant["_id"]}, {"$set": {"Available_Seats": new_available_seats}})
        return jsonify({"message": f"Table booked at {restaurant_name} for {num_of_seats} seats."}), 200
    else:
        return jsonify({"message": f"Sorry, {restaurant_name} doesn't have enough available seats for {num_of_seats} people."}), 400
    
# API Endpoint for booking a table at a restaurant
@app.route('/api/book/<string:Name>/<int:Seats_Required>', methods=['POST'])
def book_table_endpoint(Name, Seats_Required):
    response = book_table(Name, Seats_Required)
    return response

if __name__ == '__main__':
    app.run(debug=True)