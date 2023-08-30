#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template, request, g
from flask_babel import Babel

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
    template = render_template("6-index.html", locale=locale)
    return template
