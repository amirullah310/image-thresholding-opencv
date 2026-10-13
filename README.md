# Praktikum Pengolahan Citra Digital - Image Thresholding

Repository ini berisi implementasi berbagai teknik **Segmentasi Citra (Image Thresholding)** menggunakan Python dan OpenCV. Citra uji yang digunakan adalah citra Gedung Politeknik Negeri Lhokseumawe (`gedungpnl.jpeg`).

---

## 📌 Daftar Metode yang Diimplementasikan

Praktikum ini dibagi menjadi 3 metode thresholding utama:

### 1. Simple (Global) Thresholding
Menetapkan satu nilai ambang batas (*threshold*) global tetap untuk seluruh piksel pada citra:
* **Binary Threshold (`cv2.THRESH_BINARY`)**: Piksel dengan nilai $> T$ diubah menjadi nilai maksimum ($255$), lainnya menjadi $0$.
* **Binary Threshold Inverted (`cv2.THRESH_BINARY_INV`)**: Kebalikan dari Binary Threshold.
* **Truncated Threshold (`cv2.THRESH_TRUNC`)**: Piksel dengan nilai $> T$ dipotong menjadi nilai $T$, piksel lainnya tidak berubah.
* **To-Zero Threshold (`cv2.THRESH_TOZERO`)**: Piksel dengan nilai $< T$ diubah menjadi $0$, lainnya tidak berubah.
* **To-Zero Inverted (`cv2.THRESH_TOZERO_INV`)**: Piksel dengan nilai $> T$ diubah menjadi $0$, lainnya tidak berubah.

### 2. Adaptive Thresholding
Menghitung ambang batas secara lokal untuk setiap wilayah kecil pada citra, sangat efektif untuk citra dengan kondisi pencahayaan yang tidak merata:
* **Adaptive Mean (`cv2.ADAPTIVE_THRESH_MEAN_C`)**: Nilai threshold adalah nilai rata-rata dari blok tetangga dikurangi sebuah konstanta $C$.
* **Adaptive Gaussian (`cv2.ADAPTIVE_THRESH_GAUSSIAN_C`)**: Nilai threshold adalah jumlah berbobot (fungsi Gaussian) dari blok tetangga dikurangi konstanta $C$.

### 3. Otsu's Thresholding
Metode otomatis untuk menentukan nilai threshold optimal berdasarkan analisis histogram bimodal (meminimalkan variansi intra-kelas atau memaksimalkan variansi antar-kelas).

---

## 🖼️ Hasil Visualisasi

| Citra Asli | Grayscale |
| :---: | :---: |
| ![Original](gedungpnl.jpeg) | ![Grayscale](Simple%20Thresholding/output/0_grayscale.png) |

### Simple Thresholding (Threshold = 120)
| Binary | Binary Inverted | Truncated |
| :---: | :---: | :---: |
| ![Binary](Simple%20Thresholding/output/1_thresh_binary.png) | ![Binary Inv](Simple%20Thresholding/output/2_thresh_binary_inv.png) | ![Trunc](Simple%20Thresholding/output/3_thresh_trunc.png) |

| To-Zero | To-Zero Inverted |
| :---: | :---: |
| ![To Zero](Simple%20Thresholding/output/4_thresh_tozero.png) | ![To Zero Inv](Simple%20Thresholding/output/5_thresh_tozero_inv.png) |

### Adaptive Thresholding (Block Size = 199, C = 5)
| Adaptive Mean | Adaptive Gaussian |
| :---: | :---: |
| ![Adaptive Mean](Adaptive%20Thresholding/output/1_adaptive_mean.png) | ![Adaptive Gaussian](Adaptive%20Thresholding/output/2_adaptive_gaussian.png) |

### Otsu's Thresholding (Automatic Optimal Threshold)
| Otsu's Binary Result |
| :---: |
| ![Otsu](Otsu%20Thresholding/output/1_otsu_thresh.png) |

---

## 📂 Struktur Direktori

```text
├── Adaptive Thresholding/
│   ├── adaptive_thresholding.py   # Script implementasi Adaptive Thresholding
│   └── output/                    # Hasil citra tersimpan
├── Otsu Thresholding/
│   ├── otsu_thresholding.py       # Script implementasi Otsu's Thresholding
│   └── output/                    # Hasil citra tersimpan
├── Simple Thresholding/
│   ├── simple_thresholding.py     # Script implementasi Simple Thresholding
│   └── output/                    # Hasil citra tersimpan
├── gedungpnl.jpeg                 # Citra sampel input
├── requirements.txt               # Dependensi pustaka Python
├── .gitignore                     # Aturan ignore file git
└── README.md                      # Dokumentasi proyek
```

---

## 🚀 Cara Menjalankan

### 1. Prasyarat & Instalasi
Pastikan Python telah terpasang di sistem Anda. Install dependensi dengan perintah:
```bash
pip install -r requirements.txt
```

### 2. Eksekusi Script
Jalankan masing-masing script sesuai kebutuhan:

```bash
# Menjalankan Simple Thresholding
python "Simple Thresholding/simple_thresholding.py"

# Menjalankan Adaptive Thresholding
python "Adaptive Thresholding/adaptive_thresholding.py"

# Menjalankan Otsu's Thresholding
python "Otsu Thresholding/otsu_thresholding.py"
```

Setiap script akan menampilkan preview visual interaktif dan secara otomatis menyimpan gambar hasil binerisasi ke dalam folder `output/` masing-masing.

---

## 👤 Penulis
* **Amirullah**
* Praktikum Pengolahan Citra Digital
* Politeknik Negeri Lhokseumawe (PNL)
