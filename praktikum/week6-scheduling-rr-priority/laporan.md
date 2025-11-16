
# Laporan Praktikum Minggu [X]
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
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
