import random
import cv2
from PIL import Image
import os
import imageio

frame_duration = 10
image_size = (640, 480)
font = cv2.FONT_ITALIC
bottom_margin = 20
text_color = (32, 178, 170)
border_thickness = 2
image_dir = "image"

file_count = 0
for filename in os.listdir(image_dir):
    if os.path.isfile(os.path.join(image_dir, filename)):
        file_count += 1

if os.path.exists('result'):
    print('ok')
else:
    os.mkdir('result')

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

    new_filename = "modified_" + i
    cv2.imwrite(f"{image_dir}/{new_filename}", img)


image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)
               if filename.endswith('.jpeg')]

image_pairs = []
for index, image_path in enumerate(image_paths):
    if index < len(image_paths) // 2:
        pair_index = len(image_paths) // 2 + index
        image_pairs.append((image_path, image_paths[pair_index]))

for i, image_pair in enumerate(image_pairs):
    frames = []
    for image_path in image_pair:
        try:
            image = Image.open(image_path)
            image = image.resize(image_size)
            frames.append(image)
        except PermissionError:
            print(f"Error accessing image: {image_path}")
    if frames:
        frames[0].convert('RGB').save(
            f'result/esenin{i}.gif',
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=500,
            loop=0)
    print(f"Created GIF {i} successfully!")
