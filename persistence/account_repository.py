class AccountRepository(object):
    __sampleAnalyticsDataStore = None
    __collectionName = "accounts"

    def __init__(self, connectionString):
        from persistence.sample_analytics_datastore import SampleAnalyticsDataStore
        self.__sampleAnalyticsDataStore = SampleAnalyticsDataStore(connectionString)

    def findAccounts(self):
        accounts = self.__sampleAnalyticsDataStore.getCollection(self.__collectionName)
        return accounts.find()
