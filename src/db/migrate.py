import sys, os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

root = os.path.normpath(os.getcwd())

if root not in sys.path:
    sys.path.append(root)


from src.main import db, app


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()