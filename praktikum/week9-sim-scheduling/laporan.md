
# Laporan Praktikum Minggu [X]
 ## Simulasi Algoritma Penjadwalan CPU



---

## Identitas
- **Nama**  : [Miftakhul Lisna Esa Baehaqi]  
- **NIM**   : [250202951]  
- **Kelas** : [1IKRB]

---

## Tujuan
1. Tuliskan tujuan praktikum minggu ini.  
Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.


---

## Dasar Teori
- Prinsip Non-Preemptive: FCFS adalah algoritma penjadwalan yang bersifat non-preemptive. Artinya, begitu CPU dialokasikan untuk sebuah proses, proses tersebut akan memegang kendali CPU sampai ia selesai eksekusi atau berhenti secara sukarela. CPU tidak bisa "merebut" tugas di tengah jalan untuk beralih ke tugas lain.
- Mekanisme Antrean FIFO (First-In, First-Out): Logika dasarnya identik dengan antrean di dunia nyata. Proses yang masuk ke antrean ready paling awal dengan Arrival Time (AT) terkecil akan dilayani terlebih dahulu oleh CPU. Data dikelola menggunakan struktur data antrean.
- Metrik Kinerja (TAT & WT): Efisiensi algoritma diukur berdasarkan Turnaround Time (TAT) dan Waiting Time (WT). TAT mengukur total waktu sejak proses datang hingga selesai (FT - AT), sedangkan WT mengukur berapa lama proses menunggu di antrean sebelum dieksekusi (TAT - BT).


---

## Langkah Praktikum
1. Menyiapkan Dataset

Buat dataset proses minimal berisi:

| Process | Arrival Time | Burst Time |
|--------|--------------|------------|
| P1 | 0 | 6 |
| P2 | 1 | 8 |
| P3 | 2 | 7 |
| P4 | 3 | 3 |

2. Implementasi Algoritma

Program harus:

- Menghitung waiting time dan turnaround time.
- Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).
- Menampilkan hasil dalam tabel.

3. Eksekusi & Validasi

- Jalankan program menggunakan dataset uji.
- Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.
- Simpan hasil eksekusi (screenshot).
  
4. Analisis

- Jelaskan alur program.
- Bandingkan hasil simulasi dengan perhitungan manual.
- Jelaskan kelebihan dan keterbatasan simulasi.


---

## Kode / Perintah


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/code%201.png)
![screenshot hasil](./screenshots/code%202.png)

---

## Analisis
1. Alur eksekusi program.
- P1 datang pada waktu 0 dan langsung dieksekusi karena belum ada program lain yang datang dan harus dieksekusi. Program P1 selesai di waktu 6 karena memiliki BT 6.
- P2 datang pada waktu 1 dan harus menunggu P1 selesai dieksekusi. P2 dieksekusi pada waktu 6 dan selesai pada waktu 14 karena memiliki BT 8.
- P3 datang pada waktu 2 dan harus menunggu P1 dan P2 selesai dieksekusi. P3 dieksekusi pada waktu 14 dan selesai pada waktu 21 karena memiliki BT 7.
- P4 datang pada waktu 3 dan harus menunggu P1,P2 dan P3 selesai dieksekusi. P4 dieksekusi pada waktu 21 dan selesai pada waktu 24 karena memiliki BT 3.
2. Bandingkan hasil simulasi dengan perhitungan manual. Berdasarkan hasil yang terlihat, hasil perhitungan otomatis maupun perhitungan memiliki hasil yang sama.
3. Jelaskan kelebihan dan keterbatasan simulasi.
- Kelebihan dalam simulasi ini adalah kita tidak perlu mencoba-coba algoritma langsung pada sistem operasi yang sedang berjalan karena berisiko membuat komputer crash.
- Kekurangannya adalah simulasinya terlalu sederhana, tidak memperhitungkan gangguan yang mungkin muncul atau kemampuan kinerja hardware. Sehingga hasil simulasi tidak 100% sesuai kondisi di dunia nyata.

---

## Kesimpulan
1. Keadilan Berdasarkan Urutan Kedatangan: Algoritma FCFS terbukti sebagai metode penjadwalan yang paling adil secara kronologis, karena menggunakan metode non-preemptive.
2. Efisiensi Tergantung pada Variasi Burst Time: Jika proses pertama memiliki Burst Time yang sangat lama, maka akan terjadi lonjakan besar pada rata-rata Waiting Time bagi proses-proses berikutnya, yang secara teknis dikenal sebagai fenomena Convoy Effect.
3. Akurasi Perhitungan melalui Simulasi: Melalui simulasi Python, dapat dibuktikan bahwa nilai Finish Time (FT) suatu proses merupakan akumulasi dari waktu mulai ditambah durasi kerjanya. Simulasi ini mempermudah visualisasi dan perhitungan metrik performa sistem (TAT dan WT) secara otomatis dibandingkan perhitungan manual yang rentan terhadap kesalahan manusia.

---

## Quiz
1. [1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?]  

- Keamanan Sistem: Menguji algoritma langsung pada sistem nyata (seperti kernel OS yang sedang berjalan) sangat berisiko karena jika ada kesalahan logika, sistem bisa crash atau membeku.

- Efisiensi Biaya dan Waktu: Simulasi memungkinkan kita melihat performa algoritma tanpa perlu perangkat keras yang mahal atau menunggu proses nyata yang mungkin memakan waktu lama.

- Eksperimen yang Fleksibel: Kita bisa dengan mudah mengubah-ubah parameter (seperti mengganti Burst Time atau Arrival Time) untuk melihat bagaimana algoritma bereaksi terhadap berbagai skenario beban kerja.

- Analisis Prediktif: Simulasi memberikan gambaran statistik (seperti Average Waiting Time) yang akurat sebelum algoritma tersebut benar-benar diterapkan.:**

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
- Akurasi: Pada dataset kecil, hasil manual dan simulasi akan sama. Namun, pada dataset besar (misal ratusan proses), perhitungan manual sangat rentan terhadap human error (kesalahan hitung), sedangkan simulasi tetap konsisten dan akurat.

- Kecepatan: Simulasi komputer dapat memproses ribuan data dalam hitungan detik, sementara perhitungan manual akan memakan waktu berjam-jam.

- Visualisasi: Simulasi dapat otomatis menghasilkan Gantt Chart yang rapi untuk data yang kompleks, yang hampir mustahil digambar secara manual dengan presisi jika datanya terlalu banyak. 
3. . Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.

- Jawaban: FCFS (First-Come, First-Served) adalah algoritma yang paling mudah diimplementasikan.

Penjelasan:

- Logika Sederhana: Algoritma ini hanya menggunakan konsep antrian (FIFO - First In First Out). Proses yang datang pertama akan dilayani pertama kali.

- Tanpa Prioritas Complex: Tidak membutuhkan pengecekan sisa waktu (seperti SJF) atau pembagian jatah waktu (Time Quantum seperti Round Robin), sehingga struktur kodenya jauh lebih pendek dan sederhana.

- Minim Overhead: Karena tidak ada proses interupsi (preemption) atau perpindahan antar antrian yang rumit, beban kerja sistem untuk mengatur jadwal menjadi sangat ringan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
tugas telat di up jadi deadline menyempiy
- Bagaimana cara Anda mengatasinya?  
tidak ada

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
