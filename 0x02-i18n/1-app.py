#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Babel config class """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def index():
    """Render page"""
    locale = request.args.get("locale")
    template = render_template("1-index.html", locale=locale)
    return template


if __name__ == '__main__':
    app.run(debug=True)