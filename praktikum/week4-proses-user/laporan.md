
# Laporan Praktikum Minggu [4]
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : [Belinda Lani Regina]  
- **NIM**   : [2503202576]  
- **Kelas** : [1DSARA]

---

## Tujuan
> 1. Dapat menjelaskan konsep proses dan user dalam sistem operasi Linux.
> 2. Dapat menampilkan daftar proses yang sedang berjalan dan statusnya.
> 3. Dapat menggunakan perintah untuk membuat dan mengelola user.
> 4. Dapat menghentikan atau mengontrol proses tertentu menggunakan PID.
> 5. Dapat menjelaskan kaitan antara manajemen user dan keamanan sistem
---

## Dasar Teori
1. Proses adalah program yang sedang dieksekusi dan menjadi unit utama kerja sistem operasi. Setiap proses memiliki PID (Process ID) unik untuk identifikasi dan pengelolaan.
(Silberschatz et al., 2018)
2. Manajemen Proses Sistem operasi Linux mengatur pembuatan, penjadwalan, dan terminasi proses. Perintah seperti ps, top, kill, dan pstree digunakan untuk memantau dan mengontrol proses.
(Tanenbaum & Bos, 2015)
3. Hierarki Proses (Parent–Child), semua proses di Linux berasal dari proses induk systemd atau init. Proses baru dibuat melalui sistem panggilan fork() dan exec().
(OSTEP, 2018)
4. Manajemen User, Linux mendukung banyak pengguna (multiuser). Pengelolaan akun dilakukan dengan adduser, passwd, usermod, dan deluser. Hak akses diatur berdasarkan pengguna dan grup.
(Linux Manual Pages)
5. Keamanan dan Hak Akses, sistem izin file Linux terdiri dari read (r), write (w), dan execute (x) untuk pemilik, grup, dan lainnya. Ini menjaga agar hanya pengguna berwenang yang dapat mengakses file tertentu.
(Silberschatz et al., 2018)
---

## Langkah Praktikum
1.**Setup Environment**
- Gunakan Linux (Ubuntu/WSL).
- Pastikan Anda sudah login sebagai user non-root.
- Siapkan folder kerja:
```
   praktikum/week4-proses-user/
```

2. **Eksperimen 1 – Identitas User Jalankan perintah berikut:**
```
whoami
id
groups
```
- Jelaskan setiap output dan fungsinya.
- Buat user baru (jika memiliki izin sudo):
```
sudo adduser praktikan
sudo passwd praktikan
```
- Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses Jalankan:**
```
ps aux | head -10
top -n 1
```
- Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
- Simpan tangkapan layar top ke:
```
praktikum/week4-proses-user/screenshots/top.png
```

4. **Eksperimen 3 – Kontrol Proses**
- Jalankan program latar belakang:
```
sleep 1000 &
ps aux | grep sleep
```
Catat PID proses `sleep`.
- Hentikan proses:
```
kill <PID>
```
- Pastikan proses telah berhenti dengan ps aux | grep sleep.

5. **Eksperimen 4 – Analisis Hierarki Proses Jalankan:**
```
pstree -p | head -20
```
- Amati hierarki proses dan identifikasi proses induk (init/systemd).
- Catat hasilnya dalam laporan.

