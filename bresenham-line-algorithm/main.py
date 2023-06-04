import cv2
import numpy as np

def draw_line(img, x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope_error = dx - dy

    if x1 < x2:
        x_step = 1
    else:
        x_step = -1

    if y1 < y2:
        y_step = 1
    else:
        y_step = -1

    x = x1
    y = y1

    while x != x2 or y != y2:
        img[y, x] = (255, 255, 255)  

        slope_error_2 = 2 * slope_error

        if slope_error_2 > -dy:
            slope_error -= dy
            x += x_step

        if slope_error_2 < dx:
            slope_error += dx
            y += y_step

    img[y, x] = (255, 255, 255)


width = 800
height = 600
image = np.zeros((height, width, 3), dtype=np.uint8)

x1, y1 = 100, 100
x2, y2 = 700, 400
draw_line(image, x1, y1, x2, y2)

cv2.imshow("line", image)

k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()
