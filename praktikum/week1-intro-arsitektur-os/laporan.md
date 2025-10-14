
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Mohammad Fatikh Mahsun]  
- **NIM**   : [250202952]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
 
> Fungsi Utama Sistem Operasi:
Fungsi utama sistem operasi yaitu  sebagai penghubung antara perangkat keras dan perangkat lunak serta menjaga efisiensi dan keamanan dalam penggunaan sumber daya komputer. 
1.Manajemen Proses: Sistem operasi mengatur proses yang berjalan di komputer, termasuk penjadwalan CPU agar proses-proses dapat berjalan secara efisien dan tidak saling mengganggu.
2.Manajemen Memori: Mengelola alokasi memori utama untuk berbagai aplikasi agar dapat berjalan tanpa tumpang tindih dan memastikan penggunaan memori optimal.
3.Manajemen File dan Perangkat Keras: Mengelola penyimpanan data seperti file dan direktori serta mengontrol perangkat keras (seperti printer, keyboard) melalui driver agar dapat digunakan oleh aplikasi dan pengguna dengan lancar.
Peran Kernel:
Kernel adalah bagian inti dari sistem operasi yang memiliki hak akses penuh ke semua sumber daya hardware dan menjalankan fungsi-fungsi dasar seperti manajemen proses, manajemen memori, dan komunikasi antar perangkat keras. Kernel berjalan di mode kernel (privileged mode) untuk menjalankan operasi tingkat rendah secara efisien dan aman.
System Call:
System call adalah antarmuka atau mekanisme yang digunakan oleh program aplikasi untuk berkomunikasi dengan kernel. Melalui system call, aplikasi dapat meminta layanan sistem operasi seperti membuka file, mengalokasikan memori, atau melakukan penjadwalan proses tanpa harus mengakses hardware secara langsung. Dengan ini, system call menjadi jembatan penting antara program pengguna dengan kernel, menjaga keamanan dan stabilitas sistem.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

1.Sistem operasi adalah perangkat lunak inti yang menghubungkan pengguna dan perangkat keras komputer dengan mengelola semua sumber daya komputer secara efisien dan stabil.
2.Fungsi utama sistem operasi meliputi manajemen proses, manajemen memori, manajemen perangkat keras , dan manajemen file.
3.Kernel adalah bagian inti sistem operasi yang berjalan di mode kernel dengan hak akses penuh untuk menjalankan tugas-tugas dasar dan mengatur sumber daya sistem.
4.System call adalah mekanisme yang memungkinkan aplikasi berkomunikasi dengan kernel untuk meminta layanan sistem operasi seperti akses file, memori, dan perangkat keras.
5.Dengan sistem operasi, perangkat keras dan perangkat lunak dapat bekerja bersama secara terkoordinasi agar komputer dapat menjalankan program dengan benar dan aman. 

---

## Langkah Praktikum

1.Melakukan fork terhadap repositori yang telah ditentukan.

2.Mengubah nama repositori hasil fork sesuai dengan ketentuan.

3.Melakukan clone repositori tersebut ke dalam direktori kerja di komputer lokal.

4.Membuat struktur direktori baru di dalam repositori lokal.

5.Di dalam direktori tersebut, dibuat sebuah file laporan.md dan subdirektori screenshot/.

6.Menyusun ringkasan mengenai sejarah kriptografi dan prinsip CIA Triad di dalam file laporan.md.

7.Mengerjakan dan mencantumkan jawaban kuis yang diberikan pada modul ke dalam laporan.

8.Menambahkan semua perubahan ke Git (stage), lalu melakukan commit dengan pesan week1-intro-cia dan mengunggahnya (push) ke repositori remote di GitHub.

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
![Screenshot hasil](screenshots/example.png)

---

## Analisis
1.Jelaskan makna hasil percobaan.
2.Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
3.Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?

1.Makna hasil percobaan adalah apa yang didapat atau terjadi setelah melakukan sebuah uji coba atau eksperimen, khususnya dalam sistem operasi. Hasil ini bisa berupa bagaimana kernel, panggilan sistem (system call), dan struktur sistem operasi bekerja saat menjalankan komputer, mengatur sumber daya, dan menjalankan aplikasi dengan baik dan efisien 

2. Hubungan hasil dengan teori:
•kernel berfungsi mengatur sumber daya agar sistem berjalan dengan baik dan efisien.
•System call ini sebagai jembatan yang menghubungkan program pengguna dengan fungsi utama dalam kernel.
•Arsitektur sistem operasi mempengaruhi bagaimana kernel dan system call diorganisasi.

3.Perbedaan hasil di lingkungan OS berbeda (Linux vs Windows):
•Linux menggunakan kernel monolitik yang menggabungkan berbagai fungsi penting dalam satu bagian besar, seperti pengelolaan memori dan penjadwalan proses.
•sedangkan windows memakai kernel hybrid yang menggabungkan fitur dari monolitik dan microkernel, dengan tambahan subsistem seperti pengelola daya dan objek.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1.Sistem operasi berperan penting sebagai penghubung antara perangkat keras dan perangkat lunak, mengelola sumber daya komputer agar dapat bekerja secara efisien dan stabil.
2.Fungsi utama sistem operasi meliputi manajemen proses, manajemen memori, dan manajemen file serta perangkat keras, yang memungkinkan pengguna dan aplikasi untuk menjalankan tugas dengan lancar.
3.Kernel sebagai inti sistem operasi menjalankan fungsi-fungsi dasar dengan hak akses penuh, sedangkan system call menjadi mekanisme komunikasi antara aplikasi dengan kernel untuk meminta layanan sistem.

---

## Quiz
1.Tiga fungsi utama sistem operasi adalah:
•Manajemen Proses: Mengatur proses yang berjalan, penjadwalan CPU, sinkronisasi antar proses, dan pengalihan konteks agar sistem berjalan efisien.
•Manajemen Memori: Mengalokasikan dan mengelola memori utama serta memori virtual untuk aplikasi yang berjalan agar tidak saling tumpang tindih.
•Manajemen File dan Perangkat Keras: Mengelola file dan direktori di sistem penyimpanan serta mengontrol perangkat input/output agar dapat digunakan oleh aplikasi dan pengguna .

2.Perbedaan Kernel Mode dan User Mode:
•Kernel Mode (Mode Kernel): Mode eksekusi dengan hak akses penuh ke semua sumber daya sistem seperti memori, perangkat keras, dan CPU. Kernel OS berjalan di mode ini untuk melakukan tugas tingkat rendah yang kritikal.
•User Mode (Mode Pengguna): Mode eksekusi dengan hak akses terbatas dimana aplikasi pengguna berjalan. Aplikasi tidak dapat mengakses hardware secara langsung dan harus meminta layanan melalui sistem operasi agar lebih aman dan stabil .

3.Contoh OS dengan arsitektur:
•Monolithic Kernel: Linux, BSD, Windows 9x.
•Microkernel: QNX, Mach, L4.
Model monolithic menggabungkan semua layanan dalam kernel, sedangkan microkernel memecah layanan ke ruang user demi modularitas dan keamanan.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?
  
-Bagian yang paling menantang pada minggu ini adalah : mengatur waktu antara belajar materi baru dan mengerjakan tugas secara efektif. 
-Dan cara mengatasi nya: itu dengan membagi materinya agar lebih mudah dipahami dan tetap konsisten serta berdiskusi dengan teman agar mendapatkan sudut pandang baru. 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
