import sqlite3
import os.path
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = (BASE_DIR + '\\Form.db')




class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("login system")
        self.root.app_width = 1199
        self.root.app_height = 600

        self.root.screen_width = root.winfo_screenwidth()
        self.root.screen_height = root.winfo_screenheight()

        x = (self.root.screen_width / 2) - (self.root.app_width / 2)
        y = ( self.root.screen_height / 2) - (self.root.app_height / 2)
        self.root.geometry(f'{self.root.app_width}x{self.root.app_height}+{int(x)}+{int(y)}')
        self.root.resizable(False, False)

        global username
        global Password

        self.username = StringVar()
        self.Password = StringVar()

        # login Frame
        Frame_Login = Frame(self.root, bg="Dark Orange")
        Frame_Login.place(x=330, y=150, width=500, height=400)
        #Title & subtitle
        title= Label(Frame_Login, text="Login Here", font=("impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        subtitle= Label(Frame_Login, text="Admin Login", font=("Goudy Old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90, y=100)

        #username
        lbl_user = Label(Frame_Login, text="Username", font=("Goudy Old style", 15, "bold"), fg="black",bg="white").place(x=90, y=140)
        self.username = Entry(Frame_Login,  font=("Goudy Old style", 15,),bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320,height=35)
        # Password
        lbl_Password = Label(Frame_Login, text="Password", font=("Goudy Old style", 15, "bold"), fg="black",bg="white").place(x=90, y=210)
        self.Password = Entry(Frame_Login, font=("Goudy Old style", 15,), bg="#E7E6E6",show='*')
        self.Password.place(x=90, y=240, width=320, height=35)
        #register button
        register = Button(Frame_Login, command=self.nexten, text="New User? Register Here", bd=0, cursor="hand2",
                          font=("Goudy Old style", 12, "bold"), fg="black", bg="white").place(x=90, y=365)
        # button
        Forget = Button(Frame_Login, command=self.nexten, text="Forgot Password?", bd=0, cursor="hand2",
                        font=("Goudy Old style", 12, "bold"), fg="black", bg="white").place(x=90, y=280)

        Submit = Button(Frame_Login, command=self.login, cursor="hand2", text="Login", bd=0,
                        font=("Goudy Old style", 15, "bold"), bg="blue", fg="white").place(x=90, y=320, width=180,
                                                                                           height=40)

    def login(self):
            conn = sqlite3.connect('Form.db')
            print("opened database successfully")
            cursor = conn.execute("SELECT * FROM tenant WHERE username2 = ? AND  Password2 = ?", (self.username.get(), self.Password.get()))
            row = cursor.fetchone()
            if row:
                messagebox.showinfo("info","Login Success")
                self.root.destroy()
                import Tenants
            else:
                messagebox.showinfo("info","Login Failed, Enter the correct Username or Password")

    def nexten(self):
        self.root.destroy()
        import register

root = Tk()
obj = Login(root)
root.mainloop()