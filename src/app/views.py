#!/usr/local/bin/python3
import flask
from flask import render_template, Blueprint, abort, url_for
import flask
import flask_login

from .constants import *
from . import models, forms
from . import db

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    return "Welcome !"

