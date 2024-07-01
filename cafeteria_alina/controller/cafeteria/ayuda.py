from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)


from cafeteria_alina.model.repository.repo_usuario import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion, admin

from cafeteria_alina import db


''' Controlador para las operaciones de producto '''

ayuda = Blueprint('ayuda', __name__,url_prefix='/ayuda') # Crear la sesion


# Ventana de ayuda
@ayuda.route('/')
@requiere_inicio_sesion
@admin
def main():
    return render_template('cafeteria/ayuda.html')
