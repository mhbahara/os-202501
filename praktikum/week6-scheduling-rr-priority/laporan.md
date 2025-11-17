
# Laporan Praktikum Minggu 6
Topik:Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling
---

## Identitas
- **Nama**  : NOVIA SAFITRI 
- **NIM**   : 250202923
- **Kelas** : 1IKRA

---

## Tujuan

1.Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.

2.Menyusun tabel hasil perhitungan dengan benar dan sistematis.

3.Membandingkan performa algoritma RR dan Priority.

4.Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.

5.Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.

---

## Dasar Teori
 Round Robin (RR) adalah algoritma  penjadwalan CPU yang bekerja sama  memberi setiap proses waktu CPU secara bergiliran dalam interval yang sama yang disebut time quantum. Jika waktu proses habis sebelum selesai, proses tersebut dikembalikan ke antrian belakang untuk menunggu giliran berikutnya. Algoritma ini adil dan mencegah starvation karena semua proses mendapat kesempatan yang sama, namun memiliki trade-off antara respons cepat dan overhead context switching jika time quantum terlalu kecil.

Priority Scheduling memberi CPU pada proses berdasarkan prioritasnya, di mana proses dengan prioritas tertinggi dijalankan terlebih dahulu. Algoritma ini bisa preemptive atau non-preemptive dan berisiko membuat proses prioritas rendah menunggu lama (starvation), biasanya diatasi dengan metode aging untuk menaikkan prioritas seiring waktu. Pendekatan ini efektif untuk sistem yang memerlukan pengutamaan proses tertentu.

---

## Langkah Praktikum
1.Siapkan Data Proses Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):

|Proses|Burst Time|	Arrival Time|	Priority|
|:---|:---|:---|:---|
P1|	5|	0|2|
P2	|3	|1|	1|
P3|	8|	2|	4|
P4|	6|	3	|3|

2.Eksperimen 1 – Round Robin (RR)

  Gunakan time quantum (q) = 3.

  Hitung waiting time dan turnaround time untuk tiap proses.

  Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).
     
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
Catat sisa burst time tiap putaran.

3.Eksperimen 2 – Priority Scheduling (Non-Preemptive)

Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).

Lakukan perhitungan manual untuk:

    WT[i] = waktu mulai eksekusi - Arrival[i]
    TAT[i] = WT[i] + Burst[i]

Buat tabel perbandingan hasil RR dan Priority.

4.Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)

Ubah quantum menjadi 2 dan 5.

Amati perubahan nilai rata-rata waiting time dan turnaround time.

Buat tabel perbandingan efek quantum.

5.Eksperimen 4 – Dokumentasi

Simpan semua hasil tabel dan screenshot ke:

    praktikum/week6-scheduling-rr-priority/screenshots/
Buat tabel perbandingan seperti berikut:

|Algoritma	|Avg Waiting Time	|Avg Turnaround Time|	Kelebihan|	Kekurangan|
|:---|:---|:---|:---|:---|
RR|	...|	...|	Adil terhadap semua proses|	Tidak efisien jika quantum tidak tepat|
Priority	|...|	...|	Efisien untuk proses penting|	Potensi starvation pada prioritas rendah|

6.Commit & Push

    git add .
    git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
    git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
WT[i] = waktu mulai eksekusi - Arrival[i]
    TAT[i] = WT[i] + Burst[i]
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![alt textl](<screenshots/Screenshot 2025-11-17 180821.png>)

**Ekspeerimen 1 - Round Robin (RR)**
|Proses |	Burst Time	|Aririval Time|	Finish Time P1|	Finish Time P2|	Finish Time P3|	     TAT(FT - AT) |    WT (TAT - BT)|
|:---|:---|:---|:---|:---|:---|:---|:---|
P1|	5|	0|	3(sisa 2)|	14(sisa 2)|	-| 14-O=14	|14-5=9|
P2|	3|	1|	6(selesai)|	-|	-|	6-1=5|	5-3=2|
P3|	8|	2|	9(sisa 5)	|17(sisa 2)	|22(selesai)|	22-2=20|	20-8=12|
P4|	6|	3|	12(sisa 3)|	20(selesai)	|-	|20-3=17	|17-6=11|

**Eksperimen 2 -  Priority Scheduling (Non-Preemptive)**

