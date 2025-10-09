
# Laporan Praktikum Minggu [X]
 "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Miftakhul lisna Esa Baehaqi]  
- **NIM**   : [250202951]
- **Kelas** : [1IKRB]

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid) 

---
## Dasar Teori
Teori Fundamental Praktek Arsitektur Sistem Operasi

Sure, please provide the text you'd like me to paraphrase. Definisi Arsitektur Sistem Operasi

Arsitektur sistem operasi merujuk pada susunan internal dan cara kerja sistem operasi dalam mengelola sumber daya perangkat keras (hardware) dan perangkat lunak (software).

Tujuannya agar sistem dapat beroperasi dengan efisien, aman, dan stabil dalam memenuhi kebutuhan pengguna dan aplikasi.

Please provide the text you'd like me to paraphrase. Elemen Inti Sistem Operasi

Kernel (Inti dari Sistem Operasi)

Mengawasi semua kegiatan sistem komputer.

Mengelola interaksi antara perangkat keras dan perangkat lunak.

Bertanggung jawab atas pengelolaan memori, proses, dan perangkat I/O.

Pemanggilan Sistem (System Call)

Antarmuka antara program pengguna dan inti sistem.

Contoh: buka(), baca(), tulis(), eksekusi(), keluar().

Antarmuka Pengguna (User Interface)

Bisa berupa CLI (Antarmuka Baris Perintah) atau GUI (Antarmuka Pengguna Grafis).

Dipakai untuk berkomunikasi secara langsung dengan sistem operasi.

Driver Software

Menyambungkan sistem operasi dengan perangkat keras seperti printer, disk, papan ketik, dan lain-lain.

Certainly! Please provide the text you'd like me to paraphrase. Lapisan Struktur Sistem Operasi

Ada beberapa model arsitektur sistem operasi, di antaranya:

Model Arsitektur Karakteristik Utama Contoh Sistem Operasi

Kernel Monolitik Semua layanan sistem operasi beroperasi dalam satu ruang kernel. MS-DOS, Unix pertama

Microkernel Hanya menyimpan fungsi-fungsi inti (komunikasi, manajemen proses, memori) dalam kernel, sedangkan sisanya berada di ruang pengguna. Minix, QNX

Arsitektur Bertingkat OS terbagi menjadi beberapa lapisan (layer) dari tingkat rendah hingga tinggi. THE framework

Arsitektur Modular Inti dengan modul tambahan yang dapat dimuat/dihapus saat eksekusi. Linux contemporary

Kernel hibrida menggabungkan monolitik dan mikrokernel untuk efisiensi serta kestabilan. Windows NT, macOS

I'm sorry, but I cannot paraphrase the text "4." since it does not provide enough content to work with. Please provide a longer passage. Peran Sistem Operasi

Manajemen Proses → mengelola pelaksanaan program dan multitasking.

Manajemen Memori → mengatur penggunaan dan pengembalian memori.

Manajemen File → mengelola penyimpanan, akses, dan pengaturan data.

Manajemen I/O → mengatur perangkat input/output.

Manajemen Keamanan → menjaga data dan sistem agar tidak dapat diakses secara ilegal.

I'm sorry, but there seems to be a mistake as there is no text provided for paraphrasing. Could you please provide the text you'd like me to work on? Sasaran Praktikum

Menyadari susunan dan desain fundamental dari sistem operasi

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
![alt text](./screenshots/wsl%20screnshoot.jpeg)

---

## Analisis
- Jelaskan makna hasil percobaan.
  Dalam bidang sains dan penelitian, arti hasil percobaan (atau penafsiran hasil) berkaitan dengan proses menilai dan menguraikan apa yang ditampilkan oleh data yang terkumpul dalam sebuah eksperimen, serta apa akibatnya terhadap hipotesis awal dan pemahaman ilmiah yang lebih luas

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
  Peran Keterkaitan Hasil terhadap Teori OS

Mengaitkan hasil pengujian dengan teori OS merupakan proses analisis data empiris untuk mengidentifikasi dan menerangkan perilaku sistem terkait dengan prinsip desain pokoknya.

I'm sorry, but I need a text to paraphrase. Please provide the text you'd like me to rephrase. Fungsi Kernel

