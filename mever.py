import numpy as np
import cv2
from PIL import Image
import imageio

text = 'hello'
# Loop through image filenames (assuming consistent naming)
for i in range(1, 5):
    image_path = f"image/3{i}.jpeg"  # Use f-string for clear path generation

    # Read the image
    img = cv2.imread(image_path)

    # Check if image is read successfully
    if img is None:
        print(f"Error: Could not read 3 {image_path}")
        continue  # Skip to the next iteration if image fails to load

    # Add text to the image
    cv2.putText(img, text, (300, 300), cv2.FONT_ITALIC, 10, (32, 178, 170), 10)

    # Display the result
    cv2.imshow('Result', img)

    # Save the modified image
    output_path = f"res{i+1}.jpeg"  # Use f-string for clear output path generation
    cv2.imwrite(output_path, img)

    # Wait for a key press to close the window
    cv2.waitKey(0)

# Logic for creating GIF is removed (GIF creation can be done with external tools)

print("Image processing complete!")  # Added message after processing loop
gif_frames = []

for i in range(1, 5):
    image_path = f"res{i}.jpeg"
    gif_frames.append(imageio.imread(image_path))

imageio.mimsave('processed_images.gif', gif_frames, fps=10)  # Adjust FPS as needed

print("Image processing and GIF creation complete!")
