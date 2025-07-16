import numpy as np
from pixelate.slow.transformations import resize_nearest_neighbor_slow
from pixelate.fast.transformations import resize_nearest_neighbor_fast


def test_resize_nearest_neighbor_up_and_down_fast_and_slow():
    original = np.array(
        [[[10, 20, 30], [40, 50, 60]], [[70, 80, 90], [100, 110, 120]]], dtype=np.uint8
    )

    up_slow = resize_nearest_neighbor_slow(original, 4, 4)
    up_fast = resize_nearest_neighbor_fast(original, 4, 4)

    assert np.array_equal(up_slow, up_fast)
    assert np.all(up_fast[0:2, 0:2] == original[0, 0])
    assert np.all(up_fast[0:2, 2:4] == original[0, 1])
    assert np.all(up_fast[2:4, 0:2] == original[1, 0])
    assert np.all(up_fast[2:4, 2:4] == original[1, 1])

    down_slow = resize_nearest_neighbor_slow(original, 1, 1)
    down_fast = resize_nearest_neighbor_fast(original, 1, 1)

    assert down_slow.shape == (1, 1, 3)
    assert down_fast.shape == (1, 1, 3)
    assert np.array_equal(down_slow, down_fast)
    assert np.array_equal(down_fast[0, 0], original[0, 0])
