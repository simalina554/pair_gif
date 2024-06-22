import cv2
from PIL import Image
import os
import random

font = cv2.FONT_ITALIC
bottom_margin = 20
text_color = (32, 178, 170)
border_thickness = 2
image_dir = "3/"


def rename_file(original_filename, new_filename):
    # Check if the file exists
    if os.path.exists(f"{image_dir}/{original_filename}"):
        # Rename the file
        os.rename(f"{image_dir}/{original_filename}", f"{image_dir}/{new_filename}")
        print(f"Image renamed: {original_filename} -> {new_filename}")
    else:
        print(f"Error: File not found: {original_filename}")


list12 = os.listdir(image_dir)

for i in list12:
    def random_word():
        with open("question.txt", 'r', encoding="utf-8") as file:
            lines = file.readlines()
        random_lines = random.sample(lines, 1)
        result_string = '|'.join(map(lambda x: x.strip(), random_lines))

        return result_string


    result1 = random_word()
    img = cv2.imread(f"{image_dir}/{i}")
    img_h, img_w = img.shape[:2]
    text_size = cv2.getTextSize(result1, font, 1, border_thickness)[0]
    text_baseline = img_h // 2
    text_start_x = (img_w - text_size[0]) // 2
    text_pos = (text_start_x, text_baseline)
    cv2.putText(img, result1, text_pos, font, 1, text_color, border_thickness)

    # Save the modified image with a new filename (e.g., 'modified_' + i + '.jpg')
    new_filename = "modified_" + i + ".jpeg"  # Replace 'modified_' with your desired prefix
    cv2.imwrite(f"{image_dir}/{new_filename}", img)

def add_text_to_image(image_path):
    # Read image
    img = Image.open(image_path)
    return img

image_folder = "3"
file_count = 0
for filename in os.listdir(image_folder):
    if os.path.isfile(os.path.join(image_folder, filename)):
        file_count += 1

# Set the GIF animation parameters
frame_duration = 0.5  # Duration of each frame in seconds
image_size = (640, 480)  # Size of the GIF animation (width, height)

# Get all image paths in the folder
image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder)
               if filename.endswith('.jpeg')]

# Create image pairs by matching images from the first and second halves
image_pairs = []
for index, image_path in enumerate(image_paths):
    if index < len(image_paths) // 2:
        # Pair with an image from the second half
        pair_index = len(image_paths) // 2 + index
        image_pairs.append((image_path, image_paths[pair_index]))
    else:
        # Pair with an image from the first half
        pair_index = index - len(image_paths) // 2
        image_pairs.append((image_path, image_paths[pair_index]))

# Create GIF animations for each image pair

    for i, image_pair in enumerate(image_pairs):
        frames = []
        for image_path in image_pair:
            try:
                image = Image.open(image_path)
                image = image.resize(image_size)  # Assuming image_size is defined elsewhere
                frames.append(image)
            except PermissionError:
                print(f"Error accessing image: {image_path}")  # Handle permission errors

        # Save the GIF for this pair (assuming frames list is populated)
        if frames:  # Check if frames list has images before saving
            frames[0].save(
                f'result/esenin{i}.gif',
                save_all=True,
                append_images=frames[1:],
                optimize=True,
                duration=1000,
                loop=0
            )

    print(f"Created {len(image_pairs)} GIFs successfully!")