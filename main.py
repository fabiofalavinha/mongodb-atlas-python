from pandas import DataFrame

import persistence

mongoDbSectionName = "MongoDB"
mongoDbConnectionStringPropertyName = "connectionString"

if __name__ == '__main__':

    configurationRepository = persistence.ConfigurationRepository()
    mongoDbConnectionString = \
        configurationRepository.getConfiguration(mongoDbSectionName, mongoDbConnectionStringPropertyName)

    accountRepository = persistence.AccountRepository(mongoDbConnectionString)

    accounts = accountRepository.findAccounts()

    print(DataFrame(accounts))
