
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Rizky Iqbal Hisyam
- **NIM**   : 250202926
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  

---

## Dasar Teori
**Round Robin (RR) Scheduling**

Round Robin adalah algoritma penjadwalan yang memberi waktu giliran sama rata untuk setiap proses. Setiap proses dijalankan bergantian selama waktu tertentu (time quantum). Kalau belum selesai, proses akan menunggu giliran berikutnya.
Metode ini adil dan responsif, cocok untuk sistem interaktif. Tapi kalau quantum terlalu kecil, akan sering terjadi context switching dan kalau terlalu besar, hasilnya mirip FCFS.
Intinya, Round Robin menyeimbangkan keadilan dan kecepatan respon antar proses.

**Priority Scheduling (Non-Preemptive)**

Priority Scheduling adalah proses yang dijalankan berdasarkan tingkat prioritasnya, proses dengan angka prioritas lebih kecil dijalankan lebih dulu. Dalam versi non-preemptive, proses yang sedang berjalan tidak bisa diganggu meski ada proses lain dengan prioritas lebih tinggi.
Metode ini efisien untuk proses yang punya tingkat kepentingan berbeda, tapi bisa menyebabkan proses prioritas rendah menunggu lama (*starvation*).
Intinya, Priority Scheduling fokus pada kepentingan proses, bukan urutan kedatangan.

---

## Langkah Praktikum
1. Siapkan data proses seperti berikut. 
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. Siapkan alat perhitungan manual atau spreadsheet (Excel/Google Sheets).
3. Eksperimen 1 berdasarkan algoritma *Round Robin (RR)* dengan *time quantum (q)* = 3, hitung Waiting Time (WT) dan Turnaround Time (TAT) untuk tiap proses.
4. Simulasikan eksekusi menggunakan Gantt Chart dan catat sisa Burst Time tiap putaran
5. Eksperimen 2 berdasarkan algoritma *Priority Scheduling* (angka kecil = prioritas tinggi) dan hitung WT serta TAT nya seperti pada langkah 3. 
6. Buat tabel perbandingan rata-rata WT & TAT dari kedua eksperimen tersebut dan analisis perbedaannya.
7. Eksperimen 3 berdasarkan algoritma *Round Robin (RR)* dengan mengubah *time quantum (q)* menjadi 2 dan 5, hitung WT dan TAT nya, buat tabel perbandingan efek *quantum*.
8. Commit dan push hasil praktikum
 ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```


---

## Hasil Eksekusi & Analisis
Hasil Eksperimen:
![alt text](./screenshots/RR%20&%20PS.png)

**Eksperimen 1 – Round Robin (RR)**
- *Time quantum (q)* = 3.  
- Berikut tabel perhitungan *Waiting Time* dan *Turnaround Time*:

| Proses | Arrival | Burst Time | Finish Time (P1) | Finish Time (P2) | Finish Time (P3) | TAT (FT-Arrival) | WT (TAT-Burst) |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | P1 | 0 | 5 | 3 (sisa 2) | 14 (selesai) | - | 14 - 0 = 14 | 14 - 5 = 9  |
   | P2 | 1 | 3 | 6 (selesai) | - | - | 6 - 1 = 5 | 5 - 3 = 2 |
   | P3 | 2 | 8 | 9 (sisa 5) | 17 (sisa 2) | 22 | 22 - 2 = 20 | 20 - 8 = 12 |
   | P4 | 3 | 6 | 12 (sisa 3) | 20 (selesai) | - | 20 - 3 = 17 | 17 - 6 = 11 |
   | Total | | | | | | 56 | 34 |
   | Average | | | | | | 14 | 8,5 |
   
- Simulasi Gantt Chart untuk Round Robin (RR):
 
 ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   14   17   20   22
```

**Eksperimen 2 – Priority Scheduling (Non-Preemptive)**

- Urutan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi): P1 > P2 > P4 > P3

*(P1 dijalankan lebih dulu karena sistem non-preemptive dan datang di waktu 0/saat CPU kosong, meskipun P2 memiliki Priority lebih tinggi)*   
- Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
- Berikut tabel perhitungannya:

