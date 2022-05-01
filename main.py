from datamanager import *
from getpass import getpass
import random

create_table()

print('\nCommands:\n')

print('\tAdd An Account:             /add')
print('\tRemove An Account:          /remove')
print('\tRemove All Accounts:        /remove all')
print('\tAccess An Account:          /access')
print('\tAccess All Account Names:   /access account names')
print('\tClose Program:              /close')

print()

add_account = '/add'
remove_account = '/remove'
remove_all_accounts = '/remove all'
access_account = '/access'
access_all_account_names = '/access account names'
close_program = '/close'

failed_to_encrypt = '(Failed to encrypt!)'
failed_to_decrypt = '(Failed to decrypt!)'
account_search_failure = '(Account name does not exist or the encryption key is wrong!)'

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

input_encryption_key = input("Enter Encryption Key: ")
print()

encryption_key = []

for character in input_encryption_key:
    encryption_key.append(character)

    if character in letters:
        encryption_key.append(character.upper())

encryted_characters = []

for character_index in range(len(encryption_key)):
    encryted_characters.append(' ' * (character_index + 1))



def encrypt(text):
    text_characters = []

    for text_character in text:
        text_characters.append(text_character)

    encrypted_text = ''

    try:
        for i in range(len(text_characters)):
            encrypted_text += encryted_characters[encryption_key.index(text_characters[i])]

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
                account_name_error = '(Must have an account name!)'

            if account_name_valid == True:
                input_username = input('\tUsername: ')
                input_password = getpass('\tPassword (Hidden): ')
                input_confirm_password = getpass('\tConfirm Password: ')

                if input_password == input_confirm_password:
                    encrypted_accountname = encrypt(input_account_name)
                    encrypted_username = encrypt(input_username)
                    encrypted_password = encrypt(input_password)

                    if encrypted_accountname != failed_to_encrypt and encrypted_username != failed_to_encrypt and encrypted_password != failed_to_encrypt:
                        add_row(encrypted_accountname, encrypted_username, encrypted_password)

                    else:
                        print('\n\t\t' + failed_to_encrypt)

                else:
                    print('\n\t\t(Password does not match!)')

                print()

            else:
                print('\n\t\t' + account_name_error + '\n')

        else:
            print("\t\t(Failed to scan existing account names to check if the given account name exists in the database!)\n")



    elif input_command == access_account:

        input_account_name = input('\tAccount Name: ')

        encrypted_account_name = encrypt(input_account_name)

        account_info = get_account_info(encrypted_account_name)

        if len(account_info) > 0:
            encrypted_username = account_info[0]
            encrypted_password = account_info[1]

            decrypted_username = decrypt(encrypted_username)
            decrypted_password = decrypt(encrypted_password)

            print()

            if decrypted_username != failed_to_decrypt and decrypted_password != failed_to_decrypt:
                if len(decrypted_username) > 0:
                    print('\t\tUsername: ' + decrypted_username)

                print('\t\tPassword: ' + decrypted_password + '\n')

                print('\t\t(If the password is not correct when you used it to login then the encryption key must be wrong!)\n')

            else:
                print('\t\t' + failed_to_decrypt + '\n')

        else:
            print('\n\t\t' + account_search_failure + '\n')




    elif input_command == remove_account:

        input_account_name = input('\tAccount Name: ')
        print()

        encrypted_account_name = encrypt(input_account_name)

        if encrypted_account_name == failed_to_encrypt:
            print('\t\t' + failed_to_encrypt + '\n')

        elif remove_account_info(encrypted_account_name) == True:
            print('\t\t(Account info removed)\n')

        else:
            print('\t\t' + account_search_failure + '\n')





    elif input_command == remove_all_accounts:

        while True:
            input_confirmation = input('\tConfirm? (Yes or No): ')
            print()

            if input_confirmation == 'Yes':
                remove_all_accounts_info()

                print("\t\t(All accounts' info is deleted)\n")

                break

            elif input_confirmation == 'No':
                print()
                break



    elif input_command == access_all_account_names:

        account_names = get_all_account_names()

        if(len(account_names) > 0):

            for i in range(len(account_names)):
                print(str(i + 1) + '. ' + account_names[i] + '\n')

        else:
            print('\t(0 accounts found!)\n')


    elif input_command == close_program:
        break



    else:
        print('\t(Invalid Command!)\n')
