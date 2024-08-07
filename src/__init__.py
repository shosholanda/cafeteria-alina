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
from src.controller.auth import auth
from src.controller.cafeteria.inicio import inicio
from src.controller.cafeteria.estadisticas import estadisticas
from src.controller.cafeteria.productos import productos
from src.controller.cafeteria.ventas import ventas
from src.controller.cafeteria.perfil import perfil
from src.controller.cafeteria.ayuda import ayuda
from src.controller.cafeteria.precios import precios
from src.controller.cafeteria.gastos import gastos
from src.controller.cafeteria.categorias import categorias
from src.controller.cafeteria.sucursales import sucursales
from src.controller.cafeteria.tipo_productos import tipo_productos
from src.controller.cafeteria.tipo_gastos import tipo_gastos

app.register_blueprint(auth)
app.register_blueprint(inicio)
app.register_blueprint(perfil)
app.register_blueprint(estadisticas)
app.register_blueprint(productos)
app.register_blueprint(ventas)
app.register_blueprint(ayuda)
app.register_blueprint(precios)
app.register_blueprint(gastos)
app.register_blueprint(categorias)
app.register_blueprint(sucursales)
app.register_blueprint(tipo_productos)
app.register_blueprint(tipo_gastos)

# With caution, create the database that has the same config in config.py file
with app.app_context():
    db.create_all()



