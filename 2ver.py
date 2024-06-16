import cv2
from PIL import Image
import os

font = cv2.FONT_ITALIC
text = 'Esenin'
bottom_margin = 20
text_color = (32, 178, 170)
border_thickness = 2
image_dir = "image"

for i in range(1, 5):
    img = cv2.imread(f"image/image{i}.jpeg")
    img_h, img_w = img.shape[:2]
    text_size = cv2.getTextSize(text, font, 1, border_thickness)[0]
    text_baseline = img_h - bottom_margin
    text_start_x = (img_w - text_size[0]) // 2
    text_pos = (text_start_x, text_baseline)
    cv2.putText(img, text, text_pos, font, 1, text_color, border_thickness)
    cv2.imshow('Result', img)
    cv2.imwrite(f"image/image{i}{i + 1}.jpeg", img)
    cv2.waitKey(0)


def add_text_to_image(image_path):
    # Read image
    img = Image.open(image_path)
    return img


def create_gif(frames, gif_filename, duration=100, loop=0):
    frames[0].save(
        gif_filename,
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        duration=duration,
        loop=loop
    )


image_filenames = os.listdir(image_dir)

image_pairs = []
for filename in image_filenames:
    if filename.endswith(".jpeg"):
        base_filename = filename[:-5]
        for other_filename in image_filenames:
            if other_filename.endswith(".jpeg") and other_filename.startswith(base_filename):
                if other_filename != filename:
                    image_pairs.append((filename, other_filename))

for i, (image1_filename, image2_filename) in enumerate(image_pairs):
    frames = []
    for image_path in (os.path.join(image_dir, image1_filename), os.path.join(image_dir, image2_filename)):
        img_with_text = add_text_to_image(image_path)
        frames.append(img_with_text)

    gif_filename = f"esenin_slideshow_{i + 1}.gif"
    create_gif(frames, gif_filename)

print("Slideshow creation for all image pairs complete!")
