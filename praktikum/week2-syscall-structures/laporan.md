
# Laporan Praktikum Minggu [X]
mekanisme system call dan struktur sistem operasi.

---

## Identitas
- **Nama**  : [Miftakhul Lisna Esa Baehaqi]  
- **NIM**   : [250202951]  
- **Kelas** : [1IKRB]

---

## Tujuan
-Menjelaskan konsep dan fungsi system call dalam sistem operasi.

-Mengidentifikasi jenis-jenis system call dan fungsinya.

-Mengamati alur perpindahan mode user ke kernel saat system call terjadi.

-Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.


---

## Dasar Teori
System Call (Panggilan Sistem) adalah antarmuka yang disediakan oleh SO agar program aplikasi di User Mode dapat meminta layanan dari Kernel (inti SO) yang berjalan di Kernel Mode (mode terproteksi). Ini adalah satu-satunya cara bagi program untuk mengakses sumber daya istimewa (I/O, manajemen memori, dll.)

-Percobaan strace ls secara langsung mendemonstrasikan mekanisme ini, mencatat setiap kali program ls melakukan transisi dari User Mode ke Kernel Mode untuk meminta layanan (misalnya, execve untuk memulai program, openat untuk membuka library, atau getdents untuk membaca isi direktori).

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
![hasil strace](./screenshots/strace%20ls.png.)

---

.## Analisis
- Jelaskan makna hasil percobaan. 
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
System call merupakan mekanisme utama komunikasi antara program user dan kernel.
Program di user mode tidak bisa langsung mengakses perangkat keras atau memori sistem, sehingga membutuhkan system call untuk meminta layanan kernel.

Mekanisme system call menunjukkan bahwa sistem operasi memiliki struktur berlapis yang memisahkan program user dari kernel. Kernel bertindak sebagai penghubung utama antara aplikasi dan perangkat keras, menjamin keamanan, stabilitas, serta efisiensi dalam pengelolaan sumber daya komputer.

---

## Quiz
1. [Apa fungsi utama system call dalam sistem operasi]  
   Fungsi utama system call adalah memberikan antarmuka yang aman dan terstandar agar program di user mode dapat menggunakan layanan kernel tanpa harus berinteraksi langsung dengan perangkat keras.
Dengan system call, sistem operasi dapat mengontrol akses, menjaga keamanan  
2. [Sebutkan 4 kategori system call yang umum digunakan]  
1. Process Control, 2. File Management, 3. Device Management, dan 4. Information Maintenance.
3. [Mengapa system call tidak bisa dipanggil langsung oleh user program]  
System call tidak dapat dipanggil langsung oleh program user karena alasan keamanan, stabilitas, dan pemisahan mode eksekusi.
Semua akses ke sumber daya perangkat keras harus melalui kernel, yang bertugas mengatur, memvalidasi, dan mengeksekusi permintaan tersebut secara aman.  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  semuanya menantang pak karena baru dua kali pertemuan
- Bagaimana cara Anda mengatasinya?  
  bertanya ke teman yang sudah lulus dan belajar otodidak

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
