# Tugas Praktikum Minggu 2  
Topik: Struktur System Call dan Fungsi Kernel  

---

## A. Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme system call dan struktur sistem operasi**.  
System call adalah antarmuka antara program aplikasi dan kernel yang memungkinkan aplikasi berinteraksi dengan perangkat keras secara aman melalui layanan OS.

Mahasiswa akan melakukan eksplorasi terhadap:
- Jenis-jenis system call yang umum digunakan (file, process, device, communication).
- Alur eksekusi system call dari mode user menuju mode kernel.
- Cara melihat daftar system call yang aktif di sistem Linux.

---

## B. Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## C. Langkah Pengerjaan
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

## D. Tugas & Quiz
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

### Quiz
Jawab pertanyaan berikut di bagian **Quiz** laporan:
1. Apa fungsi utama system call dalam sistem operasi?  
2. Sebutkan 4 kategori system call yang umum digunakan.  
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?

---

## E. Output yang Diharapkan
- Hasil observasi system call (`strace ls`) dimasukkan ke dalam `laporan.md`.  
- File screenshot hasil observasi disimpan di `screenshots/syscall_ls.png`.  
- Diagram alur system call disimpan di `screenshots/syscall-diagram.png`.  
- Laporan lengkap berada di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.

---

## F. Referensi
1. Abraham Silberschatz, Peter Baer Galvin, Greg Gagne. *Operating System Concepts*, 10th Edition, Wiley, 2018.  
2. Andrew S. Tanenbaum, Herbert Bos. *Modern Operating Systems*, 4th Edition, Pearson, 2015.  
3. Linux Manual Pages (`man 2 syscalls`, `man strace`).  
4. OSTEP – *Operating Systems: Three Easy Pieces*, 2018.  
5. https://man7.org/linux/man-pages/man2/syscalls.2.html
