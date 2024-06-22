from PIL import Image
import os


def pair_images(image_paths):
    """Pairs images for GIF creation.

    Args:
        image_paths (list): List of paths to image files.

    Returns:
        list: List of tuples containing image pairs.
    """
    pairs = []
    for index, image_path in enumerate(image_paths):
        # Calculate the complementary index
        pair_index = (index + 1) % len(image_paths)
        pairs.append((image_path, image_paths[pair_index]))
    return pairs


image_folder = "image"  # Change to your actual folder name
file_count = 0
for filename in os.listdir(image_folder):
    if os.path.isfile(os.path.join(image_folder, filename)):
        file_count += 1

frame_duration = 0.5
image_size = (640, 480)

# Get image paths with appropriate filtering (modify as needed)
image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder)
               if filename.endswith(('.jpg', '.jpeg', '.png'))]  # Filter for common image formats

# Pair images
image_pairs = pair_images(image_paths)

# Create and save GIFs
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
        frames[0].save(
            f'result/esenin{i}.gif',
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=frame_duration * 1000,  # Convert to milliseconds
            loop=0
        )

print(f"Created {len(image_pairs)} GIFs successfully!")
