def assert_image(image_array):
    if image_array.ndim != 3:
        raise ValueError("Wrong Image Array, check image dimensionality.")
    if image_array.shape[2] != 3:
        raise ValueError("Wrong Image Array, check image RGB channels.")
