import json
import requests
import gnupg
import uuid

## get from .env
url = "http://localhost:5279/"

#Reference:  https://guides.library.illinois.edu/data_encryption/gpgcheatsheet

print ("****")
print ("Welcome to lbry.book.py")

def listFriends():
    print("My Friends")
    with open("friends.json", "rb") as json_file:
        data = json.load(json_file)
        for f in data["friends"]:
            print(f)


def createFriend():
    print("Enter your friends PGP Key fingerprint")
    ## Download off key server


def printMenu():
    print("*** Friends")
    print("a) Add new friend")
    print("l) List friends")
    print("*** Posts")
    print("p) Add new post")
    print("r) Read post")


def downloadPGPKey(url):
    # you can add the key server to ~/.gnupg/gpg.conf
    # eg gpg --keyserver pgp.mit.edu --recv-keys 1EB2638FF56C0C53
    print("Download PGP Key from http://keys.gnupg.net")
    print("Download PGP Key from https://keys.openpgp.org")

    ##


def createPost(title, body):
    gpg = gnupg.GPG(gnupghome="/home/lucascullen/.gnupg")
    #gpg = gnupg.GPG(gnupghome='/path/to/home/directory')
    #value = input("What do you want to say in your post? :\n")
    recipient = "lucas@bitcoinbrisbane.com.au"  #input("Whats the email address of the receipent? :\n")
    print (recipient)
    
    data = gpg.encrypt(title, ["lucas@bitcoinbrisbane.com.au"])
    print (data)

    # #file_name = str(uuid.uuid4())
    # #file_name = file_name + ".txt"
    file_name = "post.txt"
    print(file_name)

    with open(file_name, "rb") as f:
         status = gpg.encrypt_file(f,recipients=[recipient],output="post.txt.gpg")
         print("ok: ", status.ok)


def upload(file_path):
    print("Upload to lbry.io")
    #curl -d'{"method": "publish", "params": {"name": "a-new-stream", "bid": "1.0", "file_path": "/tmp/tmpxe9u833p", "validate_file": false, "optimize_file": false, "tags": [], "languages": [], "locations": [], "channel_account_id": [], "funding_account_ids": [], "preview": false, "blocking": false}}' http://localhost:5279/


def getAllPosts():
    headers = {'content-type': 'application/json'}

    payload = {
        'method': 'claim_search',
        'params': [{"claim_ids": ["d4df0b7ec7b061414ebbd1891d2f6aaecbce20df"]}],
        'jsonrpc': '2.0',
        'id': 0
    }

    response = requests.post(url, json=payload).json()
    ##data = json.loads(response)
    print (response["result"])


#printMenu()
#value = input("Please enter your choice:\n")

#getAllPosts()
createPost("test title", "test body")
#listFriends()