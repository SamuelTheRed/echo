import datetime
import os

# users.txt is created, creates user with admin priveledges, and add user to users.txt
def fillUsers():
    print("First Time Logging In?\nWe'll start you off as admin\n\nusername: admin\npassword: 1234")
    ofile = open("users.txt", "w")
    ofile.write("Users\n")
    # Creates associative array of user using key-value pair
    user = {
        "username" : "admin",
        "password" : "1234"
    }
    # Places user into txt in organized way
    for key in user:
        ofile.write(key)
        ofile.write(" ")
        ofile.write(user[key])
        ofile.write("\n")
    ofile.close()

# Attempts to retrieve username from user
def getUser():
    ifile = open("users.txt", "r")
    # Initializes a user object using associative array and a users list
    user = {
        "username" : "",
        "password" : ""
    }
    users = []
    # For now, txt files have headers, this removes the header
    # TODO Transfer data storage to a database to ensure security
    title = ifile.readline()
    # Reads users.txt file and creates list of all present users
    for line in ifile:
        # Strips and splits each line into variable split then assignes key and value to each value
        line = line.strip()
        split = line.split(" ")
        key = split[0]
        try:
            value = split[1]
        except:
            value = key
        user[key] = value
        # Every other value is a password, this catches that and adds the stored value of user into the list of users then nulls the user
        if key == "password":
            users.append(user)
            user = {
                "username" : "",
                "password" : ""
            }

    ifile.close()

    # Gets input from user for username
    userIn = input("\n-----Login-----\n\nusername: ")

    # Searches stored information if username is present
    for user in users:
        if userIn == user['username']:
            # TODO Since this is the first return of password data, there should be security for passwords. Possibly store as hashed value. If DB is clean then no worries.
            return user
    
    return "notFound"

# Compares user entered text to stored password for user entered username
def getPass(username):
    if username == "notFound":
        return False
    
    userIn = input("password: ")

    # This is simply comparing strings
    # TODO Update password storing practices, this should change
    if userIn != username['password']:
        return False
    else:
        return username

# Attempts to login user using username and password
def login():
    # Allows 5 attempts
    for i in range(5):
        user = getUser()
        # After user is found, the associative array including username and password is sent to the getPass function
        # TODO ensure password storage and transportation is updated
        name = getPass(user)
        if name:
            return name['username']
    
    return False


def initializeStats(filename):
    ofile = open(filename, "w")

    ofile.write("0\n")
    ofile.write(f"{datetime.datetime.today()}\n")

    ofile.close()


def getStats(filename):
    ifile = open(filename, "r")
    stats = []

    for line in ifile:
        line = str(line)
        stats.append(line.strip())

    ifile.close()

    stats[0] = int(stats[0])

    return stats


def updateStats(filename, stats):
    ofile = open(filename, "w")
    
    ofile.write(f"{int(stats[0]) + 1}\n")
    ofile.write(f"{datetime.datetime.today()}\n")

    ofile.close()


def fillStats(name):
    filename = name + ".txt"
    try:
        ifile = open(filename, "r")
        ifile.close()
    except:
        initializeStats(filename)
    
    stats = getStats(filename)

    ofile = open("userStats.txt", "w")
    for stat in stats:
        ofile.write(f"{stat}\n")
    ofile.close()

    updateStats(filename, stats)


def changePass(name):
    ifile = open("users.txt", "r")
    user = {
        "username" : "",
        "password" : ""
    }
    users = []
    title = ifile.readline()
    for line in ifile:
        line = line.strip()
        split = line.split(" ")
        key = split[0]
        value = split[1]
        user[key] = value
        if key == "password":
            users.append(user)
            user = {
                "username" : "",
                "password" : ""
            }

    ifile.close()

    done = False

    while not done:
        new_one = input("Enter New Password: ")
        new_two = input("Re-enter New Password: ")
        if new_one == new_two:
            done == True
            break
        else:
            print("Passwords did not match")

    ofile = open("users.txt", "w")
    ofile.write("Users\n")
    for user in users:
        if user['username'] == name:
            user['password'] = new_one
        for key in user:
            ofile.write(key)
            ofile.write(" ")
            ofile.write(user[key])
            ofile.write("\n")
    ofile.close()


