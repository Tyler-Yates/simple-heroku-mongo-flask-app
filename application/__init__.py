from flask import Flask

from application.CustomJsonEncoder import CustomJsonEncoder
from application.models import ApplicationDao

app = Flask(__name__)
app.json_encoder = CustomJsonEncoder

dao = ApplicationDao()

# Import the routes file to set up the endpoints
import application.html_routes
import application.api_routes
