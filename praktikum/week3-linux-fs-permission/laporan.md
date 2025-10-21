
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
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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



## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## D. Tugas & Quiz
### Tugas
1. Dokumentasikan hasil seluruh perintah pada tabel observasi di `laporan.md`.  
2. Jelaskan fungsi tiap perintah dan arti kolom permission (`rwxr-xr--`).  
3. Analisis peran `chmod` dan `chown` dalam keamanan sistem Linux.  
4. Upload hasil dan laporan ke repositori Git sebelum deadline.

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari perintah `chmod`?  
2. Apa arti dari kode permission `rwxr-xr--`?  
3. Jelaskan perbedaan antara `chown` dan `chmod`.  

## E. Output yang Diharapkan
- Hasil observasi perintah Linux dimasukkan ke dalam `laporan.md`.  
- Screenshot hasil eksekusi disimpan di `screenshots/`.  
- Laporan lengkap tersimpan di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
