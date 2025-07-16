import numpy as np
from pixelate.utils.helpers import assert_image


def flip_horizontal_slow(image_array):
    assert_image(image_array)
    height = image_array.shape[0]
    width = image_array.shape[1]

    flipped = np.zeros((height, width, 3), dtype=np.uint8)

    for h in range(height):
        for w in range(width):
            flipped[h, w] = image_array[h, width - 1 - w]

    return flipped


def resize_nearest_neighbor_slow(image_array, new_height, new_width):
    assert_image(image_array)
    original_height = image_array.shape[0]
    original_width = image_array.shape[1]

    resized = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    scale_y = original_height / new_height
    scale_x = original_width / new_width

    for y in range(new_height):
        for x in range(new_width):
            original_y = int(y * scale_y)
            original_x = int(x * scale_x)

            original_x = max(0, min(original_x, original_width - 1))
            original_y = max(0, min(original_y, original_height - 1))

            resized[y, x] = image_array[original_y, original_x]

    return resized
