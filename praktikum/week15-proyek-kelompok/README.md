## **Mini Simulasi Sistem Operasi**

Aplikasi berbasis terminal yang mensimulasikan dua konsep utama sistem operasi: CPU Scheduling (FCFS) dan Page Replacement (LRU) melalui analogi kehidupan sehari-hari yang mudah dipahami.

## **Fitur utama**

1. **Simulasi FCFS (First-Come First-Served) - Kasir**

-  Menghitung waktu tunggu setiap pelanggan
- Menghitung waktu selesai layanan
- Visualisasi tabel hasil simulasi
- Analogi antrian kasir yang mudah dipahami

2. Simulasi LRU (Least Recently Used) - Page Replacement

- Simulasi pengelolaan RAM dengan 3 frame
- Tracking Page Fault (aplikasi yang ditutup paksa)
-  Visualisasi perubahan isi RAM setiap langkah
- Implementasi algoritma LRU yang optimal

## **Teknologi yang digunakan**

### Tabel Teknologi yang Digunakan

| Teknologi | Versi  | Kegunaan                 |
| --------- | ------ | ------------------------ |
| Python    | 3.14   | Bahasa pemrograman utama |
| Docker    | Latest | Containerization         |
| CSV       | -      | Format data input        |
| Git       | Latest | Version control          |

**Library Python yang Digunakan**:

- csv: Untuk membaca file dataset
- sys: Untuk konfigurasi sistem (disable bytecode)

# **struktur folder**

### Struktur Direktori Proyek

```text
week15-proyek-kelompok/
├── code/
│   ├── main.py            # Controller utama aplikasi
│   ├── kasir_FCFS.py      # Modul simulasi FCFS
│   ├── page.py            # Modul simulasi LRU
│   ├── Dockerfile         # Konfigurasi Docker
│   ├── README.md          # Dokumentasi aplikasi 
│   └── data/
│       ├── pelanggan.csv  # Dataset simulasi kasir (FCFS)
│       └── aplikasi.csv   # Dataset simulasi RAM (LRU)
├── screenshots/
│   ├── menu_utama.png     # Screenshot menu aplikasi
│   ├── hasil_fcfs.png     # Screenshot hasil simulasi FCFS
│   └── hasil_lru.png      # Screenshot hasil simulasi LRU
└── laporan.md             # Laporan lengkap proyek
```

## Cara Pengunaan

1. **Menjalankan Aplikasi**
 aplikasi ini dapat dijalankan menggunakan dua cara: via Docker (disarankan) atau secara Manual (Python Lokal).

 1. Menggunakan Docker (Disarankan)
Pastikan Docker Desktop / Docker Engine sudah terinstal dan berjalan.

- Build Image Buka terminal di dalam folder code/, lalu jalankan:
```python
docker build -t week15-proyek-kelompok .
```
- Jalankan Container Gunakan flag -it agar bisa berinteraksi dengan menu aplikasi:
```python
docker run -it --rm week15-proyek-kelompok
```
2. **Menjalankan Secara Manual (Local Host)**
Pastikan Python 3.x sudah terinstal di komputer Anda.

- Buka Terminal Arahkan terminal ke direktori code/.

- Jalankan Script
```python
python main.py
```

# ** cara penggunaan**

1. **Menjalankan Aplikasi**

Setelah aplikasi berjalan, Anda akan melihat menu utama:

=== MENU SIMULASI SISTEM OPERASI ===
1. Simulasi FCFS (Kasir)
2. Simulasi Page Replacement LRU
3. Jalankan Semua Simulasi
0. Keluar
-----------------------------------
Pilih menu (0-3):


2. **Pilihan Menu**
# Menu 1: **Simulasi FCFS (Kasir)**

Mensimulasikan antrian pelanggan di kasir dengan algoritma First-Come First-Served.

Input: Data dari (*data/pelanggan.csv*)

**Output**

### Hasil Simulasi FCFS (First Come First Served)

| Nama  | Waktu Layanan | Waktu Tunggu | Waktu Selesai |
| ----- | ------------- | ------------ | ------------- |
| Andi  | 4             | 0            | 4             |
| Beni  | 3             | 4            | 7             |
| Cecep | 5             | 7            | 12            |
| Deni  | 2             | 12           | 14            |


# Menu 2: **Simulasi Page Replacement LRU**

Mensimulasikan manajemen memori RAM laptop dengan algoritma Least Recently Used.

Input: Data dari (*data/aplikasi.csv*) dengan kapasitas RAM = 3 frame

**Output**:
### Hasil Simulasi Page Replacement LRU (Kapasitas RAM = 3)

| Aplikasi | Isi RAM Setelah Akses    | Page Fault |
| -------- | ------------------------ | ---------- |
| Chrome   | Chrome                   | Yes        |
| Word     | Chrome, Word             | Yes        |
| YouTube  | Chrome, Word, YouTube    | Yes        |
| Chrome   | Word, YouTube, Chrome    | No         |
| Spotify  | YouTube, Chrome, Spotify | Yes        |
| Word     | Chrome, Spotify, Word    | Yes        |

**Total Page Fault : 5**

# Menu 3: **Jalankan Semua Simulasi**

Menjalankan kedua simulasi secara berurutan dalam satu eksekusi.
**Menu 0: Keluar**
Keluar dari aplikasi dengan aman.

# ** Dataset**

Anda dapat mengubah data simulasi dengan mengedit file di folder data/.

**Format File pelanggan.csv**

nama,waktu_layanan
Andi,4
Beni,3
Cecep,5
Deni,2

**Kolom**
- nama: Nama pelanggan (string)
- waktu_layanan: Durasi layanan dalam menit (integer)

**Format File aplikasi.csv**
aplikasi
Chrome
Word
YouTube
Chrome
Spotify
Word

**Kolom**
- aplikasi: Nama aplikasi yang dibuka (string)

**Cara Memodifikasi Dataset**

- Edit file CSV menggunakan text editor atau Excel
- Simpan dengan format CSV (Comma-separated values)
- Pastikan header kolom sesuai dengan format di atas
- Jalankan ulang aplikasi untuk melihat hasil dengan data baru


**Contoh modifikasi:**
nama,waktu_layanan
Budi,10
Ani,5
Citra,15
Dodi,3
Agus,7