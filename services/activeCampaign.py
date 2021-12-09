import requests
from services.jsonBuilder import get_json_account, get_json_contact, get_json_account_contact

endpoint = "https://xrii1637705563.api-us1.com/api/3/"
headers = {"Api-Token": "f7667ea237110c74bfbe87174567c65c993eb532d7137b19365ace70d7dd003379ef6ba5"}


def get_campaigns():
    response = requests.get(endpoint + "campaigns", headers=headers)
    return response


def account(json):
    response = requests.post(endpoint + "accounts", json=get_json_account(json), headers=headers)
    # If Account exists, find and update
    if response.status_code == 422:
        list_accounts = requests.get(endpoint + "accounts", headers=headers)
        for accounts in list_accounts.json().get("accounts"):
            if accounts['name'] == json.get("AccountData").get("MerchantID"):
                response = requests.put(endpoint + "accounts/" + accounts['id'],
                                        json=get_json_account(json), headers=headers)
    return response


def contacts(json):
    response = requests.post(endpoint + "contacts", json=get_json_contact(json), headers=headers)
    # If Contact exists, find and update
    if response.status_code == 422:
        list_contacts = requests.get(endpoint + "contacts", headers=headers)
        for c in list_contacts.json().get("contacts"):
            if c['email'] == str(json.get("ContactsData").get("Email")):
                response = requests.put(endpoint + "contacts/" + c['id'],
                                        json=get_json_contact(json), headers=headers)
    return response


def account_contact(idAccount, idContact):
    requests.post(endpoint + "accountContacts",
                  json=get_json_account_contact(idAccount, idContact), headers=headers)
