
# Laporan Praktikum Minggu 3
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Farhan Ramdhani  
- **NIM**   : 250202938  
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
Dalam sistem operasi Linux, setiap file dan folder punya pengaturan izin atau permission yang menentukan siapa yang boleh membaca (read), menulis (write), dan menjalankan (execute) file tersebut. Tujuannya adalah untuk menjaga keamanan dan mencegah orang lain mengubah file tanpa izin.

Ada tiga jenis pengguna dalam pengaturan izin :

1. Owner → pemilik file.


2. Group → pengguna lain yang tergabung dalam grup yang sama.


3. Others → semua pengguna lain di sistem.



*Izin file biasanya ditampilkan dalam bentuk seperti ini :*

- `-rw-r--r--`

- Artinya pemilik bisa membaca dan menulis, sedangkan pengguna lain hanya bisa membaca.

*Untuk melihat izin file digunakan perintah :*

- `ls -l`

*Sedangkan untuk mengubah izin bisa memakai perintah :*

- `chmod`

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

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   cat /etc/passwd | head -n 5
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
### Eksperimen 1

**Penjelasan :**

Perintah `pwd` menampilkan lokasi direktori aktif tempat kita sedang bekerja.
Perintah `ls` menampilkan daftar isi folder yang ada di direktori tersebut.
Sedangkan `ls -a` menampilkan semua file termasuk file tersembunyi (yang diawali dengan titik .).

**Catatan :**

- Direktori aktif : /home/farhan/week3-linux-fs-permission

- Isi folder : percobaan.txt

### Eksperimen 2

**Penjelasan :**

Isi file /etc/passwd berisi informasi tentang semua user di sistem Linux.

**Keterangan :**

- `username` → nama pengguna

- `UID` → nomor identitas user

- `GID` → nomor identitas grup

- `home` → direktori utama user

- `shell` → jenis terminal yang digunakan

### Eksperimen 3

**Penjelasan :**

Sebelum diubah dengan chmod, file memiliki izin default, pemilik bisa membaca dan menulis, pengguna lain hanya bisa membaca.
Setelah diberi perintah chmod, file bisa dijalankan seperti program.

**Hasil :**
```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Setelah menjalankan perintah tersebut, file percobaan.txt sekarang dimiliki oleh user root. Sebelumnya file ini dimiliki oleh user biasa.




---

## Hasil Eksekusi
![alt text](../week3-linux-fs-permission/screenshots/Screenshot%202025-10-16%20220137.png) 

---

## Analisis
- Jelaskan makna hasil percobaan.  

**Jawaban :** 
Dari hasil percobaan, bisa dilihat bahwa setiap file di Linux memiliki izin akses yang berbeda-beda tergantung pengaturan permission-nya. Saat kita menggunakan perintah chmod, sistem akan langsung mengubah hak akses file sesuai nilai yang kita berikan (misalnya 644 atau 755). Hal ini menunjukkan bahwa Linux benar-benar menerapkan sistem keamanan berbasis izin pengguna.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  

**Jawaban :** 
Kalau dikaitkan dengan teori, pengaturan ini berhubungan dengan fungsi kernel dan system call. Kernel bertugas sebagai penghubung antara pengguna dan perangkat keras, sedangkan system call digunakan oleh perintah seperti chmod, chown, atau ls untuk meminta layanan dari kernel. Jadi, setiap kali kita mengubah permission, sebenarnya kita sedang berinteraksi dengan kernel lewat system call.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

**Jawaban :** 
Kalau dibandingkan dengan Windows, sistem izin file di Linux jauh lebih detail dan fleksibel. Di Windows memang ada pengaturan permission juga, tapi biasanya berbasis GUI, Sedangkan di Linux, pengaturannya berbasis perintah terminal dan bisa diatur secara lebih spesifik untuk setiap pengguna dan grup.


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

- Sistem permission di Linux berfungsi untuk mengatur siapa yang boleh membaca, menulis, dan menjalankan file.

- Pemahaman tentang permission penting untuk menjaga keamanan dan mencegah kesalahan akses di sistem Linux.


---

## Quiz
1. Apa fungsi dari perintah `chmod`?

   **Jawaban :**  Perintah `chmod` digunakan untuk mengubah izin akses (permission) pada file atau folder, misalnya agar file bisa dijalankan atau hanya bisa dibaca.

2. Apa arti dari kode permission `rwxr-xr--`?

   **Jawaban :** 
- `rwx` → pemilik file bisa membaca, menulis, dan menjalankan.
- `r-x` → grup hanya bisa membaca dan menjalankan.
- `r--` → pengguna lain hanya bisa membaca.


3. Jelaskan perbedaan antara `chown` dan `chmod`  

   **Jawaban :**  `chmod` untuk mengubah izin akses (permission) pada file, sedangkan `chown` untuk mengubah kepemilikan (owner) dari file.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

   **Jawaban :** Bagian paling sulit adalah memahami arti setiap simbol permission dan cara kerja perintah `chmod`, karena terlihat sepele tapi ternyata sangat detail dan mudah salah.


- Bagaimana cara Anda mengatasinya?  

   **Jawaban :** Saya mencoba ulang beberapa kali perintah di terminal, melihat hasilnya dengan `ls -l`, dan membaca ulang teori tentang permission dan fungsi `chmod`. Setelah mencoba langsung, jadi lebih paham cara kerjanya.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
