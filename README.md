# cafeteria-alina
Punto de venta para la cafetería ALINA


# Instalación de programas necesarios para ejecutar el punto de venta

### Sobre python3
- sudo apt install python3-venv
- sudo apt install python3-pip

### Sobre pip
- pip install virtualenv
- pip install Flask
- pip install Flask-SQLAlchemy
- pip install pymysql

*Importante* Primero hay que crear el ambiente virtual con:
1. virtualenv [env_name]

**activar**
1. source env_name/bin/activate

**desactivar**
- deactivate

### Verificar lista de paquetes
- pip list

Los paquetes se pueden instalar automáticamente desde la lista de paquetes de `requirements.txt` como.

- (foo)$ pip install -r requirements.txt

O si hay alguna modificación de paquete, guarar con:

- (foo)$ pip freeze > requirements.txt




Exported variables  are not persistent
You gotta do it every time you turn up the computer

## Run proyect
- export FLASK_APP=main
- export FLASK_ENV=production
- flask run

## Debug mode
- export FLASK_ENV=development
- flask run 


# For SQL
Its important the following information in order to connect to the specified database:
- PORT: 3306 (usually)
- USERNAME: root (usually)
- PASSWORD: 1234 (usually, or whatever the password is)

Also the database has to be created before:
- CREATE DATABASE <database_name> 

