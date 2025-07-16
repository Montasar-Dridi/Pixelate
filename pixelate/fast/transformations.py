from pixelate.utils.helpers import assert_image
import numpy as np


def flip_horizontal_fast(image_array):
    assert_image(image_array)
    return image_array[:, ::-1, :]


def resize_nearest_neighbor_fast(image_array, new_height, new_width):
    assert_image(image_array)

    original_height, original_width = image_array.shape[:2]

    scale_y = original_height / new_height
    scale_x = original_width / new_width

    original_y = (np.arange(new_height) * scale_y).astype(int)
    original_x = (np.arange(new_width) * scale_x).astype(int)

    original_y = np.clip(original_y, 0, original_height - 1)
    original_x = np.clip(original_x, 0, original_width - 1)

    resized = image_array[original_y[:, None], original_x[None, :]]

    return resized
