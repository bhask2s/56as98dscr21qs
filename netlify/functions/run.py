import json
import sys
import os
from flask import Flask, request, jsonify, send_file, render_template
from app import create_app

# Workaround to ensure the app is loaded from the correct directory
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

app = create_app()

def handler(event, context):
    from flask_lambda import FlaskLambda

    app_lambda = FlaskLambda(app)
    return app_lambda(event, context)

if __name__ == "__main__":
    app.run(debug=True)
