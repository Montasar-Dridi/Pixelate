import time
from pixelate.utils.image_io import load_image
from pixelate.slow.transformations import resize_nearest_neighbor_slow
from pixelate.fast.transformations import resize_nearest_neighbor_fast


image = load_image("data/test_image.jpg")

new_height = image.shape[0] // 2
new_width = image.shape[1] // 2


start_slow = time.time()
resized_slow = resize_nearest_neighbor_slow(image, new_height, new_width)
end_slow = time.time()
print(f"Slow resize took: {end_slow - start_slow:.6f} seconds")

start_fast = time.time()
resized_fast = resize_nearest_neighbor_fast(image, new_height, new_width)
end_fast = time.time()
print(f"Fast resize took: {end_fast - start_fast:.6f} seconds")