def addUser():
    ifile = open("users.txt", "r")
    user = {
        "username" : "",
        "password" : ""
    }
    users = []
    title = ifile.readline()
    for line in ifile:
        line = line.strip()
        split = line.split(" ")
        key = split[0]
        value = split[1]
        user[key] = value
        if key == "password":
            users.append(user)
            user = {
                "username" : "",
                "password" : ""
            }

    ifile.close()

    new_user = input("Enter New User's Username: ")
    new_pass = input("Enter New User's Password: ")
    new_user = {
        "username" : new_user,
        "password" : new_pass
    }
    flag = False

    for user in users:
        if user['username'] == new_user["username"]:
            flag = True

    if not flag:
        users.append(new_user)
    else:
        print("User already exists")

    ofile = open("users.txt", "w")
    ofile.write("Users\n")
    for user in users:
        for key in user:
            ofile.write(key)
            ofile.write(" ")
            ofile.write(user[key])
            ofile.write("\n")
    ofile.close()


def deleteUser():
    inuser = input("What user do you want to delete? (cancel = x): ")
    if inuser == "x":
        return False
    elif inuser == "admin":
        final = input("Deleting admin is not advised, are you sure you want to proceed? (y/x): ")
        if final == "x":
            return False
    
    filename = inuser + ".txt"
        
    try:
        os.remove(filename)
    except:
        print("User had no stats")

    ifile = open("users.txt", "r")
    user = {
        "username" : "",
        "password" : ""
    }
    users = []
    title = ifile.readline()
    for line in ifile:
        line = line.strip()
        split = line.split(" ")
        key = split[0]
        value = split[1]
        user[key] = value
        if key == "password":
            users.append(user)
            user = {
                "username" : "",
                "password" : ""
            }

    ifile.close()
    inuser_dict = {}

    for user in users:
        if inuser == user['username']:
            inuser_dict = user
            
    if len(inuser_dict) > 0:
        users.remove(inuser_dict)
    else:
        print("User not found")

    ofile = open("users.txt", "w")
    ofile.write("Users\n")
    for user in users:
        for key in user:
            ofile.write(key)
            ofile.write(" ")
            ofile.write(user[key])
            ofile.write("\n")
    ofile.close()

    if inuser == "admin":
        os.remove("users.txt")
        return False
    return True


def seeStats():
    stats = getStats("userStats.txt")
    print(f"\nNumber of times logged in: {stats[0]}")
    print(f"Last logged in: {stats[1]}")


def switchAdmin(name):
    done = False

    while not done:
        print("\n--------------------------------")
        print("What would you like to do today?")
        print("p -- Change Password")
        print("a -- Add User")
        print("d -- Delete User")
        print("s -- See Stats")
        print("r -- Run Echo Terminal (IO)")
        print("x -- Exit")
        c = input(": ")
        
        match c:
            case 'p':
                changePass(name)
            case 'a':
                addUser()
            case 'd':
                admin = deleteUser()
                if not admin:
                    return False
            case 's':
                seeStats()
            case 'r':
                runIO()
            case 'x':
                done = True
    return True


def switch(name):
    done = False

    while not done:
        print("\n--------------------------------")
        print("What would you like to do today?")
        print("p -- Change Password")
        print("s -- See Stats")
        print("x -- Exit")
        c = input(": ")
        
        match c:
            case 'p':
                changePass(name)
            case 's':
                seeStats(name)
            case 'x':
                done = True
    return True


def run():
    try:
        ifile = open("users.txt", "r")
        ifile.close()
    except:
        fillUsers()

    name = login()

    if not name:
        print("Try Again Later")
        return False
    
    print(f"\nWelcome {name}!")

    fillStats(name)

    if name == "admin":
        admin = switchAdmin(name)
        if not admin:
            return False
    else:
        switch(name)


def clear():
    os.remove("userStats.txt")

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


variables = {}
arrays = {}
commands = ["end", "start", "newfile", "writeto", "echo", "newvar", "newarr", "kill", "help"]

