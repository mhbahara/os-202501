# Tugas Praktikum Minggu 1  
Topik: Arsitektur Sistem Operasi  

---

## A. Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **arsitektur dasar sistem operasi**: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.  

Mahasiswa juga diperkenalkan pada:
- Perbedaan mode eksekusi **kernel mode** dan **user mode**.
- Mekanisme **system call** (panggilan sistem).
- Perbandingan model arsitektur OS seperti **monolithic kernel**, **layered approach**, dan **microkernel**.

Eksperimen akan dilakukan menggunakan perintah dasar Linux untuk melihat informasi kernel dan modul aktif.

---

## B. Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).

---

## C. Langkah Pengerjaan
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
   ```

---

## D. Tugas & Quiz
### Tugas
1. Buat diagram arsitektur OS (format PNG/SVG).  
2. Tuliskan ringkasan (±500 kata) mencakup:
   - Perbedaan *monolithic kernel*, *microkernel*, dan *layered architecture*.
   - Contoh OS yang menerapkan tiap model.
   - Analisis: model mana yang paling relevan untuk sistem modern.  
3. Tambahkan hasil ke `praktikum/week1-intro-arsitektur-os/laporan.md`.

### Quiz
Jawab pertanyaan berikut di bagian **Quiz** pada laporan:
1. Sebutkan tiga fungsi utama sistem operasi.  
2. Jelaskan perbedaan antara *kernel mode* dan *user mode*.  
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.

---

## E. Output yang Diharapkan
- File laporan (`laporan.md`) lengkap dengan hasil observasi.  
- Diagram arsitektur OS (`diagram-os.png`).  
- File hasil terminal (`screenshots/`).  
- Semua artefak sudah di-*commit* ke repositori pribadi GitHub.

---

## F. Referensi
1. Abraham Silberschatz, Peter Baer Galvin, Greg Gagne. *Operating System Concepts*, 10th Edition, Wiley, 2018.  
2. Andrew S. Tanenbaum, Herbert Bos. *Modern Operating Systems*, 4th Edition, Pearson, 2015.  
3. OSTEP – *Operating Systems: Three Easy Pieces*, 2018.  
4. Linux Kernel Documentation – https://www.kernel.org/doc/
