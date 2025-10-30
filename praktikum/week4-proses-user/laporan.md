
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux
---

## Identitas
- **Nama**  : Faiq Atha Rulloh
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---

## A. Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **konsep proses dan manajemen user dalam sistem operasi Linux.**  
Mahasiswa akan memahami bagaimana sistem operasi:
- Membuat dan mengatur proses (process management).  
- Mengelola user, group, serta hak akses pengguna.  
- Menampilkan, menghentikan, dan mengontrol proses yang sedang berjalan.  
- Menghubungkan konsep user management dengan keamanan sistem operasi.
  
---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.  

---

## Dasar Teori
1. **Proses** adalah program yang sedang berjalan di sistem Linux.
2. Setiap proses memiliki **nomor identitas (PID)** untuk membedakannya.
3. Perintah seperti `ps`, `top`, dan `kill` digunakan untuk melihat dan mengatur proses.
4. **User dan group** digunakan untuk mengatur siapa yang boleh menjalankan atau mengubah sesuatu di sistem.
5. **Hak akses (permission)** membantu menjaga keamanan agar hanya pengguna yang berwenang yang bisa melakukan tindakan tertentu.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
3. Perintah yang dijalankan.  
4. File dan kode yang dibuat.  
5. Commit message yang digunakan.

---

## Kode / Perintah
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```
---

## Hasil Eksekusi
**Eksperimen 1**
![Screenshot hasil](<screenshots/Eksperimen 1 Bab 4.png>)

**Eksperimen 2**
![Screenshot hasil](<screenshots/Eksperimen 2 bab 4.png>)

**Eksperimen 3**
![Screenshot hasil](<screenshots/Eksperimen 3 Bab 4.png>)

**Eksperimen 4**
![Screenshot hasil](<screenshots/Eksperimen 4 bab 4.png>)




---

## Analisis
**Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
 - Jelaskan setiap output dan fungsinya.
  - `whoami` = Perintah whoami digunakan untuk menampilkan nama pengguna (username) yang sedang aktif atau login di sistem Linux.
     - Perintah `whoami` fungsinya untuk menampilkan nama pengguna yang sedang login di sistem.
     - Hasil `faiqatha` menunjukkan bahwa user yang sedang aktif atau menjalankan terminal bernama *faiqatha*.
 - ` id` = Perintah id fungsinya untuk menampilkan identitas pengguna dan grup yang sedang aktif di sistem Linux.
     - `uid=1000(faiqatha)` artinya user id fungsinya menunjukan id unik  user *faiqatha* yang sedang login. 
     - `gid=1000(faiqatha)` artinya group ID Utama fungsinya Menunjukkan ID grup utama tempat user *faiqatha* tergabung.
     - `groups=...` artinya grup tambahan fungsinya Menampilkan daftar grup lain yang memberi izin dan akses tertentu.


  - `groups` = Perintah groups digunakan untuk menampilkan daftar grup tempat user saat ini tergabung.

| Grup        | Arti                  | Fungsi                                                      |
| ----------- | --------------------- | ----------------------------------------------------------- |
| **adm**     | Administrator logs    | Dapat membaca file log sistem.                              |
| **dialout** | Serial port access    | Mengakses perangkat serial seperti modem.                   |
| **cdrom**   | CD/DVD access         | Mengakses dan menggunakan perangkat CD/DVD.                 |
| **floppy**  | Floppy access         | Mengakses disket (floppy drive).                            |
| **sudo**    | Superuser privileges  | Menjalankan perintah dengan hak akses administrator (root). |
| **audio**   | Audio devices         | Mengelola dan menggunakan perangkat suara.                  |
| **dip**     | Dial-up networking    | Mengatur koneksi jaringan manual (mis. PPP).                |
| **video**   | Video devices         | Mengakses perangkat grafis atau kamera.                     |
| **plugdev** | Plug and Play devices | Mengelola perangkat eksternal seperti USB drive.            |
| **users**   | General users         | Grup umum untuk semua pengguna biasa.                       |
| **netdev**  | Network devices       | Mengelola perangkat jaringan (Wi-Fi, Ethernet).             |

   - Perintah `sudo adduser praktikan` digunakan untuk menambah user baru bernama praktikan.

| Bagian                                          | Makna                                               | Fungsi                                                                                            |
| ----------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **sudo**                                        | Menjalankan perintah dengan hak akses administrator | Memungkinkan user biasa (*faiqatha*) menjalankan perintah yang memerlukan izin root.              |
| **adduser praktikan**                           | Menambahkan pengguna baru bernama *praktikan*       | Membuat akun baru di sistem Linux lengkap dengan home directory dan pengaturan awal.              |
| **[sudo] password for faiqatha:**               | Permintaan kata sandi pengguna                      | Sistem meminta password *faiqatha* untuk memastikan ia berhak menjalankan perintah sebagai admin. |
| **fatal: The user `praktikan' already exists.** | Pesan kesalahan                                     | Menunjukkan bahwa user bernama *praktikan* sudah ada, jadi tidak bisa dibuat lagi.                |

   - Perintah `sudo passwd` praktikan berfungsi untuk mengubah atau menetapkan password baru bagi akun praktikan.
     
