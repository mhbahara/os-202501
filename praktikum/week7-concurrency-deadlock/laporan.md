
# Laporan Praktikum Minggu [7]
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas Kelompok
- **Nama**  :

1. PASYA AWAN RIZKY SAPUTRO (250202959)
2. MOHAMMAD FATIKH MAHSUN (250202952)
3. LUTHFI AULIA RAHMAN (250202948)


- **Kelas** : 1 IKRB

---

## Tujuan
1. Mengidentifikasi empat kondisi penyebab deadlock (mutual exclusion, hold and wait, no preemption, circular wait).
2. Menjelaskan mekanisme sinkronisasi menggunakan semaphore atau monitor.
3. Menganalisis dan memberikan solusi untuk kasus deadlock.
4. Berkolaborasi dalam tim untuk
menyusun laporan analisis.
5. Menyajikan hasil studi kasus secara sistematis.


 1. Mengidentifikasi Empat Kondisi Penyebab Deadlock

 Deadlock dapat terjadi ketika keempat kondisi Coffman terpenuhi secara bersamaan:

- Mutual Exclusion
Resource hanya dapat digunakan oleh satu proses pada satu waktu.

- Hold and Wait
Proses memegang satu resource sambil menunggu resource lain yang sedang digunakan proses lain.

- No Preemption
Resource tidak dapat direbut paksa; hanya bisa dilepas sukarela oleh proses yang memegangnya.

- Circular Wait
Terdapat rantai proses yang saling menunggu resource, membentuk siklus melingkar.

2. Sinkronisasi Menggunakan Semaphore

Semaphore adalah mekanisme sinkronisasi berbasis nilai integer, digunakan untuk mengatur akses ke resource yang dipakai bersama (shared resource).

Terdapat dua jenis semaphore:

1. Binary Semaphore (mutex)
Nilainya hanya 0 atau 1 → untuk mutual exclusion.

2. Counting Semaphore
Memungkinkan banyak proses mengakses beberapa resource sejenis (misal 3 printer → semaphore bernilai 3).

Dua operasi utama semaphore

wait(P) → proses meminta akses
Jika nilai semaphore > 0 → bisa masuk
Jika nilai semaphore ≤ 0 → proses menunggu

signal(V) → proses melepaskan akses
Menaikkan nilai semaphore dan membangunkan proses yang menunggu

3. Contoh Kasus Deadlock

Terdapat dua proses dan dua resource:

P1: memegang R1, dan menunggu R2

P2: memegang R2, dan menunggu R1

Gambaran:
P1 → menunggu R2
   R1 → dipegang P1

P2 → menunggu R1
   R2 → dipegang P2

- Analisis Kondisi Deadlock

Periksa 4 kondisi Coffman:

Mutual Exclusion → benar
R1 dan R2 hanya bisa digunakan satu proses.

Hold and Wait → benar
P1 memegang R1 sambil menunggu R2; P2 memegang R2 sambil menunggu R1.

No Preemption → benar
Resource tidak bisa direbut paksa.

Circular Wait → benar
P1 → R2 → P2 → R1 → P1 (melingkar)

✔ Semua kondisi terpenuhi → deadlock terjadi.

- Solusi Deadlock

Ada beberapa pendekatan:

A. Deadlock Prevention (Pencegahan)

Menghilangkan salah satu dari empat kondisi deadlock.

Hilangkan Hold and Wait
Proses harus meminta semua resource di awal.
→ Tidak bisa menunggu sambil memegang resource.

Hilangkan Circular Wait
Tetapkan urutan pemberian resource.
Misal: setiap proses harus meminta resource berdasarkan nomor ID:

Resource harus diminta dengan urutan R1 → R2


Maka kasus P1 dan P2 tidak akan saling menunggu melingkar.

B. Deadlock Avoidance (Penghindaran)

Menggunakan algoritma seperti Banker’s Algorithm untuk memastikan sistem tidak masuk ke keadaan tidak aman.

Sistem hanya memberikan resource jika aman.

