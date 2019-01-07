'''
    Nicole Binder 10 November 2018
    Program extracts a hidden message from an image.
'''
import sys
from PIL import Image

def get_hidden_message(image):
    hidden_message = ''
    binary_message = ''
    binary_letter = ''
    digit_count = 0
    image_width = image.size[0]
    image_height = image.size[1]
    pixels = image.load()
    rotated_image = Image.new("RGB", (image_height, image_width))
    rotated_pixels = rotated_image.load()
    for y in range(image_height):
        for x in range(image_width):
            blue = pixels[x , y][2]
            if blue % 2 == 0:
                binary_message += '0'
            else:
                binary_message += '1'
    for digit in binary_message:
        binary_letter += digit
        digit_count += 1
        if digit_count == 8:
            if binary_letter == '00000000':
                break
            else:
                hidden_message += reveal_message(binary_letter)
            digit_count = 0
            binary_letter = ''
    return hidden_message

def reveal_message(binary_letter):
    '''Takes 8 digit string of Binary ASCII Code and converts to letter
    (Note that I know there is module that can do this but I
    was having difficulty getting the right data types)'''
    hidden_message = ''
    if binary_letter == '10000000':
        hidden_message += ' '
    if binary_letter == '01100001':
        hidden_message += 'a'
    if binary_letter == '01100010':
        hidden_message += 'b'
    if binary_letter == '01100011':
        hidden_message += 'c'
    if binary_letter == '01100100':
        hidden_message += 'd'
    if binary_letter == '01100101':
        hidden_message += 'e'
    if binary_letter == '01100110':
        hidden_message += 'f'
    if binary_letter == '01100111':
        hidden_message += 'g'
    if binary_letter == '01101000':
        hidden_message += 'h'
    if binary_letter == '01101001':
        hidden_message += 'i'
    if binary_letter == '01101010':
        hidden_message += 'j'
    if binary_letter == '01101011':
        hidden_message += 'k'
    if binary_letter == '01101100':
        hidden_message += 'l'
    if binary_letter == '01101101':
        hidden_message += 'm'
    if binary_letter == '01101110':
        hidden_message += 'n'
    if binary_letter == '01101111':
        hidden_message += 'o'
    if binary_letter == '01110000':
        hidden_message += 'p'
    if binary_letter == '01110001':
        hidden_message += 'q'
    if binary_letter == '01110010':
        hidden_message += 'r'
    if binary_letter == '01110011':
        hidden_message += 's'
    if binary_letter == '01110100':
        hidden_message += 't'
    if binary_letter == '01110101':
        hidden_message += 'u'
    if binary_letter == '01110110':
        hidden_message += 'v'
    if binary_letter == '01110111':
        hidden_message += 'w'
    if binary_letter == '01111000':
        hidden_message += 'x'
    if binary_letter == '01111001':
        hidden_message += 'y'
    if binary_letter == '01111010':
        hidden_message += 'z'
    if binary_letter == '01000001':
        hidden_message += 'A'
    if binary_letter == '01000010':
        hidden_message += 'B'
    if binary_letter == '01000011':
        hidden_message += 'C'
    if binary_letter == '01000100':
        hidden_message += 'D'
    if binary_letter == '01000101':
        hidden_message += 'E'
    if binary_letter == '01000110':
        hidden_message += 'F'
    if binary_letter == '01000111':
        hidden_message += 'G'
    if binary_letter == '01001000':
        hidden_message += 'H'
    if binary_letter == '01001001':
        hidden_message += 'I'
    if binary_letter == '01001010':
        hidden_message += 'J'
    if binary_letter == '01001011':
        hidden_message += 'K'
    if binary_letter == '01001100':
        hidden_message += 'L'
    if binary_letter == '01001101':
        hidden_message += 'M'
    if binary_letter == '01001110':
        hidden_message += 'N'
    if binary_letter == '01001111':
        hidden_message += 'O'
    if binary_letter == '01010000':
        hidden_message += 'P'
    if binary_letter == '01010001':
        hidden_message += 'Q'
    if binary_letter == '01010010':
        hidden_message += 'R'
    if binary_letter == '01010011':
        hidden_message += 'S'
    if binary_letter == '01010100':
        hidden_message += 'T'
    if binary_letter == '01010101':
        hidden_message += 'U'
    if binary_letter == '01010110':
        hidden_message += 'V'
    if binary_letter == '01010111':
        hidden_message += 'W'
    if binary_letter == '01011000':
        hidden_message += 'X'
    if binary_letter == '01011001':
        hidden_message += 'Y'
    if binary_letter == '01011010':
        hidden_message += 'Z'
    return hidden_message

def main():
    if len(sys.argv) != 2:
        print('Usage: {0} imagefile'.format(sys.argv[0]))
        exit()

    image_file_name = sys.argv[1]
    if '.' in image_file_name:
        index_of_last_dot = image_file_name.rfind('.')
        image_file_base_name = image_file_name[:index_of_last_dot]
    else:
        image_file_base_name = image_file_name

    image = Image.open(image_file_name)

    message = get_hidden_message(image)
    print(message)
main()
