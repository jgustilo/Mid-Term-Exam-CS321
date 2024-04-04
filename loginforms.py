from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from os import path
import re

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#1 ACCOUNT AVAILABLE FOR NOW(ADMIN)
def validate_password(password):
    """Checks if the password meets the security requirements."""
    conditions = [
        re.search(r"[A-Z]", password),  # At least one uppercase
        re.search(r"[a-z]", password),  # At least one lowercase
        re.search(r"[0-9]", password),  # At least one number
        re.search(r"[!@#$%^&*()\-+=]", password),  # At least one special character
        len(password) >= 6   
    ]
    return all(conditions)

def signin():
    username=user.get()
    password=code.get()

    password = code.get()
    if not validate_password(password):
        messagebox.showerror("Invalid Password", "Password does not meet requirements.")
        return  # Stop login attempt
    
#IF ELIF STATEMENT FOR USER LOGIN
    if username=='admin1' and password=='s@mplE123':
        screen=Toplevel(root)
        screen.title("Hybrid Neural Network")
        screen.geometry('900x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Hello, Welcome!\n CNLTK webpage is under construction^_^', bg='#fff', font=('Times New Roman', 25, 'bold')).pack(expand=True)

        screen.mainloop()

#ERROR MESSAGE FOR INCORRECT CREDENTIALS
    elif username!='admin1' or password != 's@mplE123':
        messagebox.showerror("Invalid","Invalid Username or Password")

#PHOTO CALL PATH FOR LOG IN IMAGE(DRAFT IMG ONLY)
photo = ImageTk.PhotoImage(Image.open(path.join(path.dirname(__file__), 'login.png')))
label = Label(root, image=photo, bg='white').place(x=50, y=50)

frame =Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

#SIGN IN BUTTON
heading = Label(frame,text='Sign in' , fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

#DELETES USERNAME TEXT WHEN CLICKED
def on_enter(e):
    user.delete(0, 'end')
    
#USER USERNAME INPUT
def on_leave(e):
    name= user.get()
    if name=='':
        user.inster(0, 'Username')
        
#FOR USERNAME PLACEHOLDER/INPUT BOX
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#DELETES PASSWORD TEXT WHEN CLICKED
def on_enter(e):
    code.delete(0, 'end')
    
#USER PASSWORD INPUT
def on_leave(e):
    name= code.get()
    if name=='':
        code.insert(0, 'Password')
        
        
#FOR PASSWORD PLACEHOLDER/INPUT BOX        
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
code.place(x=30, y=150)
code.insert(0,'Password')
def on_enter(e):
    if code.get() == 'Password': #This line checks if it's the placeholder
        code.delete(0, 'end')
        code.configure(show="*") #This line hides inpud on focus

def on_leave(e):
    if not code.get(): #This checks if the field is empty
        code.insert(0, 'Password')
        code.configure(show=" ") #This shows the password on blur
        
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


#FOR SIGN UP PART

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35,y=204)
label= Label(frame, text="Don't have an account?" , fg='black', bg='white' ,font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

#SIGN UP BUTTON
sign_up= Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215,y=270)

root.mainloop()
