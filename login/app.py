from flask import Flask, request, render_template, session, abort, flash
import os
import requests
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['restaurant']
mongo_users_coll = db['users']

app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        userAccount = session.get('user')
        return render_template('index.html', userAccount=userAccount)


@app.route('/login', methods=['POST'])
def authenticate():
    query = {"Username": request.form['username'], "Password": request.form['password']}
    valid_login = mongo_users_coll.count_documents(query)
    if valid_login > 0:
        session['logged_in'] = True
        session['user'] = request.form['username']
    else:
        flash('Invalid Login Attempt')
    return index()


@app.route('/search/restaurant', methods=['POST'])
def search_res():
    build_call_url = "http://127.0.0.1:5000/api/restaurants/" + request.form['search']
    search_result = requests.get(build_call_url)
    search_result = search_result.json()
    return render_template('results.html', search_result=search_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
