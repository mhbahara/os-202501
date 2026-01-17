# Laporan Praktikum Minggu 1
# Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Faiq Atha Rulloh
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---

## Tujuan

 Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
1. Arsitektur Sistem Operasi

Arsitektur sistem operasi mengacu pada cara struktur dan komponen sistem operasi diorganisasi. Secara umum, sistem operasi terdiri dari beberapa lapisan atau komponen berikut:
- Lapisan Pengguna (User Space)
- Lapisan Sistem (Kernel Space)
- Antarmuka Sistem Operasi (System Call Interface)
- Perangkat Keras (Hardware)

 2. Kernel

Kernel adalah komponen inti dari sisPerangkattem operasi yang bertugas mengelola sumber daya komputer, seperti CPU, memori, perangkat I/O, serta proses yang berjalan. Kernel memiliki berbagai fungsi penting dan biasanya terpisah dari aplikasi pengguna untuk meningkatkan stabilitas dan keamanan sistem.


---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

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
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/2025-10-10 (1).png>)

---

## Analisis
- Jelaskan makna hasil percobaan?
1. hasil dari perintah uname -a di terminal Linux, yang menampilkan informasi lengkap tentang kernel dan sistem operasi yang sedang berjalan.
2. hasil Perintah whoami dalam sistem operasi Linux digunakan untuk menampilkan nama pengguna (username) yang sedang aktif atau login ke sistem saat ini.
3. Perintah lsmod | head digunakan di Linux untuk menampilkan modul kernel yang sedang dimuat (loaded) ke dalam sistem, lalu membatasi output hanya pada 10 baris pertama menggunakan head.
4. Perintah dmesg | head digunakan untuk menampilkan 10 baris pertama dari log kernel yang dihasilkan oleh perintah dmesg. Log ini berisi pesan-pesan dari kernel Linux yang muncul saat sistem booting atau saat perangkat keras dikenali.

---

- Jelaskan perbedaan antara kernel mode dan user mode?

1. Kernel Mode
Kernel mode adalah mode eksekusi yang memungkinkan program untuk memiliki akses penuh ke seluruh perangkat keras dan memori sistem. Ini adalah tingkat akses tertinggi dalam sistem operasi. 
2. User Mode
User mode adalah mode eksekusi dengan tingkat akses terbatas yang dimiliki oleh aplikasi atau program yang dijalankan oleh pengguna. 

---

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  
Linux dan Windows memiliki konsep dasar yang sama dalam hal kernel mode dan user mode, implementasinya sangat berbeda. Linux lebih menekankan pada keterbukaan dan kontrol lebih mendalam terhadap sistem, sementara Windows fokus pada kenyamanan pengguna dan kompatibilitas perangkat keras, dengan keamanan dan pengelolaan sistem yang lebih terpadu melalui antarmuka grafis dan layanan terintegrasi.

---

## Kesimpulan

**Kernel Mode dan User Mode:**

Dalam konteks keamanan dan stabilitas, kernel mode memberikan kontrol penuh terhadap perangkat keras dan memori, tetapi juga memiliki potensi untuk merusak sistem jika ada kesalahan. Sebaliknya, user mode memberikan isolasi dan melindungi sistem dari aplikasi yang bisa saja menyebabkan kerusakan.

**Linux dan Windows:**

Linux memberikan kebebasan lebih dalam hal kontrol sistem, tetapi memerlukan pengetahuan teknis yang lebih dalam untuk mengelola dan menyesuaikan. Windows, di sisi lain, memberikan kenyamanan dan aksesibilitas, tetapi dengan keterbatasan dalam hal kontrol penuh terhadap sistem dan perangkat keras.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi:

*Tiga fungsi utama dari sistem operasi adalah:*

- Manajemen Proses: Sistem operasi mengelola proses yang berjalan di dalam komputer. Ini mencakup pembuatan, penjadwalan, dan penghentian proses, serta mengatur agar setiap proses mendapatkan waktu pemrosesan yang adil dan efisien. 

- Manajemen Memori: Sistem operasi bertanggung jawab untuk mengelola memori utama (RAM), termasuk pembagian memori antara proses yang berjalan. Ini juga mencakup pengelolaan ruang memori virtual, penanganan alokasi dan dealokasi memori, serta memastikan tidak ada proses yang saling mengganggu dalam hal akses memori.

- Manajemen Perangkat I/O (Input/Output): Sistem operasi mengelola perangkat keras input dan output seperti keyboard, mouse, printer, dan disk. Ini melibatkan pengaturan perangkat untuk komunikasi antara perangkat keras dan perangkat lunak, serta menyediakan antarmuka yang efisien dan terkontrol untuk mengakses perangkat-perangkat tersebut.

--- 

2. Jelaskan perbedaan antara kernel mode dan user mode.  
   
  *Kernel Mode:*

Kernel mode adalah mode eksekusi di mana program memiliki akses penuh dan tak terbatas ke semua sumber daya perangkat keras dan memori sistem. 

Fungsi:
- Pengelolaan memori.
- Manajemen perangkat I/O (Input/Output).
- Penjadwalan proses.
-  interupsi dan kesalahan.
- Pengelolaan sistem file.

Contoh:

Sistem operasi iKtu sendiri (kernel).
Driver perangkat keras.

 *User Mode:*

