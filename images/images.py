from flask import Flask, jsonify, send_file
from werkzeug.exceptions import NotFound, ServiceUnavailable

import json
import requests
import os
import sys

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return jsonify({})

@app.route("/health-check", methods=['GET'])
def health_check():
    return jsonify({ })

@app.route("/images/<digest>/size/<size>", methods=['GET'])
def image(digest, size):
    return send_file('girl.png', mimetype='image/png')