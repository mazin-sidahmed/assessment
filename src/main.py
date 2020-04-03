import sys, os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


root = os.path.normpath(os.getcwd())

if root not in sys.path:
    sys.path.append(root)

from src.extentions import db


app = Flask(__name__)
app.config.from_object("src.db.config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


from src.api.koncept import koncept
from src.api.new_company import new_company


app.register_blueprint(koncept)
app.register_blueprint(new_company)

if __name__ == "__main__":
    app.run()
