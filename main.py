from datamanager import *
from accountinfo import AccountInfo
from getpass import getpass
import random
from simple_term_menu import TerminalMenu

create_database()

add_account = 'Add Account'
remove_account = 'Remove Account'
remove_all_accounts = 'Remove All Accounts'
access_account = 'Access Account'
change_account_name_command = 'Change Account Name'
change_username_command = 'Change Account Username'
change_password_command = 'Change Account Password'
change_login_password_command = 'Change Login Password'
change_encryption_key = 'Change Encryption Key'
cancel_a_command = '/cancel'
close_program = '[x] Close'

print('\nTo exit any typable command, type /cancel \n')

failed_to_encrypt = '(Failed to encrypt!)'
failed_to_decrypt = '(Failed to decrypt!)'
account_search_failure = '(Account name does not exist or the encryption key is wrong!)'
account_name_required_alert = '(Must have an account name!)'
no_accounts_found = "(There're currently no accounts!)"
exit_account_names = '[x] Exit'

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '/', '?', '-', '_', '+', '=', ' ', '/', ":", ";", "'"]

def make_encryption_key(key):
    encrypted_key = ''

    for encrypted_character_index in range(len(key)):
        encrypted_key += (' ' * (characters.index(key[encrypted_character_index]) + 1))

        if encrypted_character_index < len(key) - 1:
            encrypted_key += '\t'

    return encrypted_key


encryption_key = []


if len(get_password_keeper_info(1)) == 0:
    encryption_key = characters.copy()

    random.shuffle(encryption_key)

    key = make_encryption_key(encryption_key)

    add_password_keeper_info(key)

else:
    uploaded_encrypted_key = get_password_keeper_info(1)

    encrypted_key = uploaded_encrypted_key.split('\t')

    for encrypted_character in encrypted_key:
        encryption_key.append(characters[len(encrypted_character) - 1])


encrypted_characters = []


for character_index in range(len(encryption_key)):
    encrypted_characters.append(' ' * (character_index + 1))



def encrypt(text):
    text_characters = []

    for text_character in text:
        text_characters.append(text_character)

    encrypted_text = ''

    try:
        for i in range(len(text_characters)):
            encrypted_text += encrypted_characters[encryption_key.index(text_characters[i])]

            if i < len(text_characters) - 1:
                encrypted_text += '\t'

    except:
        encrypted_text = failed_to_encrypt

    return encrypted_text


def decrypt(text):
    if len(text) > 0:
        encrypted_text = text.split('\t')
        decrypted_text = ''

        try:
            for encryted_character in encrypted_text:
                encrypted_character_index = len(encryted_character) - 1
                decrypted_text += encryption_key[encrypted_character_index]

            return decrypted_text

        except:
            return failed_to_decrypt

    else:
        return ''



logged_in = False

if len(get_password_keeper_info(2)) > 0:
    input_login_password = getpass('Enter login password: ')
    print()

    if len(input_login_password) > 0:

        if input_login_password == decrypt(get_password_keeper_info(2)):
            logged_in = True

        else:
            print('\t(Incorrect password or the encryption key is wrong!)\n')

    else:
        print('\t(Must enter a password!)\n')

else:
    input_create_login_password = getpass('Create login password: ')

    if len(input_create_login_password) > 0:
        input_confirm_login_password = getpass('Confirm login password: ')
        print()

        if input_create_login_password == input_confirm_login_password:

            encrypted_login_password = encrypt(input_create_login_password)

            if encrypted_login_password == failed_to_encrypt:
                print('\t' + failed_to_encrypt + '\n')

            else:
                add_password_keeper_info(encrypted_login_password)
                logged_in = True

        else:
            print("\t(Passwords do not match!)\n")

    else:
        print('\n\t(Must enter a password!)\n')



def accounts_menu():
    decrypted_account_names = []

    for encrypted_account_name in get_all_account_names():
        decrypted_account_names.append(decrypt(encrypted_account_name))

    decrypted_account_names.sort()

    decrypted_account_names.append(exit_account_names)

    accounts_menu = TerminalMenu(decrypted_account_names)
    accounts_menu_index = accounts_menu.show()

    return decrypted_account_names[accounts_menu_index]



commands_options = [add_account, remove_account, remove_all_accounts, access_account, change_account_name_command, change_username_command, change_password_command,
                    change_login_password_command, change_encryption_key, close_program]

