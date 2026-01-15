
# Laporan Praktikum Minggu [12]
Topik: [Virtualisasi Menggunakan Virtual Machine]

---

## Identitas
| Nama | NIM | Kelas |
| :--- | :--- | :--- |
| MOHAMMAD FATIKH MAHSUN | 250202952 | 1 IKRB |
| LUTHFI AULIA RAHMAN | 250202948 | 1 IKRB |
| APRIL TRIADI | 250202930 | 1 IKRB |

---

## Tujuan
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
2. Membuat dan menjalankan sistem operasi guest di dalam VM.
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
- Virtualisasi: Teknologi yang memungkinkan pembuatan versi virtual dari sumber daya fisik (hardware) agar satu komputer fisik bisa menjalankan beberapa sistem operasi secara bersamaan.

- Virtual Machine (VM): Sebuah lingkungan komputer virtual yang berfungsi seperti komputer fisik asli, lengkap dengan CPU, RAM, dan penyimpanan sendiri.

- Host OS vs Guest OS: Host adalah sistem operasi utama pada laptop (Windows 11), sedangkan Guest adalah sistem operasi yang berjalan di dalam VM (Ubuntu).

- Hypervisor (VirtualBox): Perangkat lunak yang mengelola dan menjembatani pembagian sumber daya hardware dari laptop fisik ke dalam Virtual Machine.

- Alokasi Resource: Performa VM sangat bergantung pada jumlah RAM dan CPU yang diberikan; semakin besar alokasi, semakin lancar sistem berjalan (High Resource), dan sebaliknya (Low Resource).

---

## Langkah Praktikum
1. A. Persiapan dan Instalasi

    Mengunduh file ISO Ubuntu 24.04 Desktop dan installer Oracle VirtualBox.

    Menginstal Oracle VirtualBox pada Host OS (Windows 11).

    Mengambil screenshot hasil instalasi VirtualBox sebagai bukti (instalasi_vm.png).

2. B. Konfigurasi Awal (High Resource)

    Membuat Virtual Machine baru di VirtualBox dengan nama Linux-Ubuntu.

    Mengatur spesifikasi awal (High Resource): RAM 4096 MB (4 GB) dan CPU 2 Core.

    Memasukkan file ISO Ubuntu ke dalam VM dan melakukan proses instalasi hingga masuk ke desktop.

   Mengambil screenshot konfigurasi resource ini (konfigurasi_resource.png).

3. C. Eksperimen VM (Beban Kerja Tinggi)

   Membuka Terminal di Ubuntu untuk mengecek spesifikasi sistem.

   Membuka browser Firefox, memutar video YouTube, dan membuka 5 tab sekaligus sebagai pengujian beban kerja (stress test).

   Membuka System Monitor untuk memantau grafik penggunaan RAM dan CPU saat beban tinggi.

   Mengambil screenshot saat sistem berjalan (os_guest_running.png).

4. D. Eksperimen Mengurangi Resource (Low Resource)

    Mematikan (Shutdown) Virtual Machine.

   Masuk ke menu Settings > System di VirtualBox untuk mengubah alokasi resource.

   Menurunkan spesifikasi menjadi: RAM 2048 MB (2 GB) dan CPU 1 Core.

   Menjalankan kembali VM dan mengulangi pengujian dengan Firefox untuk mengamati penurunan performa (lag).

5. E. Analisis dan Dokumentasi

   Mencatat spesifikasi lengkap laptop asli (Host) dan laptop virtual (Guest).

   Menyusun semua screenshot dan catatan ke dalam folder yang telah ditentukan.

6. F. Commit & Push


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
 Mengecek user yang sedang aktif
whoami

 Menampilkan informasi detail kernel dan arsitektur sistem
uname -a

 Menampilkan daftar file di direktori saat ini
ls

 Mengecek penggunaan Memori (RAM)
free -h

 Menampilkan versi distribusi OS secara detail
lsb_release -a

 Mengecek jumlah core CPU yang dialokasikan
nproc

 Menampilkan ringkasan perangkat keras virtual
sudo lshw -short
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Week12.1.png)

![Screenshot hasil](screenshots/Week12.2.png)

![Screenshot hasil](screenshots/Week12.3.png)

![Screenshot hasil](screenshots/Week12.4.png)

---

## Analisis
-  Skenario High Resource (4GB RAM, 2 Core): Sistem berjalan lancar dan responsif, mampu menangani beban kerja Firefox (YouTube + 5 tab) dengan stabil.

- Skenario Low Resource (2GB RAM, 1 Core): Terjadi penurunan performa yang signifikan (lag), respons menu melambat, dan penggunaan memori mendekati batas maksimal saat stress test.

- Kesimpulan: Alokasi sumber daya (CPU & RAM) sangat berpengaruh terhadap kecepatan pemrosesan instruksi dan stabilitas Sistem Operasi di lingkungan virtual.

---

## Kesimpulan
- Pentingnya Alokasi Resource: Performa Sistem Operasi (Ubuntu) sangat bergantung pada jumlah RAM dan CPU yang diberikan; semakin besar alokasi, semakin stabil sistem dalam menangani beban kerja tinggi.

- Virtualisasi sebagai Solusi: Penggunaan VirtualBox memungkinkan pengujian sistem operasi yang berbeda di atas satu perangkat fisik (Host) tanpa risiko merusak sistem utama.

- Batas Minimum Performa: Untuk menjalankan Ubuntu 24.04 secara lancar, alokasi 4GB RAM dan 2 Core adalah pilihan ideal, sementara penggunaan 2GB RAM dan 1 Core menyebabkan sistem menjadi tidak responsif (lag).

---

## Quiz
1. Apa perbedaan antara host OS dan guest OS?

   Jawaban:

   - Host OS: Sistem operasi utama yang terpasang langsung pada hardware laptop (contoh: Windows 11 di Lenovo LOQ kamu). Ia mengelola seluruh sumber daya fisik laptop secara langsung.

   - Guest OS: Sistem operasi yang berjalan secara virtual di dalam VirtualBox (contoh: Ubuntu 24.04 yang sedang kamu unduh). Ia hanya menggunakan sebagian sumber daya yang "dipinjamkan" oleh Host OS.



2. Apa peran hypervisor dalam virtualisasi?

   Jawaban:

   - Pembagi Resource: Mengambil sebagian RAM dan CPU dari laptop aslimu untuk diberikan kepada sistem virtual (Ubuntu).

    -  Pemisah (Isolasi): Menjaga agar sistem virtual tidak mengganggu sistem utama, sehingga jika Ubuntu error, Windows kamu tetap aman.

     - Penerjemah: Menjadi jembatan agar perintah dari sistem virtual bisa dimengerti oleh perangkat keras laptopmu.



3. Mengapa virtualisasi meningkatkan keamanan sistem?

   Jawaban:

   - Isolasi (Sandboxing): Jika Ubuntu (Guest OS) terkena virus atau error, dampaknya hanya terjadi di dalam Virtual Machine tersebut dan tidak akan merusak Windows 11 (Host OS) kamu.

    - Lingkungan Pengujian yang Aman: Kamu bisa mencoba aplikasi atau file yang mencurigakan di dalam sistem virtual tanpa risiko membahayakan data penting di laptop asli.

    - Snapshot (Pemulihan Cepat): VirtualBox memiliki fitur untuk mengambil "foto" keadaan sistem yang bersih; jika terjadi kerusakan, kamu bisa mengembalikannya ke kondisi normal dalam sekejap.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
