
# Laporan Praktikum Minggu 2
Topik: Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : NOVIA SAFITRI  
- **NIM**   : 250202923
- **Kelas** : 1IKRA

---

## Tujuan

1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
System call adalah cara program aplikasi berkomunikasi dengan sistem operasi untuk meminta layanan penting seperti mengakses file,perangkat keras dan menejeman proses.Saat system cal dipanggil,CPU berpindah dari mode user ke mode kernel untuk menjalankan perintah dengan aman,lalu kembali ke mode user setelah selesai.Di Linux perintah seperti strace dapat digunakan untuk melihat dan menganalisis system call yang sedang berlangsung dalam suatu program.

---

## Langkah Praktikum
1. Setup Environment

Gunakan Linux (Ubuntu/WSL).
Pastikan perintah strace dan man sudah terinstal.
Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. Eksperimen 1 – Analisis System Call Jalankan perintah berikut:

strace ls

Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.
Simpan hasil analisis ke results/syscall_ls.txt.

3. Eksperimen 2 – Menelusuri System Call File I/O Jalankan:

strace -e trace=open,read,write,close cat /etc/passwd

Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. Eksperimen 3 – Mode User vs Kernel Jalankan:

dmesg | tail -n 10

Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. Diagram Alur System Call

Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.

Gunakan draw.io / mermaid.

Simpan di:
praktikum/week2-syscall-structure/screenshots/syscall-diagram.png

6. Commit & Push

git add .
git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
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
#Eksperimen 1
![alt text](<screenshots/stracels1.png>)
![alt text](<screenshots/stracels2.png>)
#Eksperimen 2
![alt text](<screenshots/strace -e.png>)
#Eksperimen 3
![alt text](<screenshots/dmesg.png>)
#Diagram alur system call
![alt text](<screenshots/diagram alur system call.png>)

---

## Analisis
- Jelaskan makna hasil percobaan.

   Makna hasil percobaan :
  *strace ls:strace membantu memahami dan menganalisis proses internal aplikasi secara detail,dan menampilkan setiap sistem call yang dilalukan oleh perintah ls.Ini menampilkan bagaimana  ls berinteraksi dengan kernel ,seperti membuka direktori,membaca file entri ,dan menutup file.
 *strace -e trace=open,read,write,close cat /etc/passwd: Fokus pada pengoperasian file ,menampilkan bagaimana aplikasi mengakses file tersebut secara proses demi proses dan melacak system call yang hanya berhubungan dengan membuka ,membaca,menulis,dan menutup file saat menjalankan cat /etc/passwd.
  * dmesg | tail -n 10: Menampilkan sekitar 10 baris log kernel yang biasanya berisi pesan penting terkait dengan perangkat keras,driver,atau error terbaru.ini berguna untuk melihat kejadian akhir yang dicatat oleh kernel dan membantu pemecahan masalah.   

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).

   *System call:Hasil dari percobaan strace menampilkan secara nyata bagaimana aplikasi menggunakan system call berkomunikasi dengan kernel
  *fungsi kernel:kernel berfungsi sebagai pengelola utama sumber daya sistem mengatur akses file dan perangkat keras.Saat melakukan strace cat /etc/passwd,kernel menerima dan memproses panggilan sistem contoh seperti buka,baca,dan tutup yang merupakan fungsi utama dalam mengakses file dan perangkat. 
   *Arsitektur OS:Struktur dan prosesnya terekam dalam strace menggambarkan desain arsitektur dan berlapis dari Linux,dimana kernel melayani permintaan melalui system call dan kernel mengelola aktivitas perangkat keras secara terstruktur. 
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

   Perbedaan hasil yang muncul karena Linux seringkali lebih stabil, efisien, dan aman, cocok untuk server dan sistem yang memerlukan kestabilan tinggi. Windows lebih mudah digunakan untuk pengguna umum dengan dukungan aplikasi dan perangkat keras yang sangat luas. Jadi,hasil kedua OS ini akan berbeda tergantung kebutuhan, dengan Linux lebih kuat di sisi kinerja dan terkecil, sementara Windows unggul di sisi kemudahan dan dukungan perangkat.
---

## Kesimpulan
Dari ketiga eksperimen tersebut menunjukan bagaimana systen call merupakan jembatan penting anatara aplikasi dan kernel dalam mengakses komponen komputer.Dengan strace ls ,terlihat perintah ls melakukan serangkaian system cal untuk membaca difolder dan file.Eksperimen strace -e trace=open,read,write,close cat /etc/passwd menampilakn secara jelas proses membuka,membaca,menulis dan menutup file yang menjadi operasi dasar akses file di sistem.Dan eksperimen dmesg | tail -n 10 memberikan gambaran tentang log kernel terbaru,yang berguna untuk pemantauan dan proses memperbaiki kesalahan sistem . Ketiga eksperimen ini menampilkan interaksi nyata anatar user space dan kernel ,menampilkan bagaiamana kernel mengelola permintaan aplikasi untuk menjaga sistem berjalan yang efisisen dan stabil.