6. **Commit & Push**
```
git add .
git commit -m "Minggu 4 - Manajemen Proses & User"
git push origin main
```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
- Eksperimen 1
```
whoami
id
groups
```
- Eksperimen 2
```
ps aux | head -10
top -n 1
```
- Eksperimen 3
```
sleep 1000 &
ps aux | grep sleep
```
```
kill <PID>
```
- Eksperimen 4
```
pstree -p | head -20
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis

**-Eksperimen 1**
| **No** | **Perintah / Output**                                                                                                                       | **Penjelasan Output**                                                                                                                              | **Fungsi / Tujuan**                                           |
| :----: | :------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
|    1   | `whoami`                                                                                                                                    | Menampilkan nama user aktif saat ini: **belinda**                                                                                                  | Untuk mengetahui siapa user yang sedang login                 |
|    2   | `id`                                                                                                                                        | Menampilkan UID, GID, dan daftar grup dari user *belinda* → termasuk grup **sudo**, artinya user memiliki hak administratif                        | Untuk melihat identitas user serta hak aksesnya               |
|    3   | `sudo adduser praktikan`                                                                                                                    | Menjalankan perintah pembuatan akun baru bernama *praktikan*. Sistem memilih UID dan GID baru (1002) dan membuat home directory `/home/praktikan`. | Untuk menambahkan user baru ke sistem Linux                   |
|    4   | `passwd praktikan`                                                                                                                          | Diminta untuk membuat dan mengonfirmasi password baru untuk user *praktikan*.                                                                      | Untuk mengatur password login bagi user baru                  |
|    5   | Input informasi akun: <br>• Full Name: UPB<br>• Room Number: 12<br>• Work Phone: 123456789<br>• Home Phone: 987654321<br>• Other: 123456789 | Data identitas tambahan disimpan di `/etc/passwd`.                                                                                                 | Memberikan informasi identitas tambahan untuk user (opsional) |
|    6   | `Is the information correct? [Y/n] Y`                                                                                                       | Konfirmasi bahwa semua data sudah benar dan disimpan.                                                                                              | Menyimpan informasi user ke sistem                            |
|    7   | `Adding user 'praktikan' to group 'users' ...`                                                                                              | Menambahkan *praktikan* ke grup tambahan `users`.                                                                                                  | Memberikan hak akses umum bagi user baru                      |
|    8   | `passwd: password updated successfully`                                                                                                     | Password user berhasil dibuat dan tersimpan di sistem.                                                                                             | Menandakan user siap digunakan untuk login                    |
|    9   | (Keseluruhan hasil)                                                                                                                         | Akun **praktikan** telah dibuat dengan direktori home `/home/praktikan`, password, dan grup yang sesuai.                                           | User baru berhasil ditambahkan dan siap digunakan             |

**-Eksperimen 2**
| **No** | **Perintah / Output**                                               | **Penjelasan Output**                                                                                                                                                                                                                                 | **Fungsi / Tujuan**                                                                                  |
| :----: | :------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
|    1   | `ps aux`                                                            | Menampilkan **daftar semua proses aktif** di sistem. <br>• `a` = menampilkan semua proses milik semua user. <br>• `u` = menampilkan nama user dan info detail. <br>• `x` = menampilkan proses yang tidak terkait dengan terminal (daemon/background). | Untuk memantau semua proses sistem dan pengguna.                                                     |
|    2   | `head -10`                                                          | Menampilkan **10 baris pertama** dari hasil perintah sebelumnya.                                                                                                                                                                                      | Membatasi output agar hanya menampilkan sebagian proses (tidak terlalu panjang).                     |
|    3   | **Kolom USER**                                                      | Menampilkan nama user yang menjalankan proses, contoh: `root`, `systemd+`, `message+`.                                                                                                                                                                | Menunjukkan kepemilikan proses (apakah sistem atau user biasa).                                      |
|    4   | **Kolom PID**                                                       | Menunjukkan **Process ID** unik untuk tiap proses (contoh: 1, 7, 9, 49, 144, dst).                                                                                                                                                                    | Digunakan untuk mengidentifikasi proses tertentu, misalnya saat ingin menghentikannya dengan `kill`. |
|    5   | **%CPU dan %MEM**                                                   | Menunjukkan **persentase penggunaan CPU dan memori** oleh setiap proses.                                                                                                                                                                              | Untuk memonitor beban kinerja sistem dari masing-masing proses.                                      |
|    6   | **VSZ & RSS**                                                       | `VSZ` = ukuran virtual memory (dalam KB). <br>`RSS` = ukuran memori fisik yang digunakan.                                                                                                                                                             | Menunjukkan berapa banyak memori yang dikonsumsi tiap proses.                                        |
|    7   | **TTY**                                                             | Terminal pengendali proses (biasanya kosong untuk proses sistem).                                                                                                                                                                                     | Menunjukkan di terminal mana proses dijalankan.                                                      |
|    8   | **STAT**                                                            | Status proses, misalnya: <br>• `S` = sleeping (tidak aktif sementara) <br>• `R` = running (sedang berjalan) <br>• `Z` = zombie (selesai tapi belum dibersihkan)                                                                                       | Untuk mengetahui kondisi/status proses saat ini.                                                     |
|    9   | **START & TIME**                                                    | `START` = waktu proses dimulai. <br>`TIME` = total waktu CPU yang digunakan.                                                                                                                                                                          | Menunjukkan sudah berapa lama proses aktif.                                                          |
|   10   | **COMMAND**                                                         | Nama program atau perintah yang dijalankan (contoh: `/sbin/init`, `systemd-journald`, `dbus-daemon`).                                                                                                                                                 | Menunjukkan jenis program/proses yang sedang berjalan di sistem.                                     |
|   11   | `top -n 1`                                                          | Menampilkan **ringkasan real-time kondisi sistem**, tetapi hanya 1 kali pembaruan (karena `-n 1`).                                                                                                                                                    | Untuk melihat **total CPU, memori, jumlah task**, dan **beban sistem (load average)** secara cepat.  |
|   12   | **Bagian bawah output (`Tasks`, `%Cpu(s)`, `MiB Mem`, `MiB Swap`)** | Menunjukkan statistik sistem secara umum: <br>• Jumlah task (running, sleeping, zombie) <br>• Persentase penggunaan CPU <br>• Total dan penggunaan memori serta swap                                                                                  | Untuk memonitor performa keseluruhan sistem Linux.                                                   |

**-Eksperimen 3**
| **No** | **Perintah / Output**               | **Penjelasan Output**                                                                                                                                                              | **Fungsi / Tujuan**                                                                                                                                                                        |                                                                                           |
| :----: | :---------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
|    1   | `sleep 1000 &`                      | Menjalankan perintah `sleep` selama **1000 detik** di **background** (ditandai dengan simbol `&`). <br>Output `[1] 504` menunjukkan **nomor job (1)** dan **PID proses (504)**.    | Menjalankan proses yang tidak memblokir terminal (background process).                                                                                                                     |                                                                                           |
|    2   | `ps aux                             | grep sleep`                                                                                                                                                                        | `ps aux` menampilkan daftar semua proses aktif, dan `grep sleep` memfilter hasil agar hanya menampilkan proses yang mengandung kata “sleep”.                                               | Untuk mencari dan menampilkan proses `sleep` yang sedang berjalan.                        |
|    3   | **Output hasil `ps aux              | grep sleep`**                                                                                                                                                                      | Menunjukkan dua baris hasil: <br>• `belinda 504 ... sleep 1000` → proses utama `sleep` (PID 504). <br>• `belinda 506 ... grep --color=auto sleep` → proses `grep` itu sendiri (sementara). | Mengidentifikasi PID proses `sleep` (yaitu **504**) agar bisa digunakan untuk dihentikan. |
|    4   | `kill <PID>`                        | Perintah `kill` digunakan untuk **mengirim sinyal ke proses tertentu** berdasarkan PID. <br>Namun di gambar terlihat error: `-bash: syntax error near unexpected token 'newline'`. | Error terjadi karena pengguna belum mengganti `<PID>` dengan angka sebenarnya (misalnya `kill 504`).                                                                                       |                                                                                           |
|    5   | (Jika dijalankan benar: `kill 504`) | Akan menghentikan proses `sleep` dengan PID 504. <br>Proses tidak lagi muncul jika diperiksa ulang dengan `ps aux                                                                  | grep sleep`.                                                                                                                                                                               | Untuk **menghentikan atau membunuh** proses background berdasarkan PID.                   |

**-Eksperimen 4**
| **No** | **Bagian Output**                                        | **Penjelasan Output**                                                                                                                   | **Fungsi / Tujuan**                                                                       |
| :----: | :------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
|    1   | `systemd(1)`                                             | Proses **utama (init process)** dengan **PID 1**, dijalankan saat sistem booting. Semua proses lain diturunkan (child process) darinya. | Sebagai **induk dari semua proses** dalam sistem Linux, mengatur layanan dan sesi sistem. |
|    2   | `agetty(170), agetty(181)`                               | Proses yang menangani **terminal login** (TTY).                                                                                         | Menyediakan antarmuka login pengguna di terminal.                                         |
|    3   | `cron(147)`                                              | Layanan **penjadwalan tugas otomatis**.                                                                                                 | Menjalankan tugas-tugas sistem yang dijadwalkan pada waktu tertentu.                      |
|    4   | `dbus-daemon(148)`                                       | Proses komunikasi antar aplikasi melalui **D-Bus system bus**.                                                                          | Memungkinkan aplikasi berkomunikasi dengan layanan sistem secara aman.                    |
|    5   | `init─┬─systemd-ub(2)`                                   | Menunjukkan bahwa proses `systemd` memiliki **child process** bernama `systemd-ub` dengan PID 2.                                        | Menandai **cabang proses anak** dari proses utama `systemd`.                              |
|    6   | `SessionLeader(290)` → `Relay(292)` → `bash(292)`        | Rangkaian proses yang menunjukkan **hierarki sesi login pengguna** hingga ke shell (`bash`).                                            | Menunjukkan urutan proses saat pengguna membuka terminal hingga mendapat shell.           |
|    7   | `bash(292)` → `head(508)` / `pstree(507)` / `sleep(504)` | Menunjukkan bahwa dalam shell `bash`, pengguna menjalankan beberapa proses seperti `head`, `pstree`, dan `sleep`.                       | Menampilkan proses-proses **yang dijalankan oleh pengguna** dari terminal aktif.          |
|    8   | `rsyslogd(179–201)`                                      | Sekumpulan proses `rsyslogd` (logging daemon).                                                                                          | Mengelola dan menyimpan **log sistem dan layanan**.                                       |
|    9   | `systemd-journald(9)`                                    | Proses untuk mencatat **log internal systemd**.                                                                                         | Menyimpan catatan log sistem di `/var/log/journal`.                                       |
|   10   | `systemd-logind(159)`                                    | Layanan login sistem.                                                                                                                   | Mengelola **sesi pengguna dan autentikasi login**.                                        |
|   11   | `systemd-timesyncd(141)`                                 | Sinkronisasi waktu sistem.                                                                                                              | Menyinkronkan jam sistem dengan server NTP.                                               |
|   12   | `systemd-udevd(91)`                                      | Proses yang menangani **perangkat keras (device manager)**.                                                                             | Mendeteksi dan menginisialisasi perangkat keras baru.                                     |


---

## Kesimpulan
1. Linux memiliki sistem manajemen proses yang terstruktur secara hierarkis, di mana setiap proses memiliki PID unik dan dapat dimonitor, dikontrol, atau dihentikan menggunakan perintah seperti ps, top, kill, dan pstree.
2. Manajemen user berperan penting dalam keamanan sistem, karena pengaturan hak akses dan grup pengguna menentukan siapa yang dapat menjalankan, mengubah, atau mengakses sumber daya sistem.
3. Kombinasi manajemen proses dan user memastikan sistem Linux berjalan efisien, stabil, dan aman, dengan kontrol penuh terhadap aktivitas dan izin setiap pengguna maupun proses.
---

## Tugas 
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.
   
- Eksperimen 1
  
| Perintah                          | Fungsi                                | Keterangan                                         |
| --------------------------------- | ------------------------------------- | -------------------------------------------------- |
| `whoami`                          | Menampilkan nama user aktif           | Digunakan untuk verifikasi siapa yang sedang login |
| `id`                              | Menampilkan UID, GID, dan grup user   | Berguna untuk melihat hak akses                    |
| `sudo adduser praktikan`          | Membuat user baru bernama *praktikan* | Membuat akun lengkap dengan home directory         |
| `passwd praktikan`                | Mengatur password user baru           | Password disimpan di `/etc/shadow`                 |
| Input informasi (Full Name, dll.) | Mengisi data identitas user           | Disimpan di `/etc/passwd`                          |
| Menambahkan ke grup `users`       | Memberi hak akses umum                | Agar user bisa menjalankan fungsi standar sistem   |

- Eksperimen 2
  
| **No** | **Perintah** | **Arti / Komponen Perintah**                                                                                                                                                                                                                                                                                                                  | **Fungsi Utama**                                                                                                                        | **Keterangan Tambahan / Hasil Output**                                                                                                                                                                                                     |                                                                                                                   |
| :----: | :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
|    1   | `ps aux`     | Perintah **`ps` (process status)** digunakan untuk menampilkan daftar semua proses yang sedang berjalan di sistem.<br>• `a` → Menampilkan proses dari semua user.<br>• `u` → Menampilkan proses dengan format user-oriented (menampilkan USER, PID, %CPU, %MEM, COMMAND).<br>• `x` → Menampilkan proses yang tidak terhubung dengan terminal. | Menampilkan informasi lengkap mengenai semua proses aktif di sistem Linux, termasuk proses milik user lain maupun sistem.               | Output menampilkan kolom seperti:<br>• **USER** – nama pengguna proses<br>• **PID** – ID proses<br>• **%CPU** – penggunaan CPU<br>• **%MEM** – penggunaan memori<br>• **STAT** – status proses<br>• **COMMAND** – perintah yang dijalankan |                                                                                                                   |
|    2   | `head -10`   | Perintah **`head`** digunakan untuk menampilkan **10 baris pertama** dari output sebelumnya (bisa diubah dengan opsi lain).                                                                                                                                                                                                                   | Membatasi output dari `ps aux` agar hanya menampilkan 10 proses pertama, supaya lebih mudah dibaca dan tidak terlalu panjang.           | Kombinasi `ps aux                                                                                                                                                                                                                          | head -10` digunakan untuk **melihat ringkasan proses awal secara cepat** tanpa menampilkan seluruh daftar proses. |
|    3   | `top -n 1`   | Perintah **`top`** menampilkan proses yang sedang berjalan secara **real-time**, mirip dengan Task Manager di Windows.<br>Opsi `-n 1` berarti hanya **menampilkan satu kali update** (bukan terus-menerus).                                                                                                                                   | Menunjukkan ringkasan penggunaan sumber daya sistem (CPU, memori, swap, load average) dan daftar proses aktif saat perintah dijalankan. | Output menampilkan:<br>• **Load average** (beban CPU rata-rata)<br>• **Jumlah proses aktif dan tidur (sleeping)**<br>• **Penggunaan CPU dan memori**<br>• **Daftar proses berdasarkan konsumsi CPU/memori**                                |                                                                                                                   |

- eksperimen 3
  
| **Tahap** | **Perintah**   | **Fungsi Utama**                                               |                                                              |
| --------- | -------------- | -------------------------------------------------------------- | ------------------------------------------------------------ |
| 1️      | `sleep 1000 &` | Membuat proses latar belakang yang menunggu 1000 detik.        |                                                              |
| 2️      | `ps aux        | grep sleep`                                                    | Mencari dan menampilkan proses `sleep` yang sedang berjalan. |
| 3️      | `kill 504`     | Menghentikan proses berdasarkan PID yang ditemukan sebelumnya. |                                                              |
- eksperimen 4
  
| **Perintah** | **Fungsi Utama**                                                          |                                                                                 |
| ------------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `pstree`     | Menampilkan pohon hierarki proses (process tree) dari semua proses aktif. |                                                                                 |
| `-p`         | Menampilkan **PID (Process ID)** di samping nama proses.                  |                                                                                 |
| `            | head -20`                                                                 | Menampilkan hanya **20 baris pertama** dari hasil `pstree`, agar lebih ringkas. |


2. Gambarkan hierarki proses dalam bentuk diagram pohon (pstree) di laporan.
```
systemd(1)-+-agetty(170)
           |-agety(181)
           |-cron(147)
           |-dbus-daemon(148)
           |-init-systemd(Ub(2)-+-SessionLeader(290)---Relay(292)(291)---bash(292)-+-head(508)
           |                    |                                                  |-pstree(507)
           |                    |                                                  `-sleep(504)
           |                    |-init(7)---{init}(8)
           |                    |-login(293)---bash(396)
           |                    `-{init-systemd(Ub}(9)
           |-rsyslogd(179)-+-{rsyslogd}(199)
           |               |-{rsyslogd}(200)
           |               `-{rsyslogd}(201)
           |-systemd(382)---(ds-pam)(383)
           |-systemd-journal(49)
           |-systemd-loginid(159)
           |-systemd-resolve(140)
           |-systemd-timesyn(141)---{systemd-timesyn}(145)
           |-systemd-udevd(91)
```
4. Hubungan antara user management dan keamanan sistem Linux
   User management adalah fondasi utama keamanan sistem Linux.
Dengan pengelolaan pengguna, grup, dan izin akses yang baik:
- Setiap pengguna hanya memiliki hak sesuai kebutuhannya,
- Risiko akses tidak sah dan modifikasi sistem dapat diminimalkan,
- Sistem menjadi lebih stabil, aman, dan terkontrol.
---

## Quiz
**1. Apa fungsi dari proses init atau systemd dalam sistem Linux?**

Jawab :
1. Proses Pertama (Parent of All Processes)
Menurut Silberschatz et al. (Operating System Concepts, 10th Edition):
- init/systemd adalah proses pertama yang dijalankan kernel setelah booting
- Memiliki PID 1 - identifier proses yang paling istimewa
- Menjadi parent process bagi semua proses lain dalam sistem
- Bertanggung jawab untuk memulai dan mengelola daemon sistem

2. Manajemen Proses dan Service
Tanenbaum & Bos (Modern Operating Systems, 4th Edition) menjelaskan:
- Service Management: Memulai, menghentikan, dan memantau service sistem
- Process Orchestration: Mengelola dependensi antar proses
- Daemon Supervision: Memastikan daemon kritikal tetap berjalan
- Runlevel Management: Mengelola status operasional sistem

3. Fungsi Sistem Init Tradisional (SysV init)
Berdasarkan Linux Manual Pages dan OSTEP:
- Runlevel Management: Mengelola tingkat operasi sistem (0-6)
- Service Scripts: Menjalankan script di /etc/init.d/
- Process Tracking: Melacak proses yang sedang berjalan
- Zombie Process Reaping: Mengumpulkan proses zombie yang telah terminated

4. Fungsi Systemd (Modern Implementation)
Linux Manual Pages mendokumentasikan systemd memiliki fungsi tambahan:
- Parallel Startup: Memulai service secara paralel untuk percepatan boot
- Socket Activation: Service diaktifkan berdasarkan permintaan
- Dependency Management: Mengelola dependensi service secara otomatis
- Logging Terintegrasi: Melalui journald untuk centralized logging



**3. Apa perbedaan antara kill dan killall?**

Jawab :
- kill menargetkan proses berdasarkan PID, sedangkan killall menargetkan nama program (process name).
```
kill [signal] PID
```
```
killall [signal] program_name
```
- Menurut Tanenbaum & Bos (Modern Operating Systems, 4th Edition, 2015)
  “Signals are a form of limited interprocess communication used in UNIX systems. Commands like kill send a signal to a specific process identified by PID, while more advanced utilities such as killall apply the same signal to all processes sharing the same executable name.”
Jadi, kill komunikasi sinyal ke satu proses. sedangkan killall komunikasi sinyal ke semua proses dengan nama yang sama.


**3. Mengapa user root memiliki hak istimewa di sistem Linux?**


Jawab :
1. Kebutuhan untuk Mengelola Sistem Operasi Secara Menyeluruh
Menurut Silberschatz et al. (Operating System Concepts, 10th Edition), akun root diperlukan karena sistem operasi membutuhkan entitas yang memiliki wewenang penuh untuk:
- Mengelola semua proses dan sumber daya sistem
- Mengkonfigurasi kernel dan parameter sistem
- Mengontrol akses ke perangkat keras dan sumber daya kritis

2. Prinsip Desain Keamanan Dasar
Tanenbaum & Bos (Modern Operating Systems, 4th Edition) menjelaskan bahwa hak istimewa root merupakan implementasi dari prinsip privilege separation:
- Sistem memisahkan antara pengguna biasa dengan administrator
- Root memiliki kemampuan untuk bypass semua mekanisme proteksi
- Hal ini mencegah pengguna biasa melakukan perubahan yang dapat membahayakan sistem

3. Kemampuan Khusus Root Menurut Linux Manual Pages
Berdasarkan dokumentasi resmi Linux, root memiliki hak istimewa untuk:
- Mengubah kepemilikan file (chown, chgrp)
- Mengatur permission pada file sistem (chmod)
- Mengakses semua file termasuk yang dimiliki user lain
- Mengelola proses semua user (kill, renice)
- Konfigurasi jaringan dan sistem firewall
- Instalasi software dan update sistem  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  yang paling menantang minggu ini adalah tentang cara memahami output dari perintah yang diperintahkan. 
- Bagaimana cara Anda mengatasinya?
  Cara saya mengatasinya yaitu dengan mencari bantuan di mana saya dapat memahaminya dengan lebih baik

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