| Baris Output                              | Makna                                                  | Fungsinya                                                                                |
| ----------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **sudo**                                  | Menjalankan perintah dengan hak akses administrator    | Memungkinkan user (misalnya *faiqatha*) mengubah password milik user lain (*praktikan*). |
| **passwd praktikan**                      | Mengatur atau mengubah password untuk user *praktikan* | Digunakan untuk menetapkan kata sandi baru pada akun tersebut.                           |
| **New password:**                         | Sistem meminta password baru                           | Admin mengetik kata sandi baru untuk user *praktikan*.                                   |
| **Retype new password:**                  | Konfirmasi ulang password                              | Memastikan password yang dimasukkan benar dan sama dengan sebelumnya.                    |
| **passwd: password updated successfully** | Password berhasil diperbarui                           | Menandakan proses penggantian kata sandi selesai tanpa error.                            |

---

 **Eksperimen 2 – Monitoring Proses**
  ```bash
   ps aux | head -10
   top -n 1
   ```
- Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
  
| Kolom       | Arti                               | Fungsi                                                                                                                          |
| ----------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **USER**    | Nama pengguna pemilik proses       | Menunjukkan siapa yang menjalankan proses tersebut (misalnya `root` atau `faiqatha`).                                           |
| **PID**     | Process ID (Nomor proses)          | Nomor unik yang diberikan sistem untuk mengidentifikasi setiap proses.                                                          |
| **%CPU**    | Persentase penggunaan CPU          | Menunjukkan seberapa banyak CPU digunakan oleh proses tersebut. Semakin tinggi angkanya, semakin berat proses tersebut bekerja. |
| **%MEM**    | Persentase penggunaan memori (RAM) | Menunjukkan berapa banyak memori yang dipakai proses dibanding total RAM sistem.                                                |
| **COMMAND** | Nama atau perintah yang dijalankan | Menunjukkan program atau perintah apa yang sedang berjalan (contoh: `/sbin/init`, `systemd-journald`, `snapfuse`, dll).         |

   - USER: root → proses dijalankan oleh user root
   - PID: 59 → ID prosesnya 59
   - %CPU: 0.0 → hampir tidak menggunakan CPU
   - %MEM: 0.4 → menggunakan 0,4% dari RAM
   - COMMAND: /usr/lib/systemd/systemd-journald → nama program yang dijalankan.

---