---
## Tugas
Dokumentasikan hasil eksperimen strace dan dmesg dalam bentuk tabel observasi.

#strace ls

|No|Perintah|system call|fungsi|keterangan|
|:---|:---|:---|:---|:---|
1|strace|execve()|Menjalankan program baru diproses yang sama|Saat perintah ls dieksekusi,strace mencatat panggilan execve(bin/ls/environment variabless/)=0,nilai 0 menandakan eksekusiyang dijalankan berhasil|
2|strace|mmap()|Memetakan file atau memori ke area alamat proses|Mempercepat dan memudahkan pengelolaan memori selama perintah ls berjalan|
3|strace|Mprotect()|Mengubah izin akses halaman memori pada proses eksekusi|Mengontrol hak akses memori selama eksekusi ls |
4|strace|Statfs()|Mendapatkan informasi tentang sistem file|Statfs ("/sys/fs/selinux",...)=-1 ENOENT berarti proses mencoba membaca status file system di path|
5|strace|Openat()|Membuka file dengan cara menunjuk ke rektori tertentu yang sudah diketahui |ls membuka direktori saat dengan mode baca dan opsi lain yang sesuai untuk direktori|
6|strace|Access()|Mengontrol akses pengguna|Access menentukan apakah ls dapat membaca atau menampilakan file tersebut|
7|strace|Read()|Sebagai hak akses izin yang mengizinkan pengguna untuk melihat konten file atau isi direktori|Read proses pengambilan data mentah dari file sistem agar ls bisa memprosesnya|
8|strace|write()|Menulis data sebagai output|Read proses pengambilan data mentah dari file sistem agar ls bisa memprosesnya|Write menerima buffer berisi data yang akan ditampilkan dan jumlah byte yang harus ditulis dilayar| 
9|strace|Close()|Menutup file yang digunakan dalam program |Close menunjukan dekriptor filr mana yang ditutup dana kode return o untuk sukses|



#dmesg
|No|Perintah|System call|Fungsi|keterangan|
|:---|:---|:---|:---|:---|
1|dmesg|mount EXT4 filesystem|Menghubungkan filesystem EXT4 ke sistem daftar Linux sehingga file dan data didalamnya dapat diakses dan digunakan oleh pengguna|Penyimpanan /dev/sdb1 berhasil dipasang dengan sistem file EXT4 dalam mode read/write,menggunakan odered journaling untuk menjaga keutuhan|
2|dmesg|LoadPin:kernel-module-pinning-exluded|Memastikan modul kernel hanya dimuat dari sumber terpercaya|Mekanisme keamanan kernel Linux,LoadPin melindungi dengan membatasi sumber modul kernel,namun tetap memberi pengecualian kepada modul terpercaya agar sistem tetap stabil|
3|dmesg|modprob()|Mengatur pemuatan dan penghapusan modul kernel di Linux secara otomatis|Perintah ModProb digunakan untuk memuat modul kernel tertentu ke sistem ,dan hasilnya terlihat dipesan bahwa modul berhasil dimuat tanpa error|
4|dmesg|read()dan write()|Membaca isi file dari disk dan menulis ke ruang kernel|Terjadi saat kernel membaca isi file modul (.ko) dan menuliskannya ke memory kernel|
5|dmesg|setns()|Konfigurasi jaringan (network namespace dan firewall)|Saat kernel memuat modul netfilter atau iptables, terjadi pemanggilan system call untuk mengatur namespace dan komunikasi jaringan anatr proses kernel|


A.Mengapa system cell penting untuk keamanan OS?
System call sangat penting untuk keamanan sistem operasi karena memungkinkan OS mengontrol akses aplikasi ke sumber daya sistem. Bayangkan system call seperti "pintu masuk" yang dijaga ketat, sehingga OS bisa memastikan hanya permintaan yang aman yang diproses.
Dengan system call, OS bisa mengontrol akses, mencegah serangan, mengamankan sistem, memantau perilaku aplikasi, dan menerapkan kebijakan keamanan. System call memungkinkan OS untuk memverifikasi identitas aplikasi dan pengguna, serta memeriksa apakah mereka memiliki hak akses yang diperlukan.
System call juga membantu mencegah serangan seperti eskalasi hak istimewa, malware, dan virus yang dapat merusak sistem. Dengan demikian, system call sangat penting untuk menjaga keamanan dan stabilitas sistem operasi, serta melindungi data dan sumber daya sistem dari ancaman internal dan eksternal. System call juga memungkinkan OS untuk meningkatkan keamanan dengan memantau aktivitas sistem dan mendeteksi potensi ancaman.


B.Bagaimana OS memastikan transisi user–kernel berjalan aman?

 Untuk memastikan transisi antara mode pengguna (user mode) dan mode kernel (kernel mode) aman, sistem operasi (OS) menerapkan beberapa mekanisme penting. Berikut adalah cara-cara OS memastikan transisi yang aman:
1. OS memisahkan mode CPU menjadi dua mode utama, yaitu mode pengguna (user mode) dan mode kernel (kernel mode). Dengan demikian, kode yang berjalan di mode pengguna tidak dapat langsung mengakses sumber daya kernel tanpa melalui prosedur yang terkontrol.
2. Menggunakan System Call : System call adalah cara resmi bagi aplikasi di mode pengguna untuk meminta layanan dari kernel. Ketika aplikasi membutuhkan akses ke sumber daya kernel, seperti mengakses file atau jaringan, aplikasi tersebut akan melakukan system call. System call ini kemudian akan memicu interupsi yang menyebabkan CPU beralih dari mode pengguna ke mode kernel.
3. Memvalidasi Akses Memori dan Izin : Sebelum menjalankan perintah yang diminta oleh system call, kernel akan memvalidasi apakah aplikasi yang melakukan system call memiliki izin yang diperlukan untuk mengakses sumber daya yang diminta. Kernel juga akan memeriksa apakah alamat memori yang diakses valid dan tidak melanggar batasan keamanan.
4. Menerapkan Proteksi Hardware : OS juga menggunakan fitur proteksi hardware seperti ring level untuk memisahkan privilege level antara mode pengguna dan mode kernel. Ring level ini memastikan bahwa kode yang berjalan di mode pengguna tidak dapat mengakses sumber daya yang hanya dapat diakses oleh kernel. Selain itu, tabel interupsi juga digunakan untuk mengarahkan interupsi ke penanganan yang tepat di kernel.

C.Sebutkan contoh system call yang sering digunakan di Linux.

Sistem operasi (OS) Linux menggunakan system call sebagai antarmuka antara program pengguna dan kernel untuk melakukan operasi penting. System call memungkinkan program meminta layanan kernel untuk membuat proses baru, mengelola file, dan berkomunikasi antarproses. Contoh system call yang umum digunakan antara lain `fork()`, `exec()`, `wait()`, `exit()`, `getpid()`, `open()`, `read()`, `write()`, `close()`, `kill()`, `pipe()`, `chdir()`, `chmod()`, dan `sleep()`. Dengan menggunakan system call, program dapat berinteraksi dengan kernel untuk melakukan operasi yang tidak dapat dilakukan secara langsung di mode pengguna. Pemahaman tentang system call membantu memahami mekanisme kerja sistem operasi secara langsung. System call memiliki peran penting dalam pengelolaan proses dan sumber daya pada Linux, sehingga memungkinkan OS untuk mengontrol akses dan menjaga keamanan sistem secara efektif.


## Quiz
1. Apa fungsi utama system call dalam sistem operasi?  
   Jawaban: System call berperan sebagai jembatan komunikasi antara program pengguna dan kernel,program meminta layanan sistem operasi dengan cara yang aman dan terstandar. Ketika program membutuhkan akses ke sumber daya sistem seperti file, memori, proses, atau perangkat, system call menyediakan antarmuka yang terkendali untuk melakukan permintaan tersebut. System call memastikan permintaan tersebut diproses dengan aman dan terkendali, sehingga mencegah program pengguna mengakses sumber daya sistem secara tidak sah atau tidak terkendali dan system call membantu menjaga stabilitas dan keamanan sistem operasi
2. Sebutkan 4 kategori system call yang umum digunakan.    
   Jawaban: *Manajemen Berkas (File Management):Digunakan untuk membuat, membuka, membaca, menulis, dan menutup file.
            *Manajemen Proses (Process Management):Digunakan untuk membuat, menjalankan, menghentikan, atau mengatur proses.
            *Manajemen Memori (Memory Management):Digunakan untuk mengalokasikan, membebaskan, atau memetakan ruang memori.
            *Komunikasi Antarproses (Interprocess Communication / IPC): Digunakan agar proses dapat saling bertukar data atau berkoordinasi.  
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   Jawaban: System call tidak bisa dipanggil langsung oleh user program karena alasan keamanan, stabilitas, dan pengendalian akses dalam sistem operasi
System call tidak bisa dipanggil langsung oleh user program karena alasan keamanan,stabilitas,dan pengendalian akses dalam sistem operasi.Dan alasan lain kenapa system call tidak bisa dipanggil oleh user program karena hanya kernel yang memiliki hak akses penuh ke sumber daya sistem. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

   Sebenarnya hal yang paling menantang minggu adalah ketika mendapat tugas termasuknya matkul sistem operasi yang selalu menjadi pikiran setiap minggu ,karena tugas sistem operasi yang rumit cara penegrjaannya   
- Bagaimana cara Anda mengatasinya?

   Cara saya mengatasi hal tersebut saya mengatur waktu untuk mengerjakan tugas satu persatu dan mengerjakan diluar kampus bareng teman-teman agar tidak terlalu stres ddengan tugas yang begitu banyak. 
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
