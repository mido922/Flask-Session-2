from flask import Flask
from app.config import config_options as AppConfig
from app.models import db


def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    print("Current config is: ", current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)



    return app