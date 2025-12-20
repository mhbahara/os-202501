
# Laporan Praktikum Minggu 9
Topik:Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  :NOVIA SAFITRI
- **NIM**   : 250202923
- **Kelas** : 1IKRA

---

## Tujuan

1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.

2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.

3. Menyajikan output simulasi dalam bentuk tabel atau grafik.

4. Menjelaskan hasil simulasi secara tertulis.

5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori

---

## Langkah Praktikum
1. Menyiapkan Dataset

Buat dataset proses minimal berisi:

|Proses|	Arrival Time|	Burst Time|
|:---|:---|:---|
|P1|	0	|6|
|P2|	1|	8|
|P3|	2	|7|
|P4	|3|	3|

2. Implementasi Algoritma

    Program harus:

   * Menghitung waiting time dan turnaround time.

   * Mendukung minimal 1 algoritma (FCFS atau SJF non-preemptive).

   * Menampilkan hasil dalam tabel.

3. Eksekusi & Validasi

   * Jalankan program menggunakan dataset uji.

   * Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.

   * Simpan hasil eksekusi (screenshot).

4. Analisis

    * Jelaskan alur program.
 
    * Bandingkan hasil simulasi dengan perhitungan manual.
 
    * Jelaskan kelebihan dan keterbatasan simulasi.

5. Commit & Push

      git add 
     git commit -m "Minggu 9 - Simulasi Scheduling CPU"
     git push origin main


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.*
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md
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
1.Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
   
   **Jawaban:**  Simulasi diperlukan untuk menguji algoritma scheduling karena cara kerja dan hasilnya bisa dipahami dengan mudah tanpa harus diimplementasikan langsung pada sistem operasi sebenarnya. Dengan simulasi,perhitungan menjadi lebih cepat dan tepat,berbagai kondisi proses dapat dicoba,serta hasil yang diperoleh dapat dibandingkan dengan teori/perhitungan manual sehingga kinerja algoritma dapat dievaluasi dengan baik. 

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?

|Aspek|Simulasi|Perhitungan|
|:---|:---|:---|
Jumlah data|Bisa menangani dataset besar tanpa kesulitan | Semakin besar dataset maka semakin sulit dihitung|
Kecepatan| Perhitungannya sangat cepat meskipun datanya banyak|Perhitungannya lambat jika data semakin besar dan banyak|
Akurasi| Hasilnya akurat dan konsisten |Cenderung sering terjadi kesalahan| 

4. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.

   **Jawaban:**  Algoritma yang lebih mudah untuk diimplementasikan adalah algoritma FCFS(First Come First Serve) karena simulasi FCFS itu dijalankan sesuai urutan kedatangan dan tanpa perhitungan yang rumit.Prosesnya hanya mengatur antrian proses dan menghitung waktu tunggu selesainya,sehingga mudah dipahami dan sederhana.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
