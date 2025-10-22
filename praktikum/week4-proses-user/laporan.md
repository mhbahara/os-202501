
# Laporan Praktikum Minggu 4
Topik : Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Farhan Ramdhani  
- **NIM**   : 250202938  
- **Kelas** : 1IKRB

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
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
### 1. User dan Identitas Linux

Di sistem Linux, setiap orang yang masuk ke sistem disebut user (pengguna). Tiap user punya identitas sendiri berupa nama pengguna (username), nomor ID (UID), dan biasanya juga tergabung dalam kelompok tertentu (group). Identitas ini menentukan apa saja yang boleh atau tidak boleh dilakukan di sistem.


### 2. Root dan Non-root User

Root adalah pengguna tertinggi di Linux, Ia bisa melakukan apa saja, termasuk menghapus file penting sistem. Sedangkan non-root user adalah pengguna biasa dengan izin terbatas supaya sistem tetap aman.

### 3. PID (Process ID)
Setiap proses punya nomor identitas unik yang disebut PID, gunanya supaya sistem bisa membedakan satu proses dengan proses lain.

---

## Langkah Praktikum
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

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
```
### 1. whoami
Perintah `whoami` menampilkan nama user yang sedang aktif login di shell saat ini.
Fungsi utamanya untuk mengecek identitas pengguna saat ini,terutama setelah berpindah user dengan perintah seperti `su` atau `sudo su`.
### 2. id
Menampilkan informasi identitas pengguna lengkap, meliputi User ID, Group ID, dan Groups.
### 3. groups
Menampilkan nama-nama grup tempat user saat ini tergabung.
### 4. PID proses sleep
- 1275 
- 1735 
- 1969 
- 1983
### 5. pstree -p | head -20
Proses utama (induk) dalam sistem Linux adalah `systemd(1)`.
Semua proses lain (seperti `cron`, `dbus-daemon`, `rsyslogd`, dan `bash`) merupakan turunan atau anak dari `systemd`.




## Tabel Observasi Perintah `ps aux | head -10` dan `top -n 1`

| *Kolom* | *Nama Lengkap* | *Keterangan / Fungsi* | *Penjelasan Singkat* |
|------------|------------------|---------------------------|-------------------------|
| *PID* | Process ID | Nomor unik yang diberikan sistem untuk setiap proses. | Digunakan untuk mengenali dan mengelola proses, misalnya saat menghentikan dengan `kill`. |
| *USER* | Pemilik proses | Nama user yang menjalankan proses tersebut. | Menunjukkan siapa pemilik dan pengendali proses. |
| *%CPU* | Pemakaian CPU | Persentase penggunaan CPU oleh proses. | Nilai tinggi menunjukkan proses sedang aktif menggunakan prosesor. |
| *%MEM* | Pemakaian Memori | Persentase penggunaan RAM oleh proses. | Menunjukkan seberapa banyak memori yang dipakai oleh proses. |
| *COMMAND* | Nama Program / Perintah | Nama aplikasi atau perintah yang sedang berjalan. | Menunjukkan perintah atau program yang dieksekusi oleh proses tersebut. |

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![alt text](../week4-proses-user/screenshots/Screenshot%202025-10-22%20165817.png)
![alt text](../week4-proses-user/screenshots/Screenshot%202025-10-22%20165853.png)
![alt text](../week4-proses-user/screenshots/Screenshot%202025-10-22%20165912.png)

---

## Analisis
- Jelaskan makna hasil percobaan. 

  **Jawaban :**  Dari percobaan ini bisa dilihat bahwa setiap kali kita menjalankan perintah di Linux, sistem langsung membuat proses baru yang punya nomor unik (PID).

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).

  **Jawaban :** Setiap kali kita ketik perintah di terminal, perintah itu dikirim ke kernel lewat system call. Kernel yang kemudian menjalankan, memantau, atau menghentikan proses sesuai permintaan kita.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

  **Jawaban :** 
Di Linux, semua pengaturan proses dan user dilakukan lewat terminal dengan perintah teks seperti `ps`, `top`, `kill`, atau `pstree`. Kita bisa lihat dan kontrol proses secara langsung.
Sementara di Windows, hal serupa dilakukan lewat Task Manager atau perintah tasklist, tapi tampilannya grafis dan lebih dibatasi.


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Linux mengatur proses dan pengguna dengan sistem identitas dan izin akses yang jelas, sehingga lebih aman dan terkontrol.


2. Kernel berperan penting sebagai penghubung antara pengguna dan perangkat keras lewat system call.


3. Dibanding Windows, Linux lebih terbuka dan fleksibel dalam memantau serta mengatur proses secara langsung.




---

## Tugas
### 1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  

  **Jawaban :** 
  ```bash
