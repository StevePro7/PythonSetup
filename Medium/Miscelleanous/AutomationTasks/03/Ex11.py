# 11. Automate Image Processing
from PIL import Image


def resize_image(image_path, output_path, size):
    with Image.open(image_path) as img:
        img.resize(size).save(output_path)
