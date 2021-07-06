import ConfigParser


class ConfigurationRepository(object):
    __configParser = ConfigParser.ConfigParser()

    def __init__(self):
        self.__configParser.read('config.ini')

    def getConfiguration(self, sectionName, propertyName):
        return self.__configParser.get(sectionName, propertyName)
