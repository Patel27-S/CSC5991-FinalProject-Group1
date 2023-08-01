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

# Reservation Functions:

def book_table(restaurant_name, num_of_seats):
    restaurant = db['restaurants'].find_one({"Name": restaurant_name})
    if restaurant is None:
        return jsonify({"message": "Restaurant not found."}), 404

    available_seats = restaurant["Available_Seats"]
    
    if available_seats >= num_of_seats:

        new_available_seats = available_seats - num_of_seats
        db['restaurants'].update_one({"_id": restaurant["_id"]}, {"$set": {"Available_Seats": new_available_seats}})

    #Updated with booked tables infromation

        booked_tables = restaurant.get("Booked_Tables", [])
        booked_tables.append({"num_of_seats": num_of_seats})
        db['restaurants'].update_one({"_id": restaurant["_id"]}, {"$set": {"Booked_Tables": booked_tables},"$push": {"Booked_Tables": {"num_of_seats": num_of_seats}} })

        return jsonify({"message": f"Table booked at {restaurant_name} for {num_of_seats} seats."}), 200
    else:
        return jsonify({"message": f"Sorry, {restaurant_name} doesn't have enough available seats for {num_of_seats} people."}), 400
    
def get_booked_tables(restaurant_name):

    restaurant = db['restaurants'].find_one({"Name": restaurant_name})

    if restaurant is None:

        return jsonify({"message": "Restaurant not found."}), 404

    booked_tables = restaurant.get("Booked_Tables", [])

    return jsonify({"booked_tables": booked_tables}), 200

def get_booked_table_info(restaurant_name, table_number):
    restaurant = db['restaurants'].find_one({"Name": restaurant_name})

    if restaurant is None:
        return jsonify({"message": "Restaurant not found."}), 404

    booked_tables = restaurant.get("Booked_Tables", [])

    for table in booked_tables:
        if table.get("num_of_seats") == table_number:
            return jsonify({"booked_table_info": table}), 200

    return jsonify({"message": f"Table {table_number} is not booked at {restaurant_name}."}), 404


def is_table_booked(restaurant_name, table_number):
    restaurant = db['restaurants'].find_one({"Name": restaurant_name})

    if restaurant is None:
        return jsonify({"message": "Restaurant not found."}), 404

    booked_tables = restaurant.get("Booked_Tables", [])

    for table in booked_tables:
        if table.get("num_of_seats") == table_number:
            return True

    return False


def update_reservation(restaurant_name, table_number, new_seats):
    restaurant = db['restaurants'].find_one({"Name": restaurant_name})

    if restaurant is None:
        return jsonify({"message": "Restaurant not found."}), 404

    booked_tables = restaurant.get("Booked_Tables", [])

    for table in booked_tables:
         if table.get("num_of_seats") == table_number:
            if new_seats <= table.get("num_of_seats"):
                table["num_of_seats"] = new_seats
                db['restaurants'].update_one({"_id": restaurant["_id"]}, {"$set": {"Booked_Tables": booked_tables}})
                return jsonify({"message": f"Reservation for Table {table_number} at {restaurant_name} updated to {new_seats} seats."}), 200
            else:
                return jsonify({"message": f"New number of seats ({new_seats}) exceeds the original number of seats ({table.get('num_of_seats')})."}), 400

    return jsonify({"message": f"Table {table_number} is not booked at {restaurant_name}."}), 404


def cancel_reservation(restaurant_name, table_number):
    restaurant = db['restaurants'].find_one({"Name": restaurant_name})

    if restaurant is None:
        return jsonify({"message": "Restaurant not found."}), 404

    booked_tables = restaurant.get("Booked_Tables", [])

    for table in booked_tables:
        if table.get("num_of_seats") == table_number:
            booked_tables.remove(table)
            db['restaurants'].update_one({"_id": restaurant["_id"]}, {"$set": {"Booked_Tables": booked_tables}})
            return jsonify({"message": f"Reservation for Table {table_number} at {restaurant_name} has been canceled."}), 200

    return jsonify({"message": f"Table {table_number} is not booked at {restaurant_name}."}), 404


# API Endpoints:
    
# API Endpoint for booking a table at a restaurant

@app.route('/api/book/<string:Name>/<int:Seats_Required>', methods=['POST'])
def book_table_endpoint(Name, Seats_Required):
    response = book_table(Name, Seats_Required)
    return response

# API Endpoint for returning booked tables infromation 

@app.route('/api/booked_tables/<string:Name>', methods=['GET'])
def get_booked_tables_endpoint(Name):
    response = get_booked_tables(Name)
    return response

# API Endpoint for returning specific booked table info

@app.route('/api/booked_tables/<string:Name>/<int:Table_Number>', methods=['GET'])
def get_booked_table_info_endpoint(Name, Table_Number):
    response = get_booked_table_info(Name, Table_Number)
    return response

# API Endpoint for checking specific table is booked or not 

@app.route('/api/is_table_booked/<string:Name>/<int:Table_Number>', methods=['GET'])
def is_table_booked_endpoint(Name, Table_Number):
    response = jsonify({"is_booked": is_table_booked(Name, Table_Number)})
    return response

# API Endpoint for Update a reservation 

@app.route('/api/update_reservation/<string:Name>/<int:Table_Number>/<int:New_Seats>', methods=['PUT'])
def update_reservation_endpoint(Name, Table_Number, New_Seats):
    response = update_reservation(Name, Table_Number, New_Seats)
    return response

# API Endpoint for Cancel a reservation

@app.route('/api/cancel_reservation/<string:Name>/<int:Table_Number>', methods=['DELETE'])
def cancel_reservation_endpoint(Name, Table_Number):
    response = cancel_reservation(Name, Table_Number)
    return response

if __name__ == '__main__':
    app.run(debug=True)