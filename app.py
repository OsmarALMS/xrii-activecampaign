from flask import Flask, request, jsonify
from services.filesService import FileService
from services.azureSQL import test_connection, insert_account, insert_contact
from exceptions import InvalidUsage
from services.activeCampaign import account, contacts, account_contact

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(dict(status='Success'))


@app.route("/test_connection")
def connection():
    return jsonify(dict(dbVersion=test_connection()))


@app.route("/integration", methods=['POST'])
def integration():
    json = request.json
    FileService.valid_json(json)

    # ACCOUNT
    account_return = account(json)
    if account_return.status_code in (200, 201):
        insert_account(account_return.json().get("account").get("id"), json)
    else:
        return account_return.json(), account_return.status_code

    # CONTACT
    contact_return = contacts(json)
    if contact_return.status_code in (200, 201):
        insert_contact(contact_return.json().get("contact").get("id"),
                       account_return.json().get("account").get("id"), json)
    else:
        return contact_return.json(), contact_return.status_code

    # ASSOCIATE ACCOUNT/CONTACT
    account_contact(account_return.json().get("account").get("id"),
                    contact_return.json().get("contact").get("id"))

    return jsonify(dict(status='Success'))


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