| Proses | Priority | Start | Arrival (A) | Burst (B) |  WT = Start − A |    TAT = WT + B |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|     P1 | 2 |     0 |           0 |         5 |               0 |   0 + 5 = 5 |
|     P2 | 1 |     5 |           1 |         3 |   5 − 1 = 4 |   4 + 3 = 7 |
|     P4 | 3 |     8 |           3 |         6 |   8 − 3 = 5 |  5 + 6 = 11 |
|     P3 | 4 |    14 |           2 |         8 | 14 − 2 = 12 | 12 + 8 = 20 |
| Total | | | | | 21 | 43 |
| Average | | | | | 5,25 | 10,75 |

- Simulasi Gantt Chart untuk Priority Scheduling:
```
     | P1 | P2 | P4 | P3 |
     0    5    8    14   22  
```

**Eksperimen 3 – Analisis Variasi Time Quantum**

Hasil eksperimen:
![alt text](./screenshots/RR%20(q=2,%20q=5).png)
- Tabel perhitungan untuk *Time Quantum (q)* = 2

| Proses | Arrival | Burst Time | Finish Time (P1) | Finish Time (P2) | Finish Time (P3) | Finish Time (P4) | TAT (FT-Arrival) | WT (TAT-Burst) |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | P1 | 0 | 5 | 2 (sisa 3) | 10 (sisa 1) | 16 (selesai) | - | 16 - 0 = 16 | 16 - 5 = 11 |
   | P2 | 1 | 3 | 4 (sisa 1) | 11 (selesai) | - | - | 11 - 1 = 10 | 10 - 3 = 7 |
   | P3 | 2 | 8 | 6 (sisa 6) | 13 (sisa 4) | 18 (sisa 2) | 22 | 22 - 2 = 20 | 20 - 8 = 12 |
   | P4 | 3 | 6 | 8 (sisa 4) | 15 (sisa 2) | 20 (selesai) | - | 20 - 3 = 17 | 17 - 6 = 11 |
   | Total | | | | | | | 63 | 41 |
   | Average | | | | | | | 15,75 | 10,25 |

- Gantt Chart untuk RR q=2
```
     | P1 | P2 | P3 | P4 | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    2    4    6    8   10    11   13   15   16   18   20   22
```

- Tabel perhitungan untuk *Time Quantum (q)* = 5

| Proses | Arrival | Burst Time | Finish Time (P1) | Finish Time (P2) | TAT (FT-Arrival) | WT (TAT-Burst) |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | P1 | 0 | 5 | 5 (selesai) | - | 5 - 0 = 5 | 5 - 5 = 0  |
   | P2 | 1 | 3 | 8 (selesai) | - | 8 - 1 = 7 | 7 - 3 = 4 |
   | P3 | 2 | 8 | 13 (sisa 3) | 21 | 21 - 2 = 19 | 19 - 8 = 11 |
   | P4 | 3 | 6 | 18 (sisa 1) | 22 | 22 - 3 = 19 | 19 - 6 = 13 |
   | Total | | | | | 50 | 28 |
   | Average | | | | | 12,5 | 7 |

- Gantt Chart untuk RR q=5
```
     | P1 | P2 | P3 | P4 | P3 | P4 |
     0    5    8    13   18   21   22 
```

- Tabel perbandingan efek *Quantum*:

| Metrik / Time Quantum                | Quantum = 2                                                                        | Quantum = 5                                                                                  | Analisis / Efek yang Terjadi                                                                                          |
| :---: | :---: | :---: | :---: |
| Rata-rata Waiting Time (WT)        | 10.25                                                                                  | 7.00                                                                                             | Ketika quantum lebih besar, waktu tunggu rata-rata menurun karena proses lebih jarang dipreempt.                          |
| Rata-rata Turnaround Time (TAT)    | 15.75                                                                                  | 12.50                                                                                            | Turnaround time menurun karena setiap proses dapat menyelesaikan lebih banyak instruksi setiap giliran CPU.               |
| Observasi Umum                       | Quantum kecil membuat sistem lebih adil terhadap proses pendek tetapi overhead tinggi. | Quantum besar membuat sistem lebih efisien untuk proses panjang, namun fairness sedikit menurun. |                                              -                                                                             |

