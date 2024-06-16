import cv2
font = cv2.FONT_ITALIC
text = 'Esenin'
bottom_margin = 20
text_color = (32, 178, 170)
border_thickness = 2

for i in range(1, 5):
    img = cv2.imread(f"image/image{i}.jpeg")
    img_h, img_w = img.shape[:2]
    text_size = cv2.getTextSize(text, font, 1, border_thickness)[0]
    text_baseline = img_h - bottom_margin
    text_start_x = (img_w - text_size[0]) // 2
    text_pos = (text_start_x, text_baseline)
    cv2.putText(img, text, text_pos, font, 1, text_color, border_thickness)
    cv2.imshow('Result', img)
    cv2.imwrite(f"image/image{i}{i+1}.jpeg", img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
