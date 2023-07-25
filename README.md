# CSC5991-FinalProject-Group1

To run and test the code that inserts data into a MongoDB database using Python, follow these steps ( I am working on Windows Subsystem for Linux):

Install MongoDB: Make sure you have MongoDB installed on your system. If you haven't installed it yet, you can download and install it from the official MongoDB website (https://www.mongodb.com/try/download/community).
or for Linux
sudo apt update
sudo apt upgrade
sudo apt install mongodb
sudo service mongodb start
sudo service mongodb status
sudo systemctl enable mongodb


Start MongoDB Server: Start the MongoDB server by running the mongod command in your terminal or command prompt. This will start the MongoDB server, allowing you to connect to it and interact with databases.

Prepare JSON Data Files: Create two JSON files in the same directory as your Python script - restaurant_list.json and user_list.json. Fill these files with the data you want to insert into the respective MongoDB collections.

Install Required Libraries --> pip install pymongo 
Run the Python Script --> python insert_data.py

Verify Data in MongoDB
mongo
use restaurant
db.restaurants.find().pretty()
OR
you can run my test_db.py script and it will prrint the json data in the database

similarily for users collection,
mongo
use restaurant
db.users.find().pretty()

To run:
- run mongoDb server (on linux --> sudo mongod --dbpath /data/db)
- run insert_data.py to have database locally (python insert_data.py)
- run app.py to have server serving information from database (python app.py)
---> Displayed Here:
---- http://localhost:5000/api/users    (All user information from database)
---- http://localhost:5000/api/users/username/<username>   (User information according to the username)
---- http://localhost:5000/api/users/email/<email>  (User information according to the email)
---- http://localhost:5000/api/restaurants (All restaurant information from database)

