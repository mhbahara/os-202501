
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
**Eksperimen 1 - FCFS (First Come First Served)**

Proses berdasarkan urutan kedatangan (Arrival Time).Urutan eksekusi dari P1 -> P2 -> P3 -> P4 
Proses| 	Burst Time|	Arivval Time| 	Start Time|	Finish Time|	Waiting Time|	Turnaround Time|
|:---|:---|:---|:---|:---|:---|:---|
P1|	6|	0|	0|	6|	0|	6|
P2|	8|	1|	6|	14|	5|	13|
P3|	7|	2|	14|	21|	12|	19|
P4|	3|	3|	21|	24|	18|	21|
Total|||||					35|	59|
Average|||||					8,75|	14,75|

**Eksperimen 2 - SJF (Shortest Job First)**

Proses berdasarkan Burst Time terpendek (dengan memperhatikan waktu kedatangan).Urutan eksekusi dari P1-> P4 -> P3 -> P2

Proses| 	arrival  time|	burst Time| 	Start Time|	Finish Time|	Waiting Time|	Turnaround Time|
|:---|:---|:---|:---|:---|:---|:---|
P1|	0|	6|	0|	6|	0|	6|
P2|	3|	3|	6|	9|	3|	6|
P3|	2|	7|	9|	16|	7|	14|
P4|	1|	8|	16|	24|	15|	23|
Total|||||					25|	49|
Average|||||					6,25|	12,25|

**Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**

1.Bandingkan hasil FCFS dan SJF pada tabel berikut:
Algoritma|	Avg Waiting Time|	Avg Turnaround Time|	Kelebihan|	Kekurangan|
|:---|:---|:---|:---|:---|
FCFS|8,75	|14,75	|Sederhana dan mudah diterapkan|	Tidak efisien untuk proses panjang|
SJF|6,25|	12,25|Optimal untuk job pendek|	Menyebabkan starvation pada job panjang|

2.Kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya?

SJF(Shortest Job First) lebih unggul dari FCFS(First Come First Served) ketika durasi  proses diketahui sebelumnya dan terdapat perbedaan besar dalam waktu eksekusi proses.SJF mengutamakan proses dengan waktu pengerjaan paling cepat sehingga dapat menurunkan rata-rata waktu tunggu dan total penyelesaia proses menjadi lebih efisien untuk sistem yang berbeda-beda.Sementara FCFS(First Come First Served) lebih dari SJF(Shortest Job First) ketika sistem membutuhkan kemudahan dan keadilan dalam urutan proses ,FCFS melakukan proses sesuai urutan datang ,jadi yang dulu pasti akan dilayani dulu tanpa resiko ada yang tidak dilayani.



---

## Kesimpulan
Algoritma FCFS melayani proses sesuai urutan kedatangan, sehingga implementasinya sederhana dan adil karena tidak memprioritasikan proses tertentu.Dan kekurangan dari algoritma tersebut ialah dapat menyebabkan waktu yang cukup lama  terutama ketika proses dengan waktu pengerjaan  panjang datang lebih dulu  ,sehingga proses lain harus nunggu lebih lama.

Algoritma SJF proses dengan waktu eksekusi paling singkat didahulukan, yang membuat rata-rata waktu tunggu lebih kecil.Namun,walaupun SJF efektif untuk meningkatkan efisien CPU dan mengurangi waktu tunggu,algortima ini bisa tertunda dengan waktu yang lama jika ada proses pendek yang terus datang.

Pemilihanan antara FCFS dan SJF disesuaikan sesuai dengan kebutuhan sistem dan karakteristik beban kerja agar kinerja sistem dapat maksimal.FCFS dipilih untuk sistem yang mengutamakan kepentingan dan keadilan sedangkan SJF dipilih untuk sistem yang menuntut optimasi waktu tunggu dan efisen. 


---
#Tugas

1.Hitung waiting time dan turnaround time dari minimal 2 skenario FCFS dan SJF.

