import sys
import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from app.routes import initialize_routes
from app.config import Config

# Añadir el directorio base al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    api = Api(app)
    initialize_routes(api)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
