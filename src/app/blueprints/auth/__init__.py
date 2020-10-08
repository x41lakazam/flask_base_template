from flask import Blueprint

from app import db

blueprint = Blueprint('auth', __name__)

from . import views, models

