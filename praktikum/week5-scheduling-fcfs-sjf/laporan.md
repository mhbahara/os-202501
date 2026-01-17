
# Laporan Praktikum Minggu [X]
## Algoritma penjadwalan CPU (CPU Scheduling) menggunakan dua pendekatan dasar:

- FCFS (First Come First Served)
- SJF (Shortest Job First)


---

## Identitas
- **Nama**  : [Miftakhul Lisna Esa Baehaqi]  
- **NIM**   : [250202951]  
- **Kelas** : [1IKRB]

---

## Tujuan
1. Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.
.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari algoritma penjadwalan CPU (CPU Scheduling) menggunakan dua pendekatan dasar:

- FCFS (First Come First Served)
- SJF (Shortest Job First)
  
Tujuan utamanya adalah memahami bagaimana sistem operasi menentukan urutan eksekusi proses, serta bagaimana waiting time dan turnaround time memengaruhi performa sistem.

Mahasiswa akan melakukan simulasi dan perbandingan hasil perhitungan kedua algoritma ini menggunakan tabel observasi manual atau spreadsheet (Excel/Google Sheets) tanpa perlu melakukan instalasi atau pemrograman tambahan.



---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

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
![Screenshot hasil](./screenshots/hasil%20eksekusi.png)

---
## Eksperimen 1 – FCFS (First Come First Served)
Urutkan proses berdasarkan Arrival Time: P1 -> P2 -> P3 -> P4
- tabel perhitungan fcfs
  ![hasil eksperimen 1](./screenshots/eksperimen%201%20fcfs.png)

  Avg WT = 35 / 4 = 8.75 (langkah pembagian: 35 ÷ 4 = 8 sisa 3 → 3/4 = 0.75 → 8.75)
Jumlah TAT: 6 + 13 + 19 + 21 =

6 + 13 = 19

19 + 19 = 38

38 + 21 = 59

Avg TAT = 59 / 4 = 14.75 (59 ÷ 4 = 14 sisa 3 → 3/4 = 0.75 → 14.75)

Gantt Chart:
| P1 | P2 | P3 | P4 |
0 6 14 21 24

## Eksperimen 2 – SJF (Shortest Job First)
Urutkan proses berdasarkan Burst Time terpendek (dengan memperhatikan waktu kedatangan): P1 -> P4 -> P3 -> P2

Tabel Perhitungan SJF
![eksekusi 2](./screenshots/ekperimen%202%20sjf.png)

Jumlah WT: 0 + 3 + 7 + 15 = 25 → Avg WT = 25 / 4 = 6.25

Jumlah TAT: 6 + 6 + 14 + 23 = 49 → Avg TAT = 49 / 4 = 12.25

Gantt Chart:
| P1 | P4 | P3 | P2 |
0 6 9 16 24

## Perbandingan Hasil FCFS dan SJF

|            **Algoritma**           | **Avg Waiting Time (WT)** | **Avg Turnaround Time (TAT)** | **Kelebihan**                                                               | **Kekurangan**                                                                     |
| :--------------------------------: | :-----------------------: | :---------------------------: | :-------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| **FCFS** (First Come First Served) |            8.75           |             14.75             | Sederhana dan mudah diimplementasikan                                       | Tidak efisien bila proses panjang datang lebih dulu (*convoy effect*)              |
|      **SJF (Non-Preemptive)**      |            6.25           |             12.25             | Menurunkan rata-rata waktu tunggu dan turnaround (efisien untuk job pendek) | Dapat menyebabkan *starvation* pada proses panjang; memerlukan estimasi burst time |


---

## Analisis
1. Rata-rata Waiting Time (WT):

- Pada FCFS, rata-rata WT = 8.75,
-  sedangkan pada SJF, rata-rata WT = 6.25.

Artinya, SJF lebih efisien karena total waktu tunggu rata-rata lebih rendah 2.5 satuan waktu dibanding FCFS.

Hal ini terjadi karena SJF mengeksekusi proses dengan burst time paling pendek lebih dulu, sehingga proses-proses kecil cepat selesai tanpa menunggu proses besar.

