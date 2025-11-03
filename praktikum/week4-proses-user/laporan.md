
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux
---

## Identitas
- **Nama**  : NOVIA SAFITRI
- **NIM**   : 25020923
- **Kelas** : 1IKRA

---

## Tujuan
1.Menjelaskan konsep proses dan user dalam sistem operasi Linux.

2.Menampilkan daftar proses yang sedang berjalan dan statusnya.

3.Menggunakan perintah untuk membuat dan mengelola user.

4.Menghentikan atau mengontrol proses tertentu menggunakan PID.

5.Menjelaskan kaitan antara manajemen user dan keamanan sistem.

---

## Dasar Teori
Manajemen proses adalah cara mengatur program yang sedang berjalan di komputer.Linux membuat nomor khusus untuk setiap program agar dapat dikenali dan dikendalikan,misalnya memulai,menghentikan,atau memberi prioritas.Manajemen pengguna cara mengatur siapa yang bisa masuk dan menggunakan komputer,setiap orang yang memakai Linux punya akun dengan nama dan pasword sendiri sehingga data/aksesnya aman.Tujuan dari keduanya agar komputer berjalan lancar,semua program dijalankan ddengan baik,dan hanya orang yang mempunya izin yang dapat mengakses sistem.

---

## Langkah Praktikum

1.Setup Environment

Gunakan Linux (Ubuntu/WSL).

Pastikan Anda sudah login sebagai user non-root.

Siapkan folder kerja:

    praktikum/week4-proses-user/

2.Eksperimen 1 – Identitas User Jalankan perintah berikut:

    whoami
    id
    groups
Jelaskan setiap output dan fungsinya.

Buat user baru (jika memiliki izin sudo):

    sudo adduser praktikan
    sudo passwd praktikan
Uji login ke user baru.

3.Eksperimen 2 – Monitoring Proses Jalankan:

    ps aux | head -10
    top -n 1
Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.

Simpan tangkapan layar top ke:

    praktikum/week4-proses-user/screenshots/top.png
4.Eksperimen 3 – Kontrol Proses

Jalankan program latar belakang:

    sleep 1000 &
    ps aux | grep sleep
Catat PID proses sleep.
Hentikan proses:

    kill <PID>
Pastikan proses telah berhenti dengan ps aux | grep sleep.

5.Eksperimen 4 – Analisis Hierarki Proses Jalankan:

    pstree -p | head -20
Amati hierarki proses dan identifikasi proses induk (init/systemd).

Catat hasilnya dalam laporan.
Commit & Push

    git add .
    git commit -m "Minggu 4 - Manajemen Proses & User"
    git push origin main
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

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<screenshots/week4 1.png>)
![alt text](<screenshots/week4 2.png>)
![alt text](<screenshots/week4 3.png>)
---

## Analisis

1.Jelaskan setiap output dan fungsinya.

*Whoami 
output:safitrinovia

Fungsi: Memastikan identitas user yang sedang menjalankan perintah, berguna ketika berpindah user atau untuk konfirmasi akses.

*id
output:Menampilkan informasi lengkap tentang user saat ini, termasuk User ID (UID), Group ID (GID), dan grup-grup yang user tersebut tergabung di dalamnya.

Fungsi:Memberikan informasi detail tentang identitas user dan hak grupnya yang berguna untuk manajemen akses dan troubleshooting

* groups
  output:safitrinovia adm dialout cdrom floppy sudo audio dip video plugdev users netdev

   fungsi:mengetahui grup mana saja yang memberikan hak akses kepada user; penting untuk pengelolaan izin dan kontrol sumber daya.

2.Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.
-PID (Process ID): Merupakan nomor unik yang diberikan kepada setiap proses yang berjalan. Ini adalah identitas proses yang digunakan oleh kernel untuk mengelola proses tersebut.

-USER: Nama pengguna (user) yang menjalankan proses tersebut. Menunjukkan kepemilikan proses.

-%CPU: Persentase penggunaan CPU oleh proses tersebut dari total kapasitas CPU yang tersedia dalam periode waktu tertentu. Menunjukkan seberapa aktif proses menggunakan CPU.

-%MEM: Persentase penggunaan memory fisik (RAM) oleh proses terhadap total RAM yang tersedia di sistem. Menunjukkan beban memori yang digunakan oleh proses.

-COMMAND: Nama perintah atau aplikasi yang dijalankan oleh proses tersebut. Memudahkan identifikasi proses berdasarkan perintah yang memulai proses.

3.Catat PID proses sleep.

PID proses sleep adalah 562 
Angka 1 nomor job  

4.Amati hierarki proses dan identifikasi proses induk (init/systemd).
-Proses induk utama (unit/system)diLinux adalah sistem dengan PID1

