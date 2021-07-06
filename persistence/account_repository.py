class AccountRepository(object):
    __mongoDbClient = None
    __databaseName = "sample_analytics"
    __collectionName = "accounts"

    def __init__(self, connectionString):
        self.__mongoDbClient = self.__buildMongoDbClient(connectionString)

    def __buildMongoDbClient(self, connectionString):
        from pymongo import MongoClient
        client = MongoClient(connectionString)
        return client[self.__databaseName]

    def findAccounts(self):
        accounts = self.__mongoDbClient[self.__collectionName]
        return accounts.find()
