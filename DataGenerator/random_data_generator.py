import random
import json
import os
import numpy as np
from faker import Faker

# Instantiating the Faker Class.
fake = Faker()


# Writing the Lists for first_names, last_names and email_domain for generating
# different permutations & combintations.

first_names = ['John', 'Harry', 'Will', 'Bill', 'Ricky', 'Gatey', 'Elijah', 'Amelia', 'James', 'Ava', 'William',
               'Jash', 'Mike', 'Isabella', 'David', 'Brad', 'Henry', 'Evelyn', 'Queens', 'Kater']

last_names = ['Smith', 'Johnson', 'Williams', 'DeVillers', 'Ponting', 'Richardson', 'Miller', 'Davis', 'James', 'Martin',
              'DuPlesis', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'McCullum', 'Jackson', 'Martin', 'Lee']


email_domain = [ 'wayne.edu', 'google.com', 'yahoo.com', 'hotmail.com']

# For Phone Numbers of individual Users :-
def generate_random_10_phone_numbers_list(length):
    '''
    Function that helps generating 10 digit numbers. If length = 5, there'd be a list of 
    five 10-digit unique numbers returned.
    '''
    numbers_list = [str(random.randint(10**9, 10**10 - 1)) for _ in range(length)]
    return numbers_list


length_of_list = 10 # Has to be same or greater than the number of users.
phone_numbers = generate_random_10_phone_numbers_list(length_of_list)



# For Addresses of the Users :-
def generate_random_addresses_list(length):
    '''
    Function that helps generating random addresses. If length = 5, there'd be a list of 
    Length=5 random addresses returned.
    '''
    addresses_list = [fake.address() for _ in range(length)] # Using 'faker' to generate 10 random addresses
    return addresses_list

length_of_list = 10
random_addresses_list = generate_random_addresses_list(length_of_list)


# Number of Seats a User would require:-
def generate_random_integers(length):
    random_integers = [random.randint(2, 10) for _ in range(length)]
    return random_integers


user_list = []
user_file = open("./DataGenerator/user_list.json", "w+") # Creating a File and giving the Access to Write.


for x in range(10):
    tem_first_name = random.choice(first_names)
    tem_last_name = random.choice(last_names)
    phone_number = phone_numbers[x] # Ensuring each user has a unique number by not using 'random' library.
    address = random.choice(random_addresses_list) # Two users registered on the App may have same address.
    number_of_seats = random.choice(generate_random_integers(10))
    user_list.append({"Username": tem_first_name+tem_last_name,
                      "Password": fake.password(),
                      "First_Name": tem_first_name,
                      "Last_Name": tem_last_name,
                      "Email": tem_first_name+tem_last_name+"@"+random.choice(email_domain),
                      "Phone_Number": phone_number,
                      "Address": address,
                      "Seats_Needed": number_of_seats})
print(user_list)
json.dump(user_list, user_file, indent=4)
user_file.close()


# Generating Fake Restaurants' data :-

