# PRESENTASI PROYEK KELOMPOK: MINI SIMULASI OS
**Topik:** CPU Scheduling (FCFS) dan Page Replacement (LRU) melalui analogi kehidupan sehari-hari yang mudah dipahami.

**WEEK:** 15

---

## Nama Anggota Kelompok 
- Miftakhul Lisna Esa Baehaqi (250202951)
- Ilham Dzufikar Barokah (250202942)
- Asyifani Lutfiana Nadzif (250202931)
- Ihsan Mu'arif (250202921)
- Hanif Arunndaya Usman (25020241)
---
  
## 1. PENDAHULUAN
### Latar Belakang
* Sistem oprasi adalah menghubungkan antara pengguna dan perangkat keras
* OS mengatur proses, CPU, dan memori agar berjalan feisien 
* Konsep seperti CPU Scheduling dan Memory Management sering sulit dipahami
* Oleh karena itu dibuat simulasi agar kosep lebih muda dimengerti

## Studi Kasus
1.  **Simulasi FCFS (simulasi kasir)**
Studi kasus:
- Sebuah kasir melayani pelangan sesuai urutan datang
- Setiap pelangan sesuai urutan datang
- Setiap pelanggan memiliki waktu layanan berbeda
- Pelanggan harus menungu hingga layanan sebelumnya selesai
* CONTOH Simulasi FCFS:
  
| Nama  | Waktu Layanan | Waktu Tunggu | Waktu Selesai |
| ----- | ------------- | ------------ | ------------- |
| Andi  | 4             | 0            | 4             |
| Beni  | 3             | 4            | 7             |
| Cecep | 5             | 7            | 12            |
| Deni  | 2             | 12           | 14            |

2.  **Simulasi LRU (Simulasi RAM Leptop)**, Studi kasus:
* Leptop memiliki RAM terbatas (3 aplikasi)
* Pengguna membuka banyak aplikasi secara pergantian
* Sistem harus menghapus aplikasi yang lama tidak digunakan
 * Contoh hasil LRU:
  
| Aplikasi | Isi RAM Setelah Akses    | Page Fault |
| -------- | ------------------------ | ---------- |
| Chrome   | Chrome                   | Yes        |
| Word     | Chrome, Word             | Yes        |
| YouTube  | Chrome, Word, YouTube    | Yes        |
| Chrome   | Word, YouTube, Chrome    | No         |
| Spotify  | YouTube, Chrome, Spotify | Yes        |
| Word     | Chrome, Spotify, Word    | Yes        |


---

## 2. ARSITEKTUR APLIKASI
### Tech Stack
* **Bahasa:** Python (Berbasis CLI/Terminal).
* **Environment:** Docker (Untuk konsistensi / *reproducible*).
* **Version Control:** Git (Branching per fitur).

### Desain Modular
Secara garis besar, arsitektur aplikasi terdiri dari tiga komponen utama:
1.  **Controller Utama (`main.py`):** Modul ini tidak menghitung FCFS atau LRU, hanya mengatur jalannya program.
2.  **Modul FCFS** Modul ini hanya fokus FCFS, tidak peduli menu atau modul lain.
3.  **Modul LRU** Modul ini hanya fokus LRU, tidak berhubungan dengan kasir.

---

## 3. LIVE DEMO

**Skenario Demo:**
1.  **Jalankan Docker:**
    `docker run -it --rm week15-proyek-kelompok`


---

## 4. HASIL & ANALISIS: Simulasi FCFS (First Come First Served)
**Hasil:**
| Nama  | Waktu Layanan | Waktu Tunggu | Waktu Selesai |
| ----- | ------------- | ------------ | ------------- |
| Andi  | 4             | 0            | 4             |
| Beni  | 3             | 4            | 7             |
| Cecep | 5             | 7            | 12            |
| Deni  | 2             | 12           | 14            |