Rata-rata Turnaround Time (TAT):

FCFS menghasilkan TAT rata-rata 14.75, sedangkan SJF hanya 12.25.

Ini menunjukkan SJF lebih cepat menyelesaikan seluruh proses (secara rata-rata).

Kesimpulan Performa:

SJF unggul dalam hal efisiensi waktu karena:

- Mengurangi waktu tunggu dan waktu total penyelesaian.

- Lebih optimal untuk beban kerja dengan variasi durasi proses.

FCFS cocok untuk sistem yang adil dan sederhana, tetapi kurang efisien jika terdapat proses dengan burst time yang sangat panjang di awal (menyebabkan convoy effect).

- Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya. 
  
  1. Kondisi SJF Lebih Unggul dari FCFS

Algoritma SJF (Shortest Job First) lebih unggul ketika sistem memiliki banyak proses dengan durasi eksekusi yang bervariasi, terutama jika terdapat banyak proses pendek.

Kondisi unggulnya SJF:

Sebagian besar proses memiliki burst time pendek.

→ Karena SJF mengeksekusi proses dengan waktu terpendek lebih dulu, total waktu tunggu (WT) dan waktu penyelesaian (TAT) jadi lebih kecil.

Beban kerja bersifat batch (non-interaktif).

→ Misalnya, dalam sistem pemrosesan data atau komputasi ilmiah, di mana tidak perlu respon cepat untuk setiap pengguna.

Tujuan sistem adalah efisiensi throughput.

→ SJF mengoptimalkan rata-rata waktu penyelesaian, sehingga CPU lebih efisien digunakan. 

- Tidak ada algoritma yang selalu terbaik di semua situasi.
SJF unggul dalam efisiensi, sedangkan FCFS unggul dalam keadilan.


---

## Kesimpulan
Kesimpulan

Dari hasil percobaan dan analisis algoritma penjadwalan CPU menggunakan FCFS (First Come First Served) dan SJF (Shortest Job First), dapat disimpulkan bahwa:

1. SJF menghasilkan rata-rata waktu tunggu (Waiting Time) dan waktu penyelesaian (Turnaround Time) yang lebih kecil dibandingkan FCFS, terutama ketika proses memiliki burst time yang bervariasi.

2. FCFS lebih unggul dari sisi kesederhanaan dan keadilan, karena proses dieksekusi berdasarkan urutan kedatangan tanpa diskriminasi.

3. SJF lebih efisien digunakan pada sistem batch processing atau pekerjaan dengan durasi pendek, sedangkan FCFS lebih sesuai untuk sistem interaktif atau multi-user agar tidak terjadi starvation.

4. Pemilihan algoritma harus disesuaikan dengan tujuan sistem operasi — apakah lebih mengutamakan efisiensi waktu atau keadilan eksekusi.

## Kesimpulan akhir:

Tidak ada algoritma yang selalu terbaik di semua situasi.
SJF unggul dalam efisiensi, sedangkan FCFS unggul dalam keadilan.

---

## Quiz
1. [Apa perbedaan utama antara FCFS dan SJF?
]  
   **Jawaban:**   FCFS menjadwalkan berdasarkan urutan kedatangan proses. SJF memilih proses dengan burst time terpendek (di antara proses yang sudah tiba).

2. [Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum]  
   **Jawaban:** Karena SJF mengeksekusi proses berukuran kecil terlebih dahulu sehingga mengurangi akumulasi waktu tunggu untuk banyak proses — proses kecil tidak menunggu lama di belakang proses panjang. 
3. [Apa kelemahan SJF jika diterapkan pada sistem interaktif]  
   **Jawaban:**  SJF dapat menyebabkan starvation (penundaan berkepanjangan) pada proses panjang jika proses pendek terus datang; juga memerlukan estimasi burst yang tidak selalu akurat.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  hemmm mungkin karena banyak tugas yang berbarengan jadi cukup lama utuk mengumpulkan mood untuk tugas ini
- Bagaimana cara Anda mengatasinya?  
  shalat dan meminta pertolongan kepada allah

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
