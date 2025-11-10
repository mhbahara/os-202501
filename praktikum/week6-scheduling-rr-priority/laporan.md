
# Laporan Praktikum Minggu [X]
## Topik:Dua algoritma lanjutan penjadwalan CPU, yaitu:

- Round Robin (RR)
- Priority Scheduling

---

## Identitas
- **Nama**  : [Miftakhul Lisna Esa b aehaqi]  
- **NIM**   : [250202951]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.
3. Membandingkan performa algoritma RR dan Priority.
4. Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.


---

## Dasar Teori

1. Konsep Dasar CPU Scheduling
CPU Scheduling adalah mekanisme sistem operasi untuk menentukan urutan eksekusi proses di CPU ketika terdapat banyak proses dalam antrian siap (ready queue). Tujuannya adalah memaksimalkan pemanfaatan CPU, meminimalkan waktu tunggu (waiting time), dan memberikan respon yang adil antar proses.


2. Round Robin (RR) Scheduling
Algoritma ini menggunakan pendekatan preemptive dengan membagi waktu CPU menjadi slot kecil yang disebut time quantum. Setiap proses mendapat jatah waktu CPU secara bergiliran. Jika proses belum selesai dalam satu quantum, proses dikembalikan ke antrian siap. Keunggulannya adalah keadilan (fairness) dan respon cepat untuk sistem interaktif, tetapi efisiensinya sangat tergantung pada ukuran quantum.


3. Priority Scheduling
Setiap proses diberi nilai prioritas, dan CPU dialokasikan ke proses dengan prioritas tertinggi terlebih dahulu. Algoritma dapat bersifat preemptive atau non-preemptive. Kelebihannya adalah efisien untuk menangani proses penting, tetapi dapat menimbulkan starvation bagi proses prioritas rendah jika tidak ada mekanisme aging.


4. Parameter Evaluasi: Waiting Time dan Turnaround Time

- Waiting Time (WT): total waktu proses menunggu di antrian siap sebelum mendapatkan CPU.

- Turnaround Time (TAT): total waktu sejak proses tiba hingga selesai dieksekusi (TAT = Finish Time − Arrival Time).
Kedua nilai ini digunakan untuk mengukur efisiensi dan keadilan algoritma.

5. Trade-off antara Efisiensi dan Keadilan
Round Robin menekankan keadilan dengan membagi CPU secara merata, sedangkan Priority Scheduling menekankan efisiensi bagi proses penting. Pemilihan algoritma bergantung pada tujuan sistem — apakah lebih penting responsivitas (RR) atau penanganan prioritas (Priority).

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
![Screenshot hasil eksperimen 1 dan 2](./screenshots/eksperimen%201%20dan%202.png)

---
## Eksperimen 1 — Round Robin (q = 3)
![hasil eksperimen 1](./screenshots/eksperimen%201.png)

(Gantt chart, urutan eksekusi)

Tiap entry: NamaProcess : start - end
P1: 0–3, P2: 3–6, P3: 6–9, P4: 9–12, P1: 12–14, P3: 14–17, P4: 17–20, P3: 20–22

Penjelasan singkat urutan:

- Putaran 1 (t=0..12): setiap process yang sudah datang mendapat kuanta 3 (P1, P2, P3, P4).

- Setelah putaran 1: sisa burst → P1=2, P2=0, P3=5, P4=3.

- Lanjutkan putaran 2: P1 (2) selesai 12–14, P3 (3) 14–17 (rem 2), P4 (3) 17–20 selesai, P3 (2) 20–22 selesai.

## Eksperimen 2 — Priority Scheduling (Non-Preemptive)

Aturan: pilih proses siap (arrival ≤ current time) dengan nilai priority paling kecil (angka kecil = prioritas tinggi). Jika CPU idle, lompat ke arrival berikutnya.

Urutan eksekusi & hasil

Urutan eksekusi (start–finish):
P1: 0–5, P2: 5–8, P4: 8–14, P3: 14–22

![eksperimen 2](./screenshots/eksperimen%202.png
)

## Eksperimen 3 — Variasi Time Quantum (RR dengan q = 2 dan q = 5)
RR, q = 2

Gantt (ringkas):
P1:0–2, P2:2–4, P3:4–6, P1:6–8, P4:8–10, P2:10–11, P3:11–13, P1:13–14, P4:14–16, P3:16–18, P4:18–20, P3:20–22

