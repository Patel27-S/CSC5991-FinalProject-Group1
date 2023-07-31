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

# Install the required Python packages
RUN pip3 install blinker==1.6.2 \
    click==8.1.6 \
    colorama==0.4.6 \
    dnspython==2.4.1 \
    Flask==2.3.2 \
    itsdangerous==2.1.2 \
    Jinja2==3.1.2 \
    MarkupSafe==2.1.3 \
    pymongo==4.4.1 \
    Werkzeug==2.3.6

# Set the working directory for each Flask app
WORKDIR /app/ratings
COPY ratings/app.py .

WORKDIR /app/reservation
COPY reservation/app.py .

WORKDIR /app/restaurants
COPY restaurants/app.py .

WORKDIR /app/users
COPY users/app.py .

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
