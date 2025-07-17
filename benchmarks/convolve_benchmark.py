import time
import numpy as np
from pixelate.utils.image_io import load_image, save_image
from pixelate.slow.filters import convolve_slow
from pixelate.fast.filters import convolve_rgb_fast


image = load_image("data/test_image.jpg")


kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])


start_slow = time.time()
result_slow = convolve_slow(image, kernel)
end_slow = time.time()
save_image(result_slow, "data/output/convolve_output.jpg")
print(f"Convolution (slow) took: {end_slow - start_slow:.6f} seconds")


start_fast = time.time()
result_fast = convolve_rgb_fast(image, kernel)
end_fast = time.time()
print(f"Convolution (fast) took: {end_fast - start_fast:.6f} seconds")
