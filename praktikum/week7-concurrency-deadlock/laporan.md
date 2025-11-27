
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Nama Mahasiswa]  
- **NIM**   : [NIM Mahasiswa]  
- **Kelas** : [Kelas]

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1.Mengidentifikasi empat kondisi penyebab deadlock (mutual exclusion, hold and wait, no preemption, circular wait).
2.Menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.
3.Menganalisis dan memberikan solusi untuk kasus deadlock.
4.Berkolaborasi dalam tim untuk menyusun laporan analisis.
5.Menyajikan hasil studi kasus secara sistematis.
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
Concurrency adalah kondisi ketika beberapa proses atau thread dapat berjalan secara bersamaan, baik secara paralel pada banyak inti prosesor maupun secara bergantian sangat cepat pada satu inti CPU. Tujuan utama concurrency adalah meningkatkan pemanfaatan CPU, efisiensi, dan responsivitas sistem. Namun, concurrency juga menimbulkan sejumlah permasalahan seperti race condition, inkonsistensi data, kelaparan (starvation), dan deadlock, sehingga mekanisme sinkronisasi seperti lock, semaphore, dan monitor sangat diperlukan untuk menjaga konsistensi dan koordinasi antarproses. Salah satu masalah penting yang muncul dari concurrency adalah deadlock, yaitu keadaan ketika dua atau lebih proses saling menunggu resource yang tidak pernah dilepaskan sehingga tidak ada proses yang dapat melanjutkan eksekusi. Deadlock hanya dapat terjadi jika empat kondisi terpenuhi secara bersamaan, yaitu mutual exclusion (resource hanya dapat digunakan satu proses pada satu waktu), hold and wait (proses memegang satu resource sambil menunggu resource lain), no preemption (resource tidak bisa diambil paksa), dan circular wait (terjadi rantai proses yang saling menunggu secara melingkar). Penyebab deadlock umumnya berasal dari pengelolaan resource bersama yang tidak tepat, penguncian yang tidak konsisten, dan koordinasi proses yang salah. Dalam sistem operasi, penanganan deadlock dapat dilakukan melalui pencegahan (preventing), penghindaran (avoidance), pendeteksian (detection), dan pemulihan (recovery). Dengan demikian, concurrency dan deadlock memiliki hubungan erat karena eksekusi bersamaan tanpa pengaturan yang baik dapat memicu kondisi saling menunggu yang berujung pada deadlock.
---

## Langkah Praktikum
1.Persiapan Tim

-Bentuk kelompok beranggotakan 3–4 orang.
-Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).
2.Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)

-Implementasikan versi sederhana dari masalah Dining Philosophers tanpa mekanisme pencegahan deadlock.
-Contoh pseudocode
```bash
while true:
  think()
  pick_left_fork()
  pick_right_fork()
  eat()
  put_left_fork()
  put_right_fork()
```
-Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).
-Identifikasi kapan dan mengapa deadlock terjadi.
3.Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)

-Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
-Menggunakan semaphore (mutex) untuk mengontrol akses.
-Membatasi jumlah filosof yang dapat makan bersamaan (max 4).
-Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).
-Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.
4.Eksperimen 3 – Analisis Deadlock

-Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.

-Sajikan hasil analisis dalam tabel seperti contoh berikut:
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
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
