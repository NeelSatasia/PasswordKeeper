from datamanager import *
from getpass import getpass
import random
from simple_term_menu import TerminalMenu

create_database()

add_account = 'Add'
remove_account = 'Remove'
remove_all_accounts = 'Remove All'
access_account = 'Access'
access_all_account_names = 'Access Account Names'
change_account_name_command = 'Change Account Name'
change_username_command = 'Change Username'
change_password_command = 'Change Password'
change_login_password_command = 'Change Login Password'
forgot_password = 'Forgot Login Password'
cancel_a_command = '/cancel'
close_program = 'Close'

print('\n')

failed_to_encrypt = '(Failed to encrypt!)'
failed_to_decrypt = '(Failed to decrypt!)'
account_search_failure = '(Account name does not exist or the encryption key is wrong!)'
account_name_required_alert = '(Must have an account name!)'
no_accounts_found = "(There're currently no accounts!)"

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '/', '?', '-', '_', '+', '=', ' ', '/', ":", ";"]

encryption_key = []


if len(get_password_keeper_info(1)) == 0:
    for character in characters:
        encryption_key.append(character)

    random.shuffle(encryption_key)

    encrypted_key = ''

    for encrypted_character_index in range(len(encryption_key)):
        encrypted_key += (' ' * (characters.index(encryption_key[encrypted_character_index]) + 1))

        if encrypted_character_index < len(encryption_key) - 1:
            encrypted_key += '\t'

    add_password_keeper_info(encrypted_key)

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
    encrypted_text = text.split('\t')
    decrypted_text = ''

    try:
        for encryted_character in encrypted_text:
            encrypted_character_index = len(encryted_character) - 1
            decrypted_text += encryption_key[encrypted_character_index]

        return decrypted_text

    except:
        return failed_to_decrypt



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
    print()

    if len(input_create_login_password) > 0:
        encrypted_login_password = encrypt(input_create_login_password)

        if encrypted_login_password == failed_to_encrypt:
            print('\t' + failed_to_encrypt + '\n')

        else:
            add_password_keeper_info(encrypted_login_password)
            logged_in = True

    else:
        print('\t(Must enter a password!)\n')



commands_options = [add_account, remove_account, remove_all_accounts, access_account, access_all_account_names, change_account_name_command, change_username_command, change_password_command,
                   change_login_password_command, close_program]

commands_menu = TerminalMenu(commands_options)


