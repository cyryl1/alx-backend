#!/usr/bin/env python3
"""Initialize flask application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Render the template index.html for the root URL."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5002)
