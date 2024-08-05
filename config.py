#Persistent default configurations for the server

class Config:

    DEBUG = True
    TESTING = True

    #Database configuration
    DATABASE_USER = "root"
    DATABASE_PASSWORD = "password"
    IP_ADDRESS = "127.0.0.1"
    PORT = 3306
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{IP_ADDRESS}:{PORT}/cafeteria_alina"

    #Track modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#Default configuration for production mode.
#Extends from Config class
class ProductionConfig(Config):

    DEBUG = False

#Default configration for debug mode (developer)
#Extends from Config class
class DeveloperConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev'
    TESTING = True
    
