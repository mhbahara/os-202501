
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock



---

## Identitas
- **Nama**  :NOVIA SAFITRI
- **NIM**   : 250202923
- **Kelas** :1IKRA

---

## Tujuan

1. Mahasiswa mampu mengidentifikasi empat kondisi penyebab deadlock (mutual exclusion, hold and wait, no preemption, circular wait).

2. Mahasiswa mampu menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.

3. Mahasiswa mampu menganalisis dan memberikan solusi untuk kasus deadlock.

4. Mahasiswa mampu berkolaborasi dalam tim untuk menyusun laporan analisis.

5. Mahasiswa mampu menyajikan hasil studi kasus secara sistematis.

---

## Dasar Teori
Sinkronisasi adalah cara untuk mengatur sebagian proses yang berjalan bersamaan agar tidak terjadi bentrokan saat mengakses data yang sama.Tujuan supaya data tetap konsisten proses berjalan dengan teratur tanpa saling menganggu.Metode seperti semaphore dan mutex membantu untuk memastikan hanya satu proses yang masuk ke bagian sistem pada satu waktu,sehingga data tetap aman dan hasil kerja tidak berantakan.

Masalah deadlock terjadi saat sebagian proses saling menunggu kapasitas yang dipegang proses lain,sehingga menyebabkan tidak ada yang maju atau selesai.Deadlock muncul karena proses saling menahan kapasitas,tidak bisa dipaksa melepasnya dan saling menunggu secara melingkar.

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
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

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
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
