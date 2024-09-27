import stat
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import tempfile
import sqlite3

app = Tk()
app.title("Bill and Receipts")
app_width = 1199
app_height = 600

app.screen_width = app.winfo_screenwidth()
app.screen_height = app.winfo_screenheight()

x = (app.screen_width / 2) - (app_width / 2)
y = (app.screen_height / 2) - (app_height / 2)

app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
app.resizable(False, False)


frame_login1 = Frame(app, bg="white")
frame_login1.place(x=0, y=0, height=700, width=1366)

frame_input = Frame(app, bg='white')
frame_input.place(x=320, y=130, height=450, width=630)

label1 = Label(text="Electricity Bill and Receipts", font=('impact', 32, 'bold'), fg="black", bg="white")
label1.place(x=45, y=20)


tenant_text = StringVar()
tenant_label = Label(app,text="Tenants Name", font=("Goudy old style", 20, "bold"), fg="orangered",bg="white")
tenant_label.place(x=30, y=95)
tenant_entry = Entry(app,font=("times new roman", 15, "bold"), bg="lightgray")
tenant_entry.place(x=30, y=145, width=270, height=35)

Number_text = StringVar()
Number_label = Label(app,text="House Number:", font=("Goudy old style", 20, "bold"), fg="orangered", bg="white")
Number_label.place(x=30, y=195)
Number_entry = Entry(app,font=("times new roman", 15, "bold"), bg="lightgray")
Number_entry.place(x=30, y=245, width=270, height=35)

Unit_text = StringVar()
Unit_label = Label(app,text="Units:", font=("Goudy old style", 20, "bold"), fg="orangered",bg="white")
Unit_label.place(x=30, y=300)
Unit_entry = Entry(app,font=("times new roman", 15, "bold"), bg="lightgray")
Unit_entry.place(x=30, y=345, width=270, height=35)




def check_function():
    name = tenant_entry.get()
    House_Number = Number_entry.get()
    Units = Unit_entry.get()
    if Unit_entry.get() == "" or tenant_entry.get() == "" or Number_entry.get() == "":
        messagebox.showerror("Error","Please enter the required fields")
    else:
        amount = int(Unit_entry.get()) * charge;
        round(amount)
        receipt.delete(1.0, END)
        receipt.insert(END, "          Electricity Bill")
        receipt.insert(END, f"\n\nTenant Name =:\t{tenant_entry.get()},")
        receipt.insert(END, f"\n\nHouse Number =:\t{Number_entry.get()},")
        receipt.insert(END, f"\n\nAmount =: ksh   ")
        receipt.insert(END, round(amount))
        receipt.insert(END, f"    \n\nMpesa Paybill Number: 4024059")
        receipt.insert(END, f"    \n\nKCB BANK account number: 011120442444")
        conn = sqlite3.connect('Form.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Bill (id INTEGER PRIMARY KEY, Tenant_Name TEXT, House_Number TEXT, Units INTEGER)")
        cursor.execute('INSERT INTO Bill (Tenant_Name,House_Number,Units) VALUES(?,?,?)',(name, House_Number, Units))
        conn.commit()

def call():
    res = messagebox.askquestion("Log out", f"Do you really want to log out?")
    if res == "yes":
       app.destroy()
       import main
    else:
       messagebox.showinfo("Return", "Return to the application")

def back():
    app.destroy()
    import Tenants
calc = Button(app,text='Logout', font=34, height=4, width=10, command= call)
calc.place(x=80, y=400)
def Next():
    app.destroy()
    import Water

calc = Button(app,text='Water Bill', font=34, height=4, width=10, command= Next)
calc.place(x=1050, y=500)


unit=Unit_entry.get()
charge=15.80



receipt = Text(app, height=20, width=70, border=0, bg="lightgray",font="TimesnewRoman")
receipt.place(x=500, y=90)
ok = Button(app, text='Calculate', font=34, height=4, width=10, command=check_function)
ok.place(x=80, y=500)
ok = Button(app, text='Back', font=34, height=4, width=5, command=back)
ok.place(x=20, y=500)


def print_area():
    q=receipt.get('1.0','end- 1c')
    temp_file = tempfile.mktemp('.txt')
    open(temp_file, 'w').write(q)
    os.chmod(temp_file,stat.S_IWRITE)
    os.startfile(temp_file,'Print')




prin = Button(app,text='Print', font=34, height=4, width=10,command=print_area)
prin.place(x=800, y=500)


def delete():
    receipt.delete(1.0,END)

delet = Button(app, text='Delete', font=34, height=4, width=10, command=delete)
delet.place(x=550, y=500)
app.mainloop()