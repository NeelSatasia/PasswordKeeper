from datamanager import *
from getpass import getpass
import os
import random

create_database()

show_commands = '/show commands'
add_account = '/add'
remove_account = '/remove'
remove_all_accounts = '/remove all'
access_account = '/access'
access_all_account_names = '/access account names'
change_account_name_command = '/change account name'
change_username_command = '/change username'
change_password_command = '/change password'
cancel_a_command = '/cancel'
close_program = '/close'

def show_all_commands():
    print('\n\nCommands:\n')

    print('\tAdd an account:                  ' + add_account)
    print('\tRemove an account:               ' + remove_account)
    print('\tRemove all accounts:             ' + remove_all_accounts)
    print('\tAccess an account:               ' + access_account)
    print('\tAccess all account names:        ' + access_all_account_names)
    print('\tChange account name:             ' + change_account_name_command)
    print('\tChange username of an account:   ' + change_username_command)
    print('\tChange password of an account:   ' + change_password_command)
    print('\tExit from current command:       ' + cancel_a_command)
    print('\tClose program:                   ' + close_program)

show_all_commands()

print()

failed_to_encrypt = '(Failed to encrypt!)'
failed_to_decrypt = '(Failed to decrypt!)'
account_search_failure = '(Account name does not exist or the encryption key is wrong!)'
account_name_required_alert = '(Must have an account name!)'
no_accounts_found = "(There're currently no accounts!)"

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '/', '?', '-', '_', '+', '=', ' ']

encryption_key = []


if len(get_encryption_key_info()) == 0:
    for character in characters:
        encryption_key.append(character)

    random.shuffle(encryption_key)

    encrypted_key = ''

    for encrypted_character_index in range(len(encryption_key)):
        encrypted_key += (' ' * (characters.index(encryption_key[encrypted_character_index]) + 1))

        if encrypted_character_index < len(encryption_key) - 1:
            encrypted_key += '\t'

    add_encryption_key(encrypted_key)

else:
    uploaded_encrypted_key = get_encryption_key_info()

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




while True:

    input_command = input('Enter a commmand: ')
    print()

    if input_command ==  add_account:

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
                    input_username = input('\tUsername: ')

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

    elif input_command == access_account:

        if len(get_all_account_names()) > 0:

            input_account_name = input('\tAccount Name: ')
            print()

            if input_account_name != cancel_a_command:

                encrypted_account_name = encrypt(input_account_name)

                account_info = get_account_info(encrypted_account_name)

                if len(account_info) > 0:
                    encrypted_username = account_info[0]
                    encrypted_password = account_info[1]

                    decrypted_username = decrypt(encrypted_username)
                    decrypted_password = decrypt(encrypted_password)

                    if decrypted_username != failed_to_decrypt and decrypted_password != failed_to_decrypt:
                        if len(decrypted_username) > 0:
                            print('\t\tUsername: ' + decrypted_username)

                        print('\t\tPassword: ' + decrypted_password + '\n')

                        print('\t\t(If the password is not correct when you used it to login then the encryption key must be wrong!)\n')

                    else:
                        print('\t\t' + failed_to_decrypt + '\n')

                else:
                    print('\t\t' + account_search_failure + '\n')

        else:
            print('\t' + no_accounts_found + '\n')




    elif input_command == remove_account:

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




    elif input_command == remove_all_accounts:

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



    elif input_command == access_all_account_names:

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




    elif input_command == change_account_name_command:
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




    elif input_command == change_username_command:

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





    elif input_command == change_password_command:
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



    elif input_command == show_commands:
        show_all_commands()



    elif input_command == close_program:
        break



    else:
        print('\t(Invalid Command!)\n')
