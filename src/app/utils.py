from datetime import datetime, date
from functools import reduce
import flask
import flask_login
from flask import flash
from sqlalchemy.ext.declarative import declared_attr
import wtforms
import json
import re
import urllib
from sqlalchemy.ext.mutable import MutableList
from wtforms.fields.html5 import DateField

from . import db
from . import models


class ModelMixin(object):

    id                  = db.Column(db.Integer, primary_key=True)
    created_at          = db.Column(db.DateTime, default=datetime.utcnow)
    updated             = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def get_or_na(self, attr):
        """ returns attribute or N/A"""
        r = reduce(getattr, attr.split('.'), self)
        if r is None:
            return "N/A"
        return str(r)

    @classmethod
    def get_current_user(cls):
        try:
            return flask_login.current_user.id
        except:
            return None

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        # Save this model to the database.
        db.session.add(self)

        try:
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            print("[Error on save]", str(error))

        return self

    def update(self):
        db.session.commit()

    def __unicode__(self):
        obj.__mapper__.attrs.keys()

def url_encode(url):
    return urllib.parse.quote(url, safe='')

