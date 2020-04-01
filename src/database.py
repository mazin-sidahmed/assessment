from src.main import app
from flask_sqlalchemy import SQLAlchemy


app.config.from_object("src.db.config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)