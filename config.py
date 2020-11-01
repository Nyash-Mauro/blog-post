import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
      
     DEBUG = False
     TESTING = False
     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:@localhost/'
     QUOTES_API = 'http://quotes.stormconsultancy.co.uk/random.json'
     SECRET_KEY = 'nyaga'
     SQLALCHEMY_TRACK_MODIFICATIONS = True
  
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://@localhost/"


class TestingConfig(Config):
    TESTING = True

config_options = {
'test':TestingConfig,
'production':ProductionConfig,
'development': DevelopmentConfig
}
