#!/usr/bin/env python3
"""
Flask app with a single route and babel instanse in a
variable to force the locale from a url parameter
"""


from flask import Flask, render_template, request
from flask_babel import Babel, get_locale, _


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
app.jinja_env.globals['get_locale'] = get_locale


@babel.localeselector
def get_locale() -> str:
    """
    Get the best locale from the user

    Returns:
        str: A language code such as 'en' or 'fr'
    """
    locale_from_url = request.args.get("locale")
    if locale_from_url in app.config['LANGUAGES']:
        return locale_from_url

    return (request.accept_languages.best_match(app.config['LANGUAGES']))


@app.route("/")
def home() -> str:
    """Return the index file for the stated route"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
