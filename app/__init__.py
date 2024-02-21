from flask import Flask
from app.config import config_options as AppConfig
from app.models import db
from flask_migrate import Migrate

def create_app(config_name='prd'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    print("Current config is: ", current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(current_config)

    db.init_app(app)
    migrate= Migrate(app,db, render_as_batch=True)


    return app