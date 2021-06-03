import json
import os
import secrets


CONF_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/vax/config/"


with open(CONF_DIR + "config.json") as conf_file:
    config_data = json.load(conf_file)


class Config:
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(16))


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
