# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Config:
    FLASKE_ENV = "development"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="SUPER_BAD_KEY")
    WTF_CSRF_ENABLED = True


class ProductionConfig(Config):
    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
