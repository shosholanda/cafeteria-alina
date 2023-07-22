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

cafe = Blueprint('cafe', __name__) # Crear la sesion


# Ventana de estadísticas
@cafe.route('/estadisticas')
@requiere_inicio_sesion
def estadisticas():
    return "estadisticas"