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
from cafeteria_alina.controller.cafeteria.inicio import inicio
from cafeteria_alina.controller.cafeteria.estadisticas import estadisticas
from cafeteria_alina.controller.cafeteria.inventario import inventario
from cafeteria_alina.controller.cafeteria.productos import productos
from cafeteria_alina.controller.cafeteria.ventas import ventas
from cafeteria_alina.controller.cafeteria.perfil import perfil
from cafeteria_alina.controller.cafeteria.ayuda import ayuda
from cafeteria_alina.controller.cafeteria.precios import precios
from cafeteria_alina.controller.cafeteria.categorias import categorias
from cafeteria_alina.controller.cafeteria.sucursales import sucursales
from cafeteria_alina.controller.cafeteria.tipo_productos import tipo_productos

app.register_blueprint(auth)
app.register_blueprint(inicio)
app.register_blueprint(perfil)
app.register_blueprint(estadisticas)
app.register_blueprint(inventario)
app.register_blueprint(productos)
app.register_blueprint(ventas)
app.register_blueprint(ayuda)
app.register_blueprint(precios)
app.register_blueprint(categorias)
app.register_blueprint(sucursales)
app.register_blueprint(tipo_productos)


# With caution, create the database that has the same config in config.py file
with app.app_context():
    db.create_all()



