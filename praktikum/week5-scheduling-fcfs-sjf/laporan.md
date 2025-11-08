
# Laporan Praktikum Minggu [X]
Topik:  Penjadwalan CPU – FCFS dan SJF
---

## Identitas
- **Nama**  : Novia Safitri
- **NIM**   : 25020923
- **Kelas** : 1IKRA
---

## Tujuan
1.Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.

2.Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.

3.Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.

4.Menjelaskan kelebihan dan kekurangan masing-masing algoritma.

5.Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.


---

## Dasar Teori
Penjadwalan CPU adalah cara mengatur proses yang ingin menggunakan CPU agar bisa berjalan dengan efisien dan tidak saling menunggu terlalu lama. FCFS (First Come, First Served) adalah metode paling sederhana yang menjalankan proses sesuai urutan kedatangannya, jadi proses yang datang duluan akan dikerjakan duluan tanpa jeda. Walaupun mudah, metode ini kadang membuat proses yang cepat harus menunggu lama jika berada di belakang proses yang lama.SJF (Shortest Job First) memilih proses yang waktu kerjanya paling singkat untuk dikerjakan duluan, sehingga rata-rata waktu tunggu menjadi lebih kecil dan hasilnya lebih efisien. Ada dua jenis SJF: yang tidak bisa dihentikan sampai selesai dan yang bisa diganti jika ada proses baru yang lebih singkat. Meskipun SJF bagus untuk mengurangi waktu tunggu, metode ini memerlukan perkiraan waktu proses dan bisa menyebabkan proses lama terus tertunda jika banyak proses cepat yang datang terus-menerus.

---

## Langkah Praktikum
1.Siapkan Data Proses Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):

|Proses|	Burst Time|	Arrival Time|
|:---|:---|:---|
P1|6|	0|
P2|	8|	1|
P3|	7|	2|
P4|	3|	3|

2.Eksperimen 1 – FCFS (First Come First Served)

Urutkan proses berdasarkan Arrival Time.
Hitung nilai berikut untuk tiap proses:

    Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
    Turnaround Time (TAT) = WT + Burst Time
Hitung rata-rata Waiting Time dan Turnaround Time.
Buat Gantt Chart sederhana:

    | P1 | P2 | P3 | P4 |
    0    6    14   21   24


3.Eksperimen 2 – SJF (Shortest Job First)

Urutkan proses berdasarkan Burst Time terpendek (dengan memperhatikan waktu kedatangan).

Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.

Bandingkan hasil FCFS dan SJF pada tabel berikut:

|Algoritma|	Avg Waiting Time|	Avg Turnaround Time|	Kelebihan|	Kekurangan|
|:---|:---|:---|:---|:---|
FCFS|	...	|...|	Sederhana dan mudah diterapkan|	Tidak efisien untuk proses panjang|
SJF|	...|	...|	Optimal untuk job pendek|	Menyebabkan starvation pada job panjang|

4.Eksperimen 3 – Visualisasi Spreadsheet (Opsional)

Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
Gunakan formula dasar penjumlahan/subtraksi.
Screenshot hasil perhitungan dan simpan di:

    praktikum/week5-scheduling-fcfs-sjf/screenshots/

5.Analisis

Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.


Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.

6.Commit & Push

    git add .
    git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
    git push origin main
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
Turnaround Time (TAT) = WT + Burst Time
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt text](<screenshots/Screenshot 2025-11-08 062311.png>)


---

## Analisis
-Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.
Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.



---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
---
#Tugas
1.Hitung waiting time dan turnaround time dari minimal 2 skenario FCFS dan SJF.
2.Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).
3.Analisis kelebihan dan kelemahan tiap algoritma.
---
## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?

   Jawaban: FCFS (First Come First Served) adalah metode penjadwalan yang mengeksekusi proses sesuai urutan kedatangan tanpa gangguan, tetapi bisa menyebabkan proses pendek menunggu lama jika di depan ada proses panjang (efek konvoi).Sedangkan SJF (Shortest Job First) adalah proses dengan waktu pengerjaan paling singkat untuk dieksekusi duluan, sehingga rata-rata waktu tunggu lebih rendah  dan sistem lebih efisien, tapi butuh perkiraan lama proses dan berisiko proses panjang tertunda terus (starvation

2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?

Jawaban:SJF dapat menghasilkan rata-rata waktu tunggu minimum karena selalu memilih proses dengan waktu pengerjaan paling singkat untuk dikerjakan terlebih dahulu.Untuk mengurangi waktu tunggu proses yang pendek dengan tidak membiarkannya menunggu di belakang proses yang panjang, sehingga total waktu tunggu seluruh proses menjadi lebih sedikit. 

3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?
Jawaban:Kelemahan SJF (Shortest Job First) jika diterapkan pada sistem interaktif yaitu jika diterapkan pada sistem interaktif,sulit memprediksi burst time proses yang akan dieksekusi selanjutnya sehingga menjadikannya kurang cocok untuk sistem waktu nyata yang membutuhkan respon cepat.Selain itu, SJF dapat menyebabkan starvation pada proses yang memiliki waktu eksekusi lebih panjang karena selalu memprioritaskan proses dengan waktu terpendek, kondisi ini juga menghasilkan waktu tanggap yang kurang memadai bagi proses interaktif karena proses dieksekusi sampai selesai tanpa interupsi.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
