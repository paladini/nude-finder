import os
import sys
from nude import Nude

def main():

    if len(sys.argv) > 1:
        rootdir = sys.argv[1]
    else:
        rootdir = os.getcwd()
        
    print("Searching for nudes recursively inside '{}' folder.".format(os.getcwd()))
    
    # Search for files recursively
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fn = os.path.join(subdir, file)
            try:
                n = Nude(fn)
                n.resize()
                n.parse()
                if (n.result):
                    print(fn)
            except Exception as e:
                sys.stderr.write("Exception: {}".format(e))