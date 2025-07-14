import time
from pixelate.utils.image_io import save_image, load_image
from pixelate.slow.pixel_ops import to_grayscale_slow
from pixelate.fast.pixel_ops import to_grayscale_fast


image = load_image("data/test_image.jpg")

start_slow = time.time()
result_slow = to_grayscale_slow(image)
duration_slow = time.time() - start_slow
save_image(result_slow, "data/output/grayscale_output.jpg")
print(f"Slow version duration: {duration_slow:.6f} seconds")

start_fast = time.time()
result_fast = to_grayscale_fast(image)
duration_fast = time.time() - start_fast
print(f"Fast version duration: {duration_fast:.6f} seconds")
