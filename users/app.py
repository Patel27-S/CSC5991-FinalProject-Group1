from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['restaurant']  # Replace 'restaurant' with your database name

# Helper function to convert ObjectId to string in a array
def jsonify_with_objectid_array(data):
    for document in data:
        document['_id'] = str(document['_id'])
    return jsonify(data)

# Helper function to convert ObjectId to string in a jsonObject
def jsonify_with_objectid(data):
    data['_id'] = str(data['_id'])
    return jsonify(data)

# API Endpoint to fetch all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(db['users'].find({}))
    return jsonify_with_objectid_array(users)

# API Endpoint to fetch a user by username
@app.route('/api/users/username/<username>', methods=['GET'])
def getUser_by_username(username):
    user_details = db['users'].find_one({"Username": username})
    hide_password = {"Password": ""}
    user_details.update(hide_password)
    return jsonify_with_objectid(user_details)

# API Endpoint to fetch a user by email
@app.route('/api/users/email/<email>', methods=['GET'])
def getUser_by_email(email):
    user_details = db['users'].find_one({"Email": email})
    hide_password = {"Password": ""}
    user_details.update(hide_password)
    return jsonify_with_objectid(user_details)

if __name__ == '__main__':
    app.run(debug=True)
