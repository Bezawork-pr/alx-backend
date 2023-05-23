#!/usr/bin/env python3
"""Use flask_babel"""
from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """To keep track of the list
    of supported languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """Greet page visitors"""
    return render_template('1-index.html')
