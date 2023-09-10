from flask_sqlalchemy import SQLAlchemy
from config.Config import DevelopmentConfig
from flask import Flask

configuration = DevelopmentConfig()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{configuration.MYSQL_USER}@{configuration.MYSQL_HOST}/{configuration.MYSQL_DB}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)