- Proses anak dari system (1)

  * cron(350): menjadwalkan tugas otomatis
  * agetty(332): menangani login diterminal
  * bash (336):shell yang digunakkan user safitrinovia
  * sleep(562):proses yang dijalankan user dari terminal
  * pstree(565)dan head(566): menampilkan struktur proses dan memotong output 


---

## Kesimpulan

Sistem Linux bersifat multi-user dan multi-proses, artinya banyak pengguna dan proses dapat berjalan secara bersamaan.Perintah whoami dan id digunakan untuk mengetahui identitas pengguna yang sedang aktif serta informasi UID, GID, dan grupnya.Perintah adduser berfungsi untuk menambahkan pengguna baru ke sistem, lengkap dengan direktori home dan konfigurasi dasarnya.Perintah ps aux menampilkan daftar seluruh proses yang sedang berjalan di sistem beserta PID, pengguna, dan statusnya.Perintah sleep digunakan untuk menunda eksekusi selama waktu tertentu; jika dijalankan di background (&), maka akan memiliki PID tersendiri.Perintah pstree menampilkan struktur hierarki proses dalam bentuk pohon, memperlihatkan hubungan antara proses induk dan anak.Dari hasil pstree, diketahui bahwa proses induk utama sistem Linux adalah systemd (PID 1), yang menjadi sumber dari semua proses lain.

