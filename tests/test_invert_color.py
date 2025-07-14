from pixelate.slow.pixel_ops import invert_color_slow
from pixelate.fast.pixel_ops import invert_color_fast
import time
import numpy as np


def test_invert_color_slow_fast():
    dummy_image = np.random.randint(0, 256, (200, 200, 3), dtype=np.uint8)

    start_time_slow = time.time()
    result_slow = invert_color_slow(dummy_image)
    end_time_slow = time.time()
    slow_duration = end_time_slow - start_time_slow

    start_time_fast = time.time()
    result_fast = invert_color_fast(dummy_image)
    end_time_fast = time.time()
    fast_duration = end_time_fast - start_time_fast

    print(f"Slow version duration: {slow_duration:.6f} seconds")
    print(f"Fast version duration: {fast_duration:.6f} seconds")

    assert fast_duration < slow_duration, "Fast version is not faster than slow version"

    assert np.array_equal(result_slow, result_fast), (
        "Results of slow and fast versions are not the same"
    )
