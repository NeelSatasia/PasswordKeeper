import sqlite3

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
        EncryptedPassword text,
        EncryptedPasswordInNums text
    )
    """
    )

    db.commit()
    db.close()

def add_row(account_name, username, encrypted_password, encrypted_password_in_nums):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT AccountName FROM Accounts")

    info_valid = True

    for stored_accountname in cursor.fetchall():
        if stored_accountname == account_name:
            prin('\n\tAccount name already exists')
            info_valid = False
            break

    if info_valid == True:
        cursor.execute("INSERT INTO accounts values(null, '" + account_name + "', '" + username + "', '" + encrypted_password + "', '" + encrypted_password_in_nums + "')")

    db.commit()
    db.close()

    return info_valid

def get_account_info(account_name):
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Accounts WHERE AccountName = '" + account_name + "'")

    for row in cursor.fetchall():
        account_info = [row[2], row[3], row[4]]

        db.commit()
        db.close()

        return account_info

    db.commit()
    db.close()

    return ''

def get_all_account_names():
    db = sqlite3.connect(file_name)

    cursor = db.cursor()

    cursor.execute("SELECT AccountName FROM Accounts")

    accounts = []

    for stored_accountname in cursor.fetchall():
        accounts.append(stored_accountname[0])

    db.commit()
    db.close()

    return accounts
