import sqlite3
import random

file_name = 'database.db'

def create_database():
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Accounts (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EncryptedAccountName text,
        EncryptedUsername text,
        EncryptedPassword text
    )

    """
    )

    db.commit()
    db.close()




def add_row(account_name, username, encrypted_password):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT EncryptedAccountName FROM Accounts")

    info_valid = True

    for stored_accountname in cursor.fetchall():
        if stored_accountname == account_name:
            prin('\n\tAccount name already exists')
            info_valid = False
            break

    if info_valid == True:
        cursor.execute("INSERT INTO accounts values(null, '" + account_name + "', '" + username + "', '" + encrypted_password + "')")

    db.commit()
    db.close()

    return info_valid




def get_account_info(account_name):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Accounts WHERE EncryptedAccountName = '" + account_name + "'")

    account_info = []

    for row in cursor.fetchall():
        account_info.append(row[2])
        account_info.append(row[3])

    db.commit()
    db.close()

    return account_info




def get_all_account_names():
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT EncryptedAccountName FROM Accounts")

    accounts = []

    for stored_accountname in cursor.fetchall():
        accounts.append(stored_accountname[0])

    db.commit()
    db.close()

    return accounts




def remove_account_info(encrypted_account_name):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    account_removed = False

    if len(get_account_info(encrypted_account_name)) > 0:
        cursor.execute("DELETE FROM Accounts WHERE EncryptedAccountName = '" + encrypted_account_name + "'")
        account_removed = True

    db.commit()
    db.close()

    return account_removed




def remove_all_accounts_info():
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("DELETE FROM Accounts")

    db.commit()
    db.close()



def change_account_name(encrypted_old_account_name, encrypted_new_account_name):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("UPDATE Accounts SET EncryptedAccountName = '" + encrypted_new_account_name + "' WHERE EncryptedAccountName = '" + encrypted_old_account_name + "'")

    db.commit()
    db.close()


def change_username(encrypted_account_name, encrypted_new_username):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("UPDATE Accounts SET EncryptedUsername = '" + encrypted_new_username + "' WHERE EncryptedAccountName = '" + encrypted_account_name + "'")

    db.commit()
    db.close()


def change_password(encrypted_account_name, encrypted_new_password):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("UPDATE Accounts SET EncryptedPassword = '" + encrypted_new_password + "' WHERE EncryptedAccountName = '" + encrypted_account_name + "'")

    db.commit()
    db.close()
