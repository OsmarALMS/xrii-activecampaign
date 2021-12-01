from flask import Flask, request, jsonify
from services.filesService import FileService
from services.azureSQL import test_connection, insert_json
from exceptions import InvalidUsage

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
    insert_json(json)
    return jsonify(dict(status='Success'))


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
