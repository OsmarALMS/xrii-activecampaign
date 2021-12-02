import requests

endpoint = "https://xrii1637705563.api-us1.com/api/3/"
headers = {"Api-Token": "f7667ea237110c74bfbe87174567c65c993eb532d7137b19365ace70d7dd003379ef6ba5"}


def get_campaigns():
    response = requests.get(endpoint + "campaigns", headers=headers)
    return response