User mode adalah mode eksekusi dengan akses terbatas yang dimiliki oleh aplikasi atau program yang dijalankan oleh pengguna.

Fungsi: 
- Menjalankan aplikasi pengguna (misalnya browser, pengolah kata, dll).
- Melakukan perhitungan atau manipulasi data.
- Mengelola antarmuka pengguna (GUI).

Contoh:Aplikasi pengguna seperti Microsoft Word, Chrome, atau pemutar media.


---

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
   
    1. Monolithic Kernel:

Sistem operasi dengan monolithic kernel memiliki semua fungsionalitas kernel (manajemen memori, penjadwalan, komunikasi antar proses, manajemen perangkat keras, dll.) dalam satu kode besar yang berjalan di tingkat kernel. Kernel ini mengelola hampir seluruh aspek dari sistem operasi dan biasanya memberikan performa yang lebih tinggi, namun lebih kompleks dalam hal pengelolaan dan pemeliharaan.
Contoh OS dengan Monolithic Kernel:
- Linux
- Unix
- BSD (Berkeley Software Distribution)
- Xv6

---

2. Microkernel:
Sistem operasi dengan microkernel memisahkan sebagian besar fungsionalitasnya ke dalam modul-modul yang berjalan di luar kernel. Hanya komponen dasar seperti manajemen memori, penjadwalan proses, dan komunikasi antar proses yang dijalankan dalam kernel, sementara fungsi lainnya seperti driver perangkat keras dan sistem file dijalankan di ruang pengguna (user space). Pendekatan ini meningkatkan fleksibilitas dan isolasi, meskipun seringkali bisa menurunkan performa dibandingkan dengan monolitik.
Contoh OS dengan Microkernel:
- Minix
- QNX
- L4
- HURD
- Mach

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
 Yang paling menantang pada minggu ini adalah cara penggunaan fungsi perintah pada aplikasi linux
- Bagaimana cara Anda mengatasinya?  
cara mengatasinya adalah terus mencoba dan mencari referensi dari AI,book dll

---
# Arsitektur Sistem Operasi

Sistem Operasi (OS) merupakan perangkat lunak sistem yang berfungsi mengelola perangkat keras dan menyediakan layanan bagi program aplikasi. Pada pertemuan pertama ini, kita akan mempelajari arsitektur dasar sistem operasi: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.

## Tugas

1. Perbedaan monolithic kernel, microkernel, dan layered architecture.
2. Contoh OS nyata yang menggunakan masing-masing model.
3. Analisis: model mana yang paling relevan untuk sistem modern?

## Jawaban

### 1. Perbedaan Arsitektur Kernel

#### Monolithic Kernel
**Konsep:** “Semua dalam satu.” Semua layanan inti sistem operasi (seperti manajemen memori, penjadwalan proses, sistem file, driver perangkat) dijalankan dalam ruang alamat yang sama dengan kernel.

**Kelebihan:**
- Performanya sangat tinggi karena tidak ada overhead perubahan mode untuk komunikasi antar layanan inti.
- Komunikasi antar komponen kernel sederhana dan cepat.

**Kekurangan:**
- Stabilitas dan Keamanan Lebih Rendah.
- Sulit Diperbesar (Less Scalable) dan Kompleks.
- Ukuran kernel menjadi sangat besar.

#### Microkernel (Kernel Mikro)
**Konsep:** “Minimalis.” Kernel hanya berisi fungsi-fungsi yang paling penting dan mendasar, seperti manajemen memori minimal, penjadwalan proses (scheduler), dan komunikasi antar proses (IPC). Layanan lainnya (seperti driver, sistem file, network stack) dijalankan sebagai proses server di ruang user (user space).

**Kelebihan:**
- Stabilitas dan Keamanan Tinggi.
- Modularitas dan Kemudahan Pertuasan.
- Portabilitas.

**Kekurangan:**
- Overhead Performa.

#### Layered Architecture (Arsitektur Berlapis)
**Konsep:** Sistem operasi diorganisir dalam lapisan-lapisan (layer/tingkatan), di mana setiap lapisan dibangun di atas lapisan yang lebih rendah.

**Kelebihan:**
- Desain yang Terstruktur dan Modular.
- Abstraksi.

**Kekurangan:**
- Overhead Performa.
- Kekakuan.

### 2. Contoh OS Nyata

#### Monolithic Kernel
- **Linux** (Ubuntu, Fedora, Debian, CentOS, dll)
- **Unix Tradisional** (BSD: FreeBSD, OpenBSD, Solaris versi awal)
- **MS-DOS & Windows 9x** (Windows 95/98/ME)

#### Microkernel
- **QNX**
- **MINIX 3**
- **GNU Hurd**
- **L4 Microkernel**

#### Layered Architecture
- **THE Operating System**
- **MULTICS**
- **Windows NT (Versi Awal)**

### 3. Analisis: Model Paling Relevan untuk Sistem Modern

Model paling relevan untuk sistem modern adalah **Hybrid Kernel** (gabungan Monolithic + Microkernel) karena:

- Mengambil performa tinggi dari monolithic kernel.
- Mengadopsi modularitas dan keamanan dari microkernel.

**Contohnya:**
- Windows NT
- macOS (XNU)
- Linux modular (dengan loadable kernel modules)

### Diagram Arsitektur 
![Screenshot hasil](<screenshots/Diagram Arsitektur OS.drawio (1).png>)



**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
