from cafeteria_alina import app

#El servidor se inicia desde aquí

@app.route('/credits')
def hola():
    return "<h1>Davidshiro Pichu</h1>\nMi primer proyecto de software en la vida real!"


if __name__ == '__main__':
    app.run()