**Analisis:**
* Pelanggan dilayani sesuai urutan kedatangan
* Tidak ada proses yang dipotong atau disela
* Waktu tunggu pelanggan meningkat seiring posisi dalam antrian
* Pelanggan dengan waktu layanan lama di awal menyebabkan pelanggan lain menunggu lebih lama
  
* **Kesimpulan:** Algoritma FCFS menjalankan proses berdasarkan urutan kedatangan sehingga mudah diterapkan dan bersifat adil, namun kurang efisien karena proses yang membutuhkan waktu lama dapat meningkatkan waktu tunggu proses lainnya.

---

## 5. HASIL & ANALISIS: Simulasi Page Replacement LRU
**Hasil: Simulasi Page Replacement LRU (Kapasitas RAM = 3)**

| Aplikasi | Isi RAM Setelah Akses    | Page Fault |
| -------- | ------------------------ | ---------- |
| Chrome   | Chrome                   | Yes        |
| Word     | Chrome, Word             | Yes        |
| YouTube  | Chrome, Word, YouTube    | Yes        |
| Chrome   | Word, YouTube, Chrome    | No         |
| Spotify  | YouTube, Chrome, Spotify | Yes        |
| Word     | Chrome, Spotify, Word    | Yes        |


**Analisis:**
* Saat RAM belum penuh, aplikasi langsung dimasukkan
* Ketika RAM penuh, aplikasi yang paling lama tidak digunakan akan dihapus
* Jika aplikasi yang sama dibuka kembali dan masih ada di RAM, tidak terjadi page fault
* Algoritma memanfaatkan kebiasaan pengguna membuka aplikasi yang sama berulang kali
* **Kesimpulan:**
* Algoritma LRU mengelola memori dengan mempertahankan data yang paling sering digunakan sehingga lebih efisien dan sesuai dengan pola penggunaan nyata, meskipun membutuhkan pengelolaan yang lebih kompleks.

---

## 6. TIM & KONTRIBUSI
Proyek ini dikerjakan secara kolaboratif dengan pembagian tugas yang jelas untuk memastikan setiap modul dapat diselesaikan tepat waktu dan terintegrasi dengan baik. Berikut adalah rincian peran dan kontribusi setiap anggota tim:
| Nama Anggota                   | Peran Utama                  | Deskripsi Kontribusi                                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Miftakhul Lisna Esa Behaqi** | Project Lead & Integrator    | - Merancang struktur awal proyek dan `main.py`<br>- Mengelola repositori Git (merge PR, resolve conflict)<br>- Membuat konfigurasi `Dockerfile` agar aplikasi berjalan di container<br>- Melakukan pengujian fungsional seluruh modul<br>- Mengumpulkan screenshot bukti demo |
| **Ikhsan Mu'arif**             | Developer (Modul Scheduling) | - Mengimplementasikan algoritma FCFS pada `kasir_FCFS.py`<br>- Menyusun logika perhitungan waktu tunggu dan waktu selesai<br>- Membuat dataset `pelanggan.csv`<br>- Melakukan unit testing pada modul FCFS                                                                    |
| **Ilham Dzufikar Barokah**     | Developer (Modul Memory)     | - Mengimplementasikan algoritma LRU pada `page.py`<br>- Membuat visualisasi tabel isi RAM dengan format ASCII<br>- Menyusun dataset `aplikasi.csv` dan skenario uji page fault<br>- Melakukan unit testing pada modul LRU                                                     |
| **Asyifani Lutfiana Nadzif**  | Documentation & QA           | - Menyusun file `Presentation.md` dan dokumentasi penggunaan<br>- Menyusun dokumen akhir `Laporan.md`<br>- Melakukan testing integrasi antar modul<br>- Menyiapkan materi presentasi                                                                                                |
| **Hanif Arumndaya Usman**      | Data & Support Engineer      | - Membantu validasi dataset dan skenario pengujian<br>- Membantu debugging error saat integrasi modul<br>- Mengecek konsistensi output simulasi FCFS dan LRU<br>- Mendukung proses presentasi dan demo aplikasi                                                               |


---
**Terima Kasih**
