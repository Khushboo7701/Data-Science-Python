with open('factorial.py') as f:
    data = f.read()
    print(data)

fo = open("file1.txt", "w+")
str = "We are learning IO in python.\nPython is a great language.\n"
fo.write(str)
str=fo.read()
print("Read String is: ",str)
str=fo.readline()
print("First line of file: ", str)
str=fo.readline()
print("Second line of file: ", str)
print("Contents of file:")
for line in fo:
    print(line, end='')
    
print ("Name of file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
print ("Current position: ", fo.tell())



fo.close()

import os
with os.scandir('img/') as entries: #with closes the iterator and frees up acquired resources
    for entry in entries:
        print(entry.name)

from pathlib import Path
entries = Path('img/')
for entry in entries.iterdir(): #iterdir() method creates an iterator of all files and folders in the img directory
    print(entry.name)

#List all the files only in the directory img
#using os.listdir()
basepath = 'img/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath,entry)):
        print(entry)

#using os.scandir()
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)

#using pathlib.Path()
from pathlib import Path
basepath = Path('img/')
entries = basepath.iterdir()
for entry in entries:
    if entry.is_file():
        print(entry.name)

#List all the sub directories only in the directory img
#using os.listdir()
basepath = 'img/'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath,entry)):
        print(entry)

#using os.scandir()
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)

#using pathlib.Path()
from pathlib import Path
basepath = Path('img/')
entries = basepath.iterdir()
for entry in entries:
    if entry.is_dir():
        print(entry.name)

#Listing file information like file size, last modified time
#using os.scandir()
basepath = 'img/'
with os.scandir(basepath) as entries:
    for entry in entries:
        info = entry.stat()
        print(info.st_mtime)

#using pathlib.Path()
from pathlib import Path
basepath = Path('img/')
entries = basepath.iterdir()
for entry in entries:
    info = entry.stat()
    print(info.st_mtime)

#Making directory
#using os
os.mkdir('dir1/')
#using pathlib.Path
p = Path('dir2/')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)

# Walking a directory tree and printing the names of the directories and files
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)

# deleting directory:
# 1. os.rmdir()
# 2. pathlib.Path.rmdir()

#Data handling
import pandas as pd

