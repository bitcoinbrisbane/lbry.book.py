from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import os


def init_app():
    app = Flask(__name__)
    
    # Register base route
    @app.route("/")
    def base():
        return "Hello"
    
    CORS(app)

    return app
