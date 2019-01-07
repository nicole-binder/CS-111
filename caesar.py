def caesar_encrypt(shift, plaintext):
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
def caesar_decrypt(shift, plaintext):
    negative_num = -1*shift
    decrypt = caesar_encrypt(negative_num, plaintext)
    return decrypt

message = input('Enter a message you would like to encrypt: ')
change = input('How many letters do you want to shift the message? ')
number = int(change)

encrypted_message = caesar_encrypt(number, message)
print('Your encrypted message is: ', encrypted_message)

decrypted_message = caesar_decrypt(number, encrypted_message)
print('Your decrypted message is: ', decrypted_message)
