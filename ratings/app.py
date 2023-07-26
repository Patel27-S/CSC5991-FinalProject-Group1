from flask import Flask, jsonify
from pymongo import MongoClient
from bson import ObjectId

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['restaurant']  # Replace 'restaurant' with your database name
ratings = db['rating']

