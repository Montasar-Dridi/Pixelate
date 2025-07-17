import time
from pixelate.slow.transformations import flip_horizontal_slow
from pixelate.fast.transformations import flip_horizontal_fast
from pixelate.utils.image_io import load_image


image = load_image("data/test_image.jpg")


start_slow = time.time()
flipped_slow = flip_horizontal_slow(image)
end_slow = time.time()
print(f"Slow flip time: {end_slow - start_slow:.6f} seconds")


start_fast = time.time()
flipped_fast = flip_horizontal_fast(image)
end_fast = time.time()
print(f"Fast flip time: {end_fast - start_fast:.6f} seconds")
