import os, time, sys, getopt
from functions import *
from os.path import exists


def main(d):

    if not d:
        if exists("config.json"):
            with open("config.json") as input:
                if not input:
                    print("The config file is empty. Use -c to create one!")
                    return
                configjson = json.load(input)
        else:
            print("The config file doesn't exist. Use -c to create one!")
            return
        #here with config usage
        
    #here with arguments
    if d.get("config") == True:
        createConfig()
        print('run the script again to use parameters from config')
        return
    elif d.get("backup") == True:
        backupFiles()
        print("backup ended successfully")
        return

    path = d['directory']
    print(saveJson(readFiles(path), "previous_files"))
        
    return

def readArgs(argv):
    try:
        opts, args = getopt.getopt(argv, "d:cb")
    except getopt.GetoptError as err:
        help_command()
        print(err) 
        sys.exit(2)

    #add this to an array/dictionary and send further
    d = dict()
    for opt, arg in opts:
        print(opt, arg)
        if opt in ('-d'):
            d['directory'] = arg
        elif opt in ('-b'):
            d['backup'] = True
        elif opt in ('-c'):
            d['config'] = True
        print(d)
    
    main(d)
    return

def help_command():
    print("Help")

    return    

if __name__ == "__main__":
    try:
        # read arguments
        readArgs(sys.argv[1:])
        time.sleep(2)
    except (ValueError, KeyError, AttributeError, IndexError) as err:
        print(err)
    except TimeoutError as err:
        print("Is the IP correct? (.env)" + err)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise