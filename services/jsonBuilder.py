
def get_json_account(json):
    return {
        "account": {
            "name": str(json.get("AccountData").get("MerchantID")),
            "accountUrl": str(json.get("AccountData").get("URL")),
            "fields": [
                {
                    "customFieldId": 1,
                    "fieldValue": str(json.get("AccountData").get("OrganisationName"))
                },
                {
                    "customFieldId": 2,
                    "fieldValue": str(json.get("AccountData").get("Address"))
                },
                {
                    "customFieldId": 11,
                    "fieldValue": str(json.get("AccountData").get("Phone"))
                },
                {
                    "customFieldId": 14,
                    "fieldValue": str(json.get("AccountData").get("Email"))
                },
                {
                    "customFieldId": 15,
                    "fieldValue": str(json.get("AccountData").get("VerfiedEmail"))
                },
                {
                    "customFieldId": 16,
                    "fieldValue": str(json.get("AccountData").get("ActiveCardDetails"))
                },
                {
                    "customFieldId": 17,
                    "fieldValue": str(json.get("AccountData").get("SelectedPlan"))
                },
                {
                    "customFieldId": 18,
                    "fieldValue": str(json.get("AccountData").get("MonthlyTrackedUsers"))
                },
                {
                    "customFieldId": 19,
                    "fieldValue": str(json.get("AccountData").get("AverageDailyUsers"))
                },
                {
                    "customFieldId": 23,
                    "fieldValue": str(json.get("AccountData").get("EngagementRate"))
                },
                {
                    "customFieldId": 24,
                    "fieldValue": str(json.get("AccountData").get("RetentionRate"))
                },
                {
                    "customFieldId": 25,
                    "fieldValue": str(json.get("AccountData").get("StickyFactor"))
                },
                {
                    "customFieldId": 26,
                    "fieldValue": str(json.get("AccountData").get("AddOns"))
                }
            ]
        }
    }


def get_json_contact(json):
    return {
        "contact": {
            "email": str(json.get("ContactsData").get("Email")),
            "firstName": str(json.get("ContactsData").get("AccountHolderName")).split(" ")[0],
            "lastName": str(json.get("ContactsData").get("AccountHolderName")).split(" ")[-1],
            "phone": str(json.get("ContactsData").get("Mobile")),
            "fieldValues": [
                {
                    "field": 4,
                    "value": str(json.get("ContactsData").get("VerfiedEmail"))
                }
            ]
        }
    }


def get_json_account_contact(idAccount, idContact):
    return {
        "accountContact": {
            "contact": idContact,
            "account": idAccount
        }
    }
