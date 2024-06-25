from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort


from cafeteria_alina.model.repository.repo_usuario import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin

from cafeteria_alina import db


''' Controlador para las operaciones de producto '''

inventario = Blueprint('inventario', __name__, url_prefix='/inventario') # Crear la sesion


# Ventana inventario
@inventario.route('/')
@requiere_inicio_sesion
@admin
def main():
    return "Inventario"
