from src.api import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Sohaib\\historique.db'
db = SQLAlchemy(app)
