import sqlite3
from tkinter import messagebox

file_name = 'database.db'

def create_table():
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Accounts (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        AccountName text,
        Username text,
        EncryptedPassword text
    )
    """
    )

    db.commit()
    db.close()

def add_row(account_name, username, password):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT AccountName FROM Accounts")

    info_valid = True

    for stored_accountname in cursor.fetchall():
        if stored_accountname == account_name:
            messagebox.showerror('showerror', 'Account name already exists!')
            info_valid = False
            break

    if info_valid == True:
        cursor.execute("INSERT INTO accounts values(null, '" + account_name + "', '" + username + "', '" + password + "')")

    db.commit()
    db.close()

def get_all_account_names():
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT AccountName FROM Accounts")

    accounts = []

    for stored_accountname in cursor.fetchall():
        accounts.append(stored_accountname)

    db.commit()
    db.close()

    return accounts
