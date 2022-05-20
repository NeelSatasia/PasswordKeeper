# PasswordKeeper

Description: This project is made to keep all your passwords encrypted in a database file where all the information about your accounds are saved such account    name, username, and password. There're multiple commands that do certain actions. When the user selects a command, it will allow the user to do certain things with any stored accounts. For example, if the user selects the add account command, it will ask the user to enter account information. After entering all the info, it will encrypt all that info in the datbase file. If the user wants to see the information, the user can select the access account command and which account the user wants to choose. The program will then decrypt the info, so the user can see it.

Python Files:

  1. main.py: Takes the input of the user and provides options to change, remove, or add account information.
  2. datamanager.py: Manages all the data entered by the user such as account name, username (optional), and password.
  3. accountinfo.py: AccountInfo object keeps track of every account information.

Modules Required:
  1. sqlite3
  2. TerminalMenu
  3. random
