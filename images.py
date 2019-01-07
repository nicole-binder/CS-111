'''
    images.py

    Nicole Binder, 1 November 2018

    An image processing program adapted from code by Jeff Ondich

'''

import sys
from PIL import Image

def get_green_image(original_image):
    ''' Returns a copy of the specified image with all the red and blue removed. '''
    green_image = original_image.copy()
    green_pixels = green_image.load()
    image_width = green_image.size[0]
    image_height = green_image.size[1]
    for row in range(image_height):
        for column in range(image_width):
            green_value = green_pixels[column, row][1]
            green_pixels[column, row] = (0, green_value, 0)

    return green_image

def get_small_image(original_image):
    ''' Returns a copy of the specified image, scaled to half size both
       horizontally and vertically. '''
    small_image_width = original_image.size[0] // 2
    small_image_height = original_image.size[1] // 2
    originalPixels = original_image.load()
    small_image = Image.new("RGB", (small_image_width, small_image_height))
    small_image_pixels = small_image.load()
    for y in range(small_image_height):
        for x in range(small_image_width):
            red = (originalPixels[2*x, 2*y][0] + originalPixels[2*x + 1, 2*y][0]\
                    + originalPixels[2*x, 2*y + 1][0] + originalPixels[2*x + 1, 2*y + 1][0]) // 4
            green = (originalPixels[2*x, 2*y][1] + originalPixels[2*x + 1, 2*y][1]\
                    + originalPixels[2*x, 2*y + 1][1] + originalPixels[2*x + 1, 2*y + 1][1]) // 4
            blue = (originalPixels[2*x, 2*y][2] + originalPixels[2*x + 1, 2*y][2]\
                    + originalPixels[2*x, 2*y + 1][2] + originalPixels[2*x + 1, 2*y + 1][2]) // 4
            small_image_pixels[x, y] = (red, green, blue)

    return small_image

def get_black_and_white_image(original_image):
    ''' Returns a copy of the specified image in black and white--or as the
        average color of the red, green, and blue in each pixel. '''

    black_and_white_image = original_image.copy()
    black_and_white_pixels = black_and_white_image.load()
    image_width = black_and_white_image.size[0]
    image_height = black_and_white_image.size[1]
    for row in range(image_height):
        for column in range(image_width):
            black_and_white_value = int((black_and_white_pixels[column, row][0] + black_and_white_pixels[column, row][1]
                                         + black_and_white_pixels[column, row][2])/3)
            black_and_white_pixels[column, row] = (black_and_white_value, black_and_white_value, black_and_white_value)
    return black_and_white_image

def get_mirror_image(original_image):
    ''' Returns a copy of the specified image, reflected horizontally. '''
    original_image_width = original_image.size[0]
    original_image_height = original_image.size[1]
    original_pixels = original_image.load()
    mirror_image = Image.new("RGB", (original_image_width, original_image_height))
    mirror_pixels = mirror_image.load()
    for y in range(original_image_height):
        z = original_image_width
        for x in range(original_image_width ):
            red = original_pixels[z - 1 ,y][0]
            green = original_pixels[z - 1,y][1]
            blue = original_pixels[z - 1,y][2]
            mirror_pixels[x, y] = (red, green, blue)
            z = z - 1
    return mirror_image

def get_rotated_image(original_image):
    ''' Returns a copy of the specified image, rotated clockwise by
        90 degrees.  '''
    original_image_width = original_image.size[0]
    original_image_height = original_image.size[1]
    original_pixels = original_image.load()
    rotated_image = Image.new("RGB", (original_image_height, original_image_width))
    rotated_pixels = rotated_image.load()
    for y in range(original_image_width):
        z = original_image_height
        for x in range(original_image_height):
            red = original_pixels[y, z - 1][0]
            green = original_pixels[y, z - 1][1]
            blue = original_pixels[y, z - 1][2]
            rotated_pixels[x, y] = (red, green, blue)
            z = z - 1
    return rotated_image

