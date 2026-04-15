#!/usr/bin/python3
""" A simple Flask API """
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
