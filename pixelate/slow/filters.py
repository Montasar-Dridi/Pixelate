import numpy as np
from pixelate.utils.helpers import assert_image, check_kernel, zero_pad_image_slow


def convolve_slow(image_array, kernel):
    assert_image(image_array)
    check_kernel(kernel)

    height, width, _ = image_array.shape
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2

    padded = zero_pad_image_slow(image_array, pad)
    output = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            for c in range(3):
                acc = 0.0
                for ky in range(kernel_size):
                    for kx in range(kernel_size):
                        pixel = padded[y + ky, x + kx, c]
                        weight = kernel[ky, kx]
                        acc += pixel * weight

                acc = max(0, min(int(round(acc)), 255))
                output[y, x, c] = acc

    return output
