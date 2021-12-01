from exceptions import InvalidUsage


class FileService:

    @staticmethod
    def valid_json(json):

        if json.get("AccountData") or json.get("Triggers"):
            if not json.get("AccountData").get("MerchantID"):
                raise InvalidUsage('Field MerchantID is required!', status_code=500)

        if json.get("ContactsData"):
            if not json.get("ContactsData").get("Email"):
                raise InvalidUsage('Field ContactsData.Email is required!', status_code=500)
