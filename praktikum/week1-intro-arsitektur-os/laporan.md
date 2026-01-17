
# Laporan Praktikum Minggu [X]
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Novia Safitri  
- **NIM**   : 250202923
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1.Menjelaskan peran sistem operasi dalam arsitektur komputer.
2.Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3.Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4.Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).

---

## Dasar Teori
1. Arsitektur sistem operasi komponen-komponen sistem operasi berinteraksi satu sama lain ,dan bertujuan untuk menciptakan sistem yang efisien ,stabil,aman,dan mudah dikelola
2.Monolithic architecture seluruh komponen sistem operasi dijalankan dalam satu ruang kernel (kernel space). Semua layanan inti seperti manajemen file, manajemen proses, dan manajemen perangkat keras saling terintegrasi dalam satu kesatuan.Contohnya linux dan UNIX tradisional
3. Layerd Architecture membagi sistem operasi ke dalam beberapa lapisan (layer) dengan tingkat abstraksi yang berbeda. Setiap lapisan hanya berinteraksi dengan lapisan di atas atau di bawahnya.
4. Microkernel hanya menyediakan fungsi dasar seperti komunikasi antar proses (IPC), manajemen memori, dan manajemen perangkat keras. Fungsi lainnya, seperti manajemen file dan driver perangkat, dijalankan di ruang pengguna (user space).
5. Perbedaan arsitektur dapat memengaruhi kinerja, stabilitas, dan keamanan sistem operasi dalam praktikum, sehingga berpengaruh pada cara sistem bekerja dan seberapa andal sistem tersebut.

---

## Langkah Praktikum
1. Setup Environment

Pastikan Linux (Ubuntu/WSL) sudah terinstal.
Pastikan Git sudah dikonfigurasi dengan benar:
git config --global user.name "Nama Anda"
git config --global user.email "email@contoh.com"
  
2. Diskusi Konsep
Baca materi pengantar tentang komponen OS.
Identifikasi komponen yang ada pada Linux/Windows/Android.
 
3. Eksperimen Dasar Jalankan perintah berikut di terminal:
uname -a
whoami
lsmod | head
dmesg | head

4. Membuat Diagram Arsitektur
Buat diagram hubungan antara User → System Call → Kernel → Hardware.
Gunakan draw.io atau Mermaid.
Simpan hasilnya di:
praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png

5. Penulisan Laporan

Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam laporan.md.
Tambahkan screenshot hasil terminal ke folder screenshots/.

6. Commit & Push
   git add .
git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
git push origin main



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
![alt text](<screenshots/ss tugas1.png>)

---

## Analisis
- Makna hasil percobaan arsitektur sistem operasi menunjukan bahwa perbedaan arsitektur memiliki pengaruh nyata terhadap cara sistem mengelola sumber daya ,menjalankan proses,serta menjaga kestabilan dan keamanannya,sehingga memahami arsitektur menjadi hal penting untuk mengoptimalkan kinerja sistem operasi  
- Hubungan  hasil dengan teori fungsi kernel ,system call, dan arsitektur os.Fungsi kernel—sebagai pengelola inti proses, memori, dan I/O—terbukti efisien jika hasil menunjukkan minimasi overhead (e.g., konteks switching rendah di SJF), mencerminkan teori multiplexing dan proteksi sumber daya. System call berfungsi sebagai jembatan user-kernel yang optimal, di mana hasil delay rendah (e.g., via fork() atau read()) mengonfirmasi teori mode switch untuk keamanan dan abstraksi hardware, meski terlalu banyak call bisa sebabkan bottleneck seperti thrashing. Secara keseluruhan, arsitektur OS (monolitik, mikrokernel, atau hybrid seperti Linux) terbukti dalam hasil percobaan: efisiensi tinggi menandakan balance antara fairness, keandalan, dan performa, sementara anomali (e.g., deadlock) menyoroti kebutuhan optimasi teori seperti Banker's Algorithm atau CFS scheduler.  
- Perbedaan hasil di lingkungan OS berbeda Linux vs Windows. Linux Hasil percobaan lebih cepat dan hemat (proses jalan lancar, memori/CPU tidak boros, file cepat dibaca/tulis). Bagus untuk kerja berat seperti server atau programming, karena OS-nya "ringan" dan langsung.
Windows hasil agak lambat tapi nyaman (ada delay saat banyak tugas, tapi stabil untuk aplikasi harian). Cocok untuk gaming, kantor, atau pemula, karena banyak fitur bantu dan mudah pakai.  

---

## Kesimpulan
 Dari hasil praktikum arsitektur sistem operasi dapat disimpulkan bahwa pratikum ini membantu  kits memahami komponen inti sistem operasi seperti kernel manajemen proses ,dan manajemen memori saling berinteraksi dalam menjalankan sistem komputer. Melalui eksperimen langsung misalnya menggunakan linux, MV atau emulator,dan melatih kita untuk menumbuhkan pemahaman akan pentingnya efisien dan kendala sistem operasi dalam skala besar. 

---
## tugas
A.Perbedaan Monolitik Kernel, Mikrokernel, dan Arsitektur Berlapis
  Arsitektur kernel merupakan fondasi utama sistem operasi (OS) yang menentukan bagaimana komponen seperti proses manajemen, memori, dan perangkat keras terintegrasi. Tiga model utama—kernel monolitik, mikrokernel, dan arsitektur berlapis ;