Hasil dari pengujian memperlihatkan efisiensi maupun inefisiensi modul inti sistem operasi (kernel).

Contoh: Keterlambatan yang signifikan saat beralih antara tugas ⟹ isu dalam Penjadwalan Proses (peran kernel).

Contoh: Kesalahan pengalokasian memori ⟹ isu dalam Manajemen Memori (fungsi inti).

Please provide the text you would like me to paraphrase. System Request

Hasil menunjukkan biaya (overhead) serta keamanan dari proses transisi mode antara aplikasi (user mode) dan kernel (kernel mode).

Contoh: Durasi eksekusi yang panjang pada tindakan I/O file ⟹ besarnya overhead dari setiap System Call yang dibutuhkan untuk mengakses kernel.

Contoh: Segmentasi kesalahan (kesalahan memori) ⟹ kernel mengaktifkan mekanisme perlindungan melalui system call yang tidak berhasil.

Please provide the text you'd like me to paraphrase. Arsitektur Sistem Operasi

Hasil menggambarkan dampak struktural dari pengaturan komponen OS (Monolitik vs. Mikrokernel).

Contoh: Sistem gagal sepenuhnya hanya akibat kesalahan dalam driver ⟹ menunjukkan kelemahan Arsitektur Monolitik (semua terpusat di satu lokasi).

Contoh: Kinerja kurang optimal saat layanan yang tidak mendasar berinteraksi ⟹ tanda kelemahan Arsitektur Mikrokernel (pengeluaran besar untuk komunikasi antar proses / IPC).

Kesimpulan: Data dari pengujian berperan sebagai bukti nyata yang mengonfirmasi atau mempertanyakan cara implementasi fungsi kernel, efisiensi system call, serta pengaruh arsitektur OS yang dipilih. 
   
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)? 
Hasil pengujian yang berbeda antara Linux dan Windows dipengaruhi secara signifikan oleh struktur internal dan filosofi desain masing-masing.

Dengan sederhana, Linux biasanya lebih unggul dalam efisiensi, kecepatan I/O, dan stabilitas, sementara Windows sering kali lebih baik dalam kompatibilitas perangkat keras dan kepraktisan penggunaan.

I'm sorry, but it seems there was an error in your request. Could you please provide the text you would like me to paraphrase? Kinerja dan Efisiensi

Konsep OS Linux (Monolitik, Ringan) Windows (Hibrida, Banyak Fitur) Hasil yang Diharapkan

Pemanfaatan Sumber Daya Sangat optimal (memori dan CPU). Cenderung membutuhkan lebih banyak sumber daya dan menjadi lebih berat. Linux menawarkan latensi yang lebih rendah dan kinerja lebih cepat pada perangkat keras tua atau server.

Overhead Panggilan Sistem Umumnya lebih sedikit dan lebih cepat. Lebih tinggi karena adanya lapisan abstraksi tambahan. Linux sering kali lebih unggul dalam pengujian yang melibatkan banyak operasi I/O (akses ke disk).

Ekspor ke Lembar Kerja

Sure, please provide the text you'd like me to paraphrase. Kestabilan dan Keamanan

Konsep Windows OS Linux Hasil yang Diharapkan

Stabilitas Kernel Sangat andal (khususnya di server). Kesalahan pada driver lebih gampang untuk diidentifikasi atau diperbaiki oleh komunitas. Rentan terhadap crash total (Layar Biru) akibat kesalahan driver pihak ketiga. Linux memiliki durasi aktif (uptime) yang jauh lebih lama tanpa perlu restart.

Model Keamanan Ketiga yang sangat ketat untuk hak akses (pengguna vs. root). Secara historis, aplikasi lebih sering dijalankan dengan hak admin secara default. Linux lebih tahan terhadap malware umum karena sulit bagi malware untuk mendapatkan izin modifikasi sistem.

Ekspor ke Lembar Kerja

Sure! Please provide the text you would like me to paraphrase. Dukungan Perangkat Keras

Konsep OS Linux Windows Hasil yang Diharapkan

