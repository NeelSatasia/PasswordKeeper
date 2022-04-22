from datamanager import *
from getpass import getpass

create_table()

print('\nCommands:\n')

print('\tAdd An Account:       /add')
print('\tRemove An Account:    /remove')
print('\tAccess An Account:    /access')
print('\tClose Program:        /close')

print()

add_account = '/add'
remove_account = '/remove'
access_account = '/access'
close_program = '/close'

while True:

    input_command = input('Enter a commmand: ')
    print()

    if input_command ==  add_account:

        input_account_name = input('\tAccount Name: ')
        input_username = input('\tUsername: ')
        input_password = getpass('\tPassword (Hidden): ')
        input_confirm_password = getpass('\tConfirm Password: ')

        print()

    elif input_command == close_program:
        break
