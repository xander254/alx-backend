#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
"""
Basic Flask app with a single route and babel instanse in a
variable
"""


class Config:
    """
    Configuration class that sets supported languages and defaults
    for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Get the best locale for the user

    Returns:
        str: A language code such as 'en' or 'fr'
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> str:
    """Return the index file for the stated route"""
    title = _("home_title")
    header = _("home_header")
    return render_template("3-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run()
