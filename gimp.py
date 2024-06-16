import numpy as np
import cv2
from PIL import *
from PIL import Image

img = cv2.imread("esenin1.jpeg")
font = cv2.FONT_ITALIC
text = 'Esenin'

cv2.putText(img, text, (300, 300), font, 10, color=(32, 178, 170), thickness=10)

cv2.imshow('Result', img)
cv2.imwrite("esenin2.jpeg", img)
cv2.waitKey()

frames = []

for frame_jpeg in range(1, 3):
    frame = Image.open(f"esenin{frame_jpeg}.jpeg")
    frames.append(frame)

frames[0].save(
    'esenin.gif',
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=1000,
    loop=0
)

