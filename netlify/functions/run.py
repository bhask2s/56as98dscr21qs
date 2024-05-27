import os
from flask import Flask
from app import create_app

app = create_app()

def handler(event, context):
    from flask_lambda import FlaskLambda

    app_lambda = FlaskLambda(app)
    return app_lambda(event, context)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
