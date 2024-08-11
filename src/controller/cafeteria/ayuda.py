from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from src.controller.auth import admin, worker, admin_or_worker


''' Controlador para las operaciones de producto '''

ayuda = Blueprint('ayuda', __name__,url_prefix='/ayuda') # Crear la sesion


# Ventana de ayuda
@ayuda.route('/')
@admin_or_worker
def main():
    return render_template('cafeteria/ayuda.html')
