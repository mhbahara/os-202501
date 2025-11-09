
# Laporan Praktikum Minggu [5]
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : [Mohammad Fatikh Mahsun]  
- **NIM**   : [250202952]  
- **Kelas** : [1IKRB]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Waiting Time (WT) = waktu mulai eksekusi - Arrival Time

Turnaround Time (TAT) = WT + Burst Time

| P1 | P2 | P3 | P4 |
0    6    14   21   24

praktikum/week5-scheduling-fcfs-sjf/screenshots/

git add .
git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
git push origin main


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/week.5.1.png)
![Screenshot hasil](screenshots/week.5.2.png)

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

1. Perbedaan utama antara FCFS dan SJF

Perbedaan utama antara First Come First Served (FCFS) dan Shortest Job First (SJF) terletak pada cara keduanya menentukan urutan eksekusi proses. FCFS menjalankan proses berdasarkan urutan kedatangan — siapa yang datang lebih dulu akan dieksekusi lebih dulu. Sementara itu, SJF memilih proses yang memiliki waktu eksekusi (burst time) paling singkat untuk dijalankan terlebih dahulu, tanpa memperhatikan urutan kedatangannya. Dengan kata lain, FCFS bersifat sederhana dan adil terhadap waktu kedatangan, sedangkan SJF lebih berfokus pada efisiensi waktu pemrosesan.

2. Alasan SJF menghasilkan rata-rata waktu tunggu minimum

SJF dapat menghasilkan rata-rata waktu tunggu paling rendah karena algoritma ini memprioritaskan proses yang membutuhkan waktu eksekusi paling singkat. Dengan cara ini, proses-proses kecil dapat segera selesai tanpa harus menunggu proses yang lebih lama. Akibatnya, total waktu tunggu seluruh proses menjadi lebih efisien. Pendekatan ini mirip dengan prinsip efisiensi dalam antrean — jika tugas-tugas ringan diselesaikan terlebih dahulu, maka beban sistem secara keseluruhan akan berkurang lebih cepat.

3. Kelemahan SJF pada sistem interaktif

Kelemahan utama SJF ketika diterapkan pada sistem interaktif adalah sulitnya memprediksi waktu eksekusi setiap proses secara akurat. Sistem interaktif biasanya melibatkan banyak permintaan pengguna dengan durasi yang tidak pasti dan berubah-ubah. Selain itu, proses yang memiliki waktu eksekusi lebih panjang cenderung tertunda terus-menerus karena selalu kalah prioritas dengan proses yang lebih singkat. Hal ini dapat menyebabkan masalah starvation atau kelaparan proses, di mana beberapa proses tidak pernah mendapat giliran untuk dijalankan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
