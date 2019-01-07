'''
	menu.py

    Nicole Binder 30 September 2018
    This program allows users to choose various string methods
    from a menu.

'''


def print_menu():
    print()
    print('A. How many characters are in the string?')
    print('B. How many letters are in the string?')
    print('C. How many consonants are in the string?')
    print('D. Is the string a palindrome?')
    print('E. What is the Caesar Cipher (shift 3) of the string?')
    print('Q. Quit')

def characters_in_string(message):
    length_string = len(message)
    return length_string

def letters_in_string(message):
    characters = 0
    for k in message:
        if k.isalpha():
            characters = characters + 1
    return characters

def consonants_in_string(message):
    only_letters = ''
    for k in message:
        if k.isalpha():
            only_letters = only_letters + k
    only_consonants = ''
    for p in only_letters:
        if p != 'a' and p !='e' and p !='i' and p !='o' and p !='u':
            only_consonants = only_consonants + p
    return len(only_consonants)


def palindrome(message):
    only_letters = ''
    for k in message:
        if k.isalpha():
            only_letters = only_letters + k
    palindrome_message = ''
    for k in only_letters:
        palindrome_message = k + palindrome_message
    if only_letters == palindrome_message:
        return True
    else:
        return False

def caesar(shift, plaintext):
    ciphertext = ''
    num = 0
    for character in plaintext:
        num = ord(character)
        num = num + shift
        if character >= 'A' and character <= 'Z':
                if num > ord('Z'):
                    num = num - 26
                    ciphertext = ciphertext + chr(num)
                elif num < ord('A'):
                    num = num + 26
                    ciphertext = ciphertext + chr(num)
                else:
                    ciphertext = ciphertext + chr(num)
        elif character >= 'a' and character <= 'z':
                    if num > ord('z'):
                        num = num - 26
                        ciphertext = ciphertext + chr(num)
                    elif num < ord('a'):
                        num = num + 26
                        ciphertext = ciphertext + chr(num)
                    else:
                        ciphertext = ciphertext + chr(num)
        else:
            ciphertext = ciphertext + character
    return ciphertext

def do_operation(response, message):
    if response == ord('a'):
         print('Your string has', characters_in_string(message), 'characters')
    elif response == ord('b'):
        print('Your string has', letters_in_string(message), 'letters')
    elif response == ord('c'):
        print('Your string has', consonants_in_string(message), 'consonants')
    elif response == ord('d'):
        w = palindrome(message)
        if w == True:
            print('Your message is a palindrome')
        else:
            print('Your message is not a palindrome')
    elif response == ord('e'):
        shift = 3
        print('Your Caesar Cipher message is: ', caesar(shift,message))

# main program

done = False
while not done:
    message = input('Please input a string: ')
    print_menu()
    response_letter = input('Your choice: ')
    response = response_letter.casefold()
    response_num = ord(response)
    if response_num == ord('q'):
        done = True
    elif response_num == ord('a'):
        do_operation(response_num, message)
    elif response_num == ord('b'):
        do_operation(response_num, message)
    elif response_num == ord('c'):
        do_operation(response_num, message)
    elif response_num == ord('d'):
        do_operation(response_num, message)
    elif response_num == ord('e'):
        do_operation(response_num, message)
    else:
        print('Letter not valid.')
