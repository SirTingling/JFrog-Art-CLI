import requests
import json
from getpass import getpass
import os

#enter credentials
username = input("Username: ")
password = getpass()

# url to jfrog instance
instance = "https://tgz.jfrog.io/"
# api url
api = "artifactory/api/security/users" 
url = instance + api
r = requests.get(url, auth = (username, password))

if r.status_code == 200:
    # Check for cached token. Create one if doesn't exist.
    print('Enter the path to the directory in which your .token_<username> file is saved.\n\
        If you don\'t have such file, it will be created at the specified path.\
        Please make sure the path is secure and known only to you.')
    tokenPath = input('path: ')
    if not os.path.exists(tokenPath):
        os.makedirs(tokenPath)
    with open((tokenPath+"/.token_"+username),"a+") as f:
        f.seek(0)
        if len(f.read()) == 0:
            f.write(input('insert token: '))
        f.seek(0)
        token = f.read()
    # 
    bearer ='Bearer ' + token
    header = {
    'Authorization': bearer
    }

    woof = requests.get('https://tgz.jfrog.io/access/api/v1/tokens', headers = header)
    print(woof.status_code,"\n",woof.text)
else:
   print('***\n',r.status_code)
