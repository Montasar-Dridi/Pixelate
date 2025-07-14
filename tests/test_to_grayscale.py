import numpy as np
import cv2
from pixelate.slow.pixel_ops import to_grayscale_slow
from pixelate.fast.pixel_ops import to_grayscale_fast


def test_to_grayscale_slow_and_fast_vs_opencv():
    img = np.random.randint(0, 256, (20, 20, 3), dtype=np.uint8)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    expected = np.stack([gray, gray, gray], axis=-1)

    out_slow = to_grayscale_slow(img)
    assert out_slow.shape == expected.shape, f"slow shape {out_slow.shape}"
    np.testing.assert_allclose(
        out_slow,
        expected,
        atol=1,
        err_msg="to_grayscale_slow deviates from OpenCV by more than 1",
    )

    out_fast = to_grayscale_fast(img)
    assert out_fast.shape == expected.shape, f"fast shape {out_fast.shape}"
    np.testing.assert_allclose(
        out_fast,
        expected,
        atol=1,
        err_msg="to_grayscale_fast deviates from OpenCV by more than 1",
    )
