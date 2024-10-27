from os import environ

from dotenv import load_dotenv, dotenv_values


class Configs:
    def __init__(self):
        load_dotenv()
        # setup non secret config variables here
        [setattr(self, key, value) for key, value in dotenv_values('.env').items()]

    def __getattr__(self, item):
        attr = environ.get(item.upper())
        setattr(self, item, attr) if attr is not None else ...  # this is not really necessary
        return attr
