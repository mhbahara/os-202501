
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Rifki Hidayat]  
- **NIM**   : [250202964]  
- **Kelas** : [1IKRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan dasar dasar arsitektur dan sistem operasi.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
<img width="1184" height="665" alt="rifki" src="https://github.com/user-attachments/assets/f6fe3e90-607c-4704-8bce-dcad3b39687f" />

---

## Analisis
uname -a adalah perintah di Linux yang digunakan untuk menampilkan semua informasi detail tentang sistem, termasuk nama kernel, nama mesin.
Perintah 1smod digunakan untuk menampilkan daftar modul kernel yang saat ini sedang dimuat (loaded) di sistem.

Modul kernel ini bisa berupa driver perangkat keras atau modul fungsional lainnya yang digunakan oleh kernel Linux Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).

Hubungkan hasil dengan teori

Hasil dapat dihubungkan dengan fungsi kernel sebagai inti sistem operasi yang menjembatani hardware dan software; panggilan sistem ((syscall)) sebagai jembatan antara aplikasi pengguna dan kernel untuk meminta layanan; dan arsitektur OS yang mendefinisikan struktur ini, di mana kernel menjadi komponen sentral yang mengelola sumber daya melalui panggilan sistem.

Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?

Perbedaan hasil antara Linux dan Windows terlihat dari struktur sistem file (garis miring / di Linux vs "C:\ di Windows), cara penamaan berkas (bisa ada dua berkas dengan nama sama di direktori berbeda di Linux, tidak bisa di Windows), sistem partisi (Linux lebih fleksibel, Windows mendukung partisi Linux namun Linux belum tentu mendukung partisi Windows), dan penggunaan baris perintah (terminal di Linux lebih ampuh, cmd di Windows lebih terbatas).

---

## Kesimpulan
Monolithic kernel adalah arsitektur sistem operasi di mana semua layanan inti OS, seperti manajemen memori, penjadwalan proses, dan manajemen perangkat keras, berjalan dalam satu ruang alamat (satu program besar) bagian dapat menyebabkan crash seluruh. Mikrokernel adalah jenis kernel sistem operasi yang hanya berisi fungsionalitas inti minimal, seperti manajemen memori dan komunikasi antarproses (IPC), sementara layanan lainnya (seperti driver perangkat dan sistem berkas) berjalan di ruang pengguna Arsitektur berlapis (layered architecture) adalah pola desain perangkat lunak yang membagi aplikasi menjadi beberapa lapisan terpisah, di mana setiap lapisan memiliki tanggung jawab tertentu dan hanya berinteraksi dengan lapisan di bawahnya, sebagai server terpisah.

---

## Quiz
Sebutkan tiga fungsi utama sistem operasi Tiga fungsi utama sistem operasi (OS) adalah: Manajemen Sumber Daya: Mengelola perangkat keras (CPU, memori, I/O). Antarmuka Pengguna: Menyediakan cara bagi pengguna untuk berinteraksi dengan komputer (misalnya, melalui GUI). Eksekusi Program: Menyediakan lingkungan untuk menjalankan aplikasi. 2.Jelaskan perbedaan antara kernel mode dan user mode. Berikut perbedaannya: Kernel Mode (Istimewa): Kontrol penuh atas hardware, tempat OS berjalan. Kegagalan berarti sistem crash. User Mode (Terbatas): Akses terbatas ke hardware, tempat aplikasi berjalan. Kegagalan hanya membuat aplikasi crash.
3.Sebutkan contoh OS dengan arsitektur monolithic dan microkernel. Monolithic Kernel: Semua layanan inti OS berada dalam satu blok di Kernel. Contoh: Linux, Solaris. Microkernel: Hanya fungsi dasar yang ada di Kernel; layanan lain berjalan terpisah di luar Kernel. Contoh: QNX, Hurd.

---

## Refleksi Diri
Tuliskan secara singkat:
kesushan di bagian codingnya  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
