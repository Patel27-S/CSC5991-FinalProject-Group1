from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Helper function to convert ObjectId to string in a jsonObject
def jsonify_with_objectid(data):
    data['_id'] = str(data['_id'])
    return jsonify(data)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['restaurant']  # Replace 'restaurant' with your database name

# API Endpoint to fetch a user by username
@app.route('/api/users/username/<username>', methods=['GET'])
def getUser_by_username(username):
    user_details = db['users'].find_one({"Username": username})
    hide_password = {"Password": ""}
    user_details.update(hide_password)
    return jsonify_with_objectid(user_details)


if __name__ == "__main__":
    app.run(debug=True)