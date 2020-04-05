import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import time

import json

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers='Content-Type')

@app.route("/classify", methods = ['POST', 'GET'])
def handleClassification():
    if request.method == 'POST':
        print("POST")
        print('=== :', request.json)
        with open('resource/request.txt', 'w') as outfile:
            json.dump(request.json, outfile)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    else:
        isOK = True
        try_count = 0
        while try_count < 10:
            try:
                with open('resource/result.txt') as json_file:
                    data = json.load(json_file)
                    print('=== : GET', data)
                    #response = jsonify(data)
                    #print('=== response :', response)
                    isOK = True
                    break
            except FileNotFoundError as error:
                print('=== : GET : ', error)
                isOK = False
            except ValueError as error:
                print('=== : GET : ', error)
                isOK = False
            except ValueError as error:
                print('=== : GET : ', error)
                isOK = False
            try_count = try_count + 1
            time.sleep(2)
        print('=== : GET : sending response')
        if isOK:
            return json.dumps(data), 200, {'ContentType': 'application/json'}
        else:
            return json.dumps(""), 500, {'ContentType': 'application/json'}

if __name__ == "__main__":
    app.run("localhost", 5000, debug = True)
