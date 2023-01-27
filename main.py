from flask import Flask

#El servidor se inicia desde aquí
app = Flask(__name__)

@app.route('/')
def hola():
    return "Mi primer proyecto de software en la vida real!"



