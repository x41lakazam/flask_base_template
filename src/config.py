#!/usr/local/bin/python3

import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_NAME = "Real Estate Raanana"

    # Uncomment to setup Setup an App icon
    # APP_ICON = "static/img/logo.jpg"

    BABEL_DEFAULT_LOCALE = "fr"
    # Your application default translation path
    BABEL_DEFAULT_FOLDER = "translations"
    # The allowed translation for you app
    LANGUAGES = {
        "en": {"flag": "gb", "name": "English"},
        "fr": {"flag": "fr", "name": "Français"},
        "he": {"flag": "il", "name": "עברית"},
    }

    # ---------------------------------------------------
    # Image and file configuration
    # ---------------------------------------------------
    # The file upload folder, when using models with files
    UPLOAD_FOLDER = basedir + "/app/static/uploads/"

    # The image upload folder, when using models with images
    IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

    # The image upload url, when using models with images
    IMG_UPLOAD_URL = "/static/uploads/"
    # Setup image size default is (300, 200, True)
    # IMG_SIZE = (300, 200, True)

    @staticmethod
    def configure(app):
        pass

class ProdConfig(Config):

    PORT  = 5050
    HOST  = "0.0.0.0"
    DEBUG = False

    WTF_CSRF_ENABLED = False
    # Your App secret key
    SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

    # Flask-WTF flag for CSRF
    CSRF_ENABLED = True

    # The SQLAlchemy connection string.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    #SQLALCHEMY_BINDS = {}


class DevConfig(Config):

    #PORT  = 8080
    HOST  = "0.0.0.0"
    DEBUG = True

    WTF_CSRF_ENABLED = False
    # Your App secret key
    SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"

    # Flask-WTF flag for CSRF
    CSRF_ENABLED = True

    # The SQLAlchemy connection string.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    #SQLALCHEMY_BINDS = {
        #"db2": 'mysql://db2.sqlite'
    #}

    SQLALCHEMY_TRACK_MODIFICATIONS = False





config = {
    "development": DevConfig,
    "production":ProdConfig,
}


