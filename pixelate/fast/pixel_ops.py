from pixelate.utils.helpers import assert_image
import numpy as np


def invert_color_fast(image_array):
    assert_image(image_array)
    return 255 - image_array


def to_grayscale_fast(image_array):
    assert_image(image_array)
    weights = np.array([0.299, 0.587, 0.114], dtype=float)

    gray_f = (image_array * weights).sum(axis=2)
    gray = np.rint(gray_f)
    gray = np.clip(gray, 0, 255).astype(np.uint8)

    gray_rgb = np.stack([gray, gray, gray], axis=-1)

    return gray_rgb


def adjust_brightness_fast(image_array, brightness_factor):
    assert_image(image_array)

    brightened_array = image_array.astype(np.int16) + brightness_factor
    brightened_array = np.clip(brightened_array, 0, 255).astype(np.uint8)

    return brightened_array