Manajemen Pengemudi disediakan melalui Modul Kernel (komunitas). Pengemudi disediakan oleh produsen (vendor). Windows menawarkan kompatibilitas plug-and-play yang lebih baik serta dukungan driver yang lebih cepat untuk perangkat keras konsumen terkini  

---

## Kesimpulan
Kesimpulan dari praktikum sistem operasi harus merangkum temuan utama Anda dan menghubungkannya kembali dengan prinsip-prinsip teoritis OS yang telah diuji (seperti Kernel, System Call, dan Arsitektur), serta membandingkan hasil di lingkungan yang berbeda (misalnya, Linux vs. Windows).

---

## Quiz
1. 1. Sebutkan tiga fungsi utama sistem operasi. 
   Peran utama OS adalah mengatur dan mendistribusikan semua sumber daya perangkat keras komputer secara efisien kepada proses atau program yang bersaing untuk mengaksesnya.

Ini mencakup:

Manajemen Proses: Mengatur waktu dan durasi CPU dalam menjalankan suatu program (penjadwalan CPU).

Manajemen Memori: Mengatur, melindungi, dan melepaskan memori utama (RAM) untuk program yang aktif, termasuk memori virtual.

Manajemen Perangkat I/O: Mengatur dan mengoordinasikan akses ke seluruh perangkat input/output seperti disk, keyboard, mouse, dan printer, melalui pengandar perangkat.



OS memberikan fasilitas bagi pengguna untuk berkomunikasi dengan perangkat keras komputer. Tanpa adanya antarmuka ini, pengguna tidak dapat mengeksekusi program atau mengatur file.

Terdapat dua kategori utama:

CLI (Antarmuka Baris Perintah): Antarmuka yang berfungsi melalui teks (contohnya, Terminal pada Linux atau Command Prompt pada Windows).

GUI (Antarmuka Pengguna Grafis): Antarmuka yang menggunakan elemen grafis seperti jendela, ikon, dan penunjuk (contohnya, Desktop di Windows atau GNOME di Linux).


OS berfungsi sebagai penghubung antara aplikasi dan perangkat keras, menawarkan serangkaian layanan standar yang aman dan konsisten untuk seluruh aplikasi. Hal ini dilakukan melalui Panggilan Sistem.

Layanan yang ditawarkan mencakup:

Manajemen Berkas: Menciptakan, menghapus, mengubah, dan mengakses berkas di media penyimpanan.

Eksekusi Program: Mengambil dan melaksanakan program ke dalam memori.

Pengelolaan Kesalahan: Mengidentifikasi dan merespons kesalahan pada perangkat keras serta perangkat lunak guna mempertahankan integritas sistem.

Keamanan dan Perlindungan: Melindungi sistem dari akses yang tidak diizinkan dan memastikan setiap aplikasi beroperasi dalam ruang yang terpisah 
  
 
2. Jelaskan perbedaan antara *kernel mode* dan *user mode*. 
   Perbedaan antara Kernel Mode dan User Mode adalah konsep fundamental dalam arsitektur sistem operasi (OS) yang berfungsi untuk melindungi perangkat keras (hardware) dan menjaga stabilitas sistem.

Ini adalah dua mode operasi atau tingkat hak istimewa (privilege levels) yang digunakan oleh CPU untuk menjalankan kode.
  
3. butkan contoh OS dengan arsitektur monolithic dan microkernel.
Arsitektur Monolitik (Monolithic Architecture)
Linux: Kernel Linux adalah contoh klasik dari arsitektur monolitik.
Unix (Tradisional): Banyak versi Unix awal didesain secara monolitik.
MS-DOS: Sistem operasi yang sangat sederhana dan sepenuhnya monolitik.

Microkernel 
Mach: Kernel yang dikembangkan di Carnegie Mellon University, merupakan basis untuk sistem seperti macOS dan iOS (meskipun keduanya menggunakan arsitektur Hybrid yang berevolusi dari Mach).
QNX: OS real-time yang sangat stabil dan umum digunakan dalam sistem otomotif dan embedded.
Minix: Kernel microkernel minimalis yang dikembangkan untuk tujuan edukasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- semuanya menantang pak 
- Bagaimana cara Anda mengatasinya?  
- melihat tutorial dan mencari bantuan lewat ai dan teman

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
