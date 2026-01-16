
# Laporan Praktikum Minggu 1
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Farhan Ramdhani  
- **NIM**   : 250202938  
- **Kelas** : 1IKRB

---

## Tujuan
1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).

---

## Dasar Teori
Sistem operasi merupakan komponen utama dalam komputer yang berfungsi mengelola sumber daya perangkat keras dan perangkat lunak. Inti dari sistem operasi adalah kernel, yang bertugas menghubungkan komunikasi antara perangkat keras dan aplikasi pengguna. Terdapat beberapa jenis arsitektur kernel yang digunakan dalam pengembangan sistem operasi, yaitu Monolithic Kernel, Microkernel, dan Layered Architecture. Masing-masing memiliki karakteristik, kelebihan, kekurangan, serta implementasi berbeda pada sistem operasi yang ada saat ini.

---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
![alt text](<../week1-intro-arsitektur-os/screenshots/Screenshot 2025-10-09 164355.png>)

![alt text](<../week1-intro-arsitektur-os/screenshots/Screenshot 2025-10-09 185033.png>)

---

## Tugas
- Analisis Perbedaan Monolithic Kernel, Micro Kernel, dan Layered Architecture
- Jenis-Jenis, Pengertian, Kelebihan, Kekurangan dan Contoh Sistem Operasi
### 1. Monolithic Kernel

**Pengertian :**

Monolithic Kernel adalah arsitektur kernel di mana seluruh komponen sistem operasi, seperti manajemen memori, sistem berkas, dan driver perangkat keras, dijalankan di dalam satu ruang kernel (kernel space).

**Kelebihan :**

- Kinerja tinggi karena komunikasi antar komponen dilakukan langsung tanpa perantara.

- Penggunaan sumber daya relatif efisien.

**Kekurangan :**

- Sulit dikembangkan karena semua bagian saling terhubung.

- Jika satu bagian mengalami kesalahan, seluruh sistem bisa mengalami crash.

**Contoh Sistem Operasi :**

- Linux

- UNIX

- MS-DOS

### 2. Microkernel

**Pengertian :**

Microkernel memiliki struktur yang lebih sederhana dan modular. Fungsi dasar seperti manajemen memori, komunikasi antar proses (IPC), dan pengendalian perangkat keras dijalankan di ruang kernel. Sementara itu, layanan lainnya seperti sistem berkas dan driver dijalankan di ruang pengguna (user space).

**Kelebihan :**

- Lebih stabil dan aman karena kesalahan pada satu layanan tidak memengaruhi kernel secara langsung.

- Lebih mudah dikembangkan dan diperbarui.

**Kekurangan :**

Kinerja bisa menurun karena banyak komunikasi antar proses dilakukan melalui pesan.
**Contoh Sistem Operasi :**

- Minix

- QNX

- macOS (berbasis Mach Microkernel)

### 3. Layered Architecture

**Pengertian :**
 Layered Architecture merupakan struktur sistem operasi yang dibangun secara berlapis (layered system). Setiap lapisan memiliki fungsi tertentu dan hanya dapat berinteraksi dengan lapisan di atas atau di bawahnya.

**Kelebihan :**

- Desain lebih terorganisasi dan mudah dipahami.

- Proses pengembangan dan pemeliharaan sistem lebih mudah dilakukan.

**Kekurangan :**

- Proses dapat menjadi lebih lambat karena harus melewati beberapa lapisan.

- Perancangan awal sistem lebih kompleks dibanding arsitektur lain.

**Contoh Sistem Operasi :**

- THE Operating System

- MULTICS

- UNIX versi awal

### Model yang Paling Relevan untuk Sistem Modern
Dalam sistem operasi modern, kebutuhan utama mencakup keamanan tinggi, stabilitas, dan efisiensi kinerja. Oleh karena itu, arsitektur yang paling relevan saat ini adalah Hybrid Kernel, yang merupakan kombinasi dari konsep Monolithic Kernel dan Microkernel. Hybrid Kernel mempertahankan kinerja cepat seperti Monolithic Kernel, tetapi tetap mengadopsi modularitas dan keamanan dari Microkernel. Model ini digunakan dalam berbagai sistem operasi modern seperti :
- Windows NT / Windows 10 / Windows 11

- macOS (XNU Kernel)

- Android (berbasis Linux Kernel yang dimodifikasi)

---

## Analisis
- Jelaskan makna hasil percobaan.  
**Jawaban :** Dari hasil percobaan dan pembuatan diagram arsitektur OS, dapat dipahami bahwa komunikasi antara pengguna dan perangkat keras komputer tidak berlangsung secara langsung. User berinteraksi melalui system call, yang menjadi pintu masuk menuju kernel. Kernel kemudian mengatur akses ke perangkat keras seperti memori, prosesor, dan penyimpanan agar proses berjalan aman dan efisien.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
**Jawaban :** Kernel berfungsi sebagai inti dari sistem operasi yang mengelola sumber daya sistem. System call menjadi jembatan antara program aplikasi (user mode) dengan kernel (kernel mode). Arsitektur OS menunjukkan bagaimana lapisan-lapisan ini saling berhubungan, memastikan keamanan dan stabilitas sistem dalam mengakses perangkat keras.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
**Jawaban :** Di Linux, system call bersifat terbuka dan mudah diamati menggunakan perintah seperti strace, sedangkan di Windows system call bersifat tertutup dan diatur melalui API sistem. Kernel Linux juga bersifat monolitik, sedangkan Windows menggunakan arsitektur hibrid (gabungan monolitik dan microkernel) untuk fleksibilitas dan keamanan yang lebih tinggi

---

## Kesimpulan
1. Kernel merupakan komponen inti yang menghubungkan antara perangkat lunak dan perangkat keras.
2. System call memungkinkan program aplikasi berinteraksi dengan kernel secara terkontrol.
3. Setiap sistem operasi memiliki cara berbeda dalam menerapkan arsitektur OS, namun prinsip dasarnya sama: menjembatani interaksi antara user dan hardware secara aman.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.

   **Jawaban:**  Mengelola sumber daya perangkat keras, menyediakan antarmuka untuk pengguna (user interface), dan mengatur eksekusi program serta keamanan sistem.

2. Jelaskan perbedaan antara *kernel mode* dan *user mode*.

   **Jawaban:**  User mode digunakan untuk menjalankan aplikasi pengguna dengan hak akses terbatas.
Kernel mode memiliki hak akses penuh terhadap perangkat keras dan sumber daya sistem.
Mode ini mencegah aplikasi biasa merusak sistem inti.

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.

   **Jawaban:**  Monolithic kernel: Linux, Unix.
Microkernel: Minix, QNX, dan Mach.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
**Jawaban :** Bagian paling menantang adalah memahami peran system call dalam alur kerja antara user dan kernel, karena konsepnya bersifat abstrak dan tidak terlihat secara langsung.

- Bagaimana cara Anda mengatasinya?  
**Jawaban :** Saya mempelajari kembali materi dari modul praktikum, mencari contoh nyata di Linux menggunakan perintah lsmod dan dmesg, serta membuat diagram di draw.io agar lebih mudah memahami alurnya.

---

## Daftar Referensi
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts (10th Edition). Wiley.
2. Tanenbaum, A. S., & Bos, H. (2015). Modern Operating Systems (4th Edition). Pearson.
3. Stallings, W. (2018). Operating Systems: Internals and Design Principles (9th Edition). Pearson.
4. Linux Kernel Documentation – https://www.kernel.org/doc/
5. Apple Developer Documentation – XNU Kernel Overview, https://developer.apple.com/

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_