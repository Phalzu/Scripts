#!/usr/bin/python3
import subprocess
import sys
import os
import hashlib

# Returns a list containing the names of the files and directories
listDir = os.listdir(sys.argv[1])

# Gets a md5-hash value for a file
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Renames all files after her md5 hash
for f in listDir:
    filePath = (sys.argv[1] + "/" + f)
    if os.path.isfile(filePath):
        end = filePath.split('.', 1)[1]
        newName = sys.argv[1] + "/" + md5(filePath) + "." + end
        process = subprocess.Popen(["mv", filePath, newName], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
