
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

## E. Hasil Eksekusi dan Analisis

![Hasil Eksekusi](<screenshots/Eksperimen 1 bab 6.png>)

**Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.

|    Proses   | Burst Time | Arrival Time | Finish | Waiting Time | Turnaround Time |
| :---------: | :--------: | :----------: | :----: | :----------: | :-------------: |
|      P1     |      5     |       0      |   14   |       9      |        14       |
|      P2     |      3     |       1      |    6   |       2      |        5        |
|      P3     |      8     |       2      |   22   |      12      |        20       |
|      P4     |      6     |       3      |   20   |      11      |        17       |
|  **Total**  |            |              |        |    **34**    |      **56**     |
| **Average** |            |              |        |    **8,5**   |      **14**     |


   - Turnaround Time = Finish Time - Arrival Time
       - 14-0 = 14
       - 6-1 = 5
       - 22-2 = 20
       - 20-3 = 17
   - Waiting Time = Turnaround Time - Burst Time
       - 14-5 = 9
       - 5-3 = 2 
       - 20-8 = 12
       - 17-6 = 11
         
   -  Simulasikan eksekusi Gantt Chart Round Robin (RR).
     
 ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12    14   17   20   22
 ```

   - Catat sisa *burst time* tiap putaran
      - Putaran 1
          - Proses: P1 (3 unitt) SISA BURST TIME:
          - P1: 5 → 2  (-3)
          - P2: 3 (belum tiba)
          - P3: 8 (belum tiba)
          - P4: 6 (belum tiba)
      - Putaran 2
          - Proses: P2 (3 unit) SISA BURST TIME:
          - P1: 2
          - P2: 3 → 0  (-3)  (SELESAI)
          - P3: 8
          - P4: 6
      - Putaran 3
          - Proses: P3 (3 unit) SISA BURST TIME:
          - P1: 2
          - P2: SELESAI
          - P3: 8 → 5  (-3)
          - P4: 6
      - Putaran 4
          - Proses: P4 (3 unit) SISA BURST TIME:
          - P1: 2
          - P2: SELESAI
          - P3: 5
          - P4: 6 → 3  (-3)
      - Putaran 5
          - Proses: P1 (2 unit) SISA BURST TIME:
          - P1: 2 → 0  (-2)  (SELESAI)
          - P2: SELESAI
          - P3: 5
          - P4: 3
      - Putaran 6
          - Proses: P3 (3 unit) SISA BURST TIME:
          - P1: SELESAI
          - P2: SELESAI
          - P3: 5 → 2  (-3)
          - P4: 3
      - Putaran 7
          - Proses: P4 (3 unit) SISA BURST TIME:
          - P1: SELESAI
          - P2: SELESAI
          - P3: 2
          - P4: 3 → 0  (-3)  (SELESAI)
      - Putaran 8
          - Proses: P3 (2 unit) SISA BURST TIME:
          - P1: SELESAI
          - P2: SELESAI
          - P3: 2 → 0  (-2)  (SELESAI)
          - P4: SELESAI
            
---


**Eksperimen 2 – Priority Scheduling (Non-Preemptive)**

|    Proses   | Burst Time | Arrival Time | Priority | Start | Finish | Waiting Time | Turnaround Time |
| :---------: | :--------: | :----------: | :------: | :---: | :----: | :----------: | :-------------: |
|      P1     |      5     |       0      |     2    |   0   |    5   |       0      |        5        |
|      P2     |      3     |       1      |     1    |   5   |    8   |       4      |        7        |
|      P3     |      6     |       3      |     3    |   8   |   14   |       5      |        11       |
|      P4     |      8     |       2      |     4    |   14  |   22   |      12      |        20       |
|  **Total**  |            |              |          |       |        |    **21**    |      **43**     |
| **Average** |            |              |          |       |        |   **5,25**   |    **10,75**    |


   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).
       - P2 → P1 → P3 → P4 (Karena Angka kecil = Prioritas TINGGI ; Angka besar = Prioritas RENDAH).


   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Waitinng Time :
       - P1 : 0 - 0 = 0
       - P2 : 5 - 1 = 4
       - P3 : 8 - 3 = 5
       - P4 : 14 - 2 = 12
   - Turnaround Timme :
       - P1 : 0 + 5 = 5
       - P2 : 4 + 3 = 7
       - P3 : 5 + 6 = 11
       - P4 : 12 + 8 = 20
         
   -  Buat tabel perbandingan hasil RR dan Priority. Perbandingan Hasil Round Robin dan Priority Scheduling (Quantum = 3)

| **Proses** | **RR Waiting Time** | **RR Turnaround Time** | **Priority Waiting Time** | **Priority Turnaround Time** |
| :--------: | :-----------------: | :--------------------: | :-----------------------: | :--------------------------: |
|   **P1**   |          9          |           14           |             0             |               5              |
|   **P2**   |          2          |            5           |             4             |               7              |
|   **P3**   |          12         |           20           |             5             |              11              |
|   **P4**   |          11         |           17           |             12            |              20              |

|           **Metode**          | **Total Waiting Time** | **Rata-rata Waiting Time** | **Total Turnaround Time** | **Rata-rata Turnaround Time** |
| :---------------------------: | :--------------------: | :------------------------: | :-----------------------: | :---------------------------: |
|        **Round Robin**        |           34           |            8,50            |             56            |             14,00             |
| **Priority (non-preemptive)** |           21           |            5,25            |             43            |             10,75             |


---

**Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**

![Hasil Eksekusi](<screenshots/Eksperimen 2 bab 6.png>)


   - Ubah *quantum* menjadi 2 dan 5.
     
     - Round Robin (RR) – Time Quantum (q = 2)
         
|    Proses   | Burst Time | Arrival Time | Finish (P1) | Finish (P2) | Finish (P3) | Finish (P4) | Waiting Time | Turnaround Time |
| :---------: | :--------: | :----------: | :---------: | :---------: | :---------: | :---------: | :----------: | :-------------: |
|      P1     |      5     |       0      |      2      |      10     |      16     |  (Selesai)  |      11      |        16       |
|      P2     |      3     |       1      |      4      |      11     |  (Selesai)  |  (Selesai)  |       7      |        10       |
|      P3     |      8     |       2      |      6      |      13     |      18     |      22     |      12      |        20       |
|      P4     |      6     |       3      |      8      |      15     |      20     |  (Selesai)  |      11      |        17       |
|  **Total**  |            |              |             |             |             |             |    **41**    |      **63**     |
| **Average** |            |              |             |             |             |             |   **10,25**  |    **15,75**    |

  
   - Round Robin (RR) – Time Quantum (q = 5)

|    Proses   | Burst Time | Arrival Time | Finish (P1) | Finish (P2) | Finish (P3) | Finish (P4) | Waiting Time | Turnaround Time |
| :---------: | :--------: | :----------: | :---------: | :---------: | :---------: | :---------: | :----------: | :-------------: |
|      P1     |      5     |       0      |      5      |  (Selesai)  |  (Selesai)  |  (Selesai)  |       0      |        5        |
|      P2     |      3     |       1      |      8      |  (Selesai)  |  (Selesai)  |  (Selesai)  |       4      |        7        |
|      P3     |      8     |       2      |      13     |      18     |      22     |  (Selesai)  |      11      |        19       |
|      P4     |      6     |       3      |      18     |      22     |  (Selesai)  |  (Selesai)  |      13      |        19       |
|  **Total**  |            |              |             |             |             |             |    **28**    |      **50**     |
| **Average** |            |              |             |             |             |             |     **7**    |     **12,5**    |



   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.
       - Tabel Perbandingan 

| Time Quantum (q) | Rata-rata Waiting Time | Rata-rata Turnaround Time | Keterangan                                            |
| :--------------: | :--------------------: | :-----------------------: | :---------------------------------------------------- |
|         2        |          10,25         |           15,75           | Quantum terlalu kecil → banyak *context switching*    |
|         3        |           8,5          |             14            | Lebih seimbang antara keadilan dan efisiensi          |
|         5        |            7           |            12,5           | Quantum besar → mirip FCFS, lebih sedikit *switching* |



   - Buat tabel perbandingan efek *quantum*.

| Time Quantum (q) | Rata-rata Waiting Time | Rata-rata Turnaround Time |     Jumlah Context Switching    | Efisiensi CPU | Karakteristik Umum                                                        |
| :--------------: | :--------------------: | :-----------------------: | :-----------------------------: | :-----------: | :------------------------------------------------------------------------ |
|       **2**      |          10,25         |           15,75           | Tinggi (sering berganti proses) |     Rendah    | Adil untuk semua proses, tetapi banyak waktu terbuang untuk *switching*   |
|       **3**      |           8,5          |             14            |              Sedang             |     Sedang    | Keseimbangan antara keadilan dan efisiensi, hasil paling seimbang         |
|       **5**      |            7           |            12,5           | Rendah (jarang berganti proses) |     Tinggi    | Mirip **FCFS**, proses cepat selesai tapi kurang adil untuk proses pendek |


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
