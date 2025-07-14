import time
from pixelate.slow.pixel_ops import adjust_brightness_slow
from pixelate.fast.pixel_ops import adjust_brightness_fast
from pixelate.utils.image_io import load_image

image = load_image("data/test_image.jpg")
brightness_factor = 40

start = time.perf_counter()
result_slow = adjust_brightness_slow(image, brightness_factor)
end = time.perf_counter()
print("Slow version time:", end - start)

start = time.perf_counter()
result_fast = adjust_brightness_fast(image, brightness_factor)
end = time.perf_counter()
print("Fast version time:", end - start)
