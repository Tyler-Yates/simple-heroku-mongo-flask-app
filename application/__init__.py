from flask import Flask

app = Flask(__name__)

# Import the routes file to set up the endpoints
import application.routes

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
