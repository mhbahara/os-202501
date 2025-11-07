
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Faiq Atha Rulloh  
- **NIM**   : 250320571  
- **Kelas** : 1DSRA

---
## A. Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **dua algoritma lanjutan penjadwalan CPU**, yaitu:
- **Round Robin (RR)**  
- **Priority Scheduling**

Kedua algoritma ini banyak digunakan pada sistem modern karena mempertimbangkan **keadilan waktu eksekusi (time quantum)** dan **tingkat prioritas proses**.  
Mahasiswa akan melakukan simulasi perhitungan manual untuk menghitung *waiting time* dan *turnaround time*, serta menganalisis efek perbedaan *time quantum* dan prioritas terhadap performa CPU scheduling.

## B. Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  

---

## C. Dasar Teori
1. _Round Robin (RR)_ adalah algoritma penjadwalan tindakan yang membagi waktu CPU ke setiap proses secara bergiliran menggunakan satuan waktu yang tetap.
2. _Time Quantum (q)_ adalah Durasi maksimum proses menggunakan CPU sebelum di ambil alih.
3. _Turnaround Time (TT)_ adalah Waktu kedatangan hingga penyelesaian proses.
4. _Waiting Time (WT)_ adalah Total waktu proses menunggu di antrian siap.
5. _Priority Scheduling_ adalah algoritma yang mengalokasikan CPU ke proses dengan prioritas tertinggi.
   
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## D. Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```


---

## E. Hasil Eksekusi

![Screenshot hasil](screenshots/example.png)

---

## Analisis 

---

## Kesimpulan

---

## F. Tugas
1. Hitung *waiting time* dan *turnaround time* untuk algoritma RR dan Priority.  
2. Sajikan hasil perhitungan dan Gantt Chart dalam `laporan.md`.  
3. Bandingkan performa dan jelaskan pengaruh *time quantum* serta prioritas.  
4. Simpan semua bukti (tabel, grafik, atau gambar) ke folder `screenshots/`.
   
---

## G. Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?
- Perbedaan utamanya dari segi kriteria penjadwalannya antara lain :
    - _Round Robin (RR)_ kriteria penjadwalannya itu Berdasarkan waktu selesai, setiap proses akan mendapatkan jatah waktu CPU yang sama Sementara,
    - _Priority Scheduling_ dari segi kriteria penjadwalannya itu Berdasarkan tingkat kepentingan (proses penting yang didahulukan) jadi, proses dengan prioritas *tertinggi* akan dilayani terlebih dahulu.

2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  
 - Pengaruh *time quantum* besar:
     - Dampak Positif :
        - Lebih sedikit waktu yang terbuang untuk peralihan proses.
        - Proses panjang dapat diselesaikan lebih efisien.
     - Dampak Negatif :
        - Waktu respon untuk proses interaktif memburuk.
        - Kehilangan manfaat utama *Round Robin (RR)*
 - Pengaruh *time quantum* kecil:
     - Dampak Positif :
        - Pembagian waktu CPU sangat merata.
        - *Waiting time* untuk proses pendek.
     - Dampak Negatif :
        - CPU banyak membuang waktu untuk switching.

3. Mengapa algoritma Priority dapat menyebabkan *starvation*?
 - *Starvation* terjadi disebabkan karena sistem terlalu fokus pada yang paling penting sampai melupakan yang biasa-biasa saja.
   
---

## H. Output yang Diharapkan
- Hasil perhitungan dan analisis dimasukkan ke `laporan.md`.  
- Screenshot tabel atau Gantt Chart disimpan di folder `screenshots/`.  
- Laporan lengkap berada di `laporan.md`.  
- Semua hasil telah di-*commit* ke GitHub tepat waktu.
   
---

## I. Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
