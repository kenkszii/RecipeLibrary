from decouple import config


class config:
  SECRET_KEY=config("SECRET_KEY")
  SQLALCHEMY_TRACK_MODIFICATION=config('SQLALCHEMY_TRACK_MODIFICATION', cast=bool)

  
class DevConfig(config):
  SQLALCHEMY_DATABASE_URI= "sqlite:///dev.db"
  DEBUG=True
  SQLALCHEMY_ECHO=True


class ProdConfig(config):
  pass


class TestConfig(config):
  SQLALCHEMY_DATABASE_URI="sqlite:///test.db"
  SQLALCHEMY_ECHO=False
  TESTING=True
