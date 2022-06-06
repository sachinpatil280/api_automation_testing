import configparser
import os

config = configparser.RawConfigParser()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if "posix" in os.name:
    config.read(os.path.join(ROOT_DIR, "../configurations/config.ini"))
else:
    config.read("..\\..\\configurations\\config.ini")


def read_config(config_section):
    values = dict(config.items(config_section))
    return values