**Eksperimen 4 – Perbandingan RR dan Priority**

- Berikut tabel perbandingan hasil RR (*q*=3) dan Priority:

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|:---:|:---:|:---:|:---:|:---:|
| RR | 8,5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
| Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

**Analisis Singkat**

Secara umum, Round Robin (RR) lebih unggul dalam keadilan dan respon cepat, karena setiap proses mendapat waktu eksekusi yang sama secara bergantian. Sementara itu, Priority Scheduling lebih fokus pada efisiensi, karena proses penting dijalankan lebih dulu.
Namun, performa RR sangat dipengaruhi oleh besar kecilnya time quantum kalau terlalu kecil, sistem jadi lambat karena sering berpindah proses; kalau terlalu besar, proses lain jadi menunggu lama. Sedangkan pada Priority, performa tergantung pada penetapan prioritas jika tidak seimbang, proses prioritas rendah bisa menunggu terlalu lama (starvation).

---

## Kesimpulan
Berdasarkan hasil eksperimen, algoritma Round Robin (RR) memberikan pembagian waktu yang lebih adil karena setiap proses mendapat giliran eksekusi secara bergantian sesuai time quantum. Metode ini cocok untuk sistem yang membutuhkan respon cepat dan adil bagi semua proses, meskipun efisiensinya tergantung pada besar kecilnya quantum.

Sementara itu, Priority Scheduling (PS) mengeksekusi proses berdasarkan tingkat kepentingan atau prioritasnya. Proses dengan prioritas tinggi akan diselesaikan lebih dulu, tetapi proses berprioritas rendah berpotensi mengalami penundaan lama (starvation). Secara keseluruhan, RR unggul dalam hal keadilan dan respon sistem, sedangkan PS lebih efisien untuk menangani proses yang memiliki tingkat kepentingan berbeda.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  
   **Jawaban:**  Perbedaan utama antara Round Robin dan Priority Scheduling ada pada cara keduanya memilih proses mana yang dijalankan lebih dulu. Pada Round Robin, setiap proses mendapat giliran waktu yang sama secara bergantian seperti antrian yang adil di loket. Tujuannya agar semua proses punya kesempatan jalan dan sistem terasa lebih responsif. Sedangkan Priority Scheduling memilih proses berdasarkan tingkat kepentingannya. Proses yang dianggap lebih penting (prioritas lebih tinggi) akan dijalankan duluan, meskipun ada proses lain yang datang lebih awal.
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  
   **Jawaban:**  Besarnya time quantum sangat berpengaruh terhadap performa sistem dalam algoritma Round Robin.Kalau time quantum terlalu kecil, proses akan sering bergantian sehingga sistem jadi sibuk melakukan context switching (perpindahan antar proses). Akibatnya, waktu CPU banyak terbuang hanya untuk pindah tugas, sistem terasa lambat dan boros waktu. Sebaliknya, kalau time quantum terlalu besar, proses pertama bisa berjalan terlalu lama sebelum proses lain mendapat giliran. Hal ini membuat sistem jadi kurang responsif, dan perilakunya hampir sama seperti FCFS.
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?  
   **Jawaban:**  Algoritma Priority Scheduling bisa menyebabkan *starvation* karena proses dengan prioritas rendah sering kali terus tertunda oleh proses yang prioritasnya lebih tinggi. Seperti pada anteran VIP, kalau terus-menerus datang orang dengan tiket prioritas, orang biasa di belakang mungkin tidak pernah dilayani. Dalam  hal ini berarti ada proses yang menunggu sangat lama, bahkan tidak sempat dijalankan sama sekali.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Bagi saya, yang paling menantang di minggu ini adalah perhitungan algoritma Round Robin.
- Bagaimana cara Anda mengatasinya?  
Mempelajari konsep dan cara kerja dari algoritma RR.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
