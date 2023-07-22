from cafeteria_alina import app

#El servidor se inicia desde aquí

@app.route('/credits')
def creditos():
    return "<h1>Davidshiro Pichu</h1>\nMi primer proyecto de software en la vida real!"

@app.route('/')
def home():
    return "<h1>Inicio página</h1>"

if __name__ == '__main__':
    app.run()
