from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.exceptions import abort


from cafeteria_alina.model.repository.repo_usuario import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion

from cafeteria_alina import db


''' Controlador para las operaciones de producto '''

perfil = Blueprint('perfil', __name__, url_prefix='/perfil') # Crear la sesion


# Ventana perfil
@perfil.route('/')
@requiere_inicio_sesion
def main():
    return "Perfil"
