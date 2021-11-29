from exceptions import InvalidUsage


class FileCsvToGcs:

    @staticmethod
    def valid_json(json):

        if not json.get("AccountData").get("MerchantID"):
            raise InvalidUsage('Field MerchantID is required!', status_code=500)
