
class Config:
  SECRET_KEY = 'chat'


class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'mysql://local:Cuenca123.@localhost/chat'
  SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
  'development' : DevelopmentConfig,
  'default': DevelopmentConfig,
}
