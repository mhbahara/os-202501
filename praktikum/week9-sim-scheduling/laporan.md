
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
## Dasar Teori

Penjadwalan CPU adalah cara sistem operasi mengatur proses yang akan dijalankan oleh CPU. Setiap proses memiliki arrival time, burst time, waiting time, dan turnaround time. Salah satu algoritma penjadwalan yang paling sederhana adalah First Come First Serve (FCFS), yaitu menjalankan proses sesuai urutan kedatangannya. Simulasi digunakan agar proses perhitungan menjadi lebih mudah, cepat, dan membantu memahami cara kerja algoritma penjadwalan CPU.

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
import csv

processes = []

with open("dataset.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # ⬅️ LEWATI HEADER

    for row in reader:
        pid = row[0]
        arrival = int(row[1])
        burst = int(row[2])
        processes.append([pid, arrival, burst])

# FCFS → urut berdasarkan arrival time
processes.sort(key=lambda x: x[1])

time = 0
total_wait = 0
total_tat = 0

print("Proses | Arrival | Burst | Waiting | Turnaround")
print("---------------------------------------------")

for p in processes:
    pid, arrival, burst = p

    if time < arrival:
        time = arrival

    waiting = time - arrival
    turnaround = waiting + burst

    time += burst

    total_wait += waiting
    total_tat += turnaround

    print(f"{pid:^6} | {arrival:^7} | {burst:^5} | {waiting:^7} | {turnaround:^10}")

n = len(processes)
print("---------------------------------------------")
print(f"Rata-rata Waiting Time   : {total_wait / n:.2f}")
print(f"Rata-rata Turnaround Time: {total_tat / n:.2f}")

```

---

## Hasil Eksekusi
Sertakan screenshot   
    
![alt text](<screenshots/week9.png>)

---

## Analisis
1. Alur program
   * import csv -> digunakan untuk mengimpor modul csv pada Python. Modul ini berfungsi untuk membaca data dari file CSV (dataset.csv) yang berisi informasi proses seperti ID proses, arrival time, dan burst time.
   * processes = [] -> menyimpan seluruh data proses yang dibaca dari file CSV. Setiap proses akan disimpan dalam bentuk list yang berisi ID proses, arrival time, dan burst time.


         with open("dataset.csv", newline="") as file:
          reader = csv.reader(file)
          next(reader)
 
membuka file dataset.csv dalam mode baca. Fungsi csv.reader() digunakan untuk membaca isi file CSV baris per baris.
Perintah next(reader) digunakan untuk melewati baris pertama file CSV karena baris tersebut merupakan header kolom, bukan data proses.

        for row in reader:
         pid = row[0]
        arrival = int(row[1])
        burst = int(row[2])
        processes.append([pid, arrival, burst])

 pid menyimpan ID proses,arrival menyimpan waktu kedatangan proses, burst menyimpan waktu eksekusi proses,dan disimpan ke dalam list processes dalam bentuk [pid, arrival, burst].

  * Proses diurutkan berdasarkan arrival time agar sesuai dengan algoritma FCFS, yaitu proses yang datang lebih awal dijalankan lebih dulu.
  * Variabel time digunakan untuk menyimpan waktu CPU selama simulasi berjalan. Variabel total_wait dan total_tat digunakan untuk menjumlahkan waiting time dan turnaround time dari seluruh proses untuk perhitungan rata-rata di akhir program.
 * Program menampilkan judul kolom dan garis pemisah tabel agar hasil simulasi terlihat rapi dan mudah dibaca di terminal.Program melakukan perulangan untuk mengeksekusi setiap proses satu per satu sesuai urutan FCFS yang telah ditentukan sebelumnya.Jika CPU masih dalam kondisi idle atau waktu CPU lebih kecil dari arrival time suatu proses, maka waktu CPU akan disesuaikan dengan arrival time proses tersebut.
  * Waiting time dihitung dari selisih antara waktu mulai eksekusi dengan arrival time. Turnaround time dihitung dengan menjumlahkan waiting time dan burst time.Setelah suatu proses dieksekusi, waktu CPU akan bertambah sesuai burst time proses tersebut. Nilai waiting time dan turnaround time juga dijumlahkan untuk perhitungan rata-rata.Hasil perhitungan setiap proses ditampilkan ke dalam tabel dengan format yang rapi sehingga mudah dipahami.Setelah seluruh proses selesai disimulasikan, program menghitung dan menampilkan rata-rata waiting time dan rata-rata turnaround time sebagai hasil akhir.  

3. Perbandingan Hasil Simulasi dengan Perhitungan Manual
   * Dari hasil program, diperoleh tabel simulasi sebagai berikut:
 
 | Proses|	AT|	BT|	WT|	TAT|
|:---|:---|:---|:---|:---|
|P1	|0	|6	|0	|6|
|P2	|1	|8	|5	|13|
|P3	|2	|7	|12	|19|
|P4 |3	|3  |18 |21|

Rata-rata Waiting Time = 8.75

Rata-rata Turnaround Time = 14.75

Dari hasil perbandingan hasil simulasi dengan hasil manual. Hasil simulasi FCFS menunjukkan nilai waiting time dan turnaround time yang sama dengan perhitungan manual karena proses dieksekusi berdasarkan urutan arrival time tanpa preemption. Rata-rata waiting time sebesar 8.75 dan turnaround time sebesar 14.75 juga sesuai dengan hasil manual, sehingga simulasi telah berjalan dengan benar.

4. Kelebihan dan keterbatasan simulasi
  * Kelebihan
    * Program mampu menghitung waiting time dan turnaround time secara otomatis sehingga mempercepat proses analisis.
    * Mengurangi kesalahan yang mungkin terjadi pada perhitungan manual dan output yang dihasilkan dalam bentuk tabel rapih dan mudah untuk dibaca
 * Keterbatasan simulasi
    * Simulasi hanya mendukung algoritma FCFS dan belum mencakup algoritma penjadwalan lain.
    * Dataset yang digunakan masih terbatas dan bersifat sederhana.
    * Tidak mempertimbangkan prioritas proses.
---

## Kesimpulan
Berdasarkan praktikum yang telah dilakukan, simulasi algoritma penjadwalan CPU menggunakan metode FCFS berhasil diimplementasikan dengan baik. Program mampu membaca dataset, menghitung waiting time dan turnaround time, serta menampilkan hasil simulasi dalam bentuk tabel yang rapi. Hasil simulasi menunjukkan nilai yang sesuai dengan perhitungan manual, sehingga dapat disimpulkan bahwa algoritma FCFS telah berjalan dengan benar dan simulasi ini membantu dalam memahami konsep dasar penjadwalan CPU secara lebih praktis.

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
****
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  Bagian yang paling menantang minggu ini itu membuat simulasi karena saya belum begitu paham bahasa di visual studio code 
- Bagaimana cara Anda mengatasinya?
  Cara saya mengatasinya dengan membaca buku  panduan dan melihat tutorial di youtube

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
