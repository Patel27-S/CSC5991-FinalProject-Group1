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


# API Endpoint to fetch all users
@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(db['users'].find({}))
    return jsonify_with_objectid_array(users)

if __name__ == '__main__':
    app.run(debug=True)
