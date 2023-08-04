from flask import Flask, jsonify, make_response
from classes.common import CommonFunctions
import json

app = Flask(__name__)

common = CommonFunctions()
SystemPath = common.get_path()

@app.route('/')
def index():
    return 'Hello world'

@app.route('/0')
def twoRoute():

    with open(SystemPath + "assets/config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["InMeeting"] = "0"

    with open(SystemPath + "assets/config.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    # return 'Complete - 0'
    data = {'message': 'Done', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 200)

@app.route('/1')
def oneRoute():

    with open(SystemPath + "assets/config.json", "r") as jsonFile:
        data = json.load(jsonFile)

    data["InMeeting"] = "1"

    with open(SystemPath + "assets/config.json", "w") as jsonFile:
        json.dump(data, jsonFile)

    # return 'Complete - 1'
    data = {'message': 'Done', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')