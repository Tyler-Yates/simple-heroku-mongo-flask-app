# simple-mongo-flask-app
A simple Heroku Flask application that connects to MongoDB.

## Prerequisites
You will need a [Heroku](https://www.heroku.com/) account to run this application.
Heroku has a [free tier](https://www.heroku.com/free).

You will also need a [MongoDB](https://www.mongodb.com/) database to run this application.
You can get a free MongoDB database by signing up for [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
MongoDB Atlas has a free tier which includes a simple cluster deployment.

## Setup
You will need to create a virtual environment to run this application.
Run the following commands at the root of this repo:
```
python3 -m venv venv
source venv/bin/activate
pip install -Ur requirements.txt
```

## Running
To run this application, you need to set some environment variables:
* `MONGO_USER` - The username for the MongoDB connection
* `MONGO_PASSWORD` - The password for the MongoDB connection
* `MONGO_HOST` - The host to connect to for the MongoDB connection

After setting up the environment variables, you can run the application locally.
Be sure you have activated the virtual environment before running this command:
```
heroku local
```

You should then be able to access the application at [http://0.0.0.0:5000](http://0.0.0.0:5000) in your browser.

## Database
This application creates a database called `test`.
It also creates a collection in that database called `test_collection`.

This application creates a TTL index on `test_collection` so documents created by this application will be
deleted after some time.
