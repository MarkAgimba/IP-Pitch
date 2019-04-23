from app import create_app,db
from app.models import User,Role
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand

#Creating app instance
app = create_app('test')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

