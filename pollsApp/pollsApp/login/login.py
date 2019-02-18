from files import files_operation as ops
def generateLoginPanel():
    try:
        name=input("Enter Name: ")
        password=input("Enter Password: ")
    except BaseException as e:
        print(e)
    else:
        return name, password
    
def checkUserCredential(name,password):
    try:
        file = ops.generateFiles("files/signup.json","r")
        content = ops.readFromFiles(file)
        if(content==None or len(content)<1 or content==""):
            raise BaseException("file content is not present")
    except BaseException as e:
        print(e)
        print("No user present Signup First")
    else:
        data=eval(content)
        check_logic= lambda x:x.get("name")==name and x.get("password")==password
        filter_data=list(filter(check_logic,data))
        if(len(filter_data)>0):
            return True
        else:
            return False