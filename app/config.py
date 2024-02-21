class Config:

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI ="sqlite:///project.db"

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:123@localhost:5432/FlaskSession2'

config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig,
}