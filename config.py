import os
class Config:
  SECRET_KEY = os.environ.get('SECRET')


class DevelopmentConfig(Config):
  DEBUG = False
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SOCKETIO_MESSAGE_QUEUE = None


config = {
  'development' : DevelopmentConfig,
  'default': DevelopmentConfig,
}
