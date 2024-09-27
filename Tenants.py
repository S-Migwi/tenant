import tkinter
from tkinter import *
from tkinter import messagebox
from db import Database
import tkcalendar
from tkcalendar import DateEntry
import db
from tabulate import tabulate
import datetime
from tkinter import ttk, NS, Scrollbar
import sqlite3

app = Tk()
tree=ttk.Treeview(app)
db = Database('store.db')
conn = sqlite3.connect('store.db')
cur = conn.cursor()
global i
i = 0
j = i + 1

def add_item():
    if tenant_text.get() == '' or Number_text.get() == '' or rent_text.get() == '' or balance_text.get() == '' or lastpayment_text.get() == DateEntry or phonenumber_text.get() == int():
        messagebox.showerror('Required Fields','Please include all fields')

    db.insert(tenant_text.get(), Number_text.get(), rent_text.get(), balance_text.get(), lastpayment_text.get(), phonenumber_text.get())
    tenant=tenant_entry.get()
    number=Number_entry.get()
    rent=rent_entry.get()
    balance=balance_entry.get()
    last=lastpayment_entry.get()
    phone=phonenumber_entry.get()

    tree.insert(parent="", index="end",values=(j,tenant,number,rent,balance,last,phone))

def clear_input():
    tenant_entry.delete(0, END)
    Number_entry.delete(0, END)
    rent_entry.delete(0, END)
    balance_entry.delete(0, END)
    lastpayment_entry.delete(0, END)
    phonenumber_entry.delete(0, END)

def remove_item():
    x = tree.selection() [0]
    tree.delete(x)
    db.remove(x)

    tenant_entry.delete(0, END)
    Number_entry.delete(0, END)
    rent_entry.delete(0, END)
    balance_entry.delete(0, END)
    lastpayment_entry.delete(0, END)
    phonenumber_entry.delete(0, END)
def select_record():
    tenant_entry.delete(0, END)
    Number_entry.delete(0, END)
    rent_entry.delete(0, END)
    balance_entry.delete(0, END)
    lastpayment_entry.delete(0, END)
    phonenumber_entry.delete(0, END)

    selected=tree.focus()
    values= tree.item(selected,"values")

    tenant_entry.insert(0, values[1])
    Number_entry.insert(0, values[2])
    rent_entry.insert(0, values[3])
    balance_entry.insert(0, values[4])
    lastpayment_entry.insert(0, values[5])
    phonenumber_entry.insert(0, values[6])


def update_item():

    selected=tree.focus()
    tree.item(selected, text="", values=(j,tenant_text.get(), Number_text.get(), rent_text.get(), balance_text.get(), lastpayment_text.get(), phonenumber_text.get()))
    db.update(selected,tenant_text.get(), Number_text.get(), rent_text.get(), balance_text.get(), lastpayment_text.get(), phonenumber_text.get())
    tenant_entry.delete(0, END)
    Number_entry.delete(0, END)
    rent_entry.delete(0, END)
    balance_entry.delete(0, END)
    lastpayment_entry.delete(0, END)
    phonenumber_entry.delete(0, END)

def clicker(e):
    select_record()
def next_page():
    app.destroy()
    import Electricity

def search_records():
    lookup_record = search_entry.get()
    #close searchbox
    search.destroy()
    #conn = sqlite3.connect()
    cur = conn.cursor()

    #clear the treeview
    for record in tree.get_children():
        tree.delete(record)
    for row in db.fetch():
        cur.execute("SELECT id, * FROM tenants WHERE Tenant LIKE ?", lookup_record)
        row = cur.fetchall()
        return row

#search frame development
def lookup_records():
    global search_entry, search

    search= Toplevel(app)
    search.title("Lookup Records")
    search.geometry("400x200")

    search_frame = LabelFrame(search, text="Tenant Name")
    search_frame.pack(padx=10,pady=10)

    search_entry = Entry(search_frame, font=("Goudy Old style",18))
    search_entry.pack(pady=20,padx=20)

    search_button = Button(search, text="Search Records",command=search_records)
    search_button.pack(padx=20,pady=20)




lookup_record = StringVar()

#create new window object
app.title('Tenants')
app.geometry('1280x780')
app.configure(bg="Dark Orange")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",background="#D3D3D3",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
style.map("Treeview",background=[("selected","blue")])
#Name of the tenant
tenant_text = StringVar()
tenant_label = Label(app, text='Tenant Name', font=('bold', 26), pady=80, bg="Dark Orange")
tenant_label.grid(row=0, column=0, sticky=W)
tenant_entry = Entry(app, textvariable=tenant_text, font=("default", 20 or 20))
tenant_entry.grid(row=0, column=1)

