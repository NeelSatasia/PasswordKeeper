from datamanager import *
from getpass import getpass
import random

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

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '/', ' ']

while True:

    input_command = input('Enter a commmand: ')
    print()

    if input_command ==  add_account:

        input_account_name = input('\tAccount Name: ')

        account_name_valid = True
        account_name_error = ''

        for account_name in get_all_account_names():
            if account_name == input_account_name:
                account_name_valid = False
                account_name_error = '(Account name already exists!)'
                break

        if account_name_valid == True and len(input_account_name) == 0:
            account_name_valid = False
            account_name_error = '(Must have an account name!)'

        if account_name_valid == True:
            input_username = input('\tUsername: ')
            input_password = getpass('\tPassword (Hidden): ')
            input_confirm_password = getpass('\tConfirm Password: ')

            if input_password == input_confirm_password:
                duplicate_password = []
                characters_fake_or_not = []

                for character in input_password:
                    duplicate_password.append(character)
                    characters_fake_or_not.append(True)

                fake_characters_size = random.randrange(1, 5)

                for i in range(fake_characters_size):
                    random_character = random.choice(characters)
                    random_index = random.randrange(len(duplicate_password))
                    duplicate_password.insert(random_index, random_character)
                    characters_fake_or_not.insert(random_index, False)

                encrypted_password = ''

                for character in duplicate_password:
                    encrypted_password += character

                encrypted_key = ''
                nums_key = ''

                for character_index in range(len(encrypted_password)):
                    encrypted_character_size = random.randrange(5, 10)
                    encrypted_key_for_character = ''

                    if characters_fake_or_not[character_index] == True:
                        num_key_for_character = characters.index(duplicate_password[character_index])

                    else:
                        num_key_for_character = -1

                    for i in range(encrypted_character_size):
                        random_character = random.choice(characters)
                        encrypted_key_for_character += random_character
                        num_key_for_character += characters.index(random_character)

                    encrypted_key += encrypted_key_for_character

                    num_to_str_key = str(num_key_for_character)
                    nums_key += num_to_str_key

                    if character_index < len(encrypted_password) - 1:
                        encrypted_key += ','
                        nums_key += ','

                add_row(input_account_name, input_username, encrypted_key, nums_key)

            else:
                print('\n\t\t(Password does not match!)')

            print()

        else:
            print('\n\t\t' + account_name_error + '\n')



    elif input_command == access_account:

        input_account_name = input('\tAccount Name: ')

        account_info = get_account_info(input_account_name)

        if len(account_info) > 0:
            username = account_info[0]
            key_list = account_info[1].split(',')
            nums_list = account_info[2].split(',')

            decrypt_password = ''

            for i in range(len(key_list)):
                convert_to_num = int(nums_list[i])

                for character in key_list[i]:
                    convert_to_num -= characters.index(character)

                if convert_to_num >= 0:
                    decrypt_password += characters[convert_to_num]

            print()

            if len(username) > 0:
                print('\t\tUsername: ' + username)

            print('\t\tPassword: ' + decrypt_password + '\n')

        else:
            print('\n\t\t(No such account name exists!)\n')

    elif input_command == close_program:
        break
