from pixelate.utils.image_io import load_image, save_image
import numpy as np
import time


def test_save_and_load_image(tmp_path):
    TEST_PATH = tmp_path / "test_image.png"

    dummy_image = np.random.randint(0, 256, (50, 50, 3), dtype=np.uint8)

    start_time_save = time.time()
    save_image(dummy_image, TEST_PATH)
    end_time_save = time.time()

    start_time_load = time.time()
    loaded_image = load_image(TEST_PATH)
    end_time_load = time.time()

    print(f"Time taken to save the image {end_time_save - start_time_save}")
    print(f"Time taken to load the image {end_time_load - start_time_load}")
    assert loaded_image.shape == dummy_image.shape
    assert np.array_equal(loaded_image, dummy_image)
