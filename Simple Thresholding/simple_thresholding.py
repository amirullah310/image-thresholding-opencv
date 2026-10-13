import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Import libraries dan persiapan gambar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, '..', 'gedungpnl.jpeg')

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f'Gambar tidak ditemukan: {IMAGE_PATH}')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Step 2: Helper function untuk menampilkan gambar
def show_image(img, title):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()


# Step 3: Menampilkan gambar asli (grayscale)
show_image(gray_image, 'Original Grayscale Image')

# Step 4: Binary Threshold
# Piksel > threshold -> 255 (putih), selainnya -> 0 (hitam)
_, thresh_binary = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)
show_image(thresh_binary, 'Binary Threshold')

# Step 5: Binary Threshold Inverted
# Piksel > threshold -> 0 (hitam), selainnya -> 255 (putih)
_, thresh_binary_inv = cv2.threshold(
    gray_image, 120, 255, cv2.THRESH_BINARY_INV)
show_image(thresh_binary_inv, 'Binary Threshold Inverted')

# Step 6: Truncated Threshold
# Piksel > threshold -> diset menjadi nilai threshold, selainnya tetap
_, thresh_trunc = cv2.threshold(gray_image, 120, 255, cv2.THRESH_TRUNC)
show_image(thresh_trunc, 'Truncated Threshold')

# Step 7: To Zero Threshold
# Piksel < threshold -> 0, selainnya tetap
_, thresh_tozero = cv2.threshold(gray_image, 120, 255, cv2.THRESH_TOZERO)
show_image(thresh_tozero, 'Set to 0')

# Step 8: To Zero Inverted Threshold
# Piksel > threshold -> 0, selainnya tetap
_, thresh_tozero_inv = cv2.threshold(
    gray_image, 120, 255, cv2.THRESH_TOZERO_INV)
show_image(thresh_tozero_inv, 'Set to 0 Inverted')

# Simpan seluruh hasil ke folder output
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)
results = {
    '0_grayscale.png': gray_image,
    '1_thresh_binary.png': thresh_binary,
    '2_thresh_binary_inv.png': thresh_binary_inv,
    '3_thresh_trunc.png': thresh_trunc,
    '4_thresh_tozero.png': thresh_tozero,
    '5_thresh_tozero_inv.png': thresh_tozero_inv,
}
for filename, img in results.items():
    cv2.imwrite(os.path.join(OUTPUT_DIR, filename), img)
print(f'Hasil disimpan di: {OUTPUT_DIR}')
