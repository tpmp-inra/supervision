import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "tpmp-will-never-guess-what"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "supervision.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
