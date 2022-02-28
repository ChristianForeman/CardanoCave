from blockfrost import BlockFrostApi, ApiError, ApiUrls


class BF_Api:
    def __init__(self, apiKeyFile):
        apiFile = open(apiKeyFile)
        self.apiKey = apiFile.readline()
        apiFile.close()
        print(self.apiKey)