import os
from functions import *


if __name__ == "__main__":
    path = os.getenv('path')
    print(readFiles(path))
    