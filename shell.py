import os

shell = "no"


with open(".username", 'a+') as f:
    f.seek(0)
    if not len(f.read()) == 0:
        f.seek(0)
        validateUser = input(("Are you \"" + f.read() + "\" ? [Y/n] "))
        if validateUser == "Y".casefold:
            print("good")
        elif validateUser == "n".casefold():
            f.truncate(0)
            f.write(input("Please insert your username: "))
    else:
        f.write(input("Please insert your username: "))
    f.seek(0)
    username = f.read()
shell = "yes"

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


def getWoof():
    print("bork bork")

funcs = {
    'cls': clearConsole,
    'edit username': confUsername,
    'getwoof': getWoof
}


while shell == "yes":

    x = input ("():")
    if x == 'exit':
        break
    elif x in funcs:
        funcs.get(str(x))()
        #funcs[x]()

    try:
        y = eval(x)
        if y: print(y)
    except:
        try:
            exec(x)
        except Exception as e:
            print("error:", e)

   
#elif x == 'clear':
#    clear = clearConsole()