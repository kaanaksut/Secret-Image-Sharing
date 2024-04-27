import cv2
import numpy as np

def psnr(image1, image2):
    image1 = image1.astype(np.float64)
    image2 = image2.astype(np.float64)
    mse = np.mean((image1 - image2) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr_value

# İki görüntüyü yükleyin
image1 = cv2.imread('1.jpg')
image2 = cv2.imread('stego_image.jpg')

# PSNR değerini hesapla
psnr_value = psnr(image1, image2)
print("PSNR değeri:", psnr_value)
