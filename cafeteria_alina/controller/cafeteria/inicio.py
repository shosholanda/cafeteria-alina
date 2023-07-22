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

inicio = Blueprint('inicio', __name__) # Crear la sesion


# Página de inicio de sesion, dentro de la sesion
@inicio.route('/inicio')
@requiere_inicio_sesion
def main():
    return render_template('cafeteria/inicio.html')