#house Number
Number_text = StringVar()
Number_label = Label(app, text='House Number', font=('bold', 26), pady=80, bg="Dark Orange")
Number_label.grid(row=0, column=2, sticky=W)
Number_entry = Entry(app, textvariable=Number_text, font=("default", 20 or 20))
Number_entry.grid(row=0, column=3)

#house rent
rent_text = StringVar()
rent_label = Label(app, text='House rent', font=('bold', 26),bg="Dark Orange")
rent_label.grid(row=1, column=0, sticky=W)
rent_entry = Entry(app, textvariable=rent_text, font=("default", 20 or 20))
rent_entry.grid(row=1, column=1)

#outstanding balance
balance_text = StringVar()
balance_label = Label(app, text='Outstanding Balance', font=('bold', 26), bg="Dark Orange")
balance_label.grid(row=1, column=2, sticky=W)
balance_entry = Entry(app, textvariable=balance_text, font=("default", 20 or 20))
balance_entry.grid(row=1, column=3)

#Last payment/date/month/year
lastpayment_text = StringVar()
lastpayment_label = Label(app, text='Last Payment', font=('bold', 26), pady=80, bg="Dark Orange")
lastpayment_label.grid(row=3, column=0, sticky=W)
lastpayment_entry = DateEntry(app, textvariable=lastpayment_text,font=("default", 20 or 20))
lastpayment_entry.grid(row=3, column=1)

phonenumber_text = StringVar()
phonenumber_label = Label(app, text='Phone Number', font=('bold', 26), pady=80, bg="Dark Orange")
phonenumber_label.grid(row=3, column=2, sticky=W)
phonenumber_entry = Entry(app, textvariable=phonenumber_text,font=("default", 20 or 20))
phonenumber_entry.grid(row=3, column=3)

my_menu=Menu(app)
app.configure(menu=my_menu)


tree["columns"]=("id","Tenant Name","House Number","House Rent","Outstanding Balance","Last Payment","Phone Number")
#adding columns in the treeview
tree.column("#0", width=0,stretch=NO)
tree.column("id", width=50,minwidth=50,anchor=tkinter.W)
tree.column("Tenant Name", width=120,minwidth=100,anchor=tkinter.CENTER)
tree.column("House Number", width=150,minwidth=50)
tree.column("House Rent", width=150,minwidth=150)
tree.column("Outstanding Balance", width=150,minwidth=50)
tree.column("Last Payment", width=150,minwidth=150)
tree.column("Phone Number", width=150,minwidth=150)

#adding headings of each column
tree.heading("#0", text="",anchor=W)
tree.heading("id", text="ID",anchor=tkinter.W)
tree.heading("Tenant Name",  text="Tenant Name",anchor=tkinter.CENTER)
tree.heading("House Number",  text="House Number",anchor=tkinter.CENTER)
tree.heading("House Rent",  text="House Rent",anchor=tkinter.CENTER)
tree.heading("Outstanding Balance",  text="Outstanding Balance",anchor=tkinter.CENTER)
tree.heading("Last Payment",  text="Last Payment",anchor=tkinter.CENTER)
tree.heading("Phone Number",  text="Phone Number",anchor=tkinter.CENTER)


#placing the treeview on a specified area
tree.grid(row=5, column=0, columnspan=3, rowspan=6,padx=20,pady=20)
#Fetching data from the database
for record in db.fetch():
    tree.insert(parent="",index="end",iid=record[0],values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]))
tree.pack

search_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)

search_menu.add_command(label="Search", command=lookup_records)




#buttons
add_btn = Button(app, text='Add', font=34,  height=4, width=10, command=add_item)
add_btn.grid(row=4, column=0)

remove_btn = Button(app, text='Remove', font=34,  height=4, width=10, command=remove_item)
remove_btn.grid(row=4, column=1)

update_btn = Button(app, text='Update', font=34,  height=4, width=10, command=update_item)
update_btn.grid(row=4, column=2)

clear_btn = Button(app, text='Clear input', font=34,  height=4, width=10, command=clear_input)
clear_btn.grid(row=4, column=3)



next_btn = Button(app, text='Bill and Receipts', font=34,  height=4, width=20,command=next_page)
next_btn.grid(row=5, column=3)

class DateEntry(tkcalendar.DateEntry):
    def _validate_date(self):
        if not self.get():
            return True

        return super()._validate_date()

#bindings
tree.bind("<ButtonRelease-1>", clicker)


#start program

app.mainloop()