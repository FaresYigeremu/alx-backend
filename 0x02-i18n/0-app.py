#!/usr/bin/env python3
"""a basic Flask app in 0-app.py
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """The home/index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
