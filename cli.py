import requests
import os
from getpass import getpass
#import json
import argparse

parser = argparse.ArgumentParser(description='gets api')
parser.add_argument('method', metavar='method', type=str, help='Enter a method.\nfor e.g: users')
args = parser.parse_args()

method = args.method

#enter credentials
username = input("Username: ")
password = getpass()

# url to jfrog instance
instance = "https://tgz.jfrog.io/"
# api url
api = "artifactory/api/security/" + method 
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

    #r2 = requests.get('https://tgz.jfrog.io/access/api/v1/tokens', headers = header)
    #print(r2.status_code,"\n",r2.text)
    print(r.content)
else:
   print('***\n',r.status_code)
