#!/usr/bin/env python3
"""
Basic Flask app with a single route and babel instanse in a
variable
"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Babel config Class"""
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
