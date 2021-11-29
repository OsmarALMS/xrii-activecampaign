from flask import Flask, request, jsonify
from services.filesService import FileCsvToGcs
from exceptions import InvalidUsage

app = Flask(__name__)


@app.route("/integration", methods=['POST'])
def integration():
    json = request.json
    FileCsvToGcs.valid_json(json)
    return jsonify(dict(status='Success'))


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    app.run()
