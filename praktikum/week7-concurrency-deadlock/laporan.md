
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock



---

## Identitas Kelompok
 **Nama**:
 1. NOVIA SAFITRI(250202923)
 2. Sukmani Intan Jumala (250202983)
 3. Ismatul Khoeriyah (250202912)
**Kelas**: 1IKRA
 

---

## Tujuan

1. Mahasiswa mampu mengidentifikasi empat kondisi penyebab deadlock (mutual exclusion, hold and wait, no preemption, circular wait).

2. Mahasiswa mampu menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.

3. Mahasiswa mampu menganalisis dan memberikan solusi untuk kasus deadlock.

4. Mahasiswa mampu berkolaborasi dalam tim untuk menyusun laporan analisis.

5. Mahasiswa mampu menyajikan hasil studi kasus secara sistematis.

---

## Dasar Teori
Sinkronisasi adalah cara untuk mengatur sebagian proses yang berjalan bersamaan agar tidak terjadi bentrokan saat mengakses data yang sama.Tujuan supaya data tetap konsisten proses berjalan dengan teratur tanpa saling menganggu.Metode seperti semaphore dan mutex membantu untuk memastikan hanya satu proses yang masuk ke bagian sistem pada satu waktu,sehingga data tetap aman dan hasil kerja tidak berantakan.Masalah deadlock terjadi saat sebagian proses saling menunggu kapasitas yang dipegang proses lain,sehingga menyebabkan tidak ada yang maju atau selesai.Deadlock muncul karena proses saling menahan kapasitas,tidak bisa dipaksa melepasnya dan saling menunggu secara melingkar.Deadlock biasanya muncul jika 4 kondisi ini terpenuhi:
- Mutual Exclusion: satu sumber daya hanya bisa dipakai oleh satu proses.
- Hold and Wait: proses menahan satu sumber daya sambil menunggu yang lain.
- No Preemption: sumber daya tidak bisa diambil paksa dari proses lain.
- Circular Wait: terbentuk lingkaran menunggu, sehingga semua proses berhenti.

Pencegahan Deadlock dapat dilakukan dengan semaphore, monitor, atau mengatur urutan pengambilan sumber daya agar proses tidak saling menunggu dalam lingkaran (circular wait). Dengan mekanisme tersebut, proses dapat berjalan lancar dan risiko deadlock dapat diminimalkan.

---

## Langkah Praktikum
1. Persiapan Tim

   * Bentuk kelompok beranggotakan 3–4 orang.

   * Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)

    * Implementasikan versi sederhana dari masalah Dining Philosophers tanpa mekanisme pencegahan deadlock.

    * Contoh pseudocode:

           while true:
           think()
           pick_left_fork()
          pick_right_fork()
          eat()
          put_left_fork()
          put_right_fork()

    * Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).

    * Identifikasi kapan dan mengapa deadlock terjadi.

3. Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)

   * Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:

      * Menggunakan semaphore (mutex) untuk mengontrol akses.

      * Membatasi jumlah filosof yang dapat makan bersamaan (max 4).

      * Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).

      * Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. Eksperimen 3 – Analisis Deadlock

    * Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.

    * Sajikan hasil analisis dalam tabel seperti contoh berikut:

|Kondisi Deadlock|	Terjadi di Versi Deadlock|	Solusi di Versi Fixed|
|:---|:---|:---|
Mutual Exclusion|	Ya (satu garpu hanya satu proses)|	Gunakan semaphore untuk kontrol akses|
Hold and Wait|	Ya	|Hindari proses menahan lebih dari satu sumber daya|
No Preemption|	Ya	|Tidak ada mekanisme pelepasan paksa|
Circular Wait|	Ya	|Ubah urutan pengambilan sumber daya|

5. Eksperimen 4 – Dokumentasi

    * Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:

    praktikum/week7-concurrency-deadlock/screenshots/

    * Tuliskan laporan kelompok di laporan.md (format IMRaD singkat: Pendahuluan, Metode, Hasil, Analisis, Diskusi).

6. Commit & Push

       git add .
       git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
       git push origin main


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
while true:
  think()
  pick_left_fork()
  pick_right_fork()
  eat()
  put_left_fork()
  put_right_fork()
