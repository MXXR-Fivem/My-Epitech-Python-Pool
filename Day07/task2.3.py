import os

def listFiles(dirPath: str=None, space: int=0):
    currentFilePath = os.path.abspath(__file__)
    currentDirPath = dirPath is None and os.path.dirname(currentFilePath) or dirPath
    current_dir_name = os.path.basename(currentDirPath)
    i = 0
    for path, dirnames, filenames in os.walk(currentDirPath):
        if i == 0 and (filenames != [] or dirnames != []):
            print(space*"  " + "|_  " + current_dir_name + " content :")
            for fileName in filenames:
                print(space*"  " + "  📄 " + fileName)
            for dirName in dirnames:
                print(space*"  " + "  ​🗂️  " + dirName + "/")
            print()
            for path in dirnames:
                listFiles(currentDirPath + "/ "[:-1] + path, space+1)
            i += 1

listFiles()