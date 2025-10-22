
# Laporan Praktikum Minggu 3
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Rizky Iqbal Hisyam 
- **NIM**   : 250202926
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.

---

## Dasar Teori
Tujuan utama dari praktikum ini adalah untuk mengoperasikan perintah Linux dasar dengan benar, serta memahami sistem izin (permission). Dalam sistem operasi Linux, setiap aktivitas pengguna hampir selalu berkaitan dengan pengelolaan file dan direktori. Untuk itu, penting memahami beberapa perintah dasar seperti `pwd`, `ls -l`, `cat`, `head`, `chmod`, dan `chown`. Keseluruhan konsep ini menjadi dasar penting bagi setiap pengguna untuk memahami cara kerja Linux secara lebih mendalam dan bertanggung jawab terhadap keamanan sistem.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

---

## Kode / Perintah
Potongan kode atau perintah utama:

Eksperimen 1
```bash
pwd
ls -l
cd /tmp
ls -a
```
Eksperimen 2
```bash
cat /etc/passwd | head -n 5
```
Eksperimen 3
```bash
echo "Hello <RIZKY IQBAL HISYAM><250202926>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt

sudo chown root percobaan.txt
ls -l percobaan.txt
```

---

## Hasil Eksekusi
Screenshot hasil percobaan:
![Screenshot hasil](./screenshots/linux_pwd.png)
![Screenshot hasil](./screenshots/linux_cat.png)
![Screenshot hasil](./screenshots/linux_permission.png)

---


## Tugas & Quiz
**Tugas Analisis Hasil Eksperimen**

### 1. Eksperimen navigasi sistem file

| **No** | **Perintah** | **Output / Hasil** | **Analisis / Penjelasan** | **Sumber Referensi** |
|:--:|:----------------|:-------------------|:---------------------------|:---------------------|
| 1 | `pwd` | `/home/rizky172007/os-202501-250202926` | Menampilkan direktori kerja (working directory) saat ini. Artinya pengguna sedang berada di folder proyek bernama `os-202501-250202926`. | Abraham Silberschatz, *Operating System Concepts*, 10th Ed., Wiley, 2018. |
| 2 | `ls -l` | `LICENSE`, `README.md`, `docs`, `praktikum` | Menampilkan isi folder aktif secara detail (satu item per baris). File dan folder tersebut berisi dokumentasi serta data tugas praktikum. | Andrew S. Tanenbaum, *Modern Operating Systems*, 4th Ed., Pearson, 2015. |
| 3 | `cd /tmp` | *(tidak ada output)* | Perintah `cd` digunakan untuk berpindah direktori. Setelah perintah ini dijalankan, direktori aktif berpindah dari `/home/...` ke `/tmp`. | *Linux Manual Pages* — `man cd`. |
| 4 | `ls -a` | `.`, `..`, `.X11-unix`, `snap-private-tmp`, `systemd-private-*` | Menampilkan semua isi direktori `/tmp`, termasuk file tersembunyi (diawali titik `.`). Folder `.X11-unix` digunakan oleh sistem grafis X11, sedangkan `systemd-private-*` adalah direktori sementara yang dibuat layanan sistem untuk menjaga keamanan dan isolasi proses. | *Linux Manual Pages* — `man ls`; *Systemd Documentation* (freedesktop.org). |


### 2. Eksperimen membaca file


| No | Username | UID | GID | Home Directory | Shell              | Keterangan                                                                 |
|----|----------|-----|-----|----------------|---------------------|------------------------------------------------------------------------------|
| 1  | root     | 0   | 0   | /root          | /bin/bash           | Akun superuser dengan hak penuh untuk mengelola sistem.                     |
| 2  | daemon   | 1   | 1   | /usr/sbin      | /usr/sbin/nologin   | Akun sistem yang menjalankan proses daemon, tidak dapat login.              |
| 3  | bin      | 2   | 2   | /bin           | /usr/sbin/nologin   | Akun sistem untuk kepemilikan file biner penting.                           |
| 4  | sys      | 3   | 3   | /dev           | /usr/sbin/nologin   | Akun sistem yang digunakan oleh layanan internal sistem operasi.            |
| 5  | sync     | 4   | 65534| /bin          | /bin/sync           | Akun khusus untuk sinkronisasi data ke disk, biasanya digunakan saat recovery. |



### 3. Eksperimen permission & ownership