def runIO(inpu="", file=False):
    global variables
    global arrays

    while True:
        if not file:
            inpu = input("echo ~: ")
        inpus = ["None"]

        if len(inpu) > 0:
            inpus = inpu.split(" ")

        if inpu == "end":
            break
        elif inpus[0] == "start" and len(inpus) == 2:
            if inpus[1][-3:] == "txt":
                try:
                    ifile = open(inpus[1], "r")
                    print(ifile.read())
                    ifile.close()
                except:
                    print("\t\tUnknown filename")
            # 
            # 
            # 
            # Needs a lot more info
            elif inpus[1][-4:] == "echo":
                try:
                    ifile = open(inpus[1], "r")
                    line = "line 1"
                    try:
                        for line in ifile:
                            line = line.strip()
                            runIO(line, True)
                    except:
                        print(f"{line}\n\t\tin {inpus[1]} has an error")
                    ifile.close()
                except:
                    print("\t\tUnknown filename")
            else:
                print("\t\tUnknown filename")
        elif inpus[0] == "newfile" and len(inpus) == 2:
            ofile = open(inpus[1], "w")
            ofile.write("\n")
            ofile.close()
        elif inpus[0] == "writeto" and len(inpus) == 2:
            ofile = open(inpus[1], "w")
            writin = input(f"{inpus[1]} ~: ")
            ofile.write(writin)
            ofile.close()
        elif inpus[0][0].isnumeric() and len(inpus) == 3:
            if inpus[1] == "+":
                print(float(inpus[0]) + float(inpus[2]))
            elif inpus[1] == "-":
                print(float(inpus[0]) - float(inpus[2]))
            elif inpus[1] == "/":
                print(float(inpus[0]) / float(inpus[2]))
            elif inpus[1] == "*":
                print(float(inpus[0]) * float(inpus[2]))
            else:
                print("\t\tUnknown operator")
        elif inpus[0] == "echo":
            for i in range(len(inpus) - 1):
                j = i + 1
                if inpus[j] in variables.keys():
                    print(variables[inpus[j]], end=" ")
                elif inpus[j] in arrays.keys():
                    for k in range(len(arrays[inpus[j]])):
                        print(arrays[inpus[j]][str(k)], end=" ")
                else:
                    print(inpus[j], end=" ")
            print()
        elif inpus[0] == "newvar" and len(inpus) > 3:
            varname = inpus[1]
            if not varname.isnumeric() and not varname in commands and not varname in arrays.keys():
                variables[inpus[1]] = inpus[3]
            else:
                print("\t\tInvalid varname")
        elif inpus[0] == "newarr" and len(inpus) > 4:
            varname = inpus[1]
            if not varname.isnumeric() and not varname in commands and not varname in variables.keys():
                arr = {}
                liss = inpus[3:]
                if liss[0] == "{" and liss[-1] == "}":
                    liss = liss[1:-1]
                    for i in range(len(liss)):
                        if liss[i] in variables.keys():
                            arr[str(i)] = variables[liss[i]]
                        else:
                            arr[str(i)] = liss[i]
                    arrays[inpus[1]] = arr
                else:
                    print("\t\tInvalid array")
            else:
                print("\t\tInvalid varname")
        elif inpus[0] in variables.keys():
            if inpus[1] == "=":
                if inpus[2] in variables.keys():
                    variables[inpus[0]] = variables[inpus[2]]
                else:
                    variables[inpus[0]] = inpus[2]
        elif inpus[0] in arrays.keys() and len(inpus) > 2:
            if inpus[1] == "=":
                if inpus[2] in arrays.keys():
                    arrays[inpus[0]] = arrays[inpus[2]]
                else:
                    arr = {}
                    liss = inpus[2:]
                    if liss[0] == "{" and liss[-1] == "}":
                        liss = liss[1:-1]
                        for i in range(len(liss)):
                            if liss[i] in variables.keys():
                                arr[str(i)] = variables[liss[i]]
                            elif liss[i] in arrays.keys():
                                arr[str(i)] = arrays[liss[i]]
                            else:
                                arr[str(i)] = liss[i]
                        arrays[inpus[1]] = arr
                    else:
                        print("\t\tInvalid array")
            else:
                print("\t\tUnknown command")
        elif inpus[0] == "kill":
            if inpus[1] in variables.keys():
                variables.pop(inpus[1])
            elif inpus[1] in arrays.keys():
                arrays.pop(inpus[1])
            elif inpus[1] == "all":
                variables = {}
                arrays = {}
        elif inpus[0] == "help":
            if len(inpus) > 1 and inpus[1] == "allcmds":
                for cmd in commands:
                    print(cmd, end=", ")
                print("")
            else:
                print("Try:\n\t- start @rg'filename'")
                print("\t- newfile @rg'filename'")
                print("\t- writeto @rg'filename'")
                print("\t- newvar @rg'varname' = @rg'varvalue'")
                print("\t- help allcmds")
                print("\t- end")
        else:
            print("\t\tUnknown command")
    
        if file == True:
            return True


if __name__ == "__main__":
    run()
    clear()