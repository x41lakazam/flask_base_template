#!/usr/local/bin/python3

import os
import logging

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.exceptions import HTTPException
from flask_bootstrap import Bootstrap


# instantiate extensions
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

def create_app(environment='development'):

    from config import config
    from .views import main_blueprint
    from .blueprints import auth
    from . import constants
    from .filters import filters
    from . import utils, forms

    # Instantiate app.
    app = Flask(__name__)

    for f in filters:
        app.add_template_filter(f)

    # Set app config.
    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    # Set up extensions.
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints.
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(main_blueprint)

    # Register bootstrap
    #bootstrap = Bootstrap(app)

    # Set up flask login.
    @login_manager.user_loader
    def get_user(id):
        return auth.models.User.query.get(int(id))

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    login_manager.anonymous_user = auth.models.AnonymousUser

    # Error handlers.
    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template('error.jin', error=exc), exc.code

    @app.context_processor
    def inject_constants():
        """
        Inject contstants to the jinja context
        """

        d = {
            item:getattr(constants, item)
                for item in dir(constants)
                if not item.startswith('_')

        }
        return d

    return app