if logged_in == True:

    while True:

        commands_menu_index = commands_menu.show()
        print()

        if commands_options[commands_menu_index] ==  add_account:

            input_account_name = input('\tAccount Name: ')

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
                        input_username = input('\tUsername (Optional): ')

                        if input_username != cancel_a_command:
                            input_password = getpass('\tPassword (Hidden): ')

                            if input_password != cancel_a_command:
                                input_confirm_password = getpass('\tConfirm Password: ')

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
                                            print('\n\t\t' + failed_to_encrypt)

                                    else:
                                        print('\n\t\t(Passwords do not match!)')

                    else:
                        print('\n\t\t' + account_name_error)

                else:
                    print("\n\t\t(Failed to scan existing account names to check if the given account name exists in the database!)")

            print()

        elif commands_options[commands_menu_index] == access_account:

            if len(get_all_account_names()) > 0:

                input_account_name = input('\tAccount Name: ')
                print()

                if input_account_name != cancel_a_command:

                    encrypted_account_name = encrypt(input_account_name)

                    account_info = get_account_info(encrypted_account_name)

                    if len(account_info) > 0:
                        encrypted_username = account_info[0]
                        encrypted_password = account_info[1]

                        decrypted_username = ''

                        if len(encrypted_username) > 0:
                            decrypted_username = decrypt(encrypted_username)

                        decrypted_password = decrypt(encrypted_password)

                        if decrypted_username != failed_to_decrypt and decrypted_password != failed_to_decrypt:
                            if len(decrypted_username) > 0:
                                print('\t\tUsername: ' + decrypted_username)

                            print('\t\tPassword: ' + decrypted_password + '\n')

                        else:
                            print('\t\t' + failed_to_decrypt + '\n')

                    else:
                        print('\t\t' + account_search_failure + '\n')

            else:
                print('\t' + no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == remove_account:

            if len(get_all_account_names()) > 0:

                input_account_name = input('\tAccount Name: ')
                print()

                if input_account_name != cancel_a_command:
                    encrypted_account_name = encrypt(input_account_name)

                    if encrypted_account_name == failed_to_encrypt:
                        print('\t\t' + failed_to_encrypt + '\n')

                    elif remove_account_info(encrypted_account_name) == True:
                        print('\t\t(Account info removed)\n')

                    else:
                        print('\t\t' + account_search_failure + '\n')

            else:
                print('\t' + no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == remove_all_accounts:

            if len(get_all_account_names()) > 0:

                while True:
                    input_confirmation = input('\tConfirm? (Yes or No): ')
                    print()

                    if input_confirmation == 'Yes':
                        remove_all_accounts_info()

                        print("\t\t(All accounts' info is deleted)\n")

                        break

                    elif input_confirmation == 'No' or input_confirmation == cancel_a_command:
                        break

            else:
                print('\t' + no_accounts_found + '\n')



        elif commands_options[commands_menu_index] == access_all_account_names:

            account_names = get_all_account_names()

            if(len(account_names) > 0):

                for i in range(len(account_names)):
                    decrypted_account_name = decrypt(account_names[i])

                    if decrypted_account_name == failed_to_decrypt:
                        print('\t' + str(i + 1) + '. ' + failed_to_decrypt + '\n')

                    else:
                        print('\t' + str(i + 1) + '. ' + decrypted_account_name + '\n')

            else:
                print('\t' + no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == change_account_name_command:
            if len(get_all_account_names()) > 0:

                input_account_name = input('\tAccount Name: ')
                print()

                if len(input_account_name) == 0:
                    print('\t\t' + account_name_required_alert + '\n')

                elif input_account_name != cancel_a_command:

                    encrypted_account_name = encrypt(input_account_name)

                    if encrypted_account_name == failed_to_encrypt:
                        print('\t\t' + failed_to_encrypt + '\n')

                    elif len(get_account_info(encrypted_account_name)) > 0:
                        input_new_account_name = input('\t\tNew Account Name: ')
                        print()

                        if len(input_new_account_name) > 0:

                            if input_new_account_name != cancel_a_command:
                                encrypted_new_account_name = encrypt(input_new_account_name)

                                if encrypted_new_account_name == failed_to_encrypt:
                                    print('\t\t\t' + failed_to_encrypt + '\n')

                                else:
                                    change_account_name(encrypted_account_name, encrypted_new_account_name)

                        else:
                            print('\t\t\t(Account must have a name!)\n')

                    else:
                        print('\t\t' + account_search_failure + '\n')

            else:
                print('\t' + no_accounts_found + '\n')




        elif commands_options[commands_menu_index] == change_username_command:

            if len(get_all_account_names()) > 0:

                input_account_name = input('\tAccount Name: ')
                print()

                if len(input_account_name) == 0:
                    print('\t\t' + account_name_required_alert + '\n')

                elif input_account_name != cancel_a_command:
                    encrypted_account_name = encrypt(input_account_name)

                    if encrypted_account_name == failed_to_encrypt:
                        print('\t\t' + failed_to_encrypt + '\n')

                    elif len(get_account_info(encrypted_account_name)) > 0:
                        input_new_username = input('\t\tNew Username: ')
                        print()

                        if input_new_username != cancel_a_command:
                            if len(input_new_username) > 0:
                                encrypted_new_username = encrypt(input_new_username)

                                change_username(encrypted_account_name, encrypted_new_username)

                            else:
                                change_username(encrypted_account_name, '')

                    else:
                        print('\t\t' + account_search_failure + '\n')

            else:
                print('\t' + no_accounts_found + '\n')





        elif commands_options[commands_menu_index] == change_password_command:

            if len(get_all_account_names()) > 0:

                input_account_name = input('\tAccount Name: ')
                print()

                if len(input_account_name) == 0:
                    print('\t\t' + account_name_required_alert + '\n')

                elif input_account_name != cancel_a_command:
                    encrypted_account_name = encrypt(input_account_name)

                    if encrypted_account_name == failed_to_encrypt:
                        print('\t\t' + failed_to_encrypt + '\n')

                    elif len(get_account_info(encrypted_account_name)) > 0:
                        input_new_password = getpass('\t\tNew Password: ')

                        if len(input_new_password) > 0:

                            if input_new_password != cancel_a_command:
                                input_confirm_new_password = getpass('\t\tConfirm Password: ')
                                print()

                                if input_confirm_new_password != cancel_a_command:

                                    if input_new_password == input_confirm_new_password:
                                        encrypted_new_password = encrypt(input_new_password)

                                        change_password(encrypted_account_name, encrypted_new_password)

                                    else:
                                        print('\t\t\t(Passwords do not match!)\n')

                        else:
                            print('\t\t\t(New password cannot be empty!)\n')


                    else:
                        print('\t\t' + account_search_failure + '\n')

            else:
                print('\t' + no_accounts_found + '\n')



        elif commands_options[commands_menu_index] == change_login_password_command:
            input_current_login_password = getpass('\tEnter current password: ')

            encrypted_current_password = encrypt(input_current_login_password)

            if encrypted_current_password == failed_to_encrypt:
                print('\t\t' + failed_to_encrypt + '\n')

            else:
                if encrypted_current_password == get_password_keeper_info(2):
                    input_new_password = getpass('\tEnter new password: ')

                    if len(input_new_password) > 0:
                        input_confirm_new_password = getpass('\tConfirm Password: ')

                        if input_new_password == input_confirm_new_password:
                            encrypted_new_password = encrypt(input_new_password)

                            change_password_keeper_info(2, encrypted_new_password)

                        else:
                            print('\t\t(Passwords do not match!)\n')

                    else:
                        print('\t\t(Must enter a password!)\n')

                else:
                    print('\t\t(Password entered is incorrect!)\n')


        elif commands_options[commands_menu_index] == close_program:
            break



        else:
            print('\t(Invalid Command!)\n')
