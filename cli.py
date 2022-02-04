import requests
import json
from getpass import getpass

#enter credentials
username = input("Username: ")
password = getpass()
artifactory = "https://tgz.jfrog.io/artifactory/" #artifactory URL
api = "api/security/users" #you can change this API URL to any API method you'd like to use

url = artifactory + api
r = requests.get(url, auth = (username, password)) #this script is only for API methods that use GET
print(username,password)
print(r.status_code)
if r.status_code == 200:
    print(r.text)