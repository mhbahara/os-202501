
# Laporan Praktikum Minggu 3
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Faiq Atha Rulloh
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---

## A. Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **pengelolaan file dan direktori menggunakan perintah dasar Linux**, serta konsep **permission dan ownership**.  
Praktikum berfokus pada:
- Navigasi sistem file dengan `ls`, `pwd`, `cd`, dan `cat`.
- Pengaturan hak akses file menggunakan `chmod`.
- Pengubahan kepemilikan file menggunakan `chown`.
- Dokumentasi hasil eksekusi dan pengelolaan repositori praktikum.

---

## B. Tujuan  
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
6. mampu ***mengoperasikan perintah Linux dasar dengan benar***
7. memahami sistem izin (permission)
8. mendokumentasikan hasilnya dalam format laporan Git.

---

## Dasar Teori
1. Semua file di Linux tersusun dalam satu sistem hierarki mulai dari direktori root (**/**).
2. Ada berbagai jenis file seperti file biasa, folder, dan link.
3. Setiap file punya izin akses (**read, write, execute**) untuk **pemilik, grup, dan pengguna lain**.
4. Izin bisa diubah dengan `chmod`, sedangkan pemilik file bisa diatur dengan `chown` atau `chgrp`.
5. Pengaturan izin bertujuan menjaga keamanan agar hanya pengguna yang berhak bisa mengakses file.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
3. Perintah yang dijalankan.  
4. File dan kode yang dibuat.  
5. Commit message yang digunakan.

---

## C. Kode / Perintah

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

 **Eksperimen 2 – Membaca File**
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

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```

---



## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
**Eksperimen 1 – Navigasi Sistem File**
- Jelaskan hasil tiap perintah.
  
1. `pwd`
   - pwd (print working directory) digunakan untuk menampilkan direktori aktif saat ini.
   - Artinya kamu sedang berada di folder /home/faiqatha, yaitu direktori home milik user “faiqatha”.
     
2. `ls -l`
   - `ls -l` menampilkan daftar isi direktori dalam format panjang (long listing).
   - Kolom-kolomnya berarti:
   -`drwx------` jenis dan permission file: d artinya direktori.
   - `rwx------` artinya hanya pemilik (faiqatha) yang bisa membaca, menulis, dan mengakses folder ini.
   - `3`  jumlah link (subdirektori atau file di dalamnya).
   - `faiqatha faiqatha` pemilik dan grup file.
   - `4096`  ukuran direktori dalam byte.
   - `Oct 13 21:45` tanggal dan waktu dibuat/dimodifikasi.
   - `snap`  nama direktori.
     
3. `cd /tmp`
   - `cd` = change directory Menampilkan daftar isi (file dan folder) dalam direktori aktif.
   - Perintah ini memindahkan kamu ke folder `/tmp`, yaitu direktori sementara (temporary) yang digunakan sistem dan aplikasi untuk menyimpan file sementara.
   - Biasanya file di `/tmp` akan dihapus otomatis saat sistem direstart.
   
4. `ls -a`
   - `ls -a` menampilkan semua file, termasuk yang tersembunyi (dimulai dengan titik “.”).
   - Isi yang terlihat:
      - `.X11-unix`  folder socket untuk sistem tampilan grafis (X11).
      - `snap-private-tmp` folder sementara yang digunakan aplikasi dari Snap.
      - Folder dengan awalan `systemd-private-...`  direktori sementara milik berbagai layanan sistem (systemd services) yang bersifat privat dan tidak bisa diakses langsung oleh user.

- Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).
  
| Aspek yang Diamati                          | Hasil                                                                  |
| ------------------------------------------- | ---------------------------------------------------------------------- |
| **Direktori Aktif**                         | `/tmp`                                                                 |
| **Isi Folder (hasil `ls`)**                 | `.X11-unix`, `snap-private-tmp`, beberapa folder `systemd-private-...` |
| **File/Folder Tersembunyi (hasil `ls -a`)** | `.X11-unix` *(titik di awal nama menunjukkan file tersembunyi)*        |

 **Eksperimen 2 – Membaca File**
  - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).
    
| Username   | UID | GID   | Home Directory | Shell               | Keterangan                                                     |
| ---------- | --- | ----- | -------------- | ------------------- | -------------------------------------------------------------- |
| **root**   | 0   | 0     | `/root`        | `/bin/bash`         | Akun superuser sistem (akses penuh)                            |
| **daemon** | 1   | 1     | `/usr/sbin`    | `/usr/sbin/nologin` | Akun sistem untuk menjalankan proses daemon (tidak bisa login) |
| **bin**    | 2   | 2     | `/bin`         | `/usr/sbin/nologin` | Akun sistem untuk menjalankan perintah biner sistem            |
| **sys**    | 3   | 3     | `/dev`         | `/usr/sbin/nologin` | Akun sistem untuk perangkat dan layanan sistem                 |
| **sync**   | 4   | 65534 | `/bin`         | `/bin/sync`         | Akun khusus untuk perintah sinkronisasi file system            |

 **Eksperimen 3 – Permission & Ownership**
   - Analisis perbedaan sebelum dan sesudah chmod.
     
| Kondisi               | Permission                                               | Keterangan                            |
| --------------------- | -------------------------------------------------------- | ------------------------------------- |
| Sebelum (`rw-r--r--`) | Pemilik: baca & tulis<br>Grup & lainnya: baca            | File dapat dibaca oleh semua pengguna |
| Sesudah (`rw-------`) | Pemilik: baca & tulis<br>Grup & lainnya: tidak ada akses | File hanya bisa diakses oleh pemilik  |

   - Catat hasilnya.
        - ls -l percobaan.txt
        - -rw------- 1 root faiqatha 25 Oct 25 20:52 percobaan.txt
     - Analisi = Karena izin file adalah rw-------, hanya pemilik (root) yang bisa: Membaca (r), Menulis (w)
     - Grup (faiqatha) dan pengguna lain tidak punya hak akses apa pun (---).

---

## Kesimpulan
- Perintah dasar Linux seperti` echo`,` ls`,` cd`, dan cat digunakan untuk membuat, menampilkan, dan mengelola file serta direktori.
Contohnya, `echo "Hello <Faiq Atha Rulloh>" > percobaan.txt` berhasil membuat file teks baru.
- File permission (hak akses) di Linux diatur menggunakan perintah chmod, yang mengontrol siapa yang boleh membaca (`r`), menulis (`w`), atau mengeksekusi (`x`) file. Setelah `chmod 600 percobaan.txt`, hanya pemilik file yang bisa membaca dan menulis, sedangkan pengguna lain tidak memiliki akses.
- Kepemilikan file (ownership) dapat diubah dengan `chown`, yang menentukan siapa pemilik dan grup dari file tersebut. Setelah `sudo chown root percobaan.txt`, file berpindah kepemilikan ke root, sehingga hanya superuser yang bisa mengaksesnya.
---

## D. Tugas & Quiz
### Tugas
1. Dokumentasikan hasil seluruh perintah pada tabel observasi di `laporan.md`.
    ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
    
 | No | Perintah  | Fungsi / Tujuan                                   | Hasil / Output                                          | Keterangan Tambahan                                                                         |
| -- | --------- | ------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1  | `pwd`     | Menampilkan direktori aktif saat ini              | `/home/faiqatha`                                        | Menunjukkan lokasi kerja user saat ini                                                      |
| 2  | `ls -l`   | Menampilkan isi direktori dalam format panjang    | `drwx------ 3 faiqatha faiqatha 4096 Oct 13 21:45 snap` | Menampilkan detail: tipe file, permission, jumlah link, pemilik, ukuran, tanggal, nama file |
| 3  | `cd /tmp` | Berpindah ke direktori `/tmp`                     | Berpindah ke folder sementara sistem                    | `/tmp` berisi file sementara yang dihapus otomatis saat restart                             |
| 4  | `ls -a`   | Menampilkan semua file, termasuk file tersembunyi | `.X11-unix`, `snap-private-tmp`, `systemd-private-...`  | File/folder dengan awalan “.” adalah tersembunyi; digunakan oleh sistem dan aplikasi        |

  ```bash
   cat /etc/passwd | head -n 5
   ```

| No | Perintah          | Fungsi / Tujuan                                                                                                                                                                                                    | Hasil / Output                                                       | Keterangan Tambahan                                                                      |                                            |
| -- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------ |
| 1  | `cat /etc/passwd` | Menampilkan isi file `/etc/passwd` yang berisi daftar akun pengguna sistem                                                                                                                                         | Daftar user dengan format: `username:x:UID:GID:deskripsi:home:shell` | File ini menyimpan informasi akun, tetapi **bukan password** (disimpan di `/etc/shadow`) |                                            |
| 2  | `                 | ` (pipe)                                                                                                                                                                                                           | Mengalirkan output dari perintah pertama ke perintah berikutnya      | -                                                                                        | Digunakan untuk menghubungkan dua perintah |
| 3  | `head -n 5`       | Menampilkan 5 baris pertama dari hasil `cat /etc/passwd`                                                                                                                                                           | Menampilkan 5 akun pertama: `root`, `daemon`, `bin`, `sys`, `sync`   | Digunakan agar tampilan tidak terlalu panjang                                            |                                            |
| 4  | Output contoh     | `root:x:0:0:root:/root:/bin/bash`<br>`daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin`<br>`bin:x:2:2:bin:/bin:/usr/sbin/nologin`<br>`sys:x:3:3:sys:/dev:/usr/sbin/nologin`<br>`sync:x:4:65534:sync:/bin:/bin/sync` | -                                                                    | Menunjukkan informasi akun sistem seperti nama, ID, direktori, dan shell                 |                                            |

  ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```

| No | Perintah                                          | Fungsi / Tujuan                    | Hasil / Keterangan                                                   |
| -- | ------------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------- |
| 1  | `echo "Hello <Faiq Atha Rulloh>" > percobaan.txt` | Membuat file baru berisi teks      | File `percobaan.txt` dibuat dengan isi “Hello <Faiq Atha Rulloh>”    |
| 2  | `ls -l percobaan.txt`                             | Melihat detail file                | Awalnya: `-rw-r--r--` → pemilik bisa baca/tulis, lain hanya baca     |
| 3  | `chmod 600 percobaan.txt`                         | Mengubah izin akses file           | Jadi: `-rw-------` → hanya pemilik yang bisa baca & tulis            |
| 4  | `sudo chown root percobaan.txt`                   | Mengubah pemilik file menjadi root | Hasil: `-rw------- 1 root faiqatha ...` → root sekarang pemilik file |



3. Jelaskan fungsi tiap perintah dan arti kolom permission (`rwxr-xr--`).
   
| **Perintah** | **Fungsi Utama**                                    | **Keterangan**                                                                                       |
| ------------ | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `ls -l`      | Menampilkan daftar file/direktori secara detail     | Termasuk jenis file, permission, pemilik, grup, ukuran, dan waktu terakhir diubah.                   |
| `chmod`      | Mengubah permission (hak akses) file atau direktori | Misal: `chmod 600 file.txt` memberi akses penuh ke pemilik, tapi menolak akses untuk grup & lainnya. |
| `chown`      | Mengubah **pemilik (owner)** file/direktori         | Contoh: `chown faiq file.txt` → mengubah pemilik file menjadi user *faiq*.                           |
| `chgrp`      | Mengubah **grup** file/direktori                    | Contoh: `chgrp staff file.txt` → ubah grup file menjadi *staff*.                                     |

`-rwxr-xr--`
- Maka artinya:
   - Pemilik dapat membuka, mengedit, dan menjalankan file.
   - Grup hanya dapat membaca dan menjalankan.
   - Pengguna lain hanya dapat membaca.

4. Analisis peran `chmod` dan `chown` dalam keamanan sistem Linux.
  -  chmod dan chown berperan penting dalam keamanan sistem Linux dengan mengendalikan siapa yang dapat mengakses, mengubah, dan menjalankan file atau direktori. Mengelola kepemilikan dan izin secara tepat adalah prinsip dasar untuk melindungi sistem dari akses yang tidak sah dan penyalahgunaan
5. Upload hasil dan laporan ke repositori Git sebelum deadline.



### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari perintah `chmod`?
   - Perintah `chmod` (singkatan dari change mode) adalah perintah dasar di sistem operasi berbasis Unix dan Linux yang berfungsi untuk mengubah izin akses (permission) pada sebuah file atau direktori. Izin ini menentukan siapa yang dapat membaca, menulis, dan mengeksekusi file tersebut.  
2. Apa arti dari kode permission `rwxr-xr--`?
   - Kode permission `rwxr-xr--` pada sistem Linux menunjukkan hak akses (permission) terhadap sebuah file atau direktori.
Kode ini terdiri dari 3 kelompok, masing-masing mewakili hak akses untuk:Pemilik, Grup, Lainnya.
3. Jelaskan perbedaan antara `chown` dan `chmod`.  

| Perintah    | Kepanjangan    | Fungsi Utama                                                  | Yang Diatur                                                                  | Contoh Penggunaan                                                                         |
| ----------- | -------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **`chown`** | *Change Owner* | Mengubah **kepemilikan** suatu file atau direktori            | **Pemilik (user)** dan **grup** dari file                                    | `chown faiq:staff dokumen.txt` → Mengubah pemilik menjadi *faiq* dan grup menjadi *staff* |
| **`chmod`** | *Change Mode*  | Mengubah **hak akses (permission)** suatu file atau direktori | **Izin akses (read, write, execute)** untuk pemilik, grup, dan pengguna lain | `chmod 755 dokumen.txt` → Memberi hak *rwxr-xr-x*                                         |


## E. Output yang Diharapkan
- Hasil observasi perintah Linux dimasukkan ke dalam `laporan.md`.  
- Screenshot hasil eksekusi disimpan di `screenshots/`.  
- Laporan lengkap tersimpan di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
   - memahami dan menerapkan konsep permission serta perintah manajemen file di Linux.
- Bagaimana cara Anda mengatasinya?
   - Belajar secara bertahap, latihan langsung di terminal, catat hasil percobaan.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
