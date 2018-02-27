import os

class Config(object):
    db_fallback = "C:\\Users\\David\\db\\bowling.db"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + db_fallback
    SQLALCHEMY_TRACK_MODIFICATIONS = False 