
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF 

---

## Identitas
- **Nama**  : Faiq Atha Rulloh
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---

## A. Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **algoritma penjadwalan CPU (CPU Scheduling)** menggunakan dua pendekatan dasar:  
- **FCFS (First Come First Served)**  
- **SJF (Shortest Job First)**  

Tujuan utamanya adalah memahami bagaimana sistem operasi menentukan urutan eksekusi proses, serta bagaimana *waiting time* dan *turnaround time* memengaruhi performa sistem.

Mahasiswa akan melakukan simulasi dan perbandingan hasil perhitungan kedua algoritma ini menggunakan **tabel observasi manual atau spreadsheet (Excel/Google Sheets)** — tanpa perlu melakukan instalasi atau pemrograman tambahan.



## Tujuan.
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  

---

## Dasar Teori
1. Konsep Penjadwalan CPU
   - Penjadwalan CPU adalah mekanisme sistem operasi untuk menentukan urutan eksekusi proses di CPU dengan tujuan meningkatkan efisiensi penggunaan CPU, mengurangi waktu tunggu, dan mempercepat waktu respon sistem. Scheduler memilih proses berdasarkan kebijakan algoritma penjadwalan tertentu.
   - > (Silberschatz et al., 2018)

2. Algoritma FCFS (First Come, First Served)
   - FCFS mengeksekusi proses berdasarkan urutan kedatangan. Proses yang datang terlebih dahulu akan dijalankan lebih dulu tanpa interupsi (non-preemptive). Kekurangannya adalah dapat terjadi convoy effect, di mana proses pendek menunggu proses panjang selesai.
   - > (Tanenbaum & Bos, 2015)

3. Algoritma SJF (Shortest Job First)
   - SJF memilih proses dengan waktu eksekusi (CPU burst time) terpendek terlebih dahulu. Algoritma ini dapat bersifat non-preemptive atau preemptive (SRTF). SJF memberikan waktu tunggu rata-rata paling optimal, tetapi memerlukan estimasi burst time yang akurat.
   - > (Silberschatz et al., 2018; OSTEP, 2018)

4. Perbandingan FCFS dan SJF
   - FCFS mudah diterapkan namun kurang efisien, sedangkan SJF lebih optimal dalam waktu tunggu tetapi kompleks dalam implementasi karena sulit memprediksi burst time proses.
   - > (Tanenbaum & Bos, 2015)

5. Tujuan Analisis Praktikum
   - Melalui simulasi dan perhitungan pada algoritma FCFS dan SJF, mahasiswa dapat memahami bagaimana kebijakan penjadwalan mempengaruhi kinerja sistem, khususnya pada parameter waktu tunggu (waiting time), waktu selesai (turnaround time), dan efisiensi CPU.
   - > (Silberschatz et al., 2018; OSTEP, 2018)


---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
       
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

---

## Kesimpulan

---

### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
4. Simpan seluruh hasil dan analisis ke `laporan.md`.

--- 

### Quiz
 Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara FCFS dan SJF?  
 - Perbedaan utama antara FCFS dan SJF
     - FCFS (First-Come, First-Served) mengeksekusi proses berdasarkan urutan kedatangan — proses pertama yang datang akan dijalankan lebih dahulu tanpa interupsi (non-preemptive).
     - SJF (Shortest Job First) memilih proses dengan waktu eksekusi terpendek (CPU burst time) untuk dijalankan terlebih dahulu. SJF dapat bersifat non-preemptive maupun preemptive (Shortest Remaining Time First – SRTF).

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
 - Karena algoritma SJF secara teoritis memberikan waktu tunggu rata-rata paling kecil dibandingkan algoritma lainnya.
Hal ini karena proses dengan burst time pendek dieksekusi terlebih dahulu, sehingga proses-proses cepat segera selesai dan tidak menunggu proses panjang. Proses panjang memang menunggu lebih lama, tetapi total waktu tunggu keseluruhan tetap minimum.

3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?
 - Kelemahan utama SJF pada sistem interaktif adalah:
     - Sulit memperkirakan burst time. Sistem interaktif memiliki proses dengan durasi yang tidak pasti, sehingga prediksi waktu eksekusi menjadi tidak akurat.
     - Dapat menyebabkan starvation. Proses dengan burst time panjang bisa terus tertunda jika proses pendek terus datang.
     - Kurang responsif. Dalam sistem interaktif, respons cepat terhadap input pengguna lebih penting daripada efisiensi rata-rata waktu tunggu.

## Output yang Diharapkan
- Hasil observasi dan perhitungan dimasukkan ke dalam `laporan.md`.  
- Screenshot tabel atau Gantt Chart disimpan di `screenshots/`.  
- Laporan lengkap berada di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
