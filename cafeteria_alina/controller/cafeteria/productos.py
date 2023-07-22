from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort

from cafeteria_alina.model.usuario import Usuario
from cafeteria_alina.model.producto import Producto

from cafeteria_alina.model.repository.repo_usuario import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion

from cafeteria_alina import db


''' Controlador para las operaciones de producto '''

productos = Blueprint('productos', __name__, url_prefix='/productos') # Crear la sesion

# Página de productos de página. EStá afuera de la sesion
@productos.route('/')
def home():
    return render_template('home.html')