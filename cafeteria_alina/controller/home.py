from flask import (
    render_template, Blueprint, flash, g, redirect, request, session, url_for
)

'''  '''

home = Blueprint('home', __name__, url_prefix='/home') # Crear la sesion

# Página de home de página. EStá afuera de la sesion
@home.route('/')
def main():
    return render_template('home.html')