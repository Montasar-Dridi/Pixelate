from pixelate.fast.pixel_ops import invert_color_fast
from pixelate.utils.image_io import load_image, save_image

image = load_image("data/test_image.jpg")
result = invert_color_fast(image)
save_image(result, "data/try.jpg")
