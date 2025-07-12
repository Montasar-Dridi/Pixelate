from PIL import Image
import numpy as np
import os


def load_image(image_path):
    image_array = np.asarray(Image.open(str(image_path)))
    return image_array


def save_image(image_array, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image = Image.fromarray(image_array)
    image.save(str(output_path))
