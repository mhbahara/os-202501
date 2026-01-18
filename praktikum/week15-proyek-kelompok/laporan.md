
## Laporan Proyek Kelompok: Mini Simulasi Sistem Operasi

**1. Pendahuluan** 
------------------------
**A. Latar Belakang**
1. Pendahuluan
A. Latar Belakang
Sistem operasi merupakan perangkat lunak sistem yang bertugas mengelola sumber daya perangkat keras dan perangkat lunak, serta bertindak sebagai perantara antara pengguna dan perangkat keras komputer. Konsep-konsep inti di dalamnya, seperti penjadwalan proses (CPU Scheduling) dan manajemen memori (Memory Management), sering kali bersifat abstrak dan sulit dipahami tanpa visualisasi yang konkret. Oleh karena itu, diperlukan sebuah pendekatan praktis untuk mendemonstrasikan bagaimana sistem operasi bekerja dalam menangani tugas-tugas tersebut.
Proyek ini, yang bertajuk "Mini Simulasi Sistem Operasi", dikembangkan untuk mengintegrasikan materi praktikum menjadi sebuah aplikasi berbasis terminal yang fungsional. Aplikasi ini dirancang untuk mensimulasikan logika sistem operasi melalui analogi kegiatan sehari-hari agar lebih mudah dipahami. Kami mengimplementasikan dua modul utama:

1. **Simulasi Kasir (FCFS)**, yang merepresentasikan algoritma CPU Scheduling tipe First-Come First-Served (FCFS). Dalam simulasi ini, pelanggan yang datang pertama kali akan dilayani hingga selesai sebelum sistem beralih ke pelanggan berikutnya, menggambarkan bagaimana antrian layanan bekerja dalam kehidupan nyata.

2. **Simulasi RAM Laptop (LRU)**, yang memodelkan algoritma Page Replacement tipe Least Recently Used (LRU). Simulasi ini menggambarkan manajemen memori pada laptop, di mana aplikasi yang paling lama tidak digunakan akan ditutup secara otomatis oleh sistem ketika kapasitas memori (RAM) telah penuh dan pengguna membuka aplikasi baru.

Pengembangan aplikasi ini juga dilakukan untuk memenuhi standar rekayasa perangkat lunak modern, termasuk penggunaan Docker untuk memastikan lingkungan eksekusi yang konsisten (reproducible environment) dan penerapan alur kerja kolaboratif menggunakan Git.

# Tujuan Proyek

Berdasarkan deskripsi tugas praktikum Minggu 15, tujuan utama dari pelaksanaan proyek ini adalah sebagai berikut:

1. Mengintegrasikan lebih dari satu konsep Sistem Operasi dengan mengimplementasikan algoritma CPU Scheduling (FCFS) serta Memory Management (Page Replacement LRU) ke dalam satu aplikasi simulasi terpadu berbasis terminal.

2. Melatih kerja tim dan pembagian peran secara terstruktur, di mana setiap anggota bertanggung jawab pada modul tertentu (CPU Scheduling, Page Replacement, integrasi, dan dokumentasi) sehingga menyerupai alur kerja pengembangan perangkat lunak nyata.

3. Menerapkan workflow Git kolaboratif, meliputi penggunaan branch terpisah untuk setiap fitur, penulisan commit message yang jelas, serta proses merge melalui Pull Request untuk menjaga stabilitas kode utama.

4. Membangun aplikasi berbasis Command Line Interface (CLI) yang terstruktur, modular, dan terdokumentasi dengan baik, sehingga mudah digunakan, diuji, dan dikembangkan lebih lanjut.

5. Menggunakan Docker untuk menciptakan environment yang reproducible, sehingga aplikasi dapat dijalankan dan didemokan dengan konfigurasi yang sama di berbagai sistem tanpa permasalahan dependensi.

## 2. Arsitektur Aplikasi

----------------------

**A. Desain Arsitektur Umum**

