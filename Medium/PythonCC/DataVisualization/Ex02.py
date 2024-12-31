# 02. Converting Images to Grayscale
from PIL import Image
import numpy as np
import requests
from io import BytesIO

# URL of the image
image_url = 'https://images.pexels.com/photos/1181671/pexels-photo-1181671.jpeg'

# Fetch the image from the URL
response = requests.get(image_url)
if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
else:
    raise Exception(f"Failed to fetch image. HTTP Status Code: {response.status_code}")

# Convert the image to a NumPy array
image_array = np.array(image)

# Convert to grayscale using weighted average
gray_image = np.dot(image_array[..., :3], [0.2989, 0.5870, 0.1140])

# Save the grayscale image
gray_image = Image.fromarray(gray_image.astype(np.uint8))
gray_image.save('example_grayscale.jpg')

print("Grayscale image saved as 'example_grayscale.jpg'")