# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU  


---

## Identitas
- **Nama**  : Faiq Atha Rulloh
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---
## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan **mengimplementasikan program simulasi sederhana algoritma penjadwalan CPU**, khususnya **FCFS atau SJF**. 

Berbeda dengan Minggu 5–6 yang berfokus pada perhitungan manual, pada minggu ini mahasiswa mulai **mengotomatisasi perhitungan menggunakan program**, menjalankan dataset uji, serta menyajikan hasil dalam bentuk tabel atau grafik. 

_Praktikum ini menjadi jembatan antara **pemahaman konseptual** dan **implementasi komputasional** algoritma sistem operasi._

---

## Tujuan
1. Membuat program simulasi algoritma penjadwalan FCFS atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
1. First-Come, First-Served (FCFS) = algoritma ini bekerja dengan prinsip antrean. Proses yang pertama kali meminta jatah waktu CPU akan dilayani terlebih dahulu.
2. Shortest Job First (SJF) = Algoritma ini memprioritaskan proses yang memiliki waktu pengerjaan (burst time) terkecil.
3. Arrival Time (AT) = Waktu Kedatangan adalah waktu di mana sebuah proses masuk ke dalam antrean dan siap untuk dikerjakan oleh CPU.
4. Burst Time (BT) = Waktu Eksekusi adalah total waktu yang dibutuhkan oleh sebuah proses untuk diselesaikan oleh CPU.
5. Turnaround Time (TAT) – Waktu Total di Sistem adalah total waktu yang dihabiskan oleh suatu proses sejak ia datang sampai ia benar-benar selesai dikerjakan.
6. Waiting Time, yaitu jumlah waktu yang dihabiskan proses hanya untuk menunggu di antrean sebelum akhirnya dilayani CPU.

---

## Kode / Perintah
```bash
def main():
    # ---  DATASET  ---
    proses_list = [
        {'id': 'P1', 'arrival': 0, 'burst': 6},
        {'id': 'P2', 'arrival': 1, 'burst': 8},
        {'id': 'P3', 'arrival': 2, 'burst': 7},
        {'id': 'P4', 'arrival': 3, 'burst': 3}
    ]

    # --- 2. LOGIKA FCFS (First-Come First-Served) ---
    # Urutkan berdasarkan waktu datang (Arrival Time) biar aman
    proses_list.sort(key=lambda x: x['arrival'])

    waktu_sekarang = 0
    total_waiting = 0
    total_turnaround = 0

    print("\n=== SIMULASI CPU SCHEDULING (FCFS) ===")
    print(f"{'Proses':<8} {'Arrival':<8} {'Burst':<8} {'Waiting':<8} {'Turnaround':<10}")
    print("-" * 50)

    for p in proses_list:
        # Cek apakah CPU harus menunggu proses datang (Idle time)
        if waktu_sekarang < p['arrival']:
            waktu_sekarang = p['arrival']

        # Proses dimulai & selesai
        start_time = waktu_sekarang
        finish_time = start_time + p['burst']

        # Hitung Metrics
        turnaround = finish_time - p['arrival']
        waiting = turnaround - p['burst']

        # Akumulasi untuk rata-rata
        total_waiting += waiting
        total_turnaround += turnaround
        
        # Update waktu sistem
        waktu_sekarang = finish_time

        # Tampilkan baris data
        print(f"{p['id']:<8} {p['arrival']:<8} {p['burst']:<8} {waiting:<8} {turnaround:<10}")

    # --- 3. HASIL AKHIR ---
    rata_waiting = total_waiting / len(proses_list)
    rata_turnaround = total_turnaround / len(proses_list)

    print("-" * 50)
    print(f"Rata-rata Waiting Time    : {rata_waiting:.2f} ms")
    print(f"Rata-rata Turnaround Time : {rata_turnaround:.2f} ms")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
```
---

 - **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  &#10003;
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  &#10003;
   - Menampilkan hasil dalam tabel. &#10003;

 - **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.   &#10003;
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.   &#10003;
   - Simpan hasil eksekusi (screenshot). &#10003;

---

## Hasil Eksekusi

![Hasil Eksperimen ](<screenshots/Eksperimen_Hasil_Simulasi_FCFS_Week_9.png>)

---

## Analisis

   - Jelaskan alur program.  
```bash
1. Mulai program.
2. Siapkan data proses (ID, arrival time, burst time).
3. Urutkan proses berdasarkan arrival time.
4. Set waktu CPU awal = 0.
5. Ulangi untuk setiap proses:
   * Jika waktu CPU < arrival time, set waktu CPU = arrival time.
   * Jalankan proses sesuai burst time.
   * Hitung turnaround time.
   * Hitung waiting time.
   * Perbarui waktu CPU.
6. Simpan total waiting time dan turnaround time.
7. Hitung rata-rata waiting time.
8. Hitung rata-rata turnaround time.
9. Tampilkan hasil simulasi.
10. Selesai.
```

- Bandingkan hasil simulasi dengan perhitungan manual.  
   - Perhitungan manual :
- ![Screenshot hasil](<screenshots/Eksperimen_PerhitunganManual FCFS_Week_5.png>)

|     Proses    | Burst Time | Arrival Time | Start |  Waiting | Turnaround | Finish |
| :-----------: | :--------: | :----------: | :---: | :------: | :--------: | :----: |
|       P1      |      6     |       0      |   0   |     0    |      6     |    6   |
|       P2      |      8     |       1      |   6   |     5    |     13     |   14   |
|       P3      |      7     |       2      |   14  |    12    |     19     |   21   |
|       P4      |      3     |       3      |   21  |    18    |     21     |   24   |
| **Rata-rata** |            |              |       | **8.75** |  **14.75** |        |
 - FCFS
     - Waiting Time    : 8,75
     - Turnaround time : 14,75
- Sementara hasil simulasi yaang menggunakan program :
- ![Screenshot hasil](<screenshots/Eksperimen_Tabel_Program_FCFS.png>)
- FCFS
     - Waiting Time    : 8,75
     - Turnaround time : 14,75

- Jelaskan kelebihan dan keterbatasan simulasi.
   - Kelebihan dari simulasi programnya adalah:
      - Sederhana
      - Adil maksudnya Proses dilayani berdasarkan urutan kedatangan.
   - Keterbatasan dari simulasi programnya adalah:
      - Tidak Mempedulikan Efisiensi maksudnya hanya melihat siapa yang datang duluan, bukan siapa yang paling cepat selesai.
       
---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
   - Karena yang pertama menghindari risiko kerusakan system, yang kedua memprediksi performa, yang ketiga mempermudah pembuatan Gantt Chart.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
   - perbandingannya adalah Waktu pengerjaannya yang manual (lama), sedangkan hasil simulasi Waktu pengerjaanya lebih cepat.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
   - Tergantung seseorangnya misalkan ingin membuat penjadwalan sederhana tanpa memikirkan efisiensi Waktu tunggu FCFS adalah pilihannya; jika ingin mengejar performa system optimal dan tidak keberatan dengan kode yang lebih rumit SJF adalah jawabannya.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
   - menentukan siapa yang berjalan? Ketika ada dua proses yang dating di Waktu yang hampir bersamaan.
- Bagaimana cara Anda mengatasinya? 
   - jika ada dua proses yang datang hampir bersamaan, lihat siapa yang tercatat satu milidetik lebih awal.


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
