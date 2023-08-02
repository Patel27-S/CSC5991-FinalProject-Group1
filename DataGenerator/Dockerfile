FROM mongo:latest

# Copy the JSON data files to the Docker container
COPY restaurant_list.json /data/restaurant_list.json
COPY user_list.json /data/user_list.json

# Load the JSON data into the MongoDB database
CMD mongoimport --host mongodb --db restaurant --collection restaurants --type json --file /data/restaurant_list.json --jsonArray && \
    mongoimport --host mongodb --db restaurant --collection users --type json --file /data/user_list.json --jsonArray
