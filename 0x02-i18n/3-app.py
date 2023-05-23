#!/usr/bin/env python3
"""Use flask_babel"""
from flask_babel import Babel, gettext
from flask import Flask, render_template, request


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
    return render_template('2-index.html')

@babel.localeselector
def get_locale():
    """ The decorated function is invoked
    for each request to select a
    language translation to
    use for that request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])
