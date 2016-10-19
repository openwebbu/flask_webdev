import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # path of our database file, required by the Flask-SQLAlchemy extension.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') # folder where we will store the SQLAlchemy-migrate data files.