commands_menu = TerminalMenu(commands_options)


if logged_in == True:

    while True:

        commands_menu_index = commands_menu.show()

        if commands_options[commands_menu_index] ==  add_account:

            input_account_name = input('Account Name: ')

            if input_account_name != cancel_a_command:

                decryptable = True
                account_name_valid = True
                account_name_error = ''

                for encrypted_account_name in get_all_account_names():
                    decrypted_account_name = decrypt(encrypted_account_name)

                    if decrypted_account_name == failed_to_decrypt:
                        decryptable = False
                        break

                    elif decrypted_account_name == input_account_name:
                        account_name_valid = False
                        account_name_error = '(Account name already exists!)'
                        break

                if decryptable == True:
                    if account_name_valid == True and len(input_account_name) == 0:
                        account_name_valid = False
                        account_name_error = account_name_required_alert

                    if account_name_valid == True:
                        input_username = input('Username (Optional): ')

                        if input_username != cancel_a_command:
                            input_password = getpass('Password (Hidden): ')

                            if input_password != cancel_a_command:
                                input_confirm_password = getpass('Confirm Password: ')

                                if input_confirm_password != cancel_a_command:

                                    if input_password == input_confirm_password:
                                        encrypted_account_name = encrypt(input_account_name)

                                        encrypted_username = ''

                                        if len(input_username) > 0:
                                            encrypted_username = encrypt(input_username)

                                        encrypted_password = encrypt(input_password)

                                        if encrypted_account_name != failed_to_encrypt and encrypted_username != failed_to_encrypt and encrypted_password != failed_to_encrypt:
                                            add_row(encrypted_account_name, encrypted_username, encrypted_password)

                                        else:
                                            print('\n\t' + failed_to_encrypt)

                                    else:
                                        print('\n\t(Passwords do not match!)')

                    else:
                        print('\n\t' + account_name_error)

                else:
                    print("\n\t(Failed to scan existing account names to check if the given account name exists in the database!)")

            print()




        elif commands_options[commands_menu_index] == access_account:

            if len(get_all_account_names()) > 0:

                account_name = accounts_menu()

                if account_name != exit_account_names:

                    print('Account Name: ' + account_name + '\n')

                    encrypted_account_name = encrypt(account_name)

                    account_info = get_account_info(encrypted_account_name)

                    encrypted_username = account_info[0]
                    encrypted_password = account_info[1]

                    decrypted_username = ''

                    if len(encrypted_username) > 0:
                        decrypted_username = decrypt(encrypted_username)

                    decrypted_password = decrypt(encrypted_password)

                    if decrypted_username != failed_to_decrypt and decrypted_password != failed_to_decrypt:
                        if len(decrypted_username) > 0:
                            print('\tUsername: ' + decrypted_username)

                        print('\tPassword: ' + decrypted_password + '\n')

                    else:
                        print('\t' + failed_to_decrypt + '\n')

            else:
                print(no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == remove_account:

            if len(get_all_account_names()) > 0:

                account_name = accounts_menu()

                if account_name != exit_account_names:
                    encrypted_account_name = encrypt(account_name)

                    if encrypted_account_name == failed_to_encrypt:
                        print(failed_to_encrypt + '\n')

                    else:
                        remove_account_info(encrypted_account_name)
                        print("(Info of account '" + account_name + "' is removed)\n")

            else:
                print(no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == remove_all_accounts:

            if len(get_all_account_names()) > 0:

                    input_login_password = getpass('Enter login password: ')
                    print()

                    if len(input_login_password) > 0:
                        encrypted_input_login_password = encrypt(input_login_password)

                        if encrypted_input_login_password == failed_to_encrypt:
                            print('\t' + failed_to_encrypt + '\n')

                        elif encrypted_input_login_password == get_password_keeper_info(2):
                            remove_all_accounts_info()

                            print("\t(All accounts' info is deleted)\n")

                        else:
                            print('\t(Password entered is incorrect!)\n')

                    else:
                        print('\t(Must enter a password!)\n')

            else:
                print(no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == change_account_name_command:

            if len(get_all_account_names()) > 0:

                account_name = accounts_menu()

                if account_name != exit_account_names:

                    encrypted_account_name = encrypt(account_name)

                    if encrypted_account_name == failed_to_encrypt:
                        print(failed_to_encrypt + '\n')

                    else:
                        input_new_account_name = input('New Account Name: ')
                        print()

                        if len(input_new_account_name) > 0:

                            if input_new_account_name != cancel_a_command:
                                encrypted_new_account_name = encrypt(input_new_account_name)

                                if encrypted_new_account_name == failed_to_encrypt:
                                    print('\t' + failed_to_encrypt + '\n')

                                else:
                                    change_account_name(encrypted_account_name, encrypted_new_account_name)

                        else:
                            print('\t(Account must have a name!)\n')

            else:
                print(no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == change_username_command:

            if len(get_all_account_names()) > 0:

                account_name = accounts_menu()

                if account_name != exit_account_names:

                    encrypted_account_name = encrypt(account_name)

                    if encrypted_account_name == failed_to_encrypt:
                        print(failed_to_encrypt + '\n')

                    else:
                        input_new_username = input('New Username: ')
                        print()

                        if input_new_username != cancel_a_command:
                            if len(input_new_username) > 0:
                                encrypted_new_username = encrypt(input_new_username)

                                change_username(encrypted_account_name, encrypted_new_username)

                            else:
                                change_username(encrypted_account_name, '')

            else:
                print(no_accounts_found + '\n')





        elif commands_options[commands_menu_index] == change_password_command:

            if len(get_all_account_names()) > 0:

                account_name = accounts_menu()

                if account_name != exit_account_names:

                    encrypted_account_name = encrypt(account_name)

                    if encrypted_account_name == failed_to_encrypt:
                        print(failed_to_encrypt + '\n')

                    else:
                        input_new_password = getpass('New Password: ')

                        if len(input_new_password) > 0:

                            if input_new_password != cancel_a_command:
                                input_confirm_new_password = getpass('Confirm Password: ')
                                print()

                                if input_confirm_new_password != cancel_a_command:

                                    if input_new_password == input_confirm_new_password:
                                        encrypted_new_password = encrypt(input_new_password)

                                        change_password(encrypted_account_name, encrypted_new_password)

                                    else:
                                        print('\t\t\t(Passwords do not match!)\n')

                        else:
                            print('\t(New password cannot be empty!)\n')

            else:
                print(no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == change_login_password_command:

            input_current_login_password = getpass('Enter current login password: ')

            encrypted_current_password = encrypt(input_current_login_password)

            if encrypted_current_password == failed_to_encrypt:
                print('\t' + failed_to_encrypt + '\n')

            else:
                if encrypted_current_password == get_password_keeper_info(2):
                    input_new_password = getpass('Enter new password: ')

                    if len(input_new_password) > 0:
                        input_confirm_new_password = getpass('Confirm Password: ')

                        if input_new_password == input_confirm_new_password:
                            encrypted_new_password = encrypt(input_new_password)

                            change_password_keeper_info(2, encrypted_new_password)
                            print()
                        else:
                            print('\n\t(Passwords do not match!)\n')

                    else:
                        print('\n\t(Must enter a password!)\n')

                else:
                    print('\n\t(Password entered is incorrect!)\n')




        elif commands_options[commands_menu_index] == change_encryption_key:
            input_login_password = getpass('Enter login password: ')
            print()

            if len(input_login_password) > 0:
                encrypted_login_password = encrypt(input_login_password)

                if encrypted_login_password == failed_to_encrypt:
                    print('\t' + failed_to_encrypt + '\n')

                elif encrypted_login_password == get_password_keeper_info(2):

                    accounts = []

                    for stored_account_name in get_all_account_names():
                        stored_account_info = get_account_info(stored_account_name)
                        accounts.append(AccountInfo(decrypt(stored_account_name), decrypt(stored_account_info[0]), decrypt(stored_account_info[1])))

                    encryption_key.clear()

                    encryption_key = characters.copy()

                    random.shuffle(encryption_key)

                    new_key = make_encryption_key(encryption_key)

                    change_password_keeper_info(1, new_key)
                    change_password_keeper_info(2, encrypt(input_login_password))

                    remove_all_accounts_info()

                    for accountinfo in accounts:
                        add_row(encrypt(accountinfo.account_name), encrypt(accountinfo.username), encrypt(accountinfo.password))

                    print('\t(Encryption Key is changed through randomization)\n')

                else:
                    print('\t(Password entered is incorrect!)\n')

            else:
                print('\t(Must enter the login password!)\n')




        elif commands_options[commands_menu_index] == close_program:
            break
