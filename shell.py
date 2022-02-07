import os
import requests
from getpass import getpass

shell = "no"

#jfrog instance
with open("cache/.instance", "a+") as f:
    f.seek(0)
    if not len(f.read()) == 0:
        f.seek(0)
        validateInstance = input(("Is your JFrog instance \"" + f.read() + "\" ? [Y/n]: "))
        if validateInstance == "Y".casefold:
            print("good")
        elif validateInstance == "n".casefold():
            f.truncate(0)
            f.write(input("Please insert your instance: "))
    else:
        f.write(input("Please insert your instance: "))
    f.seek(0)
    instance = f.read()

# CLI Username
with open("cache/.username", 'a+') as f:
    f.seek(0)
    if not len(f.read()) == 0:
        f.seek(0)
        validateUser = input(("Are you \"" + f.read() + "\" ? [Y/n]: "))
        if validateUser == "Y".casefold:
            print("good")
        elif validateUser == "n".casefold():
            f.truncate(0)
            f.write(input("Please insert your username: "))
    else:
        f.write(input("Please insert your username: "))
    f.seek(0)
    username = f.read()

#CLI Password
password = getpass()
# Validate login
r = requests.head (instance+"artifactory/api/security/users/"+username, auth=(username, password))
if r.status_code == 401:
    print("Authentication denied [401].\nYour username or password might be incorrect.")
    exit(1)
# CLI Token
print('''
Enter the path to the directory in which your .token_<username> file is saved.
If you don\'t have such file, it will be created at the specified path.
Please make sure the path is secure and known only to you.
''')
tokenPath = input('path: ')
if not os.path.exists(tokenPath):
    os.makedirs(tokenPath)
with open((tokenPath+"/.token_"+username),"a+") as f:
    f.seek(0)
    if len(f.read()) == 0:
        f.write(input('insert token: '))
    f.seek(0)
    token = f.read()
headers = {
    'Authorization': 'Bearer ' + token
    }


shell = "yes"


# Shell fucntions:

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def confInstance():
    instance = open("cache/.instance", 'r').read()
    validateConfInstance = input("Current instance is \""+instance+"\", would you like to overwrite it? [y/N]: ")
    if validateConfInstance in ('','n'.casefold()) :
        print("Username unchanged")
    elif validateConfInstance == 'y'.casefold():
        with open("cache/.instance", "a+") as f:
            f.truncate(0)
            f.write(input("Please insert your instance: "))
            f.seek(0)
            instance = f.read()
        print("Instance successfully changed to \""+instance+"\"")


def printUsername():
    print(username)

def printInstance():
    print(instance)

def postCreateUser():
    r

def headSystemPing():
    r = requests.head(instance+"access/api/v1/system/ping", headers=headers)
    print(r)
    if r.status_code == 200:
        print("Ping Successfull")

def getStorageInfo():
    failcount = 0
    passwordAuth = getpass()
    while not passwordAuth == password:
        print("Wrong password, try again")
        passwordAuth = getpass()
        failcount = failcount + 1
        if failcount == 2:
            failcount = 0
            break
    if passwordAuth == password:
        r = requests.get(instance+"artifactory/api/storageinfo", headers=headers)
        print(r,'\n',r.json())

def getSystemVersion():
    r = requests.get(instance+"artifactory/api/system/version", headers=headers)
    print(r,'\n',r.text)


def putCreateRepository(): ### Can't test this one
    failcount = 0
    passwordAuth = getpass()
    while not passwordAuth == password:
        print("Wrong password, try again")
        passwordAuth = getpass()
        failcount = failcount + 1
        if failcount == 2:
            failcount = 0
            break
    if passwordAuth == password:
        repoKey = input('enter repository key: ')
        jsonRepoConfPath = 'enter path to your repository-config.json file: '
        jsonRepoConf = open(jsonRepoConfPath, 'r').read
        data = "{"+jsonRepoConf+"}"
        r = requests.put(instance+"artifactory/api/repositories/"+repoKey, headers = headers, data = data)
        print(r,'\n',r.json())

def deleteUser():
    failcount = 0
    passwordAuth = getpass()
    while not passwordAuth == password:
        print("Wrong password, try again")
        passwordAuth = getpass()
        failcount = failcount + 1
        if failcount == 2:
            failcount = 0
            break
    if passwordAuth == password:
        userToDelete = input("!!! enter the user you want to DELETE: ")
        r = requests.delete(instance+"artifactory/api/security/users/"+userToDelete, headers = headers)
        print(r)


def postCreateUser(): ### Couldn't get it to work, kept getting response 415
    failcount = 0
    passwordAuth = getpass()
    while not passwordAuth == password:
        print("Wrong password, try again")
        passwordAuth = getpass()
        failcount = failcount + 1
        if failcount == 2:
            failcount = 0
            break
    if passwordAuth == password:
        print('insert new user details:')
        createUserUsername = input('username: ')
        createUserEmail = input('email: ')
        createUserData = {
        "schemas": [
            "urn:ietf:params:scim:schemas:core:2.0:User"
        ],
        "userName": createUserUsername,
        "active": True,
        "emails": [
            {
            "value": createUserEmail,
            "primary": True
            }
        ]
        }
        r = requests.post(instance+"access/api/v1/scim/v2/Users", headers = headers, data = createUserData)
        print(r,'\n',r.json())

def postExpirePassword():
    failcount = 0
    passwordAuth = getpass()
    while not passwordAuth == password:
        print("Wrong password, try again")
        passwordAuth = getpass()
        failcount = failcount + 1
        if failcount == 2:
            failcount = 0
            break
    if passwordAuth == password:
        userToExpire = input('Enter a username to expire it\'s password: ')
        r = requests.post(instance+'/api/security/users/authorization/expirePassword/'+userToExpire, headers = headers)
        print(r,'\n',r.content)

def miscHelp():
    print('Console Usage:\n'+('∙'*14))
    
    for a in functionsHelp:
        print(a,':')
        for b in functionsHelp[a]:
            # if type(b) == dict:
            print("\t",b,":",functionsHelp[a][b])
    
    print('*Note that all misc commands are unprefixed.')

functionsHelp = {
    'DELETE': {
        'user': 'Removes an Artifactory user.\n\t\t\tDANGEROUS.'
    },
    'edit': {
        'instance': 'Change the instance this CLI runs requests against\n'
    },
    'get': {
        'storage info': 'Returns storage summary information regarding binaries, file store and repositories\n',
        'system version': 'Retrieve information about the current Artifactory version, revision, and currently installed Add-ons\n'
    },
    'head': {
        'system ping': 'Sends a ping request to instance\n'
    },
    'misc': {
        "clear": '''Clears console.
            \t Alternative commands : cls
            ''',
        "exit": '''Exits console.
            \tAlternative commands: quit, ex
        ''',
        "help": '''Show this help message.
            \tAlternative commands: h, info, inf
            '''
    },
    'print': {
        'instance': 'Prints the isntance this CLI runs requests against\n',
        'username': 'Prints the username this CLI uses\n'
    },
    'post': {
        'create user': '''This API will create a single user
            \t\tTHIS OPTION IS NOT WORKING
        ''',
        'expire password': 'Expires a user\'s password\n\t\t\tThis option could not be tested because i have no PRO access, but i believe it should work if i were to have access'
    },
    'put': {
        'create repository': '''Creates a new repository in Artifactory with the provided configuration. Supported by local, remote, virtual and federated repositories
            \t\t\tThis option could not be tested
            '''
    }
}

shellFunctions = {
    'DELETE user': deleteUser,
    'clear': clearConsole,
    'cls': clearConsole,
    'edit instance': confInstance,
    'get storage info': getStorageInfo,
    'get system version': getSystemVersion,
    'head system ping': headSystemPing,
    'help': miscHelp,
    'print instance': printInstance,
    'print username': printUsername,
    'post create user': postCreateUser,
    'post expire password': postExpirePassword,
    'put create repository': putCreateRepository
}


while shell == "yes":

    x = input ("():")
    if x in ('exit','exi','ex','quit'):
        break

    elif x in ('h','info','inf'):
        x = 'help'
        if x in shellFunctions:
            shellFunctions.get(x)()

    elif x in shellFunctions:
        shellFunctions.get(x)()

    elif x == '':
        continue
    else:
        print('use \'help\' to get help')
