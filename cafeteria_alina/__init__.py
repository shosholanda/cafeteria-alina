#App
from flask import Flask
#SQL connections
from flask_sqlalchemy import SQLAlchemy

#The package of the project.
# From here all the app will be running with the configuration saved in config.py

app = Flask(__name__)

# Load all the configurations
app.config.from_object("config.DeveloperConfig")

# load database conections
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()



