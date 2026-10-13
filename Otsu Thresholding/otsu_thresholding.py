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

# Step 4: Otsu's Thresholding
# Nilai threshold tidak ditentukan manual (diisi 0), melainkan dihitung
# otomatis oleh metode Otsu berdasarkan histogram gambar
ret, otsu_thresh = cv2.threshold(
    gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print('Calculated Otsu threshold value:', ret)
show_image(otsu_thresh, "Otsu's Thresholding")

# Simpan seluruh hasil ke folder output
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)
results = {
    '0_grayscale.png': gray_image,
    '1_otsu_thresh.png': otsu_thresh,
}
for filename, img in results.items():
    cv2.imwrite(os.path.join(OUTPUT_DIR, filename), img)
print(f'Hasil disimpan di: {OUTPUT_DIR}')
