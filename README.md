# Pixelate
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)

Pixelate is an educational image processing library built to compare naive loop-based algorithms with their vectorized NumPy counterparts. Each operation has a `slow` and `fast` implementation so you can explore the performance and readability differences between the two styles.

## Features

- **Pixel Operations**: invert colors, convert to grayscale, and adjust brightness.
- **Geometric Transformations**: horizontal flip and nearest-neighbor resize.
- **Convolution Filters** for applying arbitrary kernels.
- **Utilities** for loading and saving images via Pillow.
- Ready-to-run **benchmarks** and **tests** demonstrating correctness and speed differences.

The modules are organized so that every function has a matching fast (vectorized) and slow (naive) version:

```
pixelate/
  fast/
    filters.py
    pixel_ops.py
    transformations.py
  slow/
    filters.py
    pixel_ops.py
    transformations.py
  utils/
    helpers.py
    image_io.py
```

## Installation

Clone the repository and install the requirements:

```bash
pip install -r requirements.txt
```

You can also install the package directly:

```bash
pip install pixelate
```

The project requires Python 3.10 or newer.

## Usage Example

```python
import numpy as np
from pixelate.fast.pixel_ops import invert_color_fast
from pixelate.slow.pixel_ops import invert_color_slow
from pixelate.utils.image_io import load_image, save_image

img = load_image("path/to/image.png")

# Compare slow and fast implementations
slow_result = invert_color_slow(img)
fast_result = invert_color_fast(img)

save_image(fast_result, "out_fast.png")
```

Check the `benchmarks/` folder for scripts that measure execution time for the slow and fast versions of each operation.

## Running Tests

Use `pytest` to run the unit tests:

```bash
pytest
```

## License

Pixelate is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.
