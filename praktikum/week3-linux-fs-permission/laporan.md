
# Laporan Praktikum Minggu [X]
Pengelolaan file dan direktori menggunakan perintah dasar Linux, serta konsep permission dan ownership.

---

## Identitas
- **Nama**  : [Miftakhul Lisna Esa Baehaqi]  
- **NIM**   : [250202951]  
- **Kelas** : [1IKRB]

---

## Tujuan
-Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
-Menggunakan chmod dan chown untuk manajemen hak akses file.
-Menjelaskan hasil output dari perintah Linux dasar.
-Menyusun laporan praktikum dengan struktur yang benar

---

## Dasar Teori
- Ringkasan Teori Dasar Linux File System
Struktur File Hierarkis (Root Directory):
Sistem berkas Linux diorganisasi dalam struktur pohon tunggal yang disebut hierarki direktori, berakar pada direktori root (/). Semua file dan direktori lain, termasuk disk drive dan perangkat keras, dipasang (mounted) di bawah hirarki ini. Pemahaman ini penting karena semua perintah pengelolaan file (ls, cd, mkdir, dll.) beroperasi dalam konteks struktur jalur (path) ini.

- Perintah Dasar CLI (Command Line Interface):
Pengelolaan file dan direktori di Linux sangat bergantung pada perintah baris yang spesifik. Perintah dasar seperti ls (melihat), cd (berpindah), mkdir (membuat direktori), cp (menyalin), dan mv (memindahkan/mengganti nama) adalah alat utama yang memungkinkan pengguna berinteraksi dan memanipulasi file system secara efisien tanpa antarmuka grafis.

- Konsep Ownership (Kepemilikan):
Setiap file atau direktori di Linux harus memiliki dua entitas kepemilikan: seorang Pemilik (Owner), yang diwakili oleh User ID (UID), dan Grup Pemilik (Group), yang diwakili oleh Group ID (GID). Konsep ini mendasari keamanan awal sistem. Perintah chown (change owner) digunakan untuk memanipulasi kepemilikan ini, biasanya memerlukan hak akses root (sudo).

- Konsep Permissions (Hak Akses):
Permissions adalah mekanisme keamanan utama yang mengontrol apa yang dapat dilakukan terhadap file oleh tiga kategori pengguna: Owner, Group, dan Others. Ada tiga jenis hak akses: Read (Baca - r), Write (Tulis - w), dan Execute (Eksekusi - x). Perintah chmod (change mode) digunakan untuk memodifikasi hak akses ini, baik melalui notasi simbolik (u+w) maupun notasi numerik (oktal) (755).

- Prinsip Everything is a File:
Dalam filosofi Unix/Linux, segalanya, termasuk direktori, perangkat keras (hardware), dan soket (socket), diperlakukan sebagai file. Ini menyederhanakan cara sistem mengelola sumber daya dan merupakan alasan mengapa direktori juga memiliki permissions (rwx) yang sama dan dapat dimanipulasi dengan chmod dan chown.




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
![Screenshot pwd](./screenshots/screenshot%20pwd.png)
![screenshot n5](./screenshots/eksperimen%202%20head%20n5.png)
![hasil dokumentasi percobaan](./screenshots/dokumentasi%204.png)

---

## Analisis
 Jelaskan makna hasil percobaan. 
Dalam percobaan ini Mengetahui bagaimana program ls (list directory) berinteraksi dengan sistem operasi melalui system call — yaitu layanan yang disediakan kernel untuk program user.
-Berdasarkan hasil percobaan strace cat /etc/passwd, dapat disimpulkan bahwa kernel berfungsi sebagai pengendali utama dalam eksekusi operasi file melalui system call. Proses perpindahan antara user mode dan kernel mode membuktikan konsep arsitektur berlapis pada sistem operasi, di mana setiap akses ke sumber daya harus melalui kernel untuk menjamin keamanan dan stabilitas sistem.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS). 
- Kernel menangani semua operasi I/O (membuka, membaca, menulis, menutup file) atas perintah dari program user. Tanpa kernel, program tidak bisa mengakses perangkat keras secara aman.
- strace memperlihatkan bagaimana system call menjadi jembatan komunikasi antara program cat (di user mode) dan kernel (di kernel mode).
- Percobaan strace membuktikan konsep transisi mode (user ↔ kernel) yang merupakan ciri khas arsitektur sistem operasi berlapis (layered architecture), di mana lapisan aplikasi tidak dapat langsung mengakses hardware, tetapi harus melalui lapisan kernel. 
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
- Walaupun kedua OS memiliki tujuan yang sama (menghubungkan program dengan hardware melalui kernel), implementasi dan nama system call berbeda.
Linux mengikuti standar POSIX dengan system call terbuka dan dapat dilacak melalui strace, sedangkan Windows menggunakan API tertutup yang berlapis (Win32 → NTDLL → Kernel), sehingga lebih sulit dilihat langsung oleh pengguna.
---

