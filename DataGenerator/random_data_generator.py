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

last_names = ['Smith', 'Johnson', 'Williams', 'De Villers', 'Ponting', 'Richardson', 'Miller', 'Davis', 'James', 'Martin',
              'Du Plesis', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'McCullum', 'Jackson', 'Martin', 'Lee']


email_domain = [ 'wayne.edu', 'google.com', 'yahoo.com', 'hotmail.com']


user_list = []
user_file = open("user_list.json", "w+") # Creating a File and giving the Access to Write.

for x in range(10):
    tem_first_name = random.choice(first_names)
    tem_last_name = random.choice(last_names)
    user_list.append({"Username": tem_first_name+tem_last_name,
                      "Password": fake.password(),
                      "First_Name": tem_first_name,
                      "Last_Name": tem_last_name,
                      "Email": tem_first_name+tem_last_name+"@"+random.choice(email_domain)})
print(user_list)
json.dump(user_list, user_file, indent=4)
user_file.close()


