#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Greet page visitors"""
    return render_template('0-index.html')
