import numpy as np
from pixelate.slow.filters import convolve_slow
from pixelate.fast.filters import convolve_rgb_fast


def test_convolve_rgb_slow_and_fast_same_output_and_shape():
    image = np.random.randint(0, 256, (10, 10, 3), dtype=np.uint8)
    kernel = np.ones((3, 3)) / 9

    result_slow = convolve_slow(image, kernel)
    result_fast = convolve_rgb_fast(image, kernel)

    assert result_fast.shape == result_slow.shape
    assert result_fast.dtype == result_slow.dtype

    diff = np.abs(result_fast.astype(int) - result_slow.astype(int))
    assert np.max(diff) <= 1

    assert result_fast.min() >= 0 and result_fast.max() <= 255