**Eksperimen 3 – Kontrol Proses**
   - Catat PID proses `sleep`. 
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
      - Catat PID proses `sleep`.
     ```bash
     faiqatha     494  0.0  0.0   3124  1664 pts/0    S    10:01   0:00 sleep 1000
     faiqatha     509  0.0  0.0   4088  1920 pts/0    S+   10:02   0:00 grep --color=auto sleep
      ````
  - Hentikan proses:
     ```bash
    ` kill 494`
     faiqatha     731  0.0  0.0   4088  1920 pts/0    S+   10:11   0:00 grep --color=auto sleep [1]+  Terminated              sleep 1000
     ```
     
---

 **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.
   ```bash  
systemd(1)─┬─agetty(230)
            ├─cron(200)
            ├─dbus-daemon(201)
            ├─rsyslogd(227)
            ├─snapd(216)
            └─init-systemd(ub(2))─┬─SessionLeader(973)─┬─Relay(978)─┬─bash(978)─┬─head(1293)
                                                         ├─pstree(1292)
                                                         ├─sleep(1280)
                                                         └─sleep(1288)
   ```


  - Proses utama (induk) dalam sistem adalah `systemd (PID 1)`.Ini adalah proses pertama yang dijalankan saat sistem Linux booting.
  - Semua proses lain seperti `agetty`, `cron`, `dbus-daemon`, `rsyslogd`, dan `snapd` adalah turunan (child process) dari `systemd`.
  - Proses yang kamu jalankan di terminal (misalnya `pstree`, `head`, dan `sleep`) juga akhirnya diturunkan dari `systemd` melalui `bash` (shell yang kamu pakai).

---

## Kesimpulan
1. User dan Grup = Setiap pengguna punya ID unik dan grup untuk mengatur hak akses.
2. Perintah penting = `whoami`, `id`, `groups` untuk cek info user : `adduser`, `passwd` untuk menambah dan mengubah user/password.
3. Proses sistem = `ps` dan `top` untuk memantau proses, CPU, dan memori.

---
## D. Tugas & Quiz
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.
**Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
 - `whoami`
     - Perintah `whoami` digunakan untuk menampilkan nama pengguna (username) yang sedang aktif atau login di sistem Linux.Fungsi mengetahui identitas user yang sedang menjalankan terminal.
 - `id`
     - Perintah `id` digunakan untuk menampilkan identitas pengguna dan grup yang sedang aktif di sistem Linux. 
 - `groups`
    - Perintah `groups` digunakan untuk menampilkan daftar grup tempat user saat ini tergabung.

 **Eksperimen 2 – Monitoring Proses**
  ```bash
   ps aux | head -10
   top -n 1
   ```
- `ps aux | head -10`
   - Perintah ini menampilkan daftar proses yang sedang berjalan di sistem Linux. Perintah ini menampilkan daftar proses yang sedang berjalan di sistem Linux. digunakan untuk melihat semua proses aktif beserta pengguna, ID, dan sumber daya yang digunakan (CPU dan memori).Kolom-kolom seperti USER, PID, %CPU, %MEM, dan COMMAND membantu kita memantau dan mengelola proses yang berjalan di sistem Linux.
- `top -n 1`
   -Perintah top digunakan untuk memantau proses yang sedang berjalan secara real-time di sistem Linux — mirip seperti “Task Manager” di Windows.
  
**Eksperimen 3 – Kontrol Proses**
   ```bash
    sleep 1000 &
    ps aux | grep sleep
  ```
 ```bash
  kill <PID>
 ```
- `sleep 1000 &`
    - `sleep 1000`  memerintahkan sistem untuk *tidur* atau berhenti sejenak selama 1000 detik.
    -  `&` menandakan bahwa proses dijalankan di background, sehingga terminal tetap bisa digunakan untuk perintah lain
- `ps aux | grep sleep`
    - `ps aux`  menampilkan daftar lengkap semua proses yang sedang aktif.
    - `|`  pipe, digunakan untuk meneruskan output dari `ps aux` ke perintah berikutnya.
    - `grep sleep`  mencari teks *sleep* di hasil keluaran tersebut.
- `kill 494`
    - `kill` mengirim sinyal ke proses. Secara default mengirim sinyal `SIGTERM` untuk meminta proses berhenti dengan aman.
    - `494` nomor PID dari proses target yang ingin dihentikan.

     
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.
   
 ```bash  
