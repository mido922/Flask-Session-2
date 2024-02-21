class Config:

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI ="sqlite:///project.db"

class ProductionConfig(Config):
    DEBUG=False

config_options = {
    "dev": DevelopmentConfig,
    "prd:": ProductionConfig,
}