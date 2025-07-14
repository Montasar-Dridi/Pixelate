from pixelate.utils.helpers import assert_image
import numpy as np


def invert_color_slow(image_array):
    assert_image(image_array)
    image_array_copy = image_array.copy()

    HEIGHT = image_array_copy.shape[0]
    WIDTH = image_array_copy.shape[1]
    CHANNEL = image_array_copy.shape[2]

    for h in range(HEIGHT):
        for w in range(WIDTH):
            for c in range(CHANNEL):
                image_array[h, w, c] = 255 - image_array_copy[h, w, c]

    return image_array_copy


def to_grayscale_slow(image_array):
    assert_image(image_array)

    HEIGHT = image_array.shape[0]
    WIDTH = image_array.shape[1]

    grayscale_array = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    for h in range(HEIGHT):
        for w in range(WIDTH):
            red = image_array[h][w][0]
            green = image_array[h][w][1]
            blue = image_array[h][w][2]

            gray = int(round(0.299 * red + 0.587 * green + 0.114 * blue))
            gray = max(0, min(255, gray))
            grayscale_array[h, w, 0] = gray
            grayscale_array[h, w, 1] = gray
            grayscale_array[h, w, 2] = gray

    return grayscale_array


def adjust_brightness(image_array, brightness_factor):
    assert_image(image_array)

    HEIGHT = image_array.shape[0]
    WIDTH = image_array.shape[1]
    CHANNEL = image_array.shape[2]

    brightened_array = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    for h in range(HEIGHT):
        for w in range(WIDTH):
            for c in range(CHANNEL):
                brightened_channel = image_array[h, w, c] + brightness_factor
                if brightened_channel > 255:
                    brightened_channel = 255
                elif brightened_channel < 0:
                    brightened_channel = 0
                brightened_array[h, w, c] = brightened_channel

    return brightened_array
