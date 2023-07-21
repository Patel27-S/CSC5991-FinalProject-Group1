import random
import json
import os
import numpy as np
from faker import Faker


from random_data_generator_users import (generate_random_10_phone_numbers_list, generate_random_addresses_list)

# Instantiating the Faker Class.
fake = Faker()

# Generating Fake Restaurants' data :-

# restaurant_names has the 'name' field of all the restaurants.
restaurant_names = ['The Savory Spoon', 'Fusion Bites', 'Catch Burger', 'Sizzling Food', 
                    'The Green Leaf Cafe', 'Sweet Indulgence Dessert Bar', 'The IceCream Place',
                    'Hey Pizzeria', 'Da Planet Pizza', 'The Kofta Palace', 'Da Foodie Paradise']



# Each restaurant would have a unique Phone Number :-
length_of_list = 10 # Has to be same or greater than the number of restaurants.
restaurant_phone_numbers = generate_random_10_phone_numbers_list(length_of_list)


# Each restaurant would have a unique Address :-
length_of_list = 10
restaurant_random_addresses_list = generate_random_addresses_list(length_of_list)


# Number of Available Seats for each Restaurant :-
def generate_random_integers(length):
    random_integers = [random.randint(2, 20) for _ in range(length)]
    return random_integers

list_of_available_seats = generate_random_integers(20)

restaurant_list = []
restaurant_file = open("./DataGenerator/restaurant_list.json", "w+") # Creating a File and giving the Access to Write.


for x in range(10):
    name = restaurant_names[x]
    phone_number = restaurant_phone_numbers[x]
    address = restaurant_random_addresses_list[x] # Two users registered on the App may have same address.
    available_seats = random.choice(list_of_available_seats)
    restaurant_list.append({
                      "Name": name,
                      "Phone_Number": phone_number,
                      "Address": address,
                      "Available_Seats": available_seats,
                     })
print(restaurant_list)
json.dump(restaurant_list, restaurant_file, indent=4)
restaurant_file.close()

