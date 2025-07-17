import numpy as np
from pixelate.utils.helpers import assert_image, check_kernel, zero_pad_image_fast


def convolve_rgb_fast(image_array, kernel):
    assert_image(image_array)
    check_kernel(kernel)

    height, width, _ = image_array.shape
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2

    padded = zero_pad_image_fast(image_array, pad)

    output = np.zeros_like(image_array, dtype=np.float32)
    kernel_flipped = np.flipud(np.fliplr(kernel))

    for c in range(3):
        for ky in range(kernel_size):
            for kx in range(kernel_size):
                output[:, :, c] += (
                    kernel_flipped[ky, kx]
                    * padded[ky : ky + height, kx : kx + width, c]
                )

    return np.clip(output, 0, 255).astype(np.uint8)