1. whoami
Fungsi: Menampilkan nama user yang sedang aktif/login di sistem Linux.

2. id
Fungsi: Menampilkan informasi detail user, seperti UID (User ID), GID (Group ID), dan grup tempat user

3. groups
Fungsi: Menampilkan daftar grup yang diikuti oleh user yang sedang login.

4. sudo adduser
Fungsi: Menambahkan pengguna (user) baru ke sistem Linux.

5. sudo passwd
Fungsi: Mengatur atau mengubah password untuk user tertentu.

6. ps aux
Fungsi: Menampilkan semua proses yang sedang berjalan di sistem, termasuk nama user, PID, penggunaan CPU/memori, dan perintah yang dijalankan.

7. top
Fungsi: Menampilkan proses yang berjalan secara real-time, mirip seperti Task Manager di Windows.

8. sleep 1000 &
Fungsi: Menjalankan proses sleep di background selama 1000 detik.

9. grep
Fungsi: Menyaring atau mencari teks tertentu dari hasil perintah lain.

10. kill <PID>
Fungsi: Menghentikan proses berdasarkan nomor PID.

11. pstree
Fungsi: Menampilkan struktur proses dalam bentuk pohon (tree), sehingga terlihat hubungan antara proses induk (parent) dan proses anak (child).
```

### 2. Gambarkan hierarki proses dalam bentuk diagram pohon `pstree` di laporan.  

  **Jawaban :** 

```bash
  systemd(1)
 ├── agetty(199)
 ├── agetty(205)
 ├── cron(182)
 │    └── dbus-daemon(183)
 ├── init
 │    └── systemd(Ub)(2)
 │         ├── SessionLeader(1651)
 │         │    └── Relay(1652)
 │         │         └── bash(1653)
 │         │              └── su(1675)
 │         │                   └── bash(1679)
 │         │                        └── sleep(1735)
 │         └── SessionLeader(1865)
 │              └── Relay(1872)
 │                   └── bash(1872)
 │                        └── su(1903)
 │                             └── bash(1907)
 │                                  ├── head(2038)
 │                                  ├── pstree(2037)
 │                                  └── sleep(1969)
 ├── rsyslogd(207)
 ├── systemd-journald(55)
 ├── systemd-logind(193)
 ├── systemd-resolved(154)
 └── systemd-timesyncd(167)
```

### 3. Jelaskan hubungan antara user management dan keamanan sistem Linux.

  **Jawaban :** 
  Manajemen user di Linux sangat berpengaruh terhadap keamanan, karena setiap user punya hak akses sendiri-sendiri. Dengan sistem ini, user biasa tidak bisa mengubah file penting milik sistem atau user lain, sehingga risiko kerusakan dan penyalahgunaan bisa diminimalkan.

---

## Quiz
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux ?

   **Jawaban :** `ini`t atau `systemd` adalah proses pertama yang dijalankan oleh kernel saat Linux mulai. Fungsinya untuk menginisialisasi sistem, menjalankan layanan (service), dan mengatur semua proses lain.
2. Apa perbedaan antara `kill` dan `killall` ?  

   **Jawaban :** `kill` digunakan untuk menghentikan proses tertentu berdasarkan PID (Process ID), sedangkan `killall` digunakan untuk menghentikan semua proses dengan nama yang sama. 
3. Mengapa user `root` memiliki hak istimewa di sistem Linux ?  

   **Jawaban :** User `root` adalah administrator utama sistem. Ia memiliki hak penuh untuk mengubah konfigurasi sistem, mengakses semua file, dan menjalankan perintah tanpa batasan izin. Tujuannya agar ada satu user yang bisa mengatur, memperbaiki, atau mengelola seluruh sistem dengan bebas. Tapi harus hati-hati, karena kesalahan kecil dengan user `root` bisa mem pengaruhi seluruh sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  

  **Jawaban :** 
Bagian yang paling menantang adalah memahami hubungan antarproses di Linux dan cara kerja `systemd`, karena banyak istilah baru seperti `daemon`, `session leader`, dan `child process` yang awalnya agak membingungkan.

- Bagaimana cara Anda mengatasinya?  

  **Jawaban :** 
Saya mengatasinya dengan mencoba langsung di terminal WSL, menjalankan perintah seperti `pstree`, `ps -ef`, dan `sudo su` sambil mencatat hasilnya. Dengan melihat hasil nyata, saya jadi lebih paham bagaimana proses saling terhubung di sistem Linux.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
