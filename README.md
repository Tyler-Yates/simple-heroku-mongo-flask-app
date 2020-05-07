# simple-heroku-mongo-flask-app
A simple Heroku Flask application that connects to MongoDB.

## Prerequisites
You will need a [Heroku](https://www.heroku.com/) account and the
[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) to run this application.
Heroku has a [free tier](https://www.heroku.com/free).
It is recommended that you follow [Heroku's guide](https://devcenter.heroku.com/articles/getting-started-with-python)
to getting started with Python before running this application.

You will also need a [MongoDB](https://www.mongodb.com/) database to run this application.
You can get a free MongoDB database by signing up for [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
MongoDB Atlas has a free tier which includes a simple cluster deployment.

This README assumes you are running on Linux.

You will need a [Python 3](https://www.python.org/about/) interpreter to run this application.
The Python 3 interpreter should include the `venv` module.

## Setup
You will need to create a virtual environment to run this application.
Run the following commands at the root of this repo:
```
python3 -m venv venv
source venv/bin/activate
pip install -Ur requirements.txt
```

Tell Heroku that you want this repo to be an application:
```
heroku create
```

## Running
To run this application, you need to set some environment variables:
* `MONGO_USER` - The username for the MongoDB connection
* `MONGO_PASSWORD` - The password for the MongoDB connection
* `MONGO_HOST` - The host to connect to for the MongoDB connection

### Local
After setting up the environment variables, you can run the application locally.
Be sure you have activated the virtual environment before running this command:
```
heroku local
```

You should then be able to access the application at [http://0.0.0.0:5000](http://0.0.0.0:5000) in your browser.

### Heroku
Once you have verified that the application works locally, you can deploy to Heroku:
```
git push heroku master
```

Once the deploy succeeds you can spin up a web dynamo to serve requests:
```
heroku ps:scale web=1
```

You can use the following command to open the Heroku deployment in your browser:
```
heroku open
```

## Tests
You can use [tox](https://tox.readthedocs.io/en/latest/) to run the tests in this repo.

First, install tox in the virtual environment:
```
pip install tox
```

Next, simply run `tox` in the root of the repo.
In addition to running the unit tests, code linting and formatting will be performed using
[isort](https://github.com/timothycrosley/isort), [black](https://github.com/psf/black),
and [flake8](https://flake8.pycqa.org/en/latest/).

## Database
This application creates a database called `test`.
It also creates a collection in that database called `test_collection`.

This application creates a TTL index on `test_collection` so documents created by this application will be
deleted after some time.
