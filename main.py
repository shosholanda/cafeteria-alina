from src import app
from livereload import Server

from flask import (
    render_template, g, redirect, request, session, url_for
)

#El servidor se inicia desde aquí

@app.route('/credits')
def creditos():
    return "<h1>Davidshiro Pichu</h1>\nMi primer proyecto de software en la vida real!"

@app.route('/')
def home():
    '''Página publica'''
    if g.user:
        return redirect(url_for('inicio.main'))
    return render_template('home.html')

def cafeteria_alina():
    '''Correr desde el server waitress-serve'''
    return app

if __name__ == '__main__':
    # Excecute with python3 main.py
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve(port=5000)


