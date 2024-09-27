import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

app = Tk()
app.title('Tenants')

app.app_width = 1199
app.app_height = 600

app.screen_width = app.winfo_screenwidth()
app.screen_height = app.winfo_screenheight()

x = (app.screen_width / 2) - (app.app_width / 2)
y = (app.screen_height / 2) - (app.app_height / 2)
app.geometry(f'{app.app_width}x{app.app_height}+{int(x)}+{int(y)}')
app.resizable(False, False)

username2=StringVar()
Email=StringVar()
Password2=IntVar()
Confirm=IntVar()

def database():
    name=username2.get()
    email=Email.get()
    password=Password2.get()
    confirm=Confirm.get()
    if Password2.get() != Confirm.get():
        messagebox.showerror("Error", "Password and Confirm Password do not match")
    elif username2.get() == "" or Email.get() == "" or Password2.get() == "" or Confirm.get() == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("INFO", "Registered Successfully, Return to Login Page")
    conn =sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tenant (id INTEGER PRIMARY KEY, username2 TEXT, Email TEXT, Password2 INTEGER, Confirm INTEGER)")
    cursor.execute('INSERT INTO tenant (username2,Email,Password2,Confirm) VALUES(?,?,?,?)',(name,email,password,confirm))
    conn.commit()


frame_login1 = Frame(app, bg="white")
frame_login1.place(x=0, y=0, height=700, width=1366)

frame_input = Frame(app, bg='white')
frame_input.place(x=320, y=130, height=450, width=630)

label1 = Label(frame_input, text="Register Here", font=('impact', 32, 'bold'), fg="black", bg="white")
label1.place(x=45, y=20)

label2 = Label(frame_input, text="Username", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
label2.place(x=30, y=95)
username2 = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
username2.place(x=30, y=145, width=270, height=35)

label3 = Label(frame_input, text="Password", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
label3.place(x=30, y=195)
Password2 = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray",show='*')
Password2.place(x=30, y=245, width=270, height=35)

label4 = Label(frame_input, text="Email-id", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
label4.place(x=330, y=95)
Email = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray")
Email.place(x=330, y=145, width=270, height=35)

label5 = Label(frame_input, text="Confirm Password", font=("Goudy old style", 20, "bold"), fg="orangered",
                   bg="white")
label5.place(x=330, y=195)
Confirm = Entry(frame_input, font=("times new roman", 15, "bold"), bg="lightgray",show='*')
Confirm.place(x=330, y=245, width=270, height=35)




def register():
    if username2.get() == "" or Password2.get() == "" or Email.get() == "" or Confirm.get() == "":
        messagebox.showerror("Error", "All Fields Are Required",)
    if Password2.get() != Confirm.get():
        messagebox.showerror("Error", "Password and Confirm Password Should be the Same",)


btn = Button(frame_input, command=database, text="Register", cursor="hand2", font=("times new roman", 15),
                 fg="white", bg="orangered", bd=0, width=15, height=1)
btn.place(x=90, y=340)


def ReturnLogin():
    app.destroy()
    import main
btn2 = Button(frame_input, command=ReturnLogin,  text="Already Registered? Login", cursor="hand2",font=("calibri", 10), bg="white", fg="black", bd=0)
btn2.place(x=110, y=390)



app.mainloop()