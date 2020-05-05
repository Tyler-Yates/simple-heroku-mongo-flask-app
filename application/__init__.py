from flask import Flask

from application.data.custom_json_encoder import CustomJsonEncoder
from application.data.dao import ApplicationDao

app = Flask(__name__)
app.json_encoder = CustomJsonEncoder

dao = ApplicationDao()

# Import the routes files to set up the endpoints
import application.routes.html_routes
