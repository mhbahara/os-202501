
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

```while true:
  think()
  pick_left_fork()
  pick_right_fork()
  eat()
  put_left_fork()
  put_right_fork()
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Deadlock.png)
![Screenshot hasil](./screenshots/Fixed.1.png)
![Screenshot hasil](./screenshots/Fixed.2.png)


---

## Analisis
**EKSPERIMEN 1**

Analisis versi deadlock

Dalam simulasi Dining Philosophers ini, deadlock terjadi ketika seluruh filsuf secara bersamaan mengambil garpu yang berada di sebelah kiri mereka, sehingga seluruh garpu 1 sampai 5 sudah dalam keadaan terpakai. Ketika para filsuf melanjutkan untuk mencoba mengambil garpu di sebelah kanan, tidak ada satu pun garpu yang tersedia karena masing-masing sudah dipegang oleh filsuf berikutnya. Kondisi tersebut menyebabkan setiap filsuf memegang satu garpu sambil menunggu garpu lainnya, namun tidak ada yang dapat melanjutkan atau melepaskan garpu yang mereka pegang. Situasi ini membentuk sebuah lingkaran saling menunggu, di mana P1 menunggu P2, P2 menunggu P3, P3 menunggu P4, P4 menunggu P5, dan P5 kembali menunggu P1. Karena tidak terdapat mekanisme yang memungkinkan pelepasan garpu secara paksa maupun aturan yang dapat memutus rantai penantian tersebut, seluruh proses berhenti dan tidak ada filsuf yang dapat mulai makan. Dengan demikian, deadlock muncul tepat pada saat semua filsuf mencoba mengambil garpu kanan, dan pada titik inilah seluruh syarat deadlock terpenuhi sehingga sistem benar-benar macet.

**EKSPERIMEN 2**

Versi fixed

Pada versi FIXED dari permasalahan Dining Philosophers, solusi sinkronisasi diterapkan menggunakan mekanisme semaphore/monitor sehingga situasi deadlock dapat dihindari sepenuhnya. Dalam versi ini, setiap filsuf tidak lagi mengambil garpu secara bersamaan tanpa aturan; melainkan mereka harus memperoleh izin terlebih dahulu sebelum mengambil garpu. Mekanisme kontrol ini memastikan bahwa tidak semua filsuf dapat mencoba mengambil dua garpu pada saat yang sama. Misalnya, sistem dapat membatasi maksimum empat filsuf yang diperbolehkan duduk untuk makan secara bersamaan, atau memaksa setiap filsuf untuk mengambil garpu dengan urutan yang sudah ditentukan (misalnya selalu mengambil garpu dengan nomor lebih kecil terlebih dahulu). Dengan pembatasan tersebut, tidak akan terbentuk situasi saling menunggu melingkar, karena pola pengambilan garpu menjadi lebih teratur dan tidak memungkinkan kelima filsuf menahan satu garpu sambil menunggu garpu lainnya secara bersamaan. Ketika seorang filsuf selesai makan, ia akan melepaskan kedua garpu yang digunakan sehingga filsuf lain dapat melanjutkan proses makan secara bergiliran. Melalui pengaturan ini, seluruh filsuf dapat makan sampai selesai tanpa terjadi kebuntuan, dan sistem tetap berjalan secara aman serta terkoordinasi. Versi FIXED ini menunjukkan bahwa dengan pengaturan akses sumber daya yang tepat, permasalahan deadlock dapat sepenuhnya dicegah.


**EKSPERIMEN 3**

Pada versi pertama simulasi Dining Philosophers, terjadi deadlock karena terpenuhinya keempat kondisi deadlock secara bersamaan. Mutual Exclusion terjadi karena setiap garpu hanya dapat dipegang oleh satu filsuf pada satu waktu. Hold and Wait muncul ketika setiap filsuf sudah memegang garpu kiri sambil menunggu garpu kanan yang sedang dipegang filsuf lain. No Preemption terjadi karena garpu yang sudah dipegang tidak bisa diambil paksa oleh filsuf lain; mereka hanya bisa melepaskan garpu setelah selesai makan. Sedangkan Circular Wait terbentuk ketika P1 menunggu P2, P2 menunggu P3, P3 menunggu P4, P4 menunggu P5, dan P5 menunggu P1, sehingga membentuk lingkaran menunggu yang sempurna.
Pada versi FIXED, kondisi-kondisi tersebut dipecahkan melalui mekanisme sinkronisasi dan pengaturan urutan pengambilan garpu. Mutual Exclusion tetap ada, tetapi dikontrol dengan semaphore atau monitor sehingga akses garpu menjadi teratur. Hold and Wait dihindari dengan memastikan filsuf hanya mengambil kedua garpu ketika keduanya tersedia, sehingga tidak ada yang menahan satu garpu sambil menunggu yang lain. No Preemption diatasi dengan melepaskan garpu setelah selesai makan sehingga proses lain dapat menggunakannya, dan Circular Wait dihilangkan dengan menentukan urutan pengambilan garpu atau membatasi jumlah filsuf yang boleh makan bersamaan, sehingga tidak terbentuk lingkaran saling menunggu. Dengan pengaturan ini, semua filsuf dapat makan secara bergiliran tanpa terjadi deadlock.

| Kondisi Deadlock | Terjadi di Versi Deadlock                                 | Solusi di Versi Fixed                                                                       |
| ---------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Mutual Exclusion | Ya, satu garpu hanya dapat dipegang satu filsuf           | Tetap ada, tetapi diatur menggunakan semaphore/monitor agar akses terkontrol                |
| Hold and Wait    | Ya, filsuf memegang satu garpu sambil menunggu garpu lain | Filsuf hanya mengambil kedua garpu jika keduanya tersedia                                   |
| No Preemption    | Ya, garpu tidak bisa diambil paksa dari filsuf lain       | Garpu dilepas setelah selesai makan sehingga dapat digunakan proses lain                    |
| Circular Wait    | Ya, membentuk lingkaran menunggu antara semua filsuf      | Dihindari dengan urutan pengambilan garpu atau membatasi jumlah filsuf yang makan bersamaan |




---

## Kesimpulan
Kesimpulan Sinkronisasi Proses

Sinkronisasi proses diperlukan agar beberapa proses yang berjalan bersamaan tidak saling mengganggu, terutama saat mengakses data atau sumber daya yang sama. Tujuannya adalah menjaga agar data tetap konsisten, mencegah konflik, dan memastikan setiap proses berjalan dengan urutan yang benar. Tanpa sinkronisasi, program bisa menghasilkan data yang salah atau perilaku yang tidak terduga.

Kesimpulan Masalah Deadlock

Deadlock adalah kondisi ketika dua atau lebih proses saling menunggu sumber daya yang tidak pernah dilepaskan sehingga semuanya berhenti dan tidak ada yang bisa lanjut. Deadlock terjadi karena perebutan sumber daya dan kondisi saling menunggu yang tidak terselesaikan. Untuk mencegahnya, sistem harus mengatur penggunaan sumber daya dengan baik, seperti menghindari saling tunggu atau memberi batasan kapan proses boleh meminta sumber daya.

---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.
2. Mengapa sinkronisasi diperlukan dalam sistem operasi?
3. Jelaskan perbedaan antara semaphore dan monitor.1. Empat kondisi utama penyebab deadlock (Coffman Conditions)

  **Jawaban**

1.  Deadlock hanya bisa terjadi jika keempat kondisi berikut terpenuhi secara bersamaan:

- Mutual Exclusion (Eksklusi Saling Mengunci)
Sumber daya tidak dapat digunakan oleh lebih dari satu proses pada waktu yang sama.

- Hold and Wait (Menahan dan Menunggu)
Proses sudah memegang satu resource, lalu menunggu resource lain yang sedang dipegang proses lain.

- No Preemption (Tidak Ada Perebutan)
Resource tidak bisa diambil paksa oleh sistem; hanya bisa dilepaskan secara sukarela oleh proses.

- Circular Wait (Menunggu Secara Melingkar)
Terjadi rantai proses A menunggu resource yang dipegang B, B menunggu resource yang dipegang C, dan seterusnya hingga kembali ke A.


2. Mencegah Race Condition
Ketika beberapa proses/threads mengakses data bersama secara bersamaan, hasil bisa salah jika tidak disinkronkan.

- Mengatur akses ke resource bersama (shared resources)
Supaya tidak terjadi konflik data, contoh: dua proses menulis file yang sama.

- Menjamin Konsistensi Data
Sinkronisasi memastikan urutan eksekusi yang benar sehingga data tidak rusak.

- Koordinasi antar proses/thread
Beberapa proses perlu menunggu proses lain menyelesaikan tugas tertentu.

3. 
| **Aspek**                | **Semaphore**                                         | **Monitor**                                                                                      |
| ------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Konsep**               | Variabel integer khusus untuk mengatur akses resource | Struktur abstraksi tingkat tinggi yang berisi variabel, prosedur, dan mekanisme penguncian       |
| **Cara Kerja**           | Menggunakan operasi `wait()` (P) dan `signal()` (V)   | Menggunakan mekanisme lock otomatis dan *condition variable*                                     |
| **Level Abstraksi**      | Lebih rendah (low-level)                              | Lebih tinggi (high-level)                                                                        |
| **Kesalahan Penggunaan** | Mudah salah (misal lupa signal)                       | Lebih aman karena penguncian otomatis                                                            |
| **Kompleksitas**         | Lebih kompleks dan rawan deadlock                     | Lebih sederhana untuk programmer                                                                 |
| **Contoh Pemakaian**     | Sinkronisasi dasar, mutual exclusion sederhana        | Sinkronisasi yang lebih terstruktur di bahasa seperti Java, C#, dan Python (via locks/condition) |


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
