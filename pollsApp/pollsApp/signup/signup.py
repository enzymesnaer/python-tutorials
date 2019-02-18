import random as r
from files import files_operation as ops
def generateUserName():
	try:
		username = ""
		txt="abcdefghijklmnopqerstuvwxyz!@#$%^&*"
		for i in range(6):
			username += r.choice(txt)
	except BaseException as e:
		print(e)
	else:
		return username


def generateSignUpPanel():
	try:
		name=input("Enter Name")
		username=generateUserName()
		password=input("Enter password")
		conf_password=input("Enter Confirm password")
		if(password!=conf_password):
			raise BaseException("password and conf_password cannot match")
	except BaseException as e:
		print(e)
		generateSignUpPanel()
	else:
		return username,name,password
		

def saveUserCredential(username,name,password):
    try:
        file = ops.generateFiles("files/signup.json","r")
        content = ops.readFromFiles(file)
       
    except BaseException as e:
        print(e)
        file =ops.generateFiles("files/signup.json","w+")
        info={"name":name,"username":username,"password":password}
        data =[]
        data.append(info)
        ops.writeOnFiles(file,str(data))
    else:
        data=eval(content)
        filter_data=list(filter(lambda x:(x.get("password")==password) and x.get("name")==name,data))
        if(len(filter_data)>0):
            print("already exist")
        else:
            file =ops.generateFiles("files/signup.json","w")
            info={"name":name,"username":username,"password":password}
    		#data =[]
            data.append(info)
            ops.writeOnFiles(file,str(data))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        