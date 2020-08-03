from flask import Flask, Response, jsonify
from flask_cors import CORS

import requests
import os
import json
import gnupg

app = Flask(__name__)
CORS(app)


def createPost(title, body):
    gpg = gnupg.GPG(gnupghome="/home/lucascullen/.gnupg")
    #gpg = gnupg.GPG(gnupghome='/path/to/home/directory')

    #recipient = input("Whats the email address of the receipent? :\n")
    recipient = "lucas@bitcoinbrisbane.com.au"
    print(recipient)
    
    data = gpg.encrypt(title, recipient)
    print(data)

    file_name = str(uuid.uuid4())
    file_name = "data/" + file_name + ".json"
    print(file_name)

    #file_name = "post.txt"
    #print(file_name)

    json_post = { "type":"text", "title": title, "body": body }
    print(json.dumps(json_post))

    with open(file_name, "w") as outfile:
        json.dump(json_post, outfile)

        with open(file_name, "rb") as f:
            status = gpg.encrypt_file(f,recipients=[recipient],output=file_name + ".txt")
            print("ok: ", status.ok)
            return file_name + ".txt"



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
    #app.run(os.environ['IP_ADDRESS'], port=os.environ['PORT'], debug=os.environ['DEBUG'])
    app.run('127.0.0.1', 5001)