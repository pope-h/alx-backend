#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template, request
from flask_babel import Babel


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Render page"""
    locale = request.args.get("locale")
    template = render_template("1-index.html", locale=locale)
    return template
