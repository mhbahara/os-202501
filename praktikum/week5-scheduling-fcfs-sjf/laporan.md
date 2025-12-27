
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Farhan Ramdhani  
- **NIM**   : 250202938  
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan. 

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

`Penjadwalan CPU` adalah mekanisme dalam sistem operasi untuk menentukan proses mana yang akan dieksekusi oleh CPU pada waktu tertentu. Tujuannya adalah memaksimalkan penggunaan CPU, mempercepat waktu respons, serta mengurangi waktu tunggu dan waktu penyelesaian proses.

Dua algoritma yang paling dasar dan sering dipakai untuk pembelajaran adalah `FCFS (First Come First Served)` dan `SJF (Shortest Job First).`

**1. FCFS (First Come First Served)**

***Pengertian :***

`FCFS` adalah algoritma penjadwalan paling sederhana. Proses yang datang lebih dulu, akan dilayani lebih dulu.

***Cara kerja :***

1. Proses ditempatkan pada antrean `(queue)`.
2. CPU mengeksekusi proses berdasarkan urutan kedatangan.
3. `Non preemptive` : kalau proses sudah berjalan, tidak bisa ditunda sampai selesai.

***Kelebihan :***
- Mudah diimplementasikan.
- Bersifat adil untuk semua proses `(first-come-first-served)`.
- Tidak perlu prediksi `burst time`.

***Kekurangan :***
- Rawan `convoy effect` : proses pendek harus menunggu proses panjang yang datang lebih dulu.
- Menambah waktu tunggu rata-rata jika variasi `burst time` besar.

**2. SJF (Shortest Job First)**

***Pengertian :***

`SJF` adalah algoritma yang memilih proses dengan waktu eksekusi `(burst time)` paling pendek di antara proses yang sudah tiba. Tujuan utamanya adalah meminimalkan waktu tunggu rata-rata. Ada dua versi `SJF`, yaitu :
1. `Non preemptive` : proses yang sudah mulai tidak bisa dihentikan.
2. `Preemptive` (Shortest Remaining Time First) : bisa dipotong jika ada proses dengan `burst` lebih pendek yang tiba.

***Cara kerja :***

1. CPU memilih proses yang `burst time`-nya paling kecil.
2. ika ada beberapa proses datang di waktu berbeda, pemilihan hanya dari yang sudah tiba.

***Kelebihan :***

- Terbukti menghasilkan waktu tunggu rata-rata paling kecil.
- Efisien saat banyak proses pendek.

***Kekurangan :***

- Membutuhkan estimasi `burst time` yang akurat.
- Bisa terjadi `starvation` untuk proses panjang jika terus muncul proses pendek.
- Tidak selalu cocok untuk sistem interaktif.

**3. Parameter Penting dalam Penjadwalan**

***1. Waiting Time (WT)***

Yaitu lama waktu proses menunggu di antrean sebelum dieksekusi.

Rumus :

```
WT = Start\ Time - Arrival\ Time
```

***2. Turnaround Time (TAT)***

Yaitu total waktu sejak proses datang hingga selesai.

Rumus :

```
TAT = Finish\ Time - Arrival\ Time
```

---

## Langkah Praktikum
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

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:

     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
   
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24

### 1. Hasil perhitungan : ###

*A. FCFS*
- Rata-rata Waiting Time (WT) = 8,75
- Rata-rata Turnaround Time (TAT) = 14,75

*B. SJF (non preemptive)*
- Rata-rata Waiting Time (WT) = 6,25
- Rata-rata Turnaround Time (TAT) = 12,25

### 2. Perbandingan singkat : ###
- SJF menurunkan `WT` sebesar = 28,6% (dari 8,75 menjadi 6,25).
- SJF juga menurunkan `TAT` sebesar = 17,0% (dari 14,75 menjadi 12,25).

### 3. Keunggulan : ###

*A. SJF unggul ketika :*
- Ada variasi durasi job `(burst)` yang cukup besar. Job pendek bisa diselipkan dulu sehingga antrian tidak mengular.
- Pola kedatangan relatif tenang atau dapat diprediksi (estimasi `burst` cukup akurat).


*B. FCFS unggul / lebih cocok ketika :*
- Butuh kesederhanaan & keadilan (masuk duluan, dilayani duluan).
- Durasi job relatif mirip, sehingga efek `konvoi` kecil 
- Informasi / estimasi `burst` tidak tersedia atau tidak bisa diandalkan.
- Ingin perilaku mudah diprediksi tanpa risiko `starving` job panjang.

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![alt text](../week5-scheduling-fcfs-sjf/screenshots/Screenshot%202025-11-03%20220954.png)

---

## Analisis
### 1. Jelaskan makna hasil percobaan.  
Algoritma `SJF` memberikan `waiting time` dan `turnaround time` yang lebih rendah dibanding `FCFS`. Hal ini menunjukkan bahwa urutan penjadwalan sangat memengaruhi efisiensi eksekusi proses.
### 2. Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
Dari hasil percobaan saya, sejalan dengan teori :
- `FCFS` : sederhana, adil, tetapi tidak optimal.
- `SJF` : optimal secara matematis, tetapi membutuhkan estimasi `burst time`.
### 3. Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows) ?  Waktu eksekusi proses bisa berbeda walaupun algoritma perhitungan teorinya sama.
Linux cenderung lebih stabil dan presisi untuk eksperimen akademik.
Windows lebih agresif dalam boosting prioritas proses interaktif, sehingga hasil simulasi bisa sedikit berbeda jika dijalankan secara nyata.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

1. Algoritma `SJF` memberikan rata-rata `waiting time` dan `turnaround time` yang lebih efisien dibanding `FCFS`, terutama ketika variasi `burst time` besar.
2. `FCFS` tetap berguna untuk sistem yang membutuhkan kesederhanaan dan keadilan, tetapi performanya kurang optimal untuk job panjang.
3. Pemilihan algoritma penjadwalan sangat dipengaruhi kebutuhan sistem.

---

## Tugas

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| `FCFS` | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
| `SJF` | 6,25 | 12,25 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF ?  
   **Jawaban :** `FCFS` memproses sesuai urutan kedatangan, sedangkan `SJF` memilih proses dengan `burst time` paling pendek di antara yang sudah tiba.

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum ?  
   **Jawaban :** Karena proses yang durasinya pendek diprioritaskan, sehingga proses tidak menumpuk dan waktu tunggu rata-rata seluruh proses menjadi lebih kecil.


3. Apa kelemahan SJF jika diterapkan pada sistem interaktif ?  
   **Jawaban :** 
- Sulit memprediksi `burst time` secara akurat.
- Risiko `starvation` pada proses panjang.
- Proses panjang terasa diabaikan, sehingga kurang cocok untuk interaksi pengguna real time.

---

## Refleksi Diri
Tuliskan secara singkat:

1. Apa bagian yang paling menantang minggu ini? 

Memahami cara mengerjakan tugasya, seperti membuat rumus untuk eksperimen  

2. Bagaimana cara Anda mengatasinya?  

Saya coba memahami langkah-langkahnya dulu dari teori, lalu membuat tabel perhitungan di `Excel`. Setelah itu saya bandingkan hasilnya dengan teori agar lebih yakin bahwa perhitungannya benar.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
