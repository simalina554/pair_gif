import os

import numpy as np
import cv2
from PIL import Image
import imageio

# Define image directories
 # Directory containing "res" images
image_dir = "image"  # Directory containing "image" images
text='hello'
# Loop through image pairs
for i in range(1, 5):
    res_image_path = os.path.join(f"res{i}.jpeg")
    image_path = os.path.join(image_dir, f"image{i}.jpeg")

    # Check if images exist
    if not os.path.isfile(res_image_path) or not os.path.isfile(image_path):
        print(f"Error: Missing images {res_image_path} or {image_path}")
        continue

    # Read images
    res_img = cv2.imread(res_image_path)
    img = cv2.imread(image_path)

    # Check if images are read successfully
    if res_img is None or img is None:
        print(f"Error: Failed to read images {res_image_path} or {image_path}")
        continue

    # Add text to the "image" image
    cv2.putText(img, text, (300, 300), cv2.FONT_ITALIC, 10, (32, 178, 170), 10)

    # Combine images (replace with your desired processing)
    combined_image = np.hstack((res_img, img))

    # Save the combined image
    combined_image_path = f"combined_{i}.jpeg"
    cv2.imwrite(combined_image_path, combined_image)

# Create GIF from combined images
gif_frames = []

for i in range(1, 5 + 1):
    combined_image_path = f"combined_{i}.jpeg"
    gif_frames.append(imageio.imread(combined_image_path))

imageio.mimsave('processed_images.gif', gif_frames, fps=10)  # Adjust FPS as needed

print("Image processing and GIF creation complete!")
