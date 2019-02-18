
def generateFiles(filePath,mode):
    try:
        file = open(filePath, mode)
    except BaseException as e:
        print(e)
    else:
        return file

def writeOnFiles(file,content):
    try:
        file.write(content)
    except BaseException as e:
        print(e)
    else:
        print("file write success")
        file.close()


def readFromFiles(file):
    try:
        content = file.read()
    except BaseException as e:
        print(e)
    else:
        return content