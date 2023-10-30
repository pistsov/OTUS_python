from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_DB_URL = "postgresql://postgres:secretpassword@0.0.0.0:5432/postgres"

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    DEFAULT_DB_URL,
)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_ECHO = False
    SECRET_KEY = "ad93f037b760e6873c1d5141d85afae803f42bcf25bf557527417efe9a14ad8f"


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False