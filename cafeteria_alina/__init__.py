#App of the proyect.
# The main function imports this file.
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

# Importar vistas a la aplicación
from cafeteria_alina.controller.auth import auth
from cafeteria_alina.controller.home import home
from cafeteria_alina.controller.cafeteria.inicio import inicio
from cafeteria_alina.controller.cafeteria.perfil import perfil

app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(inicio)
app.register_blueprint(perfil)


# With caution, create the database that has the same config in config.py file
with app.app_context():
    db.create_all()