systemd(1)─┬─agetty(230)
            ├─cron(200)
            ├─dbus-daemon(201)
            ├─rsyslogd(227)
            ├─snapd(216)
            └─init-systemd(ub(2))─┬─SessionLeader(973)─┬─Relay(978)─┬─bash(978)─┬─head(1293)
                                                         ├─pstree(1292)
                                                         ├─sleep(1280)
                                                         └─sleep(1288)
  ```

3. Jelaskan hubungan antara user management dan keamanan sistem Linux.
  - User management dan keamanan sistem Linux saling berkaitan erat. Dengan pengaturan user, group, dan permission yang baik, administrator dapat mengontrol akses, melindungi data penting, mencegah kesalahan pengguna, dan memperkuat keamanan sistem secara keseluruhan.
   
4. Upload laporan ke repositori Git tepat waktu.

### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?
   - *Inisialisasi Sistem*
       - Memulai Proses Awal: Sebagai proses pertama, ia bertanggung jawab untuk menginisialisasi sistem setelah kernel selesai memuat.
       - Mengatur Lingkungan Awal: Ini termasuk mengatur hostname, mengonfigurasi perangkat jaringan loopback, dan mengatur sistem file API penting seperti /sys, /proc, dan /dev.
       - Mengatur Jam Sistem: Memastikan jam sistem diatur dengan benar, terutama jika tidak ada RTC (Real-Time Clock) yang berfungsi baik.
   
    - *Manajemen Layanan*
       - Memulai, Menghentikan, dan Mengelola Layanan.
       - Menyelesaikan Ketergantungan (Dependencies).
       - Pemantauan dan Restart Otomatis.
   
    - *Pengelolaan Proses*
       - Pengelompokan Kontrol (Cgroups): systemd menempatkan proses yang berbeda ke dalam Linux control groups (cgroups) individu, yang memungkinkan pelacakan, manajemen, dan alokasi sumber daya secara efektif.

    - *Shutdown dan Reboot*
       - Mengelola Transisi Status Sistem: Ketika Anda meminta sistem untuk shutdown atau reboot, systemd-lah yang mengelola transisi ini.
   
2. Apa perbedaan antara `kill` dan `killall`?
  - `kill`
     - Perintah ini memerlukan *PID (Process ID)* sebagai argumen. PID adalah nomor unik yang diberikan oleh kernel kepada setiap proses yang sedang berjalan.
         - contoh: `kill -9 1234 5678` (Mengirim sinyal SIGKILL ke proses dengan PID 1234 dan 5678).

  - `killall`
    - Perintah ini memerlukan *nama perintah (executable name)* sebagai argumen.
         - Contoh: `killall chrome` (Mengirim sinyal default `SIGTERM` ke SEMUA proses yang bernama `chrome`).
   
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?
   - Pengguna root memiliki hak istimewa di sistem Linux karena perannya sebagai *pengendali utama sistem*, yang diperlukan untuk menjalankan fungsi *administratif dan pemeliharaan* yang penting.

---

## E. Output yang Diharapkan
- Hasil observasi seluruh perintah dimasukkan ke dalam `laporan.md`.  
- Screenshot hasil eksekusi disimpan di folder `screenshots/`.  
- Laporan lengkap tersimpan di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
   - Bagian paling menantang adalah memahami hubungan antara proses, PID, dan perintah manajemen proses seperti ps, kill, dan systemd.
- Bagaimana cara Anda mengatasinya?
   - cara mengatasinya adalah dengan membaca ulang materi tentang manajemen proses, mencoba langsung perintah di terminal, dan mencatat hasilnya satu per satu agar lebih mudah memahami.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
