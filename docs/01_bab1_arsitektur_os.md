# 01 – Arsitektur Sistem Operasi

## A. Pengantar
Sistem Operasi (OS) merupakan perangkat lunak sistem yang berfungsi mengelola perangkat keras dan menyediakan layanan bagi program aplikasi. Pada pertemuan pertama ini, kita akan mempelajari **arsitektur dasar sistem operasi**: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.

Mahasiswa diperkenalkan pada konsep **mode kernel vs mode user**, **sistem panggilan (syscall)**, serta perbedaan model arsitektur OS seperti **monolithic kernel**, **layered approach**, dan **microkernel**.

---

## B. Tujuan Praktikum
Setelah menyelesaikan praktikum ini, mahasiswa mampu:
1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS dengan alat bantu digital (draw.io / mermaid).

---

## C. Indikator Pencapaian
- Mahasiswa dapat membuat diagram arsitektur OS yang benar.  
- Mahasiswa dapat menjelaskan perbedaan **monolithic kernel** dan **microkernel**.  
- Mahasiswa mampu menuliskan ringkasan peran kernel dan syscall dalam interaksi program dengan hardware.  

---

## D. Materi Pokok
1. **Komponen OS**: Kernel, Shell, Device Driver, File System, System Libraries.  
2. **Mode Operasi CPU**: User Mode vs Kernel Mode.  
3. **System Call**: mekanisme komunikasi antara program aplikasi dengan kernel.  
4. **Model Arsitektur**:
   - Monolithic Kernel  
   - Layered OS  
   - Microkernel  
   - Hybrid  

---

## E. Langkah Praktikum
1. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen apa saja yang ada di Linux/Windows/Android.

2. **Membuat Diagram Arsitektur**
   - Gunakan draw.io, Mermaid, atau diagram ASCII sederhana.
   - Tampilkan hubungan antara hardware → kernel → system call → aplikasi → user.

3. **Eksperimen Ringan**
   - Jalankan perintah `uname -a`, `lsmod`, dan `dmesg | head` di Linux.
   - Catat modul kernel yang tampil dan fungsinya.
   - Analisis: mengapa OS membutuhkan kernel dan driver?

---

## F. Tugas
1. Buatlah diagram arsitektur OS (format PNG/SVG) dan simpan di:
```
praktikum/week1-intro-arsitektur-os/screenshots/
```
2. Tuliskan ringkasan (±500 kata) berisi:
- Perbedaan monolithic kernel, microkernel, dan layered architecture.
- Contoh OS nyata yang menggunakan masing-masing model.
- Analisis: model mana yang paling relevan untuk sistem modern?
3. Tambahkan ke `laporan.md` dalam folder minggu ini.
```
praktikum/week1-intro-arsitektur-os/laporan.md
```
4. Commit & push hasil ke repositori pribadi GitHub.

---

## G. Referensi
1. Abraham Silberschatz, Peter Baer Galvin, Greg Gagne. *Operating System Concepts*, 10th Edition, Wiley, 2018.  
2. Andrew S. Tanenbaum, Herbert Bos. *Modern Operating Systems*, 4th Edition, Pearson, 2015.  
3. Linux Kernel Documentation – https://www.kernel.org/doc/  
,
