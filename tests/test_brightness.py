import numpy as np
from pixelate.slow.pixel_ops import adjust_brightness_slow
from pixelate.fast.pixel_ops import adjust_brightness_fast


def test_adjust_brightness_both_versions():
    dummy_image = np.array(
        [[[100, 150, 200], [50, 60, 70]], [[255, 0, 128], [30, 40, 50]]], dtype=np.uint8
    )

    brightness_factor = 30

    expected = np.array(
        [[[130, 180, 230], [80, 90, 100]], [[255, 30, 158], [60, 70, 80]]],
        dtype=np.uint8,
    )

    result_slow = adjust_brightness_slow(dummy_image, brightness_factor)
    result_fast = adjust_brightness_fast(dummy_image, brightness_factor)

    assert np.array_equal(result_slow, expected)
    assert np.array_equal(result_fast, expected)