| No | Perintah yang Dijalankan | Hasil / Output (`ls -l`) | Analisis / Keterangan | Referensi |
|----|---------------------------|--------------------------|------------------------|------------|
| 1 | `echo "Hello <RIZKY IQBAL HISYAM><250202926>" > percobaan.txt` | *File baru dibuat* | Membuat file teks baru bernama `percobaan.txt` dengan isi teks tertentu. Pemilik awal adalah user yang sedang login. | Shotts, *The Linux Command Line*, 2019 |
| 2 | `ls -l percobaan.txt` | `-rw-r--r-- 1 rizky172007 rizky172007 38 Oct 20 22:07 percobaan.txt` | Permission default (`rw-r--r--` / 644) menunjukkan bahwa pemilik dapat membaca dan menulis, sedangkan group dan others hanya dapat membaca. | GNU Coreutils Manual – `ls` |
| 3 | `chmod 600 percobaan.txt` | *Tidak ada output (izin berubah)* | Mengubah mode akses menjadi `600` (`rw-------`), artinya hanya pemilik file yang dapat membaca dan menulis. | Tanenbaum, *Modern Operating Systems*, 2015 |
| 4 | `ls -l percobaan.txt` | `-rw------- 1 rizky172007 rizky172007 38 Oct 20 22:07 percobaan.txt` | Hanya user `rizky` yang memiliki akses penuh terhadap file, sedangkan group dan others tidak memiliki akses. | Silberschatz, *Operating System Concepts*, 2018 |
| 5 | `sudo chown root percobaan.txt` | *Tidak ada output (pemilik berubah)* | Mengubah kepemilikan file dari `rizky` menjadi `root`. | Linux Manual Page – `chown(1)` |
| 6 | `ls -l percobaan.txt` | `-rw------- 1 root rizky172007 38 Oct 20 22:07 percobaan.txt` | File kini dimiliki oleh `root`. Karena permission masih `600`, user biasa tidak dapat membaca maupun menulis file tersebut. | Silberschatz, *Operating System Concepts*, 2018 |


**Quiz**
1. Apa fungsi dari perintah `chmod`? 
   
   **Jawaban:** Fungsi `chmod` yaitu untuk mengubah *permission* (hak akses) file atau direktori.

2. Apa arti dari kode permission `rwxr-xr--`?  

   **Jawaban:** berikut penjelasan tiap bagian dari kode `rwxr-xr--`

| Bagian | Arti | Keterangan |
|:--|:--|:--|
| **-** | Jenis file | `-` = file biasa, `d` = direktori, `l` = link |
| **rwx** | Hak akses **user (pemilik)** | Dapat *read (r)*, *write (w)*, dan *execute (x)* |
| **r-x** | Hak akses **group (grup)** | Dapat *read (r)* dan *execute (x)* saja |
| **r--** | Hak akses **others (lainnya)** | Hanya *read (r)* saja |



3. Jelaskan perbedaan antara `chown` dan `chmod`.  

   **Jawaban:** Perintah chmod dan chown adalah dua lapisan kontrol keamanan utama di Linux.
`chmod` memiliki peran dalam mengatur mode/tingkat akses (akses kontrol) terhadap file. Sedangkan `chown` mengatur kepemilikan (ownership) file.
Keduanya memiliki peran untuk mengatur hak akses, menjaga kerahasiaan, dan ketersediaan data dalam sistem.

---

## Kesimpulan
**Kesimpulan**

Dari percobaan manajemen file dan permission di Linux, dapat disimpulkan bahwa sistem ini dirancang untuk membantu pengguna mengenali posisi dan isi direktori, serta mengatur hak akses file.
Secara keseluruhan, eksperimen ini menunjukkan bahwa Linux tidak hanya efisien dalam mengelola file, tetapi juga kuat dalam menjaga keamanan dan keteraturan sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Hal yang menantang minggu ini tentunya pengoperasian Linux dan memahami fungsi dari perintah manajemen file, seperti `ls`, `pwd`, `cd`, `cat`, `chmod` dan `chown`

- Bagaimana cara Anda mengatasinya?  
Mempelajari dari berbagai sumber dan referensi terkait.

---

## Referensi
1. Abraham Silberschatz, Peter Baer Galvin, Greg Gagne. *Operating System Concepts*, 10th Edition, Wiley, 2018.  
2. Andrew S. Tanenbaum, Herbert Bos. *Modern Operating Systems*, 4th Edition, Pearson, 2015.  
3. Linux Manual Pages (`man chmod`, `man chown`, `man ls`).  
4. OSTEP – *Operating Systems: Three Easy Pieces*, 2018.  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