Aplikasi "Mini Simulasi Sistem Operasi" ini dibangun menggunakan arsitektur modular berbasis Command Line Interface (CLI) dengan bahasa pemrograman Python. Struktur aplikasi dirancang secara terpisah antara logika utama program (main controller) dan logika algoritma simulasi (business logic) untuk memudahkan pemeliharaan dan pengembangan kode.

Secara garis besar, arsitektur aplikasi terdiri dari tiga komponen utama:

1. **Controller Utama (main.py):** Bertindak sebagai pintu masuk (entry point) aplikasi yang menangani interaksi pengguna, menampilkan menu pilihan, dan memanggil fungsi dari modul yang relevan.
2. **Modul Logika (Logic Modules):** Berkas terpisah yang berisi implementasi algoritma sistem operasi, yaitu (*kasir_FCFS.py*) untuk penjadwalan CPU menggunakan algoritma FCFS dan (*page.py*) untuk manajemen memori menggunakan algoritma LRU.
3. **Manajemen Data (Data Layer):** Penyimpanan data input statis dalam bentuk berkas CSV yang terletak di direktori (*data/*) untuk dibaca oleh modul logika.

Seluruh komponen ini dibungkus dalam Docker container untuk menjamin aplikasi dapat berjalan secara konsisten di berbagai lingkungan sistem operasi tanpa hambatan dependensi.


# **B. Deskripsi Modul**
Aplikasi ini mengintegrasikan dua modul utama yang mensimulasikan fungsi inti sistem operasi:

1. Modul CPU Scheduling - FCFS (Simulasi Kasir)
Modul ini mensimulasikan algoritma penjadwalan proses First-Come First-Served (FCFS) dengan analogi sebuah antrian pelanggan di kasir.

- **Berkas Sumber:** (*kasir_FCFS.py*)
- **Input Data:** Berkas (*data/pelanggan.csv*) yang memuat daftar nama pelanggan dan waktu layanan yang dibutuhkan.

**Logika Proses:**

- Sistem membaca data pelanggan dari file CSV menggunakan modul (*csv.DictReader*).
- Sistem memproses antrian secara berurutan. Pelanggan yang datang lebih awal akan dilayani hingga selesai sebelum beralih ke pelanggan berikutnya (non-preemptive).
- Sistem menghitung waktu tunggu (waiting time) untuk setiap pelanggan dengan formula: (*waktu_tunggu[i]*) = (*waktu_tunggu[i-1]*) + (*waktu_layanan[i-1]*).
- Sistem menghitung waktu selesai untuk setiap pelanggan dengan formula: (*waktu_selesai[i]*) = (*waktu_tunggu[i]*) + (*waktu_layanan[i].*)

**Output**:** Tabel status layanan yang menampilkan nama pelanggan, waktu layanan, waktu tunggu, dan waktu selesai untuk setiap pelanggan dalam format yang terstruktur.

2. **Modul Page Replacement - LRU (Simulasi RAM Laptop)**
Modul ini mensimulasikan algoritma manajemen memori Least Recently Used (LRU) dengan analogi manajemen aplikasi yang berjalan di RAM laptop.

**Berkas Sumber:** (*page.py*)
**Input Data:**

- Berkas (*data/aplikasi.csv*) yang berisi urutan aplikasi yang dibuka pengguna.
- Kapasitas frame (RAM) yang telah ditentukan sebanyak 3 frame.


**Logika Proses:**

- Sistem membaca urutan aplikasi (representasi page reference string) dari file CSV.
- Setiap aplikasi yang dibuka akan dimuat ke dalam list memory yang merepresentasikan RAM.
- **Jika aplikasi sudah ada di RAM (Hit):** Aplikasi dipindahkan ke posisi terakhir dalam list (menandakan baru saja digunakan), menerapkan konsep LRU.
- Jika aplikasi belum ada dan RAM belum penuh: Aplikasi langsung ditambahkan ke RAM.
Jika aplikasi belum ada dan RAM penuh (Miss/Page Fault): Sistem akan menghapus aplikasi yang paling lama tidak digunakan (indeks ke-0) untuk memberi ruang bagi aplikasi baru, kemudian menambahkan aplikasi baru tersebut.
- Setiap langkah mencatat apakah terjadi Page Fault atau tidak.


**Output**: Tabel visualisasi isi RAM pada setiap langkah, status Page Fault (Yes/No), dan total jumlah Page Fault yang terjadi.

# C. **Alur Data (Data Flow)**

Aliran data dalam aplikasi berjalan secara sekuensial sebagai berikut:


1. **Inisialisasi:** Pengguna menjalankan aplikasi melalui terminal (atau Docker). Program (*main.py*) memuat pustaka yang diperlukan dan menampilkan menu utama.
2. Pemilihan Menu: Pengguna memilih mode simulasi pada menu utama:

- Pilihan 1: Simulasi FCFS (Kasir)
- Pilihan 2: Simulasi Page Replacement LRU
- Pilihan 3: Jalankan semua simulasi
- Pilihan 0: Keluar dari program


3. **Pengambilan Input:**

- Jika mode FCFS dipilih, fungsi (*simulasi_kasir()*) membaca (*data/pelanggan.csv.*)
- Jika mode LRU dipilih, fungsi (*simulasi_lru()*) membaca (*data/aplikasi.csv.*)
- Jika pilihan 3 dipilih, kedua modul dijalankan secara berurutan.


4. **Pemrosesan:** Data yang telah dimuat diproses sesuai algoritma masing-masing modul (FCFS untuk kasir, LRU untuk page replacement).
5. **Penyajian Output:** Hasil perhitungan dan simulasi ditampilkan ke layar pengguna dalam format tabel ASCII yang terstruktur, diikuti dengan kembalinya program ke menu utama (loop) hingga pengguna memilih untuk keluar.

# 3. **Demo Langsung Menjalankan Aplikasi**

Sesuai dengan ketentuan teknis proyek, kami telah menyusun panduan instalasi dan eksekusi lengkap pada berkas (*code/README.md*) yang disertakan dalam repositori ini. Demo aplikasi dapat dilakukan melalui dua metode, namun kami merekomendasikan penggunaan Docker untuk hasil yang paling stabil

**3.1 Lingkungan Demo (Environment)**

Demo aplikasi ini dijalankan pada lingkungan terisolasi menggunakan Docker Container:

- **Base Image:** (*python:3.14-alpine*) (Dipilih karena ukurannya yang ringan dan efisien)
- **Working Directory:**  (**/app*)
- Struktur Container: Menyalin seluruh kode sumber (*.py*) dan folder dataset (*data/*) ke dalam direktori kerja /app di dalam container

**3.2 Prosedur Demo**

Berikut adalah ringkasan prosedur demo yang dilakukan untuk memverifikasi fungsionalitas aplikasi:

**Tahap 1: Build Image Docker**
```python
docker build -t week15-proyek-kelompok .
```
Proses ini membangun Docker bernama week15-proyek-kelompok dan memastikan seluruh dependensi dan struktur folder tersusun dengan benar sesuai konfigurasi (*Dockerfile.*)

![screenshoot](./screenshots/build%20docker.png)
 
 **Tahap 2:Eksekusi Container** 

 ```python

 docker run -it --rm week15-proyek-kelompok
```
Container dijalankan dalam mode interaktif (`-it`) untuk memungkinkan pengguna berinteraksi dengan menu CLI aplikasi. Mode `--rm` diaktifkan agar container otomatis dibersihkan setelah demo selesai, menjaga kebersihan resource sistem host.

## Tahap 3: Interaksi Pengguna

Saat aplikasi berjalan, demo mencakup empat skenario utama:

- **Skenario 1 (FCFS)**: Memilih menu "1" untuk memuat `pelanggan.csv` dan menampilkan simulasi antrian kasir dengan algoritma FCFS, menampilkan waktu tunggu dan waktu selesai setiap pelanggan.

- **Skenario 2 (LRU)**: Memilih menu "2" untuk memuat `aplikasi.csv` dan mengamati simulasi page replacement LRU dengan 3 frame, menampilkan perubahan isi RAM dan jumlah Page Fault.

- **Skenario 3 (Semua Simulasi)**: Memilih menu "3" untuk menjalankan kedua simulasi secara berurutan dalam satu eksekusi.

- **Skenario 4 (Terminasi)**: Memilih menu "0" untuk keluar dari program secara aman.


## 3.3 Bukti Eksekusi

Tangkapan layar (screenshot) hasil eksekusi program, baik tampilan menu utama maupun hasil tabel perhitungan, telah kami lampirkan dalam folder `screenshots/` sebagai bukti validasi bahwa aplikasi berjalan sesuai spesifikasi.

## 4. Hasil Pengujian dan Analisis

Pada bagian ini, kami menyajikan hasil eksekusi aplikasi menggunakan dataset standar yang telah disiapkan. Pengujian dilakukan untuk memverifikasi kebenaran logika algoritma CPU Scheduling dan Page Replacement.

## A. Hasil Pengujian Modul A (CPU Scheduling - FCFS)

# Skenario Pengujian

Kami menggunakan dataset antrian kasir (`pelanggan.csv`) dengan data pelanggan yang memiliki waktu layanan berbeda-beda. Simulasi ini menggambarkan situasi pelanggan yang datang secara berurutan ke kasir dan harus menunggu hingga pelanggan sebelumnya selesai dilayani.


## Hasil Output Aplikasi

Berikut adalah tabel hasil simulasi yang dihasilkan oleh aplikasi:

![screenshoot](./screenshots/test%20ffcs%20(1).png)


### Hasil Simulasi FCFS (First Come First Served)

| Nama  | Waktu Layanan | Waktu Tunggu | Waktu Selesai |
| ----- | ------------- | ------------ | ------------- |
| Andi  | 4             | 0            | 4             |
| Beni  | 3             | 4            | 7             |
| Cecep | 5             | 7            | 12            |
| Deni  | 2             | 12           | 14            |


*(Catatan: Data aktual disesuaikan dengan isi file `pelanggan.csv`)*

# Analisis Kinerja

Berdasarkan hasil simulasi FCFS, dapat diidentifikasi beberapa karakteristik utama algoritma:

1. **Non-Preemptive Nature**: Pelanggan yang tiba lebih awal akan dilayani terlebih dahulu hingga selesai, tanpa ada interupsi. Ini mencerminkan sifat non-preemptive dari algoritma FCFS.

2. **Convoy Effect**: Jika pelanggan dengan waktu layanan yang lama berada di awal antrian, maka semua pelanggan berikutnya harus menunggu lebih lama, bahkan jika waktu layanan mereka singkat. Hal ini menunjukkan kelemahan utama FCFS yaitu tidak efisien untuk meminimalkan average waiting time.

3. **Fairness**: Algoritma ini sangat adil karena mengikuti prinsip "siapa cepat dia dapat" tanpa diskriminasi berdasarkan prioritas atau durasi layanan.

4. **Simplicity**: Implementasi FCFS sangat sederhana dan mudah dipahami, tidak memerlukan perhitungan kompleks untuk menentukan urutan eksekusi.

## B. Hasil Pengujian Modul B (Page Replacement - LRU)

# Skenario Pengujian

Kami mensimulasikan manajemen RAM laptop menggunakan dataset riwayat aplikasi (`aplikasi.csv`) dengan urutan akses aplikasi yang bervariasi. Kapasitas RAM diset menjadi 3 aplikasi (frames), mencerminkan keterbatasan memori yang umum pada sistem komputer.
## Hasil Output Aplikasi

Berikut adalah tabel hasil simulasi yang menggambarkan perubahan isi RAM pada setiap langkah:

![screeenshoot](./screenshots/page%20replacement.png)

=== PAGE REPLACEMENT LRU - MEMORI LAPTOP ===

| Aplikasi | Isi RAM Setelah Akses    | Page Fault |
| -------- | ------------------------ | ---------- |
| Chrome   | Chrome                   | Yes        |
| Word     | Chrome, Word             | Yes        |
| YouTube  | Chrome, Word, YouTube    | Yes        |
| Chrome   | Word, YouTube, Chrome    | No         |
| Spotify  | YouTube, Chrome, Spotify | Yes        |
| Word     | Chrome, Spotify, Word    | Yes        |

**Total Page Fault : 5**

**Data aktual disesuaikan dengan isi file (*aplikasi.csv*)**

**Analisis Kinerja**

Algoritma LRU (Least Recently Used) menunjukkan karakteristik sebagai berikut:

1. **Adaptive to Usage Pattern:** LRU mempertahankan aplikasi yang baru-baru ini digunakan di dalam RAM. Ketika aplikasi yang sudah ada di RAM diakses kembali, posisinya dipindahkan ke akhir list (menandakan baru digunakan), sehingga tidak akan dihapus dalam waktu dekat.
2. **Page Fault Reduction:** Dibandingkan dengan FIFO murni, LRU lebih efisien dalam mengurangi Page Fault untuk pola akses yang berulang. Pada langkah ke-7 dalam contoh di atas, ketika Spotify diakses kembali, tidak terjadi Page Fault karena Spotify masih ada di RAM.
3. **Locality of Reference:** LRU memanfaatkan prinsip temporal locality - asumsi bahwa data yang baru saja diakses kemungkinan besar akan diakses lagi dalam waktu dekat.
4. **Overhead:** Implementasi LRU memerlukan pembaruan posisi elemen setiap kali terjadi akses (operasi remove dan append), yang menambah kompleksitas dibanding FIFO sederhana.
5. **Optimal untuk Pola Repetitif:** Untuk aplikasi yang sering dibuka secara bergantian (seperti browser, editor kode, dan aplikasi komunikasi), LRU memberikan performa yang lebih baik dibanding algoritma lain seperti FIFO

# **C. Perbandingan Metrik Kinerja

### Tabel Perbandingan FCFS dan LRU

| Aspek              | FCFS (Kasir)               | LRU (Page Replacement)                      |
| ------------------ | -------------------------- | ------------------------------------------- |
| Kompleksitas Waktu | O(n)                       | O(n × m), dimana *m* adalah kapasitas frame |
| Kompleksitas Ruang | O(n)                       | O(m), dimana *m* adalah kapasitas frame     |
| Optimal untuk      | Sistem sederhana, fairness | Sistem dengan pola akses repetitif          |
| Kelemahan Utama    | Convoy effect              | Overhead pembaruan posisi                   |

## 5. Pembagian Peran dan Kontribusi
Proyek ini dikerjakan secara kolaboratif dengan pembagian tugas yang jelas untuk memastikan setiap modul dapat diselesaikan tepat waktu dan terintegrasi dengan baik. Berikut adalah rincian peran dan kontribusi setiap anggota tim: 

### Tabel Pembagian Tugas Anggota Kelompok

| Nama Anggota | Peran Utama                  | Deskripsi Kontribusi                                                                                                                                                                                                                                                          |
| ------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Miftakhul Lisna Esa Baehaqi        | Project Lead & Integrator    | • Merancang struktur awal proyek dan `main.py`<br>• Mengelola repositori Git (merge PR, resolve conflict)<br>• Membuat konfigurasi `Dockerfile` agar aplikasi berjalan di container<br>• Melakukan pengujian fungsional seluruh modul<br>• Mengumpulkan screenshot bukti demo |
| Ikhsan Mu'arif      | Developer (Modul Scheduling) | • Mengimplementasikan algoritma FCFS pada `kasir_FCFS.py`<br>• Menyusun logika perhitungan waktu tunggu dan waktu selesai<br>• Membuat dataset `pelanggan.csv`<br>• Melakukan unit testing pada modul FCFS                                                                    |
| Ilham Dzufikar Barokah       | Developer (Modul Memory)     | • Mengimplementasikan algoritma LRU pada `page.py`<br>• Membuat visualisasi tabel isi RAM dengan format ASCII<br>• Menyusun dataset `aplikasi.csv` dan skenario uji page fault<br>• Melakukan unit testing pada modul LRU                                                     |
| Asyifani Lutfiana Nadzif       | Documentation & QA           | • Menyusun file `README.md` dan dokumentasi penggunaan<br>• Menyusun dokumen akhir `presentation.md`<br>• Melakukan testing integrasi antar modul<br>• Menyiapkan materi presentasi                                                                                                |
| Hanif Arunndaya Usman      | Data & Support Engineer      | • Membantu validasi dataset dan skenario pengujian<br>• Membantu debugging error saat integrasi modul<br>• Mengecek konsistensi output simulasi FCFS dan LRU<br>• Mendukung proses presentasi dan demo aplikasi                                                               |

## 6. Jawaban Quiz & Penutup

Sebagai bagian dari evaluasi pemahaman, berikut adalah jawaban atas pertanyaan quiz terkait pengembangan proyek ini.

1. **Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?**

**Tantangan:**

Tantangan terbesar dalam integrasi modul adalah memastikan konsistensi path file dataset ketika aplikasi dijalankan di berbagai lingkungan (Windows, Linux, macOS, dan Docker container). Selain itu, menggabungkan dua modul yang memiliki cara kerja berbeda (FCFS yang bekerja sekuensial vs LRU yang melibatkan manipulasi struktur data dinamis) ke dalam satu alur eksekusi di main.py tanpa menimbulkan konflik namespace atau side effects.

**Solusi:**

1. **Modularisasi Ketat:** Kami memisahkan setiap modul ke dalam file terpisah (*(kasir_FCFS.py dan page.py)*) dengan fungsi yang self-contained. Setiap fungsi simulasi tidak berbagi state global, sehingga dapat dipanggil secara independen dari (*main.py.*)
2. **Relative Path:** Menggunakan relative path (*(data/pelanggan.csv dan data/aplikasi.csv)*) yang konsisten di semua platform. Dalam Docker, struktur direktori dijaga agar sama dengan development environment.
3. **Error Handling:** Menambahkan pengecekan keberadaan file sebelum membaca data untuk memberikan pesan error yang informatif jika dataset tidak ditemukan.
4. **Isolation of Concerns:** Di (**main.py*), kami menggunakan percabangan menu sederhana yang hanya memanggil fungsi utama dari tiap modul tanpa perlu mengetahui detail implementasi internal

2. **Mengapa Docker membantu proses demo dan penilaian proyek?**

**Jawaban:**

Docker memberikan beberapa keuntungan signifikan dalam proses demo dan penilaian proyek:

1. **Reproducible Environment:** Docker menciptakan lingkungan yang terisolasi dan konsisten. Masalah klasik "It works on my machine" dapat dihindari karena asisten/dosen penilai tidak perlu mengkhawatirkan perbedaan versi Python, sistem operasi, atau dependensi lainnya.
2. **Portability:** Image Docker yang telah dibuild dapat dijalankan di sistem operasi apa pun (Windows, Linux, macOS) tanpa modifikasi. Ini memastikan aplikasi akan berjalan persis sama di semua platform.
3. **Dependency Isolation:** Semua dependensi aplikasi (dalam hal ini Python 3.14) dibundle dalam container, sehingga tidak akan konflik dengan instalasi Python lain di sistem host.
4. **Easy Setup:** Penilai hanya perlu menjalankan dua perintah sederhana ((*docker build*) dan (*docker run*)) tanpa perlu melakukan konfigurasi kompleks atau instalasi manual.
5. **Clean Execution:** Dengan flag --rm, container otomatis dibersihkan setelah eksekusi selesai, tidak meninggalkan "sampah" di sistem host.
6. **Documentation as Code:** Dockerfile berfungsi sebagai dokumentasi executable yang menjelaskan secara eksplit environment requirements dan setup steps.


3. **Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? Jelaskan.**
**Jawaban:**

**Modul CPU Scheduling (FCFS)** akan paling terdampak performanya, meskipun dalam implementasi saat ini dampaknya masih minimal.

**Analisis Kompleksitas:**

1. **Modul FCFS (kasir_FCFS.py):**
- Operasi pembacaan file: O(n)
- Operasi perhitungan waktu tunggu dan selesai: O(n) dengan loop sederhana
- Operasi print output: O(n)
Total: O(n) secara keseluruhan
- Catatan: Jika ditambahkan fitur sorting berdasarkan waktu kedatangan dengan algoritma seperti Bubble Sort, kompleksitas akan menjadi O(n²), dan peningkatan dataset 10x akan menyebabkan peningkatan waktu eksekusi hingga ~100x.
2. **Modul LRU (page.py):**
- Operasi pembacaan file: O(n)
- Untuk setiap page reference:
    - Operasi in (pencarian): O(m) dimana m = kapasitas frame (3)
    - Operasi remove: O(m)
    - Operasi append: O(1)
    - Operasi pop(0): O(m)
- Total: O(n × m) dimana m adalah konstanta kecil (3 frame)
- Karena m sangat kecil dan konstan, kompleksitas efektif mendekati O(n)

**Kesimpulan:**

Dalam implementasi saat ini, kedua modul memiliki kompleksitas linear O(n), sehingga peningkatan dataset 10x akan meningkatkan waktu eksekusi sekitar 10x untuk kedua modul. Namun, jika dilakukan optimisasi atau penambahan fitur:

- **FCFS** akan lebih terdampak jika ditambahkan fitur sorting (menjadi O(n²))
- **LRU** akan tetap efisien karena m (frame size) adalah konstanta kecil

Skenario Real-World: Jika dataset diperbesar menjadi 10,000 entries:

- **FCFS**: Masih sangat cepat (~milliseconds) untuk operasi linear
- **LRU**: Juga cepat karena m tetap kecil (3 frame), waktu eksekusi masih linear terhadap jumlah page references
Yang perlu diperhatikan adalah memory footprint: memperbesar dataset 10x akan meningkatkan penggunaan memori untuk menyimpan semua data, terutama pada modul FCFS yang menyimpan semua nama dan waktu layanan dalam list.

# 6.2 Kesimpulan

Proyek "Mini Simulasi Sistem Operasi" ini berhasil mencapai seluruh tujuan pembelajaran yang ditetapkan:

1. Integrasi Konsep: Berhasil menggabungkan dua algoritma sistem operasi (FCFS dan LRU) dalam satu aplikasi CLI yang kohesif dan fungsional.
2. Kolaborasi Tim: Pembagian peran yang jelas dan workflow Git yang terstruktur memastikan setiap anggota berkontribusi secara efektif.
3. DevOps Practice: Penerapan Docker membuktikan kesiapan tim dalam praktik pengembangan perangkat lunak modern yang mengutamakan reproducibility dan portability.
4. Pemahaman Mendalam: Melalui implementasi langsung, kami memperoleh pemahaman yang lebih konkret tentang:

- Bagaimana algoritma FCFS bekerja dan kelemahan convoy effect-nya
- Bagaimana algoritma LRU memanfaatkan temporal locality untuk optimasi
- Trade-off antara kesederhanaan implementasi dan efisiensi algoritma


5. Real-World Application: Penggunaan analogi nyata (kasir dan RAM laptop) membantu menghubungkan konsep abstrak sistem operasi dengan situasi yang familiar, membuat pembelajaran lebih intuitif



**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
