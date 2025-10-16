
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
![Screenshot hasil](<screenshots/2025-10-12(5).png>)
![Screenshot hasil](<screenshots/2025-10-12(5).png>)


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
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?
   **Jawaban:**  
2. Sebutkan 4 kategori system call yang paling umum digunakan!
   **Jawaban:**  
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

### Tugas
1. Dokumentasikan hasil eksperimen `strace` dan `dmesg` dalam bentuk tabel observasi.  
2. Buat diagram alur system call dari aplikasi → kernel → hardware → kembali ke aplikasi.  
3. Tulis analisis 400–500 kata tentang:
   - Mengapa system call penting untuk keamanan OS?  
   - Bagaimana OS memastikan transisi user–kernel berjalan aman?  
   - Sebutkan contoh system call yang sering digunakan di Linux.  
4. Simpan semua hasil di:
   ```
   praktikum/week2-syscall-structure/
   ```
   ---
   
**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
