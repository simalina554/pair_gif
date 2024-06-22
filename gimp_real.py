import random
import cv2
from PIL import Image
import os

font = cv2.FONT_HERSHEY_SIMPLEX
text_color = (220, 20, 60)
border_thickness = 3
image_dir = "3"
image_size = (646, 961)

file_count = 0
for filename in os.listdir(image_dir):
    if os.path.isfile(os.path.join(image_dir, filename)):
        file_count += 1

result_dir = 'result'
if not os.path.exists(result_dir):
    os.mkdir(result_dir)


def rename_file(original_filename, new_filename):
    if os.path.exists(f"{image_dir}/{original_filename}"):
        os.rename(f"{image_dir}/{original_filename}", f"{image_dir}/{new_filename}")
        print(f"Image renamed: {original_filename} -> {new_filename}")
    else:
        print(f"Error: File not found: {original_filename}")


def draw_text_on_image(image, text, font, text_color, border_thickness):
    img_h, img_w = image.shape[:2]
    text_size, _ = cv2.getTextSize(text, font, 1, border_thickness)
    text_w, text_h = text_size

    font_scale = 1
    while text_w < img_w and text_h < img_h:
        font_scale += 0.1
        text_size, _ = cv2.getTextSize(text, font, font_scale, border_thickness)
        text_w, text_h = text_size

    while text_w > img_w or text_h > img_h:
        font_scale -= 0.1
        text_size, _ = cv2.getTextSize(text, font, font_scale, border_thickness)
        text_w, text_h = text_size

    text_baseline = img_h // 2 + text_h // 2
    text_start_x = img_w // 2 - text_w // 2
    text_pos = (text_start_x, text_baseline)
    cv2.putText(image, text, text_pos, font, font_scale, text_color, border_thickness, cv2.LINE_AA)


def add_text_to_images():
    list12 = os.listdir(image_dir)

    for i in list12:
        result1 = random_word()
        img = cv2.imread(f"{image_dir}/{i}")
        draw_text_on_image(img, result1, font, text_color, border_thickness)
        new_filename = "modified_" + i
        cv2.imwrite(f"{image_dir}/{new_filename}", img)


def random_word():
    with open("question.txt", 'r', encoding="utf-8") as file:
        lines = file.readlines()
    random_lines = random.sample(lines, 1)
    result_string = '|'.join(map(lambda x: x.strip(), random_lines))

    return result_string


add_text_to_images()

image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)
               if filename.endswith('.jpg')]

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
