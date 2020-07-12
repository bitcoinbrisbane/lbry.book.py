from flask import Flask, Response, jsonify
from flask_cors import CORS

import requests
import os
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get():
    return 'ok'


@app.route('/friends', methods=['GET'])
def listFriends():
    print("My Friends")
    with open("friends.json", "rb") as json_file:
        data = json.load(json_file)
        return (data)


@app.route('/post', methods=['POST'])
def createPost():
    content = request.json
    print(content['title'])
    #return jsonify({"uuid":uuid})
    return 'ok'


if __name__ == '__main__':
    #app = init_app()
    app.run(os.environ['IP_ADDRESS'], port=os.environ['PORT'], debug=os.environ['DEBUG'])