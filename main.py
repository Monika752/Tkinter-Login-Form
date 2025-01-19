from tkinter import *
import mysql.connector
from tkinter import messagebox 
conn = mysql.connector.connect(host="localhost", user="root",password="monikasql",database="student")

Window = Tk()
Window.geometry("900x600")
Window.title("Login system")
Window.config(bg="lightgreen")
#Login function
def Login():
    Username = Username_field.get()
    Password = Password_field.get()
    print(Username,Password)
    cur = conn.cursor()
    compare="select * from registered where Name=%s and password=%s"
    param =  (Username,Password)
    cur.execute(compare,param)
    data = cur.fetchall()
    conn.commit()
    #Exception Handling
    try:
        if data[0] != "":
            print("data matched")
            messagebox.showinfo("success","Successfully Logged in")
    except mysql.connector.errors.IntegrityError:
        print("data doesn't match")
        messagebox.showerror("error","Data doesn't match")
    except IndexError:
        print("data doesn't match")
        messagebox.showerror("error","Data doesn't match")
    
#Label for Login Form
L1 = Label(Window, text="Welcome to Student Management System" ,bg="lightgreen", font=("arial",18))
L1.pack(pady=30)
Login_Frame = Frame(Window, height=400, width=400, bg="lightgrey")
Login_Frame.pack(pady=20)

#Register Frame
def Register_Frame():
    def Register():
        RUsername = RUsername_field.get()
        RPassword = RPassword_field.get()
        print(RUsername,RPassword)
        #Exception Handling
        try:
            cur = conn.cursor()
            insertion = "insert into registered(Name,password) values (%s, %s)"
            param = (RUsername,RPassword)
            cur.execute(insertion,param)
            conn.commit()
            print("Registered")
            messagebox.showinfo("success","Successfully Registered")
        
        except mysql.connector.errors.DatabaseError:
            print("Invalid Username and password")
            messagebox.showerror("error","Invalid username and password")

    Register_Frame = Frame(Login_Frame, height=360, width=400, bg="lightgrey")
    Register_Frame.pack(pady=20)

    Register_topic = Label(Register_Frame,text="Register Here", font=('arial',15),padx=40,bg="white")
    Register_topic.place(x=100, y=4)

    RUsername_label = Label(Register_Frame,text="Username :", font=("arial",15), bg="lightgrey")
    RUsername_label.place(x=30,y=60)
    RUsername_field = Entry(Login_Frame, font=("arial",15))
    RUsername_field.place(x=150, y=80)

    RPassword = Label(Register_Frame, text="Password :", font=("arial",15), bg="lightgrey")
    RPassword.place(x=30, y=130)
    RPassword_field = Entry(Register_Frame, font=("arial",15))
    RPassword_field.place(x=150, y=130)

    Reg_Button = Button(Register_Frame, text="Register", bg="blue",font=("arial",13), height=1, width=20, command=Register)
    Reg_Button.place(x=120, y= 220)
    #Back to Login
    Login_Label = Label(Register_Frame, text="If you already have an account", font=("arial",13), bg="lightgrey")
    Login_Label.place(x=15, y=295)
    Log_Button = Button(Register_Frame, text="Login", font=("arial",12),height=1, width=12, bg="orange",command=Register_Frame.destroy)
    Log_Button.place(x=260, y=295)

Login_topic = Label(Login_Frame,text="Login Here",font=("arial",15),bg="white",padx=50)
Login_topic.place(x=100,y=20)
Username_label = Label(Login_Frame, text="Username :", font=("arial",15), bg="lightgrey" )
Username_label.place(x=30,y=80)
Username_field = Entry(Login_Frame, font=("arial",15))
Username_field.place(x=150, y=80)
#password field
Password = Label(Login_Frame, text="Password :", font=("arial",15), bg="lightgrey")
Password.place(x=30, y=150)
Password_field = Entry(Login_Frame, font=("arial",15))
Password_field.place(x=150, y=150)

Login_Button = Button(Login_Frame, text="Login", bg="blue",font=("arial",13), height=1, width=20, command=Login)
Login_Button.place(x=120, y= 230)
#Register Label
Register_Label = Label(Login_Frame, text="If you don't have an account", font=("arial",13), bg="lightgrey")
Register_Label.place(x=15, y=320)
Register_Button = Button(Login_Frame, text="Register", font=("arial",12),height=1, width=15, bg="orange", command=Register_Frame)
Register_Button.place(x=240, y=315)

Window.mainloop()