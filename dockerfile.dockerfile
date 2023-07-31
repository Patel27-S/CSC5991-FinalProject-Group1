# Use the official MongoDB image from Docker Hub
FROM mongo:latest

# Copy the JSON data files to the Docker container
COPY DataGenerator/restaurant_list.json /data/restaurant_list.json
COPY DataGenerator/user_list.json /data/user_list.json

# Load the JSON data into the MongoDB database
CMD mongoimport --host mongodb --db mydb --collection restaurants --file /data/restaurant_list.json --jsonArray && \
    mongoimport --host mongodb --db mydb --collection users --file /data/user_list.json --jsonArray

# Expose the MongoDB default port (27017)
EXPOSE 27017

# Install Python and required packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory for each Flask app
WORKDIR /app/ratings
COPY ratings/app.py ratings/requirements.txt /app/ratings/
RUN pip3 install -r ratings/requirements.txt

WORKDIR /app/reservation
COPY reservation/app.py reservation/requirements.txt /app/reservation/
RUN pip3 install -r reservation/requirements.txt

WORKDIR /app/restaurants
COPY restaurants/app.py restaurants/requirements.txt /app/restaurants/
RUN pip3 install -r restaurants/requirements.txt

WORKDIR /app/users
COPY users/app.py users/requirements.txt /app/users/
RUN pip3 install -r users/requirements.txt

# Expose the ports for each Flask app
EXPOSE 5000
EXPOSE 5001
EXPOSE 5002
EXPOSE 5003

# Run each Python Flask app
CMD ["python3", "app.py", "--port", "5000"]  # ratings
CMD ["python3", "app.py", "--port", "5001"]  # reservation
CMD ["python3", "app.py", "--port", "5002"]  # restaurants
CMD ["python3", "app.py", "--port", "5003"]  # users

#This will ensure that all Flask services run on localhost but on different ports (5000, 5001, 5002, 5003) on your host machine.
#docker run -p 5000:5000 <image_id_ratings>
#docker run -p 5001:5001 <image_id_reservation>
#docker run -p 5002:5002 <image_id_restaurants>
#docker run -p 5003:5003 <image_id_users>

