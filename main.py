from cafeteria_alina import app

from flask import (
    render_template, g, redirect, request, session, url_for
)

#El servidor se inicia desde aquí

@app.route('/credits')
def creditos():
    return "<h1>Davidshiro Pichu</h1>\nMi primer proyecto de software en la vida real!"

@app.route('/')
def home():
    if g.user:
        return redirect(url_for('inicio.main'))
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