```

---

## Hasil Eksekusi
**Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
![Screenshot hasil](screenshots/example.png)

- Output

      F0 mulai berpikir
      F1 mulai berpikir
      F2 mulai berpikir
      F3 mulai berpikir
      F4 mulai berpikir
      F0 mencoba mengambil garpu kiri
      F0 mengambil garpu kiri
      F1 mencoba mengambil garpu kiri
      F1 mengambil garpu kiri
      F2 mencoba mengambil garpu kiri
      F2 mengambil garpu kiri
      F3 mencoba mengambil garpu kiri
      F4 mencoba mengambil garpu kiri
      F4 mengambil garpu kiri
      F3 mengambil garpu kiri
      F0 mencoba mengambil garpu kanan
      F1 mencoba mengambil garpu kanan
      F2 mencoba mengambil garpu kanan
      F4 mencoba mengambil garpu kanan
      F3 mencoba mengambil garpu kanan

- Identifikasi kapan dan mengapa deadlock terjadi.
  
**Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
![Screenshot hasil](screenshots/example.png)
- output

      Filosof 0 siap...
      Filosof 1 siap...
      Filosof 2 siap...
      Filosof 3 siap...
      Filosof 4 siap...
      Filosof 4 mulai berpikir...
      Filosof 1 mulai berpikir...
      Filosof 2 mulai berpikir...
      Filosof 3 mulai berpikir...
      Filosof 0 mulai berpikir...
      Filosof 4 mencoba mengambil garpu kiri
      Filosof 4 mencoba mengambil garpu kanan
      Filosof 4 mulai makan...
      Filosof 3 mencoba mengambil garpu kiri
      Filosof 3 mencoba mengambil garpu kanan
      Filosof 0 mencoba mengambil garpu kiri
      Filosof 1 mencoba mengambil garpu kiri
      Filosof 1 mencoba mengambil garpu kanan
      Filosof 1 mulai makan...
      Filosof 4 selesai makan
      Filosof 2 mencoba mengambil garpu kiri
      Filosof 3 mulai makan...
      Filosof 0 mencoba mengambil garpu kanan
      Filosof 0 mulai makan...
      Filosof 2 mencoba mengambil garpu kanan
      Filosof 1 selesai makan
      Filosof 3 selesai makan
      Filosof 2 mulai makan...
      Filosof 0 selesai makan
      Filosof 2 selesai makan

- Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.
  Dari hasil modifikasi menggunakan semaphore footman = Semaphore(4) secara efektif untuk mencegah terjadinya deadlock di masalah Dining Philosophers karena dibatasi hanya empat  filsuf yang dapat mencoba mengambil garpu pada saat bersamaan.Membatasi untuk memastikan bahwa selalu ada minimal satu filsuf yang tidak memegang garpu sama sekali, sehingga dua garpu di dekatnya tetap bebas dan memungkinkan satu filsuf lain mendapatkan  kedua garpu secara lengkap untuk makan. Dengan kondisi circular wait adalah penyebab  utama deadlock—tidak dapat terbentuk karena jumlah filsuf yang menunggu tidak pernah mencapai lima,sehingga rantai tunggu tertutup tidak terjadi.Saat satu filsuf selesai makan, ia melepaskan kedua garpu dan me-release semaphore, membuka kesempatan bagi filsuf yang menunggu untuk melanjutkan proses, menjamin bahwa sistem tetap memiliki progres, tidak ada thread yang macet permanen, dan program terus berjalan tanpa mengalami deadlock.

- buktikan bahwa deadlock telah dihindari;
**footman = threading.Semaphore(4)**
  - Maxsimal 4 filsuf yang boleh masuk proses ambil garpu
  - 1 filsuf menunggu diluar

 Jika hanya 4 filsuf yang aktif mengambil garpu: 
- maksimal 4 garpu yang bisa dikunci dan tidak mungkin semua 5 garpu sedang dipegang sekaligus

Deadlock hanya terjadi jika ada circular wait, yaitu:
     
     F0 menunggu F1
     F1 menunggu F2, …, 
     F4 menunggu F0
Tetapi circular wait butuh 5 peserta.
Di sini hanya 4 yang boleh masuk.

- setelah makan

      left.release()
      right.release()
      footman.release()

garpu kembali bebas,kapasitas semaphore bertambah,filsuf ke-5 boleh masuk tetapi sistem tetap bergerak



**Eksperimen 3 – Analisis Deadlock**
|Kondisi Deadlock|	Terjadi di Versi Deadlock|	Solusi di Versi Fixed|
|:---|:---|:---|
Mutual Exclusion|	Ya-setiap garpu hanya bisa dipegang satu filsuf pada satu waktu|	Gunakan semaphore untuk kontrol akses|
Hold and Wait|	Ya-filsuf memegang garpu kiri sambil menunggu garpu kanan	|Hindari proses menahan lebih dari satu sumber daya|
No Preemption|	Ya-garpu tidak bisa diambil paksa dari filsuf lain	|Tidak ada mekanisme pelepasan paksa|
Circular Wait|	Ya-F0 menunggu garpu F1, F1 menunggu F2, ..., F4 menunggu F0	|Ubah urutan pengambilan sumber daya|


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.

   Empat kondisi utama penyebab deadlock:

   * Mutual Exclusion yaitu situsi dimana kapasitas hanya digunakan oleh satu sistem pada suatu waktu,sehingga tidak bisa dibagi bersama.

   * Hold and Wait yaitu situasi dimana sistem memegang satu kapasitas sambil menunggu kapasitas lain yang sedang dipegang oleh sistem lain.

   * NO Preemption yaitu situasi dimana kapaitas tidak dapat diambil paksa dari sistem yang sedang memakainya sampai proses tersebut selesai.

   * Circular Wait yaitu situasi dimana terdapat putaran sistem yang saling menunggu kapasitas yang dimiliki oleh sistem lain,membentuk lingkaran ketergantungan.
   
2. Mengapa sinkronisasi diperlukan dalam sistem operasi?

   Sinkronisasi diperlukan dalam sistem operasi karena untuk mengatur berlangsungnya sebagian sistem yang berlangsung bersamaan dan bisa mengakses data secara bersamaan,jika tidak diatur dengan baik data bisa tidak konsisten atau malah bisa rusak.Sinkronisasi juga membantu menghindari dari masalah seperti deadlock dan starvation,sehingga semua proses bisa berlangsung lancar sesuai urutan yang benar
     

4. Jelaskan perbedaan antara semaphore dan monitor.

   |Aspek|Semaphore|Monitor|
   |:---|:---|:---|
   Pengertian|Komponen yang digunakan untuk mengatur akses ke kapasitas bersama dengan angka(counting)|Struktur yang menggabungkan komponen,proses,dan pengendali akses agar aman digunakan bersama|
   Cara kerja|Proses menggunakan wait()dan signal()|Akses dilakukan dengan prosedur dan monitor,manajemen antrian tunggu diatur dengan otomatis oleh sistem|
   Jenis sinkronisasi|Sinkronisasi tingkat rendah|Sinkronisasi tingakt tinggi dengan penyederhanaan|
   Kesulitan|Lebih rumit dan rawan kesalahan|Lebih dan aman |

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

 Bagian yang paling paling menantang pada minggu ke 7
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
