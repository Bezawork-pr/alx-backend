#!/usr/bin/env python3
"""Use flask_babel"""
from flask_babel import Babel
from flask import Flask, request


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """To keep track of the list
    of supported languages"""
    LANGUAGES = ["en", "fr"]

@babel.localeselector
def getlocale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

