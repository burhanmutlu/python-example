import cv2
import numpy as np

def zoom_out(image, scale_factor):
    height, width = image.shape[:2]
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Yeni boyutlara göre boş bir görüntü oluştur
    zoomed_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    for y in range(new_height):
        for x in range(new_width):
            # Yakınlaştırılan pikselin koordinatlarını hesapla
            src_x = int(x / scale_factor)
            src_y = int(y / scale_factor)

            # Yakınlaştırılan pikselin değerini atama
            zoomed_image[y, x] = image[src_y, src_x]

    return zoomed_image

image = cv2.imread('org.jpg')

scale_factor = 0.5

zoomed_out_image = zoom_out(image, scale_factor)

cv2.imshow('Original Image', image)
cv2.imshow('Zoomed Out Image', zoomed_out_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
