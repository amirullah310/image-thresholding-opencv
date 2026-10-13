import os

import cv2
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

# Step 4: Adaptive Mean Thresholding
# Threshold tiap piksel = rata-rata blok tetangga 199x199 dikurangi konstanta 5
thresh_mean = cv2.adaptiveThreshold(
    gray_image, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    199, 5
)
show_image(thresh_mean, 'Adaptive Mean Thresholding')

# Step 5: Adaptive Gaussian Thresholding
# Threshold tiap piksel = jumlah berbobot (jendela Gaussian) blok tetangga
# 199x199 dikurangi konstanta 5
thresh_gauss = cv2.adaptiveThreshold(
    gray_image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    199, 5
)
show_image(thresh_gauss, 'Adaptive Gaussian Thresholding')

# Simpan seluruh hasil ke folder output
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)
results = {
    '0_grayscale.png': gray_image,
    '1_adaptive_mean.png': thresh_mean,
    '2_adaptive_gaussian.png': thresh_gauss,
}
for filename, img in results.items():
    cv2.imwrite(os.path.join(OUTPUT_DIR, filename), img)
print(f'Hasil disimpan di: {OUTPUT_DIR}')