|Proses| 	Arrival Time| 	Burst Time| 	Priority|	Start|	Finish Time(Start - BT)|	     WT(Start - AT)	|     TAT (WT + BT)|
|:---|:---|:---|:---|:---|:---|:---|:---|
P1|	0	|5|	2|	0|0+5=5|	0-0=0	|0+5=5|
P2|	1|	3|	1|	5|5+3=8|5-1=4|4+3=7|
P4|	3|	6|	3	|8|8+6=14|8-3=5|5+6=11|
P3|	2|	8|	4|	14|14+8=22|14-2=12|12+8=20|



**Eksperimen 3 - Round Robin (RR) Quantum 2**
Proses| 	Burst Time|	Aririval Time|	Finish Time P1|	Finish Time P2|	Finish Time P3|	Finish Time P4|	TAT (FT - AT)|	WT (TAT - BT)|
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
P1|	5|	0	|2(sisa 3)|	10(sisa 1)|	16(selesai|	-|	16-0=16|	16-5=11|
P2|	3|	1|	4(sisa 1)	|119selesai)|	-|	-|	11-1=10	|10-3=7|
P3|	8|	2	|6(sisa 6)	|13(sisa 4)	|18(sisa 2)|	22(selesai)|	22-2=20|	20-8=12|
P4	|6|	3|	8(sisa 4)|	15(sisa 2))	|20(selesai)|	-|	20-3=17|	17-6=11|

**Eksperimen 3 - Round Robin (RR) Quantum 5**
|Proses| 	Burst Time|	Aririval Time|	Finish Time P1|	Finish Time P2|	TAT|	WT|
|:---|:---|:---|:---|:---|:---|:---|
P1	|5|	0|	5(selesai)|	-|5-0=5|	5-5=0|
P2|	3	|1	|8(selesai)|	-|8-1=7|	7-3=4|
P3|	8|	2|	13(sisa 3)|	21(selesai)|21-2=19	|19-8=11|
P4	|6|	3|	18(sisa 1)|	22(selesai)|22-3=19|	19-6=13|

Tabel perbandingan efek quantum:
|Quantum|Average Waiting Time(WT)|Average Turnaround Time (TAT)|Efek Perubahan quantum|
|:---|:---|:---|:---|
Q=2 (quantum yang lebih kecil)|10,25|15,75|Quantum lebih kecil yaitu 2 meningkatkan waktu tunggu dan rata-rata turnaround time lebih tinggi karena terdapat proses yang sering bergantian dan terjadi context switch sehingga proses menunggu giliran lebih lama|
Q=5 (quantum yang lebih besar)|7|12,50|Quantum yang lebih besar(5) akan mengurangi waktu tunggu dan rata-rata turnaround time,karena proses dapat dieksekusi lebih cepat dalam satu giliran tanpa banyak perpindahan|


**Ekxperimen 4 - Perbandingan Round Robin (RR) dan Priority Scheduling**

|Algoritma	|Avg Waiting Time	|Avg Turnaround Time|	Kelebihan|	Kekurangan|
|:---|:---|:---|:---|:---|
RR|	8,5|	14|	Adil terhadap semua proses,respon untuk setiap proses dan tidak ada proses yan diabaikan |	Tidak efisien jika quantum tidak tepat dan Tidak ada prioritas semua proses diperlakukan sama|
Priority	|5,25|	10,75|	Efisien untuk proses penting dan bisa digunakan preemptive atau non-preemptive|	Potensi starvation pada prioritas rendah dan lebih kompleks dalam implementasi dan manajemen prioritas|


---

## Analisis

---

## Kesimpulan

Round Robin bekerja dengan memberikan giliran CPU secara berurutan pada setiap proses menggunakan time quantum tertentu.Dengan menggunakan cara ini untuk memastikan keadilan dalam pembagian waktu eksekusi CPU sehingga setiap proses mendapat kesempatan yang sama tanpa mengalami starvation. Namun, pemilihan waktu quantum yang tepat sangat penting untuk menghindari overhead tinggi akibat terlalu sering berpindah proses atau waktu respons yang lama jika quantum terlalu besar.

