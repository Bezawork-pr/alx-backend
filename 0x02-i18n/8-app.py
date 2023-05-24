#!/usr/bin/env python3
"""Use flask_babel"""
from flask_babel import Babel, gettext
from flask import Flask, render_template, request, g
import pytz
from datetime import datetime


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
    elif g.user and g.user.get('locale')\
            and g.user.get('locale') in supported_langs:
        return g.user.get('locale')
    return request.accept_languages.best_match(supported_langs)


def get_timezone():
    """Get timezone"""
    local_time_zone = request.args.get('timezone')
    if local_time_zone is None:
        return app.config['BABEL_DEFAULT_TIMEZONE']
    if local_time_zone in pytz.all_timezones:
        return local_time_zone
    else:
        raise pytz.exceptions.UnknownTimeZoneError


class Config(object):
    """To keep track of the list
    of supported languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)
app.config.from_object(Config)


@app.route('/')
def index():
    """Greet page visitors"""
    user = get_user()
    string = "."
    time = get_timezone()
    tz = pytz.timezone(time)
    time = datetime.now(tz)
    if user is not None:
        username = user['name'] + string
    else:
        username = None
    return render_template('8-index.html', username=username, time=time)


def get_user():
    """Get user"""
    get_user = request.args.get('login_as')
    try:
        return users[int(get_user)]
    except Exeception as NotFound:
        return None


@app.before_request
def before_request():
    """before_request"""
    g.user = get_user()
