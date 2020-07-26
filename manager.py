from app import create_app
from app import db, User, socketio
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand


from config import config

config_class = config['development']
app = create_app(config_class)
migrate = Migrate(app, db)



if __name__ == '__main__':
  socketio.run(app)