**Skenario 1 - FCFS (First Come First Served)**

|Proses|Burst Time|Arivval Time|Start Time|Finish Time|Waiting Time|Turnaround Time|
|:---|:---|:---|:---|:---|:---|:---|
P1|	5|	0|	0|	5|	0|	5|
P2|	7|	1|	5|	12|	4|	11|
P3|	6|	2|	12|	18|	10|	16|
P4|	2|	3|	18|	20|	15|	17|
Total||||					|29|	49|
Average||||					|7,25|	12,25|

**Skenario 1 - SFJ (Shortest Job First)**
Proses| 	Arrival  time|	Burst Time| 	Start Time|	Finish Time|	Waiting Time|	Turnaround Time|
|:---|:---|:---|:---|:---|:---|:---|
P1|	0|	5|	0|	5|	0|	5|
P2|	3|	2|	5|	7|	2|	4|
P3|	2|	6|	7|	13|	5|	11|
P4|	1|	7|	13|	20|	12|	19|
Total|||||					19|	39|
average|||||					4,75|	9,75|

**Skenario 2 - FCFS (First Come First Served)**

|Proses| Burst Time|	Arivval Time| Start Time|Finish Time|Waiting Time|Turnaround Time|
|:---|:---|:---|:---|:---|:---|:---|
P1|	8|	0|	0|	8|	0|	8|
P2|	6|	1|	8|	14|	7|	13|
P3|	4|	2|	14|	18|	12|	16|
P4|	3|	3|	18|	21|	15|	12|
Total|||||					34|	49|
average|||||					8,5|	12,25|

**Skenario 2 - SFJ (Shortest Job First)**
Proses| 	arrival  time|	burst Time| 	Start Time|	Finish Time|	Waiting Time|	Turnaround Time|
|:---|:---|:---|:---|:---|:---|:---|
P1|	0|	8|	0|	8|	0|	8|
P2|	3|	3|	8|	11|	5|	8|
P3|	2|	4|	11|	15|	9|	13|
P4|	1|	6|	15|	21|	14|	20|
Total|||||					28|	49|
average|||||					7|	12,25|


2.Analisis kelebihan dan kelemahan tiap algoritma.
Algoritma |Kelebihan |Kelemahan|
|:---|:---|:---|
FCFS(First Come First Served)|Sederhana dan mudah diterapkan,setiap proses mendapat giliran sesuai urutan kedatangan/adil secara urutan dan cocok digunakan untuk sistem batch yang tidak dibutuhkan waktu respon cepat|Dapat menimbulkan efek konvoi(convoy effect) ketika proses yang  membutuhkan waktu lama akan dieksekusi terlebih dahulu dan menyebabkan proses lain menunggu terlalu lama dan algortitma ini tidak cocok untuk sistem interaktif/real-time karena tidak memperhatikan prioritas tugas|
SFJ (Shortest Job First)|Waktu tunggu rata-rata paling rendah jika proses dengan waktu eksekusi paling singkat diketahui dan akan dikerjakan terlebih dahulu,sehingga sistem menjadi lebih efisien,dapat meningkatkan throughput(jumlah proses selesai lebih cepat) karena proses kecil dikerjakan terlebih dahulu|Membutuhkan perkiraan waktu proes yang sulit didapat dan dapat menyebabkan travation yaitu proses dengan waktu eksekusi panjang tidak pernah dikerjakan karena selalu ada proses pendek yang datang dulu|
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
   Saya merasa  bingung ketika menentukan  waktu mulai (Start Time) dan waktu selesai (Finish Time) disetiap proses,karena harus teliti dengan urutan kedatangan dan waktu eksekusi proses sebelumnya agar perhitungan benar dan sesuai.
- Bagaimana cara Anda mengatasinya?
  Saya mecari materi tambahan terkait FCFS dan SJF di internet untuk memperdalam pengetahuan terhadapan  penyelesain perhituungan waktu mulai (Start Time) dan waktu selesai (Finish Time).

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
