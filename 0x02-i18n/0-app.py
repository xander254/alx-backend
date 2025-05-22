#!/usr/bin/env python3
from flask import Flask, render_template
"""
Basic Flask app with a single route
"""


app = Flask(__name__)


@app.route("/")
def home() -> str:
    """
    Return the index file for the stated route
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
