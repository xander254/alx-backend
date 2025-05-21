#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel
"""
Basic Flask app with a single route and babel instanse in a
variable
"""


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def home():
    """
    Return the index file for the stated route
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
