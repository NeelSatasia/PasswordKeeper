import sqlite3

def create_table():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS accounts (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        AccountType text,
        Username text,
        EncryptedPassword text
    )
    """
    )

    db.commit()
    db.close()

def add_row(account_name, username, password):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute("INSERT INTO accounts values(null, '" + account_name + "', '" + username + "', '" + password + "')")

    db.commit()
    db.close()
