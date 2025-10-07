

praktikum/week1-intro-arsitektur-os/screenshots/

---

<img width="3264" height="3264" alt="Image" src="https://github.com/user-attachments/assets/1c9a5d65-2a86-44f7-aaf1-1e27ae270732" />

praktikum/week1-intro-arsitektur-os/laporan.md

---

# Laporan: Arsitektur Kernel Sistem Operasi

## 1. Perbedaan Monolithic Kernel, Microkernel, dan Layered Architecture

Kernel itu ibarat “otak” dari sistem operasi. Tugasnya ngatur semua hal yang berhubungan antara perangkat keras (hardware) dan perangkat lunak (software). Nah, cara kerja kernel ini beda-beda tergantung dari arsitekturnya. Ada tiga jenis yang paling umum: **monolithic**, **microkernel**, dan **layered**.

Pertama, **monolithic kernel**. Di model ini, semua fungsi penting sistem operasi kayak manajemen memori, proses, file system, sampai driver perangkat, dijalankan bareng di satu tempat (kernel space). Karena semua nyatu, sistem jadi lebih cepat. Tapi kekurangannya, kalau ada satu bagian error, bisa bikin sistem langsung crash. Jadi cepat, tapi agak berisiko.

Kedua, **microkernel**. Di sini, bagian utama kernel dibuat sekecil mungkin. Hanya fungsi penting kayak komunikasi antar-proses dan manajemen memori yang dijalankan di kernel. Komponen lain seperti driver dan file system dijalankan di luar (user space). Kelebihannya, sistem lebih aman dan stabil, karena kalau satu layanan rusak, yang lain tetap jalan. Tapi karena komunikasi antar-bagiannya lebih rumit, performanya kadang sedikit lebih lambat.

Ketiga, **layered architecture**. Model ini mirip sistem berlapis, di mana setiap lapisan punya tugas masing-masing. Lapisan bawah berhubungan dengan hardware, sementara lapisan atas berhubungan dengan pengguna. Model ini gampang dijelaskan dan dirancang, tapi karena harus lewat beberapa lapisan, prosesnya bisa lebih lambat dibanding dua model sebelumnya.

---

## 2. Contoh Sistem Operasi yang Menggunakan Masing-Masing Model

Contoh **monolithic kernel** bisa dilihat di **Linux** dan **Unix**. Kedua sistem ini terkenal cepat dan sering dipakai di server.  
Untuk **microkernel**, contohnya **Minix** dan **QNX**, biasanya dipakai di sistem tertanam kayak mobil atau alat industri. **macOS** juga pakai kernel gabungan (hybrid) yang dasarnya microkernel tapi ada elemen monolithic-nya juga.  
Sedangkan **layered architecture** contohnya sistem lama **THE Operating System**, yang sering dipakai untuk belajar konsep sistem operasi.

---

## 3. Model yang Paling Cocok Buat Sistem Sekarang

Kalau lihat kebutuhan zaman sekarang, sistem operasi modern butuh yang cepat, aman, dan fleksibel. Karena itu, model **hybrid** atau gabungan antara monolithic dan microkernel jadi pilihan paling pas.  

Contohnya, **Windows 10/11** dan **macOS** pakai model hybrid, sedangkan **Linux** tetap monolithic tapi sudah bisa dimodifikasi lewat modul. Jadi bisa dibilang Linux sekarang juga cukup fleksibel.

**Microkernel murni** cocok untuk perangkat kecil atau sistem khusus yang butuh stabilitas tinggi, bukan kecepatan. Sementara model **layered** lebih sering dipakai buat pembelajaran aja, bukan di sistem nyata.

---

## Kesimpulan

Singkatnya, **monolithic kernel** itu cepat tapi rawan error, **microkernel** lebih aman tapi agak lambat, dan **layered** itu gampang dimengerti tapi kurang efisien. Untuk sistem modern, **kernel hybrid** adalah pilihan terbaik karena bisa menyeimbangkan performa, keamanan, dan kemudahan pengembangan.

---
