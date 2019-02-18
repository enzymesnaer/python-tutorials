
from tkinter import messagebox as msg
def generateSignupPanel():
    import tkinter as tk
    signupPanel = tk.Tk() # will generate a panel [main code below this]
    signupPanel.title("Signup Screen")
    signupPanel.geometry("500x500")
    username_label = tk.Label(signupPanel, text="Username : -", padx=20, pady=20)
    username_label.config(font=("Courier", 20))
    username_label.grid(row=1, column=1)
    username_entry = tk.Entry(signupPanel)
    username_entry.grid(row=1, column=2)
    password_label = tk.Label(signupPanel, text="Password : -", padx=20, pady=20)
    password_label.config(font=("Courier", 20))
    password_label.grid(row=2, column=1)
    password_entry = tk.Entry(signupPanel, show="*")
    password_entry.grid(row=2, column=2)
    def checkSignup():
        username = username_entry.get()
        password = password_entry.get()
        if(username=="admin" and password=="12345"):
            msg.showinfo("success",f"welcome {username}")
        else:
            msg.showerror("failure","wrong credential !")
    submit_Button = tk.Button(signupPanel,text="submit", command=checkSignup)
    submit_Button.grid(row=3,column=2,padx=40,pady=40)
    signupPanel.mainloop() # will keep the window open [main code above this]
if __name__=='__main__':
    generateSignupPanel()


# pip install pyinstaller --> for windows<br>
# apt-get install python-stdeb --> for debian