Hasil:
Proses | WT | TAT
P1 | 9 | 14
P2 | 7 | 10
P3 | 12 | 20
P4 | 11 | 17

Rata-rata:

- Avg WT = (9+7+12+11)/4 = 9.75

- Avg TAT = (14+10+20+17)/4 = 15.25

RR, q = 5

Gantt (ringkas):
P1:0–5, P2:5–8, P3:8–13, P4:13–18, P3:18–21, P4:21–22

Hasil:
Proses | WT | TAT
P1 | 0 | 5
P2 | 4 | 7
P3 | 11 | 19
P4 | 13 | 19

Rata-rata:

- Avg WT = (0+4+11+13)/4 = 7.0

- Avg TAT = (5+7+19+19)/4 = 12.5

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

| Quantum | Avg Waiting Time | Avg Turnaround Time | Catatan                                                                             |
| ------: | ---------------: | ------------------: | ----------------------------------------------------------------------------------- |
|   q = 2 |             9.75 |               15.25 | Banyak context switch → overhead (teoretis), fairness tinggi                        |
|   q = 3 |              8.5 |                14.0 | Seimbang pada dataset ini                                                           |
|   q = 5 |              7.0 |                12.5 | Mirip FCFS bagi tugas-besar; throughput lebih baik untuk CPU-bound yang datang awal |

---
## Eksperimen 4 – Dokumentasi
![praktikum/week6-scheduling-rr-priority/screenshots/](./screenshots/eksperimen%201%20dan%202.png )

## Tabel Perbandingan (RR vs Priority)
| Algoritma                 | Avg Waiting Time | Avg Turnaround Time | Kelebihan                                                        | Kekurangan                                                                              |
| ------------------------- | ---------------: | ------------------: | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| RR (q=3)                  |          **8.5** |            **14.0** | Adil (preemptive) — setiap proses dapat slice CPU secara teratur | Performa sangat tergantung pada pemilihan quantum; context switch jika q kecil          |
| Priority (non-preemptive) |         **5.25** |           **10.75** | Cepat untuk proses prioritas tinggi (efisien untuk job penting)  | Potensi starvation untuk prioritas rendah; hasil tergantung akurasi penetapan prioritas |
---

---

## Kesimpulan
- Priority (non-preemptive) pada dataset ini menghasilkan rata-rata WT dan TAT lebih rendah karena proses dengan prioritas tinggi dijalankan sedini mungkin. Namun ada risiko starvation untuk proses prioritas rendah.

- RR memberikan keadilan (every process mendapat CPU slice) — cocok untuk sistem interaktif — tetapi performa (avg WT/TAT) sangat dipengaruhi oleh pemilihan quantum. Quantum terlalu kecil → banyak switching; quantum terlalu besar → perilaku mirip FCFS.


---

## Quiz
1. [Apa perbedaan utama antara Round Robin dan Priority Scheduling?]  
 **Jawaban:**    
 1. Round Robin menekankan keadilan waktu eksekusi untuk semua proses.

2. Priority Scheduling menekankan pentingnya urutan eksekusi berdasarkan tingkat prioritas.

3. Pilihan algoritma tergantung kebutuhan sistem: interaktif → RR, kritikal/real-time → Priority
   
2. [Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?]  
   **Jawaban:**  
- Nilai time quantum sangat memengaruhi kinerja algoritma Round Robin.
- Quantum yang terlalu kecil → sistem adil tapi lambat (banyak switching).
- Quantum yang terlalu besar → sistem efisien tapi tidak adil (mirip FCFS).
Jadi, pemilihan quantum harus seimbang antara efisiensi dan fairness sesuai jenis beban kerja sistem.
3. [Mengapa algoritma Priority dapat menyebabkan starvation?]  
   **Jawaban:** Algoritma Priority dapat menyebabkan starvation karena proses dengan prioritas rendah bisa tertunda terus-menerus akibat kedatangan proses dengan prioritas lebih tinggi.
Solusi utamanya adalah menerapkan aging, agar sistem tetap adil dan semua proses mendapat kesempatan dieksekusi. 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  laptop digunakan ibu untuk membuat soal uts dan susah membagi waktu untuk menggunakan  laptop
- Bagaimana cara Anda mengatasinya? mengerjakan tugas diwaktu malam agar bisa menggunakan laptop  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
