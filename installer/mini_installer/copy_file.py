import os
import sys
import re
import shutil


def createFolder(directory):
    directory = re.sub('[!@#${}]', '', directory)
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def copyAll(src, dst, symlinks=False, ignore=None):
    src = re.sub('[!@#${}]', '', src)
    dst = re.sub('[!@#${}]', '', dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

