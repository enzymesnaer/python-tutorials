from signup import signup
from login import login
def playground():
	#username,name,password=signup.generateSignUpPanel()
	#signup.saveUserCredential(username,name,password)
    print("welcome to polls app".center(40,"*"))
    while(True):
        try:
            choice = int(input("1.login 2.signup 3.pollsresult 4.exit"))
            if(choice==1):
                name,password=login.generateLoginPanel()
                status = login.checkUserCredential(name,password)
                if(status==True):
                    print("login Successful")
                else:
                    print("wrong credentials")
            elif(choice==2):
                username,name,password=signup.generateSignUpPanel()
                signup.saveUserCredential(username,name,password)
            elif(choice==3):
                pass
            elif(choice==4):
                print("Thanks for using our system")
                break
            else:
                print("invalid choice")
        except BaseException as e:
            print(e)
            print("try again!")
            
if __name__ == "__main__":
    playground()
    
    