from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config.from_object("app.config.Config")
    db.init_app(app)
    return app
