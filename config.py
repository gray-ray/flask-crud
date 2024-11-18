

class Config: 
  DEBUG = False

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123456@localhost/python-flask'

  SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
  DEBUG = True


class ProductionConfig(Config):
  DEBUG = False