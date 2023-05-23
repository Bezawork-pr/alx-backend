#!/usr/bin/env python3
"""Use flask_babel"""
from flask_babel import Babel, gettext
from flask import Flask, render_template, request, g


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_locale():
    """ The decorated function is invoked
    for each request to select a
    language translation to
    use for that request"""
    supported_langs = app.config['LANGUAGES']
    local_lang = request.args.get('locale')
    if local_lang in supported_langs:
        return local_lang
    return request.accept_languages.best_match(supported_langs)


class Config(object):
    """To keep track of the list
    of supported languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel.init_app(app, locale_selector=get_locale)
app.config.from_object(Config)


@app.route('/')
def index():
    """Greet page visitors"""
    return render_template('4-index.html')

def get_user():
    """Get user"""
    get_user = request.args.get('login_as')
    try:
        return int(users[get_user])
    except:
        return None

@app.before_request
def before_request():
    """before_request"""
    g.user = get_user()
    print(g.user["name"])