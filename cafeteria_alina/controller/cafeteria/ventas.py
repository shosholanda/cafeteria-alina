from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)


from cafeteria_alina.model.repository.repo_usuario import *

from cafeteria_alina.controller.auth import requiere_inicio_sesion

from cafeteria_alina import db


''' Controlador para las operaciones de producto '''

ventas = Blueprint('ventas', __name__,url_prefix='/ventas') # Crear la sesion


# Ventana de ventas
@ventas.route('/')
@requiere_inicio_sesion
def main():
    return "Ventas"