## Kesimpulan
## kesimpulan dari eksperimen 1 

pwd
ls -l
cd /tmp
ls -a

- hasil dari perintah pwd adalah = Menampilkan direktori kerja saat ini.

- hasil dari perintah  ls -l adalah = Melihat daftar isi (file dan direktori) dari suatu direktori.

- hasil perintah dari cd /tmp adalah = perpindahan direktori kerja saat ini (Current Working Directory) Anda ke direktori
- hasil perintah dari ls -a adalah =  menampilkan daftar semua file dan direktori
  
  ## Kesimpulan dari ekperimen 2 membaca file perintah.
isi file dan struktur barisnya (user, UID, GID, home, shell)

1. Username (Nama Pengguna)
Ini adalah nama yang digunakan pengguna untuk masuk (login) ke sistem.

Contoh: root, siswa, www-data.

2. UID (User ID)
Ini adalah nomor unik yang digunakan sistem operasi untuk mengidentifikasi akun pengguna secara numerik.

UID 0: Selalu dialokasikan untuk pengguna root (administrator sistem), yang memiliki hak akses penuh.

UID 1-999 (atau 1-499 pada distribusi lama): Biasanya dialokasikan untuk akun sistem (seperti daemon, bin, lp) yang menjalankan layanan di latar belakang.

UID 1000 ke atas: Biasanya dialokasikan untuk akun pengguna biasa yang dibuat oleh administrator.

3. GID (Group ID)
Ini adalah nomor unik yang mengidentifikasi grup utama tempat pengguna tersebut berada.

Fungsi: Ketika pengguna membuat file baru, kepemilikan grup file tersebut secara default akan diatur ke GID utama ini.

Contoh: Jika GID adalah 1000, pengguna tersebut termasuk dalam grup dengan GID 1000.

4. Home Directory (Direktori Rumah)
Ini adalah lokasi awal tempat pengguna akan ditempatkan setelah berhasil login.

Fungsi: Tempat pengguna menyimpan file-file pribadinya, dokumen, dan pengaturan aplikasi.

Contoh: /root untuk pengguna root, dan /home/siswa untuk pengguna siswa.

5. Shell (Program Shell)
Ini adalah jalur absolut (absolute path) ke program yang akan dijalankan sebagai shell interpretif (antarmuka baris perintah) segera setelah pengguna login.

Contoh:

/bin/bash atau /bin/zsh: Menunjukkan pengguna memiliki akses shell interaktif penuh.

/usr/sbin/nologin atau /bin/false: Menunjukkan bahwa akun tersebut adalah akun sistem dan tidak diizinkan untuk login secara interaktif.

## kesimpulan Eksperimen 3 – Permission & Ownership 

Perintah chmod 600 membuat file sangat pribadi. Hanya Owner (userku) yang dapat membaca dan menulis ke file tersebut. Semua hak akses untuk Group dan Others dicabut, sehingga tidak ada orang lain di sistem yang dapat melihat atau mengubah isi file tersebut.


---

## Quiz
1. [Apa fungsi dari perintah chmod?
]  
   untuk mengubah hak akses (permissions) dari sebuah file atau direktori pada sistem operasi Linux dan Unix-like 
2. [Apa arti dari kode permission rwxr-xr--?]
   menunjukkan hak akses (izin) file atau direktori yang sangat spesifik untuk tiga kelompok pengguna di Linux: Pemilik (Owner), Grup (Group), dan Lainnya (Others)  
3. [Jelaskan perbedaan antara chown dan chmod]  
   Perbedaan antara chown dan chmod terletak pada aspek manajemen file yang mereka atur di Linux:

chown (Change Owner) mengatur Kepemilikan (Ownership) file dan direktori.

chmod (Change Mode) mengatur Hak Akses (Permissions) file dan direktori.

Perintah chown (Change Owner)
chown digunakan untuk mengubah siapa Pemilik (User) dan/atau Grup Pemilik (Group) dari sebuah file atau direktori. Ini adalah perintah yang berfokus pada siapa yang memiliki kendali administratif atas file tersebut.

Perintah chmod (Change Mode)
chmod digunakan untuk mengubah Hak Akses (Permissions) yang dimiliki oleh Pemilik, Grup, dan Lainnya terhadap file atau direktori (yaitu, Read/Baca, Write/Tulis, Execute/Eksekusi). Ini berfokus pada apa yang boleh dilakukan oleh setiap kelas pengguna.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  alhamdulilah sudah biasa saja
- Bagaimana cara Anda mengatasinya?
  chill saja

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