# Tugas
1.Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.
|No|Perintah|Hasil|Fungsi|Keterangan|
|:---|:---|:---|:---|:---|
1|whoami|safitrinovia|Menampilkan nama pengguna(user) yang sedang login disistem|Pengguna yang sedang masuk dan menggunakan terminal yaitu user safitrinovia|
2|id|uid=1000(safitrinovia) gid=1000(safitrinovia) groups=1000(safitrinovia),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),44(video),46(plugdev),100(users),107(netdev)|Menampilkan informasi terkait identitas user seperti UID,GID,dan grup|-uid=1000 yaitu ID unik user safitrinovia,gid=1000 yaitu ID grup utama safitrinovia,groups yaitu daftar grup tambahan user tergabung seperti sudo,video,users,dll|
3|groups|safitrinovia adm dialout cdrom floppy sudo audio dip video plugdev users netdev|Menampilkan daftar grup yang diikuti oleh user aktif|Menegaskan bahwa safitrinovia tergabung digrup-grup tersebut,termasuknya sudo itu mempunyai hak administrator|
4|sudo adduser praktikan|Adding user 'praktikan' ...,Adding new group 'praktikan' (1001),Adding new user 'praktikan' (1001) with group 'praktikan (1001)' ... Creating home directory '/home/praktikan' ...,Copying files from '/etc/skel' ...|Menambahkan akun  user baru bernama praktikan ke sistem|Sistem membuat user baru bernama praktikan,membuat direktori home /home/praktikan ,dan menyalin file bawaan|
5|Pengisian data user|Mengisi username baru dan nomor HP|Mengisi informasi tambahan untukk akun praktikan |Semua diisi dengan data identitas seperti nama dan nomor HP|
6|sudo passwd praktikan|New password:...Retype new password:..passwd:.passwor dupdated successfully|Mengatur/ mengubah passoword untuk user praktikan |Password berhasil dibuat unruk user baru praktikan|
8|ps aux l head -10|Daftar proses dari berbagai pengguna(root,systemd,safitrinovia)lengkap dengan kolom seperti PID,%CPU,%MEM,STAT,dan COMMAND |Melihat daftar proses sistem secara detail|USER = proses,PID= ID proses,CPU,%MEM= pengguna CPU&RAM,STAT= status prpses (s=sleep,R=running,dan Z=zombie),COMMAND= program yang dijalankan|
9|top -n 1| Tampilan interaktif berisi ringkasan sistem seperti load,average,task,CPU usage,memory usage dan daftar proses aktif|Menampilakan proses sistem secara real-time dan memperlihatkan penggunaan CPU,RAM,status proses  yang berjalan|Baris atas= ringkasan aktivitas CPU& memory, Bagian bawah= daftar proses dan pemakaian sumber daya tiap proses ,dan dapat digunakan untuk memnatau kinerja sistem secara berlangsung|
10|sleep 1000 & ps aux l grep sleep|Terminal menampilakan (1) 562 berarti proses sleep sedang berjalan dan muncul safitrinovia+... sleep serta grep--color=auto sleep|Menunggu 1000 detik dibackground lalu menampilkan daftar proses dan menyaring hasilnya agar hanya menampilkan proses yang berarti sleep|Simbol & digunakan agar proses berjalan ,sleep akan diam selama 1000 detik tanpa output apapun,ps aux menampilkan semua proses dan grep sendiri ikut muncul karena mengandung kata yang dicari|
11|kill <PID>|muncul error syntax error near token 'newline'|Menghentikan proses tertentu berdasarkan nomor PID|Kesalahan terjadi karena <PID> tidak diganti dengan angka sebenarnya ,seharusnya diganakan kill 562 untuk menghentikan proses sleep|
12|pstree -p | head -20|Tampilan diagram pohon dengan proses induk systemd((1) dan proses anak seperti agetty,cron,bash,pstree,dan sleep(562)|Menampilkan struktur diagram pohon proses beserta PIDnya dan membatasi tampilan hanya 20 baris pertama |pstree menampilkan hubungan antar proses induk sampai anak.simbol("__") menunjukan cabang proses yang saling berhubungan |

2.Gambarkan hierarki proses dalam bentuk diagram pohon (pstree) di laporan.

    Systemd ( 1)-+-agetty(195)
                 |-agetty(216)
                 |-cron(181)
                 |-dbus-daemon(182)
                 |-init-systemd (Ub(2)-+-SessionLeader (330)---Relay (336) (332)---bash(336)-+-head (566)         
                 |                     |                                                      |-pstree (565)       
                 |                     |                                                                                                                            `--
                 |                     |                                                       `-sleep(562)          
                 |                     |
                 |                     |
                 |                     |-init(8)---{init}(9)
                 |                     |-login(339)---bash(430)
                 |                     `-{init-systemd(Ub}(10)
                 |-rsyslogd(209)-+-{rsyslogd}(227)
                 |-{rsyslogd}(228)
                 `-{rsyslogd}(229)
                 |-snapd(188)-+-{snapd}(256)
                              |-{snapd}(260)
                              |-{snapd} (261)
                              |-{snapd} (262)
                              |-{snapd} (264)
                              |-{snapd} (283)
                              |-{snapd} (284)

3.Jelaskan hubungan antara user management dan keamanan sistem Linux.

Manajemen user di Linux adalah kunci utama untuk menjaga keamanan sistem. Dengan mengelola siapa yang boleh mengakses sistem, memberikan hak akses sesuai kebutuhan, membatasi hak istimewa, mengatur password dengan ketat, serta mengawasi aktivitas pengguna, maka risiko akses tidak sah dan penyalahgunaan dapat diminimalkan. Proses ini perlu terus dipantau dan diperbarui agar keamanan sistem tetap terjaga secara efektif dan berkelanjutan.

---

## Quiz
1.Apa fungsi dari proses init atau systemd dalam sistem Linux?
   
   Jawaban: Proses init atau system dalam Linux yaitu proses pertama yang dijalankan saat komputer nyala.Fungsi dari init atau system di Linux untuk memulai semua proses penting dan layanan sistem seperti menjalankan program yang diperlukan,memulai layar login, mengatur proses saat booting hingga siap dugunakan dan juga mengontrol proses saat shutdown agar sistem mati dengan aman. 

2.Apa perbedaan antara kill dan killall?
   
   Jawaban:
   |Aspek |kill|killall
| :--- | :---|:---|
Tujuan|Proses berdasarkan nomor PID|Proses berdasarkan nama proses|
Jumlah proses|Satu proses setiap perintah|Semua proses dengan sama|
Kelebihan|Lebih tepat dan spesifik|Bisa menghentikan banyak proses sekaligus|
Contoh|kill 1234 (menghentikan proses dengan PID 1234)|killall firefox (menghentikan semua proses firefox)|

3. Mengapa user root memiliki hak istimewa di sistem Linux?

   Jawaban: Karena user root  adalah pengguna utama yang dapt mengatur semuanya disitem.Dengan adanya hak istimewa disistem Linux root bisa membuka,mengubah atau menghapus file apapun,memmasang program dan mengatur pengguna lain.User root penting agar sistem dapat diatur dengan bebas saat ada masalah atau perbaikan,oleh karena itu user root juga harus hati-hati agar tidak merusak sistem secara tidak sengaja.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
Bagian yang paling menantang di praktikum Manajemen Proses dan User di Linux adalah memahami konsep proses dan hubungan antar proses serta mengelola penggunaan resource yang efisien.
- Bagaimana cara Anda mengatasinya?  
 Memahami lebih baik lagi dan jangan lupa kalo bingung lihat referensi yang sudah diberikan oleh dosen atau tanya kepada temen.Selain itu harus sering latihan dan monitoring sistem membantu mengatasi kendala tersebut dan menjaga sistem tetap aman dan optimal.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