C. Deadlock Detection and Recovery (Deteksi & Pemulihan)

Deteksi

Cek apakah ada siklus di resource allocation graph.

Recovery

Membunuh salah satu proses (misal P1)

Atau memaksa proses melepas resource

Setelah salah satu proses dihentikan → deadlock hilang.

D. Deadlock Ignorance (Mengabaikan)

Umum di sistem operasi modern (Windows, Linux).

Probabilitas deadlock kecil → sistem tidak mendeteksi secara khusus.
Jika deadlock terjadi → user dapat mematikan proses secara manual.

---


## Dasar Teori

---


Sinkronisasi proses adalah cara sistem operasi mengatur proses yang berjalan bersamaan agar tidak saling mengganggu saat memakai resource yang sama. Tanpa sinkronisasi, data bisa rusak, hasil bisa salah, dan proses bisa berebut masuk ke area penting (critical section).

Intinya, sinkronisasi dibutuhkan supaya:

* proses tidak saling tabrakan saat mengakses data,
* data tetap konsisten
* proses bekerja bergantian dengan rapi.

Alat yang biasa dipakai untuk sinkronisasi:

* Semaphore → seperti lampu merah untuk memberi giliran.
* Mutex/Lock → kunci agar hanya satu proses yang masuk.
* Monitor → alat otomatis yang mengatur kunci dan kondisi.

---


Deadlock adalah keadaan ketika dua atau lebih proses saling menunggu dan akhirnya semuanya berhenti. Tidak ada proses yang bisa jalan karena masing-masing menunggu resource yang dipegang proses lain.

Deadlock bisa terjadi jika memenuhi 4 kondisi:

1. **Mutual Exclusion** – resource tidak bisa dipakai bersama.
2. **Hold and Wait** – proses memegang satu resource sambil menunggu yang lain.
3. **No Preemption** – resource tidak bisa direbut paksa.
4. **Circular Wait** – proses menunggu secara melingkar.

Contohnya seperti dua orang saling menunggu untuk lewat pintu sempit → akhirnya tidak ada yang bisa lewat.

Solusi deadlock dapat berupa:

* mencegah agar kondisi penyebab tidak muncul,
* menghindari keadaan tidak aman,
* mendeteksi dan memperbaiki jika deadlock terjadi,
* atau mengabaikan jika probabilitasnya kecil.

---



---

## Langkah Praktikum
**1. Persiapan Tim**

- Bentuk kelompok beranggotakan 3–4 orang.
- Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

**2. Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**

- Implementasikan versi sederhana dari masalah Dining Philosophers tanpa mekanisme pencegahan deadlock.
- Contoh pseudocode:
while true:

  think()
  pick_left_fork()
  pick_right_fork()
  eat()
  put_left_fork()
  put_right_fork()
Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).
Identifikasi kapan dan mengapa deadlock terjadi.

**3. Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**

- Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:

- Menggunakan semaphore (mutex) untuk mengontrol akses.
- Membatasi jumlah filosof yang dapat makan bersamaan (max 4).
- Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).
- Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

**4. Eksperimen 3 – Analisis Deadlock**

- Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.

- Sajikan hasil analisis dalam tabel seperti contoh berikut:

Kondisi Deadlock	Terjadi di Versi Deadlock	Solusi di Versi Fixed
Mutual Exclusion	Ya (satu garpu hanya satu proses)	Gunakan semaphore untuk kontrol akses
Hold and Wait	Ya	Hindari proses menahan lebih dari satu sumber daya
No Preemption	Ya	Tidak ada mekanisme pelepasan paksa
Circular Wait	Ya	Ubah urutan pengambilan sumber daya


**5. Eksperimen 4 – Dokumentasi**

- Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
praktikum/week7-concurrency-deadlock/screenshots/

- Tuliskan laporan kelompok di laporan.md (format IMRaD singkat: Pendahuluan, Metode, Hasil, Analisis, Diskusi).

**6. Commit & Push**


git add .
git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
git push origin main 

  
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
