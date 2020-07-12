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


def createPost(title, body):
    gpg = gnupg.GPG(gnupghome="/home/lucascullen/.gnupg")
    #gpg = gnupg.GPG(gnupghome='/path/to/home/directory')

    #recipient = input("Whats the email address of the receipent? :\n")
    recipient = "lucas@dltx.io"
    print(recipient)
    
    data = gpg.encrypt(title, recipient)
    print(data)

    file_name = str(uuid.uuid4())
    file_name = file_name + ".json"
    print(file_name)

    #file_name = "post.txt"
    #print(file_name)

    json_post = { "type":"text", "title": title, "body": body }
    print(json.dumps(json_post))

    with open(file_name, "w") as outfile:
        json.dump(json_post, outfile)

        with open(file_name, "rb") as f:
            status = gpg.encrypt_file(f,recipients=[recipient],output=file_name + ".gpg")
            print("ok: ", status.ok)
            return file_name + ".gpg"


def upload(file_path, claim_id):
    print("Uploading to lbry.io")
    #curl -d'{"method": "publish", "params": {"name": "a-new-stream", "bid": "0.1", "file_path": ' + file_path + ', "validate_file": false, "optimize_file": false, "tags": [], "languages": [], "locations": [], "channel_id": [], "preview": false, "blocking": false}}' url
    payload = {
        'method': 'publish',
        'params': [{ 'name': '267e5a93-478c-4c57-85b8-a1ebae8956d7', 'bid': '0.1', 'file_path': file_path, 'validate_file': 'false', 'optimize_file': 'false', 'tags': [], 'languages': [], 'locations': [], 'channel_id': ['cd31c8bb7a07e19b380d401a6792c12935c79692'], 'preview': 'false', 'blocking': 'false' }],
        'jsonrpc': '2.0',
        'id': 0
    }

    response = requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": "a-new-stream", "bid": "1.0", "file_path": "bb.png", "validate_file": "false", "optimize_file": "false", "tags": [], "languages": [], "locations": [], "channel_account_id": [], "funding_account_ids": [], "preview": "false", "blocking": "false"}}).json()
    #response = requests.post(url, json=payload).json()
    print(response)


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
#file_path = createPost("test title", "test body")
#upload("267e5a93-478c-4c57-85b8-a1ebae8956d7.json.gpg.md", "FAFF0BB27DD32B8EBA2E41F60A808AD53C602BF1")
upload("/home/lucascullen/GitHub/BitcoinBrisbane/lbry.book.py/267e5a93-478c-4c57-85b8-a1ebae8956d7.txt", "cd31c8bb7a07e19b380d401a6792c12935c79692")
#listFriends()