def get_bordered_image(original_image, border_color, border_thickness):
    ''' Returns a copy of the specified image, surrounded by a solid
        border of the specified color, with the thickness of the border specified
        by the integer border_thickness. '''
    original_image_width = original_image.size[0]
    original_image_height = original_image.size[1]
    original_pixels = original_image.load()
    bordered_image_height = original_image_height + (2 * border_thickness)
    bordered_image_width = original_image_width  + (2 * border_thickness)
    bordered_image = Image.new("RGB", (bordered_image_width, bordered_image_height))
    bordered_pixels = bordered_image.load()
    for y in range(original_image_height):
        for x in range(original_image_width):
            z = x + border_thickness
            w = y + border_thickness
            red = original_pixels[x , y][0]
            green = original_pixels[x , y][1]
            blue = original_pixels[x , y][2]
            bordered_pixels[z, w] = (red, green, blue)
    for y in range(bordered_image_height):
        for x in range(bordered_image_width):
            if y <= border_thickness - 1:
                bordered_pixels[x,y] = (border_color[0], border_color[1], border_color[2])
            elif (y > border_thickness - 1) and (y < bordered_image_height - border_thickness - 1):
                if x <= border_thickness - 1:
                    bordered_pixels[x,y] = (border_color[0], border_color[1], border_color[2])
                elif x >= bordered_image_width - border_thickness - 1:
                    bordered_pixels[x,y] = (border_color[0], border_color[1], border_color[2])
            else:
                bordered_pixels[x,y] = (border_color[0], border_color[1], border_color[2])

    return bordered_image


def get_tiled_image(original_image, square_width):
    ''' Returns a copy of the specified image, modified as follows.
        Imagine superimposing a chess board, whose squares are of height and width
        given by the squareWidth parameter, on the image. Then, leave the white squares
        alone, but flip the black squares upside-down. '''
    return tiled_image

def get_image_with_fake_scratches(original_image):
    ''' Returns a copy of the specified image with white pixels added stand
        in for "scratches" on the surface of a photograph. '''
    square_width = 50
    original_image = original_image.copy()
    original_pixels = original_image.load()
    scratched_image_width = original_image.size[0]
    scratched_image_height = original_image.size[1]
    scratched_image = Image.new("RGB", (scratched_image_width, scratched_image_height))
    scratched_pixels = scratched_image.load()
    square_count_across = int(scratched_image_width / square_width)
    square_count_down = int(scratched_image_height / square_width)
    for y in range(0, scratched_image_height - 1, square_count_down):
        for x in range(scratched_image_width):
            scratched_pixels[x , y] = (255, 255, 255)
    for y in range(scratched_image_height):
        for x in range(scratched_image_width ):
            if scratched_pixels[x , y] != (255, 255, 255):
                red = original_pixels[x , y][0]
                green = original_pixels[x , y][1]
                blue = original_pixels[x , y][2]
                scratched_pixels[x , y] = (red, green, blue)
    return scratched_image

def get_median_filtered_image(original_image):
    ''' [OPTIONAL] Returns a copy of the specified image with a median filter applied,
        using a 3x3 square neighborhood of each pixel. For each pixel, you will collect the
        set of red values in the neighborhood of the pixel, and use the median of those values
        as the new red value of the pixel. Do the same for the green and blue values. '''
    median_image = original_image.copy()
    median_pixels = median_image.load()
    original_pixels = original_image.load()
    image_width = median_image.size[0]
    image_height = median_image.size[1]
    for y in range(0, image_height - 1):
        for x in range(0, image_width - 1):
            if y == 0:
                if x == 0:
                    red_value = int((median_pixels[x + 1, y][0] + median_pixels[x + 1, y + 1][0] + median_pixels[x, y + 1][0])/3)
                    green_value = int((median_pixels[x + 1, y][1] + median_pixels[x + 1, y + 1][1] + median_pixels[x, y + 1][1])/3)
                    blue_value = int((median_pixels[x + 1, y][2] + median_pixels[x + 1, y + 1][2] + median_pixels[x, y + 1][2])/3)
                    median_pixels[x, y] = (red_value, green_value, blue_value)
                else:
                    red_value = int((median_pixels[x + 1, y][0] + median_pixels[x + 1, y + 1][0] + median_pixels[x, y + 1][0]
                                    + median_pixels[x - 1, y][0] + median_pixels[x - 1, y + 1][0])/5)
                    green_value = int((median_pixels[x + 1, y][1] + median_pixels[x + 1, y + 1][1] + median_pixels[x, y + 1][1]
                                    + median_pixels[x - 1, y][0] + median_pixels[x - 1, y + 1][0])/5)
                    blue_value = int((median_pixels[x + 1, y][2] + median_pixels[x + 1, y + 1][2] + median_pixels[x, y + 1][2]
                                    + median_pixels[x - 1, y][0] + median_pixels[x - 1, y + 1][0])/5)
                    median_pixels[x, y] = (red_value, green_value, blue_value)
            elif x == 0:
                red_value = int((median_pixels[x + 1, y][0] + median_pixels[x + 1, y + 1][0] + median_pixels[x, y + 1][0]
                                + median_pixels[x, y - 1][0] + median_pixels[x + 1, y - 1][0])/5)
                green_value = int((median_pixels[x + 1, y][1] + median_pixels[x + 1, y + 1][1] + median_pixels[x, y + 1][1]
                                + median_pixels[x, y - 1][0] + median_pixels[x + 1, y - 1][0])/5)
                blue_value = int((median_pixels[x + 1, y][2] + median_pixels[x + 1, y + 1][2] + median_pixels[x, y + 1][2]
                                + median_pixels[x, y - 1][0] + median_pixels[x + 1, y - 1][0])/5)
                median_pixels[x, y] = (red_value, green_value, blue_value)
            else:
                red_value = int((median_pixels[x - 1, y - 1][0] + median_pixels[x, y - 1][0] + median_pixels[x - 1, y][0]
                                + median_pixels[x + 1, y + 1][0] + median_pixels[x, y + 1][0] + median_pixels[x + 1, y][0]
                                + median_pixels[x + 1, y - 1][0] + median_pixels[x - 1, y + 1][0])/8)
                green_value = int((median_pixels[x - 1, y - 1][1] + median_pixels[x, y - 1][1] + median_pixels[x - 1, y][1]
                                + median_pixels[x + 1, y + 1][1] + median_pixels[x, y + 1][1] + median_pixels[x + 1, y][1]
                                + median_pixels[x + 1, y - 1][1] + median_pixels[x - 1, y + 1][1])/8)
                blue_value = int((median_pixels[x - 1, y - 1][2] + median_pixels[x, y - 1][2] + median_pixels[x - 1, y][2]
                                + median_pixels[x + 1, y + 1][2] + median_pixels[x, y + 1][2] + median_pixels[x + 1, y][2]
                                + median_pixels[x + 1, y - 1][2] + median_pixels[x - 1, y + 1][2])/8)
                median_pixels[x, y] = (red_value, green_value, blue_value)
    return median_image

def get_green_screened_image(original_image, background_image, green_screen_color, color_radius):
    ''' [OPTIONAL] Returns a copy of the original image with all pixels within the
        specified color range replaced by the background image's corresponding pixel.
        Suppose green_screen_color is (R, G, B). Then a color (r, g, b) should be
        considered to be "within the color range" of (R, G, B) if the Euclidean distance
        between (r, g, b) and (R, G, B) is less than or equal to color_radius. That is,
        (r - R)**2 + (g - G)**2 + (b - B)**2 <= color_radius**2. '''
    return green_screened_image

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
    image.show()

    green_image = get_green_image(image)
    green_image.show()
    green_image.save('{0}.green.jpg'.format(image_file_base_name), 'JPEG')

    small_image = get_small_image(image)
    small_image.show()
    small_image.save('{0}.small.jpg'.format(image_file_base_name), 'JPEG')

    black_and_white_image = get_black_and_white_image(image)
    black_and_white_image.show()
    black_and_white_image.save('{0}.blackandwhite.jpg'.format(image_file_base_name), 'JPEG')

    mirror_image = get_mirror_image(image)
    mirror_image.show()
    mirror_image.save('{0}.mirror.jpg'.format(image_file_base_name), 'JPEG')

    rotated_image = get_rotated_image(image)
    rotated_image.show()
    rotated_image.save('{0}.rotated.jpg'.format(image_file_base_name), 'JPEG')

    bordered_image = get_bordered_image(image, [255, 204, 229], 50)
    bordered_image.show()
    bordered_image.save('{0}.bordered.jpg'.format(image_file_base_name, 'JPEG'))

    scratched_image = get_image_with_fake_scratches(image)
    scratched_image.show()
    scratched_image.save('{0}.scratched.jpg'.format(image_file_base_name, 'JPEG'))

    median_image = get_median_filtered_image(image)
    median_image.show()
    median_image.save('{0}.median.jpg'.format(image_file_base_name, 'JPEG'))

main()
