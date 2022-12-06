# See https://docs.python.org/2/library/configparser.html

import ConfigParser

class Properties():
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        try:
            config.read('ConfigFile.properties')
        except Exception as e:
            pass

    def setProperty(self, k, v):
        pass
