import numpy as np


def assert_image(image_array):
    if image_array.ndim != 3:
        raise ValueError("Wrong Image Array, check image dimensionality.")
    if image_array.shape[2] != 3:
        raise ValueError("Wrong Image Array, check image RGB channels.")


def check_kernel(kernel):
    if kernel.ndim != 2:
        raise ValueError("Kernel must be a 2D array.")
    if kernel.shape[0] != kernel.shape[1]:
        raise ValueError("Kernel must be square.")
    if kernel.shape[0] % 2 == 0:
        raise ValueError("Kernel size must be odd.")


def zero_pad_image_slow(image_array, pad):
    assert_image(image_array)
    height, width, channels = image_array.shape
    padded = np.zeros((height + 2 * pad, width + 2 * pad, channels), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                padded[y + pad, x + pad, c] = image_array[y, x, c]

    return padded


def zero_pad_image_fast(image_array, pad):
    assert_image(image_array)
    return np.pad(image_array, ((pad, pad), (pad, pad), (0, 0)), mode="constant")
