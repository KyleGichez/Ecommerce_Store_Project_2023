from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Register extensions
def register_extensions(app):
    db.init_app(app)