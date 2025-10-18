
# Laporan Praktikum Minggu 2
**Struktur System Call dan Fungsi Kernel**

---

## Identitas
- **Nama**  : Faiq Atha Rulloh
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---

## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme system call dan struktur sistem operasi**.  
System call adalah antarmuka antara program aplikasi dan kernel yang memungkinkan aplikasi berinteraksi dengan perangkat keras secara aman melalui layanan OS.

---

## Tujuan
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
  > _System Call_ adalah antarmuka yang disediakan oleh sistem operasi untuk memungkinkan program aplikasi mengakses layanan kernel dan sumber daya sistem secara terkendali. Fungsi utamanya adalah Akses terkendali ke Hardware, Abstraksi Hardware, Keamanan dan Proteksi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
  > Jenis-Jenis System Call beserta fungsinya:
>   - Process Control fungsinya adalah mengelola siklus hidup dan eksekusi proses.
>   - File Management fungsinya adalah operasi pada file system dan direktori.
>   - Device Management fungsinya adalah mengontrol perangkat input/output.
>   - Information Maintenance fungsinya adalah Mendapatkan dan mengatur informansi sistem.
>   - Communication fungsinya adalah Komunikasi antar proses.
>   - Protection fungsinya adalah kontrol akses dan keamanan sistem.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
 >  Alur perpindahan mode user ke kernel adalah memastikan bahwa meskipun banyak aplikasi berjalan, sistem operasi tetap memiliki kontrol atas semua sumber daya komputer, menjaga stabilitas, keamanan, dan kinerja sistem secara keseluruhan.
   
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.
   
---

## Dasar Teori 
* _System call_ adalah antarmuka yang disediakan oleh sistem operasi untuk memungkinkan program aplikasi mengakses layanan inti dari kernel.
* _System Call_ bertindak sebagai jembatan antara user mode dan kernel mode.
* Program aplikasi tidak dapat mengakses hardware atau sumber daya sistem secara langsung dan mereka harus meminta melalui _System Call_.
* Tanpa _System Call_, aplikasi tidak dapat berinteraksi dengan hardware atau sumber daya sistem (CPU,Memory,Storage,I/O Device)
* _Kernel_ Memastikan bahwa semua proses berjalan dengan aman dan efisiensi.
* _System Call_ memungkinkan portabilitas kode antar platform yang mendukung API yang sama.
  
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

3. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. **Diagram Alur System Call**
   - Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
   - Gunakan draw.io / mermaid.
   - Simpan di:
     ```
     praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```  
---

 ##  Output yang Diharapkan
- Hasil observasi system call (`strace ls`) dimasukkan ke dalam `laporan.md`.  
- File screenshot hasil observasi disimpan di `screenshots/syscall_ls.png`.  
- Diagram alur system call disimpan di `screenshots/syscall-diagram.png`.  
- Laporan lengkap berada di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.

---

## Hasil Eksekusi
screenshot hasil percobaan atau diagram dari  `strace ls`:
![Screenshot hasil](<screenshots/2025-10-12.png>)

screenshot hasil percobaan dari `strace -e trace=open,read,write,close cat /etc/passwd`:
![Screenshot](<screenshots/2025-10-12 (5).png>)

screenshot hasil percobaan dari `dmesg | tail -n 10`:
![Screenshot](<screenshots/2025-10-12 (7).png>)

Diagram alur system call dari aplikasi → kernel → hardware → kembali ke aplikasi.  
![Screenshot](<screenshots/Diagram week 2 faiq.drawio.png>)


---

## Analisis
- Jelaskan makna hasil percobaan.
  
```bash
strace ls
```
| Aspek            | Penjelasan                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------ |
| **Perintah**     | `strace ls`                                                                                |
| **Makna**        | Menjalankan `ls` sambil menampilkan semua panggilan sistem ke kernel                       |
| **Fungsi utama** | Debugging, belajar cara kerja program, mendiagnosis error                                  |

```bash
strace -e trace=open,read,write,close cat /etc/passwd
```
| Bagian perintah         | Penjelasan                                                                                    |
| ----------------------- | --------------------------------------------------------------------------------------------- |
| `strace`                | Alat untuk menelusuri (*trace*) system call antara program dan kernel                         |
| `-e trace=...`          | Filter agar hanya menampilkan system call tertentu                                            |
| `open,read,write,close` | Jenis system call yang ingin dilihat (yang digunakan untuk mengakses file)                    |
| `cat /etc/passwd`       | Program yang dijalankan dan ditelusuri — `cat` membaca dan menampilkan isi file `/etc/passwd` |

```bash
dmesg | tail -n 10
```
| Bagian perintah | Penjelasan                                                                                                              |                                             
| --------------- | ----------------------------------------------------------------------------------------------------------------------- | 
| `dmesg`         | Menampilkan **pesan log kernel (kernel ring buffer)** — yaitu catatan aktivitas sistem operasi pada level paling dasar. |                                             
| `tail -n 10`    | Menampilkan **10 baris terakhir** dari data yang diterima.                                                              |                                                                                           


- Hubungkan hasil dengan teori tersebut
  
| Perintah                                                           | Hubungan dengan lainnya                                               |        
| ------------------------------------------------------------------ | --------------------------------------------------------------------- |                                
| `strace ls`                                                        | Program ini melakukan *system call* ke kernel                         |
| `strace -e strace -e trace=open,read,write,close cat /etc/passwd`  | Semua aktivitas dari user-space ke kernel melewati lapisan ini        |
| `dmesg  tail -n 10`                                                | Kernel mencatat aktivitasnya, error, atau status sistem ke buffer log | 
 
- Apa perbedaan hasil dari percobaan tersebut?

| Perintah                                                    | Perbedaan Utama                                                                                |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **`strace ls`**                                             | Melacak semua aktivitas `ls` yang berhubungan dengan kernel (tanpa filter).                    |
| **`strace -e trace=open,read,write,close cat /etc/passwd`** | Melacak hanya aktivitas file I/O dari `cat`, jadi lebih spesifik.                              |
| **`dmesg tail -n 10`**                                      | Tidak melacak system call sama sekali — hanya menampilkan pesan kernel (log aktivitas sistem). |


---

## Kesimpulan

   - `strace ls` : menampilkan semua system call yang dilakukan program ls.

   - `strace -e  trace=open,read,write,close cat /etc/passwd` : menampilkan hanya system call yang berhubungan dengan operasi file

   - `dmesg | tail -n 10` : menampilkan log aktivitas kernel seperti pesan error, status perangkat, atau aktivitas sistem lainnya
     
---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?
   - Fungsi utama system call dalam sistem operasi adalah sebagai komunikasi antara program pengguna dan kernel 
2. Sebutkan 4 kategori system call yang paling umum digunakan!
   - `open()` fungsinya Membuka file.
   - `read()` fungsinya Membaca data dari file yang sudah dibuka.
   - `write()` fungsinya Menulis data ke dalam file..
   - `close()` fungsinya Menutup file yang sebelumnya dibuka.
   - `delete()` fungsinya Menghapus file dari sistem penyimpanan.
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   - System call berjalan di kernel mode, sedangkan program pengguna berjalan di user mode. Kedua mode ini dipisahkan untuk keamanan dan stabilitas sistem operasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
   -  Bagian yang paling menantang adalah memahami alur kerja antara user space dan kernel space
- Bagaimana cara Anda mengatasinya?
   -  Saya mengatasinya dengan membaca kembali materi tentang system call, dan mencoba menjalankan perintah secara langsung di terminal, serta memahami setiap hasil dan penjelasannya agar lebih mudah dipahami.

---

### Tugas
1. Dokumentasikan hasil eksperimen `strace` dan `dmesg` dalam bentuk tabel observasi.  
2. Buat diagram alur system call dari aplikasi → kernel → hardware → kembali ke aplikasi.  
3. Tulis analisis 400–500 kata tentang:
   - Mengapa system call penting untuk keamanan OS?
     - system call penting untuk keamanan sistem operasi karena
       1. menjadi penghubungkan antara program user (mode user) dengan kernel (mode kernel).
       2. mencegah akses langsung ke kernel.
       3. Menjalankan pemeriksaan izin (akses control).
       4. Menjaga kestabilan dan keamanan sistem.
       5. Memantau dan mencatat aktivitas sistem.
   - Bagaimana OS memastikan transisi user–kernel berjalan aman?
     - Sistem operasi memastikan transisi dari user mode ke kernel mode berjalan aman dengan beberapa mekanisme penting. Pertama, OS memanfaatkan pemisahan mode CPU, di mana program biasa hanya memiliki hak terbatas di user mode dan tidak bisa langsung menjalankan instruksi berhak tinggi. Saat sebuah program membutuhkan layanan kernel, ia harus memanggil system call yang akan memicu instruksi khusus (trap atau interrupt) untuk berpindah ke kernel mode. Proses ini tidak bisa diakses secara langsung oleh program user, sehingga mencegah penyalahgunaan.
     
   - Sebutkan contoh system call yang sering digunakan di Linux.
     - Beberapa system call yang sering digunakan di Linux antara lain yaitu Dalam sistem operasi Linux, antara lain :

 - Pertama, dalam kategori manajemen berkas (file management), terdapat system call seperti `open()` yang digunakan untuk membuka atau membuat file baru, `read()` untuk membaca data dari file, `write()` untuk menulis data ke file, dan `close()` untuk menutup file setelah digunakan. Selain itu, `lseek()` digunakan untuk memindahkan posisi pointer baca atau tulis di dalam file, sedangkan `unlink()` berfungsi untuk menghapus file dari sistem.

 - Kedua, dalam kategori pengendalian proses (process control), terdapat system call penting seperti `fork()` yang digunakan untuk membuat proses baru (child process), `exec()` untuk menjalankan program baru dalam proses yang sedang berjalan, serta `exit()` untuk mengakhiri proses. System call `wait()` digunakan agar proses induk menunggu proses anak selesai, sementara` getpid()` berfungsi untuk mendapatkan ID proses yang sedang berjalan.

 - Ketiga, dalam komunikasi antar-proses atau jaringan (interprocess communication), Linux menyediakan system call seperti `pipe()` untuk membuat saluran komunikasi antara dua proses,` socket()` untuk membuat koneksi jaringan, serta` connect()`,` send(),` dan `recv()` untuk menghubungkan dan bertukar data antar komputer melalui jaringan.

 - Keempat, pada manajemen perangkat dan sumber daya (device and resource management), terdapat system call seperti` ioctl()` yang digunakan untuk mengatur atau mengontrol perangkat keras tertentu, `mmap()` yang berfungsi memetakan file ke ruang memori proses, serta` brk()` dan `sbrk()` yang digunakan untuk mengatur ukuran ruang memori dinamis (heap) suatu proses.

- Kelima, dalam kategori keamanan dan izin akses (security and permission), terdapat system call seperti `chmod()` untuk mengubah hak akses file, `chown()` untuk mengubah kepemilikan file, dan` setuid()` maupun` setgid()` untuk mengubah identitas pengguna atau grup dari suatu proses.
     
4. Simpan semua hasil di:
   ```
   praktikum/week2-syscall-structure/
   ```
   ---
   
**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
