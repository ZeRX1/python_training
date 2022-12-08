import os

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