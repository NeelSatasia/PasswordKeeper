import sqlite3
import random

file_name = 'database.db'

#column names
accounts = 'Accounts'
password_keeper_info = 'PasswordKeeperInfo'
ID = 'ID'
encrypted_account_name = 'EncryptedAccountName'
encrypted_username = 'EncryptedUsername'
encrypted_password = 'EncryptedPassword'
key_login_password = 'KeyAndLoginPassword'


def create_database():
    db = sqlite3.connect(file_name)
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS " + accounts + "(" + ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + encrypted_account_name + " text, " + encrypted_username + " text, " + encrypted_password + " text)")

    cursor.execute("CREATE TABLE IF NOT EXISTS " + password_keeper_info + "(" + ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + key_login_password + " text)")

    db.commit()
    db.close()




def add_password_keeper_info(value):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("INSERT INTO " + password_keeper_info + " values(null, '" + value + "')")

    db.commit()
    db.close()




def get_password_keeper_info(id):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT " + key_login_password + " FROM " + password_keeper_info + " WHERE " + ID + " = " + str(id))

    info = ''

    for value in cursor.fetchall():
        info = value[0]

    db.commit()
    db.close()

    return info




def change_password_keeper_info(id, encrypted_new_info):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("UPDATE " + password_keeper_info + " SET " + key_login_password + " = '" + encrypted_new_info + "' WHERE " + ID + " = " + str(id))

    db.commit()
    db.close()




def add_row(input_encrypted_account_name, input_encrypted_username, input_encrypted_password):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT " + encrypted_account_name + " FROM " + accounts)

    info_valid = True

    for stored_accountname in cursor.fetchall():
        if stored_accountname == input_encrypted_account_name:
            prin('\n\tAccount name already exists')
            info_valid = False
            break

    if info_valid == True:
        cursor.execute("INSERT INTO " + accounts + " values(null, '" + input_encrypted_account_name + "', '" + input_encrypted_username + "', '" + input_encrypted_password + "')")

    db.commit()
    db.close()

    return info_valid




def get_account_info(account_name):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM " + accounts + " WHERE " + encrypted_account_name + " = '" + account_name + "'")

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

    cursor.execute("SELECT " + encrypted_account_name + " FROM " + accounts)

    accounts_list = []

    for stored_accountname in cursor.fetchall():
        accounts_list.append(stored_accountname[0])

    db.commit()
    db.close()

    return accounts_list




def remove_account_info(input_encrypted_account_name):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("DELETE FROM " + accounts + " WHERE " + encrypted_account_name + " = '" + input_encrypted_account_name + "'")

    db.commit()
    db.close()




def remove_all_accounts_info():
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("DELETE FROM " + accounts)

    db.commit()
    db.close()




def change_account_name(encrypted_old_account_name, encrypted_new_account_name):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("UPDATE Accounts SET " + encrypted_account_name + " = '" + encrypted_new_account_name + "' WHERE " + encrypted_account_name + " = '" + encrypted_old_account_name + "'")

    db.commit()
    db.close()




def change_username(input_encrypted_account_name, input_encrypted_new_username):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("UPDATE Accounts SET " + encrypted_username + " = '" + input_encrypted_new_username + "' WHERE " + encrypted_account_name + " = '" + input_encrypted_account_name + "'")

    db.commit()
    db.close()




def change_password(input_encrypted_account_name, input_encrypted_new_password):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("UPDATE Accounts SET " + encrypted_password + " = '" + input_encrypted_new_password + "' WHERE " + encrypted_account_name + " = '" + input_encrypted_account_name + "'")

    db.commit()
    db.close()
