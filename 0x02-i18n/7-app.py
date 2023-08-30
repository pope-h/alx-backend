#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from datetime import datetime

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Babel config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get the best match for the user's preferred language."""
    # Check for locale from URL parameters
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Check for locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Check for locale from request header
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    # Default to Babel's default locale
    return babel.default_locale


@babel.timezoneselector
def get_timezone():
    """Get the timezone from the URL parameters."""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate and return the timezone if it's valid
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    """Get the timezone from user's setting"""
    if g.user and g.user.get('timezone'):
        user_timezone = g.user['timezone']
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    """Default to UTC"""
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """Get the user from the login_as URL parameter or None."""
    login_as = request.args.get('login_as')
    if login_as is not None:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """Get the user and set it as a global."""
    g.user = get_user()


@app.route("/")
def index():
    """Render page"""
    locale = get_locale()
    user_timezone = get_timezone()
    user_tz = pytz.timezone(user_timezone)

    current_time = datetime.now(user_tz).strftime('%b %d, %Y, %I:%M:%S %p')
    template = render_template(
        "7-index.html",
        locale=locale,
        current_time=current_time
    )
    return template
