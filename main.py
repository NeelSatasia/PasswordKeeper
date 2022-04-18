from tkinter import *
from tkinter import messagebox
from datamanager import *

create_table()

main_window = Tk()
main_window.geometry("300x250")
main_window.title("Password Keeper")

main_frame = Frame(main_window)
main_frame.pack()

menu_frame = Frame(main_frame)
menu_frame.pack()

add_account_frame = Frame(main_frame)

account_name_label = Label(add_account_frame, text='Account Name:')
account_name_label.grid(row=0, column=0, padx=15, pady=10)

account_name_field = Entry(add_account_frame, width=10)
account_name_field.grid(row=0, column=1, padx=15, pady=10)

username_label = Label(add_account_frame, text='Username:')
username_label.grid(row=1, column=0, padx=15, pady=5)

username_field = Entry(add_account_frame, width=10)
username_field.grid(row=1, column=1, padx=15, pady=5)

password_label = Label(add_account_frame, text='Password:')
password_label.grid(row=2, column=0, padx=15, pady=5)

password_field = Entry(add_account_frame, width=10)
password_field.grid(row=2, column=1, padx=15, pady=5)

def add_account_info():
    if account_name_field.get() != '' and password_field.get() != '':
        add_row(account_name_field.get(), username_field.get(), password_field.get())

    else:
        messagebox.showerror('showerror', 'Account name and passoword fields are required!')

add_btn = Button(add_account_frame, text='Add', command=add_account_info, padx=5, pady=2)
add_btn.grid(row=3, column=0, columnspan=2, padx=15, pady=5)

def add_account_to_menu_frame():
    menu_frame.pack()
    add_account_frame.pack_forget()

cancel_btn = Button(add_account_frame, text='Cancel', command=add_account_to_menu_frame, padx=5, pady=2)
cancel_btn.grid(row=4, column=0, columnspan=2, padx=15, pady=5)

access_account_frame = Frame(main_window)

def add_account_info():
    account_name_field.delete(0, END)
    username_field.delete(0, END)
    password_field.delete(0, END)

    add_account_frame.pack()
    menu_frame.pack_forget()

title_label = Label(menu_frame, text='Password Keeper')
title_label.config(font=('Arial', 25))
title_label.pack(padx=20, pady=10)

add_account_btn = Button(menu_frame, text='Add Account Info', command=add_account_info)
add_account_btn.config(font=('Arial', 15))
add_account_btn.pack(padx=20, pady=5)

access_account_btn = Button(menu_frame, text='Access Account Info')
access_account_btn.config(font=('Arial', 15))
access_account_btn.pack(padx=20, pady=5)

main_window.mainloop()
