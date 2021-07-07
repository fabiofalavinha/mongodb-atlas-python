class SampleAnalyticsDataStore(object):
    __mongoDbClient = None
    __databaseName = "sample_analytics"

    def __init__(self, connectionString):
        self.__mongoDbClient = self.__buildMongoDbClient(connectionString)

    def __buildMongoDbClient(self, connectionString):
        from pymongo import MongoClient
        client = MongoClient(connectionString)
        return client[self.__databaseName]

    def getCollection(self, collectionName):
        return self.__mongoDbClient[collectionName]
