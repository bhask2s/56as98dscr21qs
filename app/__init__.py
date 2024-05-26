from flask import Flask
import os

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('templates'))
    
    with app.app_context():
        # Import routes
        from . import routes
        
        return app