Priority Scheduling mengeksekusi proses berdasarkan tingkat prioritas yang diberikan. Proses dengan prioritas lebih tinggi akan dilayani terlebih dahulu, sehingga algoritma ini cocok untuk sistem yang memerlukan penanganan prioritas tertentu, seperti sistem real-time. Namun, kelemahan utama Priority Scheduling adalah adanya risiko starvation bagi proses dengan prioritas rendah, kecuali ada mekanisme aging yang menaikkan prioritas proses yang menunggu lama.

---
## Tugas 

1.Hitung waiting time dan turnaround time untuk algoritma RR dan Priority.

* Round Robin(RR)
Proses| 	Burst Time|	Aririval Time|	Finish Time P1|	Finish Time P2|	Finish Time P3|	     WT	|     TAT|
|:---|:---|:---|:---|:---|:---|:---|:---|
P1	|5	|0	|3|	14|	selesai|	9	|14|
P2|	3|	1|	6	|selesai|	selesai|	2|	5|
P3|	8	|2	|9	|17	|22|	12|	20|
P4|	6|	3|	12	|20|	selesai|	11|	17|
Total	||||||					|34|	56|
Average	||||||					8,5|	14|

* Priority Scheduling
 | Proses| 	Arrival Time| 	Burst Time| 	Priority	|Start|	Finish Time|	     WT	|     TAT|
P1|	0|	5|	2|	0	|5	|0|	5|
P2|	1|	3|	1|	5	|8	|4|	7|
P4|	3|	6|	3	|8	|14	|5	|11|
P3	|2|	8	|4|	14|	22	|12|	20|
Total	||||||					21|	43|
Average ||||||						5,25|	10,75|

 2.Sajikan Gantt Chart
*  Round Robin(RR)

       | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
       0    3    6    9   12   14   17   20   22
 * Priority Scheduling

       | P1 | P2 | P3 | P4 |
       0    5    8    14   22
* Round Robin (RR) Quantum 2

      | P1 | P2 | P3 | P4 | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
      0    2    4    6    8   10   11   13   15   16   18    20   22
* Round Robin (RR) Quantum

      | P1 | P2 | P3 | P4 | P3 | P4 |
      0    5    8   13   18   21   22

 3. Bandingkan performa dan jelaskan pengaruh time quantum serta prioritas.

Round Robin (RR) memberikan giliran CPU secara bergilir dengan time quantum tertentu, sehingga memastikan keadilan eksekusi semua proses. Namun, jika time quantum terlalu kecil, overhead context switch meningkat. Sedangkan Priority Scheduling mengeksekusi proses berdasarkan prioritas, mempercepat eksekusi proses penting, tapi berisiko starvation untuk prioritas rendah tanpa mekanisme aging.

Pengaruh time quantum sangat krusial pada RR untuk mengatur keseimbangan efisiensi dan responsivitas, sedangkan prioritas pada Priority Scheduling menentukan proses mana yang diproses lebih dulu, mengoptimalkan waktu tunggu proses prioritas tinggi. Pemilihan algoritma tergantung kebutuhan sistem: RR untuk keadilan proses, Priority untuk penanganan prioritas kritis.

---
## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?

Jawaban:Perbedaan utama Round Robin membagi CPU secara bergiliran dengan jatah waktu yang sama untuk semua proses tanpa memandang prioritas, sehingga semua proses mendapat giliran yang adil. Sedangkan Priority Scheduling mengeksekusi proses berdasarkan prioritasnya, dengan proses prioritas tertinggi dijalankan lebih dulu, yang dapat menyebabkan proses prioritas rendah menunggu lebih lama.  

3. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?

Jawaban:  Pengaruh besar time quantum terhadap perfoma sistem,jika terlalu besar  respons sistem menjadi lambat karena proses harus menunggu lebih lama untuk mendapatkan giliran, sehingga algoritma ini berperilaku mirip First Come First Serve (FCFS) dengan waktu respons yang tinggi.Pengaruh kecil time quantum terhadap perfoma sistem,jika terlalu kecil, maka sering terjadi pergantian proses (context switching) sehingga menyebabkan overhead tinggi dan menurunkan efisiensi CPU.

4.Mengapa algoritma Priority dapat menyebabkan starvation?
  
Jawaban:Algoritma Priority dapat menyebabkan starvation karena proses dengan prioritas rendah bisa terus menunggu tanpa pernah mendapatkan giliran menjalankan CPU jika selalu ada proses dengan prioritas lebih tinggi yang masuk dan mengambil alih sumber daya. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
