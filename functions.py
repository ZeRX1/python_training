import os, json, time

def readFiles(patha):
    res = []

    # Iterate directory
    currentpath = os.listdir(patha)
    
    for path in currentpath:
        # check if current path is a file
        if os.path.isfile(os.path.join(patha, path)):
            res.append(path)
        else:
            pathf = patha + path + '/'
            res.append(readFiles(pathf))
    return res

def saveJson(array, name):
    with open(f'{name}.json', 'w') as outfile:
        outfile.write(json.dumps(tuple(array),indent=4))
    return "Data saved"

def createConfig():
    print("Welcome to config creator!")
    folders_amount = int(input("How many folders would you like to account in backup: \n"))
    folders = dict()
    while folders_amount > 0:
        print(str(folders_amount) + " left to assign")
        folders.append(({
        'path': input("What's the name of the path? \n")
        }))
        os.system('cls')
        folders_amount -= 1
    with open('config.json', 'w') as outfile:
        outfile.write(json.dumps(tuple(folders),indent=4))
    print("Config succesfully created!")
    print("Restart the script with no arguments to use config as data used!")
    time.sleep(2)
    return


def backupFiles():
    print('asdf')
    return