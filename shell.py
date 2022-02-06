import os
import requests
from getpass import getpass

shell = "no"

# CLI Username
with open(".username", 'a+') as f:
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
r = requests.get("https://tgz.jfrog.io/artifactory/api/security/users/"+username, auth=(username, password))
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
header = {
    'Authorization': 'Bearer' + token
    }


shell = "yes"


# Shell fucntions:

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def confUsername():
    username = open(".username", 'r').read()
    validateConfUser = input("Current username is \""+username+"\", would you like to overwrite it? [y/N]: ")
    if validateConfUser in ('','n'.casefold()) :
        print("Username unchanged")
    elif validateConfUser == 'y'.casefold():
        with open(".username", "a+") as f:
            f.truncate(0)
            f.write(input("Please insert your username: "))
            f.seek(0)
            username = f.read()
        print("Username successfully changed to \""+username+"\"")


def printUsername():
    print(username)

def getHelp():
    print('Console Usage:\n'+('∙'*14))
    
    for a in functionsHelp:
        print(a,':')
        for b in functionsHelp[a]:
            # if type(b) == dict:
            print("\t",b,":",functionsHelp[a][b])
    
    print('*Note that all misc commands are unprefixed.')

functionsHelp = {
    'edit': {
        'username': 'Changes the username this CLI uses',
        'token': 'Changes the access token this CLI uses'
    },
    'print': {
        'username': 'Prints the username this CLI uses'
    },
    'misc': {
        "clear": '''Clears console.
            \t Alternative commands : cls
            ''',
        "exit": '''Exits console.
            \tAlternative commands: quit, ex
        '''
    }
}

shellFunctions = {
    'clear': clearConsole,
    'cls': clearConsole,
    'help': getHelp,
    'edit username': confUsername,
    'print username': printUsername
}


while shell == "yes":

    x = input ("():")
    if x in ('exit','exi','ex','quit'):
        break

    elif x in shellFunctions:
        shellFunctions.get(x)()

    elif x == '':
        continue
    else:
        print('use \'help\' to get help')
