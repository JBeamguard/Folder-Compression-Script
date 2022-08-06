#!/usr/bin/env python3

import os
import subprocess
import shutil

# return an array of the directories inside of the given path
def getFolders(compDir):
    # get complete list of compressDir contents
    subElements = os.scandir(compDir)

    # go through list and compile array of directories
    tmpList = []
    for element in subElements:
        if element.is_dir() :
            tmpList.append(element.name)

    return tmpList

# call 7-Zip using passed in target and 
def sevenZip(dirToComp, newZipName):
    # display which folder is being targeted for compression
    print('Now zipping: ', dirToComp, "\n")

    command = [r'C:\Program Files\7-Zip\7z.exe', "a", newZipName, dirToComp]
    subprocess.call(command)

#####################
# main function
#####################
# ingest the necessary script compression and deposition targets
compressDir = input("Directory whose folders you want to compress: ")
targetDir = input("Target directory for the compressed files: ")

# get list of subfolders in the directory to be compressed
dirList = getFolders(compressDir)

# after getting list of subdirectories, compress then remove after compression
for dirToComp in dirList:
    # construct the paths for the compression and deposition targets
    compTgt = compressDir + dirToComp
    cmdZipname = targetDir + dirToComp + ".7z"
    
    # compress dirToComp using 7zip
    sevenZip(compTgt, cmdZipname)

    # remove dirToComp after compression is complete
    print('Finished compressing', dirToComp, 'now remove', dirToComp)
    shutil.rmtree(targetDir + dirToComp)
    
# after finished compressing folder, display message before exit
print('\nCompression finished, press any key to exit...')
input()