1.	Kernel monolitik merupakan desain di mana semua bagian utama kernel, seperti penggerak perangkat, penjadwal proses, serta sistem file, beroperasi dalam satu area memori yang sama (yaitu ruang kernel). Layanan-layanan sistem operasi saling terintegrasi secara rapat, sehingga komunikasi antar-komponen bisa dilakukan langsung tanpa tambahan beban. Kelebihannya mencakup kinerja yang sangat baik, karena mengurangi pergantian konteks dan membuat panggilan sistem lebih efisien. Namun, kelemahannya adalah rendahnya tingkat modularitas: jika satu modul mengalami masalah (misalnya, driver yang rusak), hal itu bisa memicu kegagalan keseluruhan kernel dan menyebabkan sistem mati total. Desain ini juga menantang untuk dikembangkan, sebab kode-nya cenderung besar, rumit, dan sulit dikelola.
2.	Mikrokernel , sebaliknya, meminimalkan ukuran kernel dengan hanya menyertakan fungsi dasar seperti komunikasi antar-proses (IPC), manajemen thread dasar, dan penjadwalan sederhana di ruang kernel. Layanan lain seperti driver, file sistem, dan jaringan dijalankan sebagai proses user-space terpisah. Komunikasi dilakukan melalui pesan-pesan IPC, yang meningkatkan modularitas dan keamanan karena kegagalan satu layanan tidak mempengaruhi inti inti. Keamanan lebih baik karena isolasi, memudahkan deteksi bug dan pemulihan. Namun, overhead IPC menyebabkan kinerja lebih lambat, terutama untuk operasi intensif seperti I/O, karena banyak konteks peralihan.
3.	Arsitektur Berlapis mengorganisir OS menjadi lapisan-lapisan hierarkis, di mana setiap lapisan bergantung pada lapisan di bawahnya dan menyediakan abstraksi untuk lapisan atas. Lapisan terbawah berinteraksi langsung dengan hardware (misalnya, kernel dasar), sementara lapisan atas menangani aplikasi user. Ini mirip dengan model OSI di jaringan, dengan prinsip enkapsulasi: perubahan di lapbawah tidak mempengaruhi yang atas jika antarmuka tetap konsisten. Keuntungannya adalah kemudahan pengembangan dan pemeliharaan karena modularitas vertikal, serta kemampuan debugging lapis demi lapis. Kekurangannya adalah performa yang lebih rendah karena data harus melewati banyak lapisan, menyebabkan kemacetan, dan ketergantungan ketat yang bisa membuat sistem menjadi kaku.
B.Contoh OS Nyata yang Menggunakan Masing-Masing Model
Kernel Monolitik : Linux adalah contoh klasik, di mana kernel-nya mencakup hampir semua layanan dalam satu modul besar, meskipun mendukung modul loadable untuk berfungsi. Windows NT juga monolitik pada intinya, dengan driver dan subsistem terintegrasi, meski memiliki elemen hybrid untuk kompatibilitas. 
Microkernel : Minix, dikembangkan oleh Andrew Tanenbaum, adalah mikrokernel pionir yang digunakan untuk pengajaran dan sistem tertanam. QNX, OS real-time untuk otomotif dan medis, menggunakan mikrokernel untuk siluet tinggi, di mana driver berjalan di ruang pengguna. Keluarga L4 (seperti seL4) juga mikrokernel, diterapkan di sistem keamanan tinggi seperti smartphone dan hypervisor.
Layered Architecture : THE OS (Technische Hogeschool Eindhoven), prototipe tahun 1960-an, adalah contoh murni dengan lapisan dari hardware hingga aplikasi. OS/2 dari IBM menggunakan pendekatan berlapis untuk kompatibilitas dengan DOS, dengan lapisan kepribadian untuk menjalankan aplikasi lama. Beberapa sistem tertanam modern seperti VxWorks memiliki elemen berlapis, meski sering hybrid. 
C. Model  yang Paling Relevan untuk OS modern 
Dalam konteks OS modern ,arsitektur monolitik tetap paling relevan untuk aplikasi umum yang memprioritaskan kinerja . Namun ,untuk sistem kritis seperti real-time embedded atau keamanan tinggi , arsitektur mikrokernel semakin relevan . Arsitektur berlapis kurang dominan saat  ini karena hambatan kinerja , tapi berguna di lingkungan legacy atau simulasi . Pilihan tergantung kebutuhan seperti performa untuk server ,keamanan untuk IoT .   


## Quiz
1. Sebutkan tiga fungsi utama sistem operasi?  
   Jawaban: Process management,Memory management,File management,Device management,User interface,and Security  
2. Jelaskan perbedaan antara kernel mode dan user mode?  
   Jawaban:Mode Kernel : Mode dengan akses penuh (istimewa) ke perangkat keras, memori, dan perangkat. Digunakan oleh kernel OS, driver, dan proses sistem. Seperti "superuser"—bisa mengubah segalanya, tapi kesalahan bisa membuat seluruh sistem crash.
Mode Pengguna : Mode terbatas (non-privileged) untuk aplikasi pengguna (browser, game, dll.). Hanya akses melalui permintaan ke kernel (system call), tidak langsung disentuh hardware. Seperti "tamu"—aman, kesalahan aplikasi tidak merusak sistem secara keseluruhan.
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel!  
   Jawaban: -Monolithic : Linux,MS-DOS,FreeBSD
            -Microkernel : Minix,QNX,L4 Microkernel,     

---

## Refleksi Diri
Tuliskan secara singkat:
-Apa bagian yang paling menantang minggu ini?
  Bagian yang menantang minggu ini, bagi saya itu ketika mengerjakan matkul sistem operasi yang cara pengerjaan dan pengumpulannya sangat membingungkan sehingga saya lumayan kesulitan ketika mengerjakan tugasnya dan beberapa kali salah dalam mengunggah tugas sistem operasi   
- Bagaimana cara Anda mengatasinya?  
  Cara saya mengatasi hal tersebut saya melihat tutorial diyoutube atau tiktok dan ketika  masih bingung saya minta diajari teman yang sudah paham 
---  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
