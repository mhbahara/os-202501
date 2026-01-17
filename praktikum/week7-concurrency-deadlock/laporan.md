
# Laporan Praktikum Minggu [X]
# Topik: Sinkronisasi Proses dan Masalah Deadlock 
Identitas Kelompok

Nama 
1. Miftakhul Lisna Esa Baehaqi (250202951) - (Ketua) - Bagian Implementasi
2. Ilham Dzufikar Barokah (250202942) - Bagian Dokumentasi
3. Ikhsan Mu'arif (250202921) - Bagian analisis
4. Hanif Arundaya Usman (250202942) - Bagian analisis
   
Kelas : 1IKRB

---

## Tujuan
Melalui praktikum ini, mahasiswa diharapkan mampu:

1. Mengidentifikasi dan menjelaskan empat kondisi utama penyebab deadlock, yaitu:

- Mutual Exclusion

- Hold and Wait

- No Preemption

- Circular Wait

2. Menganalisis bagaimana deadlock dapat terjadi pada implementasi Dining Philosophers yang menggunakan resource bersama tanpa mekanisme pengendalian yang tepat.

3. Mengimplementasikan solusi sinkronisasi menggunakan semaphore atau monitor untuk mencegah terjadinya deadlock pada skenario Dining Philosophers.

4. Membandingkan perbedaan antara versi deadlock dan versi yang telah diperbaiki, baik dari sisi perilaku program maupun keamanan sinkronisasi.

5. Menerapkan konsep concurrency, critical section, dan akses sumber daya terbatas pada konteks pemrograman multithreaded.

6. Berkolaborasi dalam kelompok untuk menganalisis, mengimplementasikan, dan mendokumentasikan hasil eksperimen secara sistematis dan terstruktur.

---

## Dasar Teori
1. Concurrency dan Shared Resource
Concurrency adalah eksekusi beberapa proses secara bersamaan yang membutuhkan pengaturan akses resource bersama agar tidak terjadi konflik.

2. Critical Section & Race Condition
Critical section adalah bagian program yang mengakses resource bersama. Jika tidak dikendalikan, dapat terjadi race condition sehingga proses menghasilkan output tidak konsisten.

3. Deadlock
Deadlock terjadi ketika proses saling menunggu resource yang tidak pernah dilepaskan. Deadlock muncul jika empat kondisi terpenuhi: mutual exclusion, hold and wait, no preemption, dan circular wait.

4. Semaphore sebagai Mekanisme Sinkronisasi
Semaphore digunakan untuk mengontrol akses resource menggunakan operasi acquire (wait) dan release (signal), sehingga hanya proses tertentu yang dapat masuk critical section.

5. Strategi Pencegahan Deadlock
Deadlock dapat dicegah dengan mengatur urutan pengambilan resource atau membatasi jumlah proses yang dapat mengakses resource secara bersamaan, seperti pada solusi Dining Philosophers.

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
![Screenshot hasil](./screenshots/eksperimen%201.png)
![eksperimen 2](./screenshots/eksperimen%202.png)

---
## hasil eksperimen 1
1. Analisis Alur (Penjelasan)
Pada simulasi ini, setiap filosof mengikuti urutan langkah yang sama:
Berpikir
Mengambil garpu kiri
Mengambil garpu kanan
Makan
Mengembalikan garpu
2. Identifikasi Deadlock
Kapan Deadlock Terjadi?
Deadlock terjadi ketika:
Semua filosof berhasil mengambil garpu kiri,
Tetapi tidak ada satu pun yang mendapatkan garpu kanan, karena semua sudah dipegang oleh filosof di sebelahnya.

## hasil eksperimen 2
Bukti Deadlock Terhindari
Dengan membatasi maksimal 4 filosof yang boleh mengambil garpu pada saat bersamaan, minimal satu filosof pasti dapat memperoleh dua garpu dan berhasil makan, kemudian melepaskannya. Siklus ini memastikan sistem tetap berjalan dan tidak terjadi keadaan saling menunggu selamanya.

## hasil eksperimen 3
| **Kondisi Deadlock** | **Terjadi di Versi Deadlock?** | **Penjelasan pada Versi Deadlock**                                                          | **Solusi di Versi Fixed**                                                 | **Penjelasan Solusi**                                                                                                                                      |
| -------------------- | ------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mutual Exclusion** |  Ya                           | Setiap garpu hanya dapat digunakan oleh satu filosof pada satu waktu.                       | **Tetap Ada (Tidak dapat dihilangkan)** tetapi dikontrol dengan semaphore | Semaphore digunakan agar penggunaan garpu lebih teratur dan tidak saling berebut tanpa kontrol sinkronisasi.                                               |
| **Hold and Wait**    |  Ya                           | Setiap filosof mengambil satu garpu dan menunggu garpu lainnya → menyebabkan waiting chain. | **Diminimalkan**                                                          | Dengan membatasi hanya 4 filosof yang bisa mengambil garpu (semaphore `room`), tidak semua filosof menunggu sambil memegang satu garpu.                    |
| **No Preemption**    |  Ya                           | Garpu tidak dapat direbut paksa dari filosof yang sudah memegangnya.                        | **Tetap Ada**, tetapi tidak menimbulkan deadlock                          | Filosof hanya mengambil garpu jika tersedia. Setelah selesai makan garpu dilepas sesuai aturan semaphore, sehingga alur tetap berjalan.                    |
| **Circular Wait**    |  Ya                           | Semua filosof mengambil garpu kiri terlebih dahulu → membentuk lingkaran menunggu.          | **Dihilangkan**                                                           | Dengan membatasi jumlah filosof yang makan (max 4), rantai menunggu melingkar tidak terbentuk, sehingga minimal satu filosof bisa makan dan melepas garpu. |

Pada versi pertama semua kondisi deadlock terpenuhi, sehingga sistem dapat berhenti total ketika seluruh filosof saling menunggu garpu.

Pada versi fixed dengan penggunaan semaphore dan pembatasan jumlah filosof yang boleh makan, kondisi deadlock diputus terutama pada bagian circular wait dan hold and wait, sehingga tidak terjadi kebuntuan.

---

## Kesimpulan
Berdasarkan rangkaian percobaan yang telah dilakukan, dapat disimpulkan bahwa masalah Dining Philosophers merupakan contoh klasik dari permasalahan sinkronisasi dalam sistem operasi, khususnya terkait dengan pembagian sumber daya terbatas. Pada versi awal simulasi tanpa mekanisme pencegahan, sistem menunjukkan terjadinya deadlock akibat terpenuhinya empat kondisi utama: mutual exclusion, hold and wait, no preemption, dan circular wait. Hal ini menyebabkan seluruh proses berhenti dan tidak ada filosofi yang dapat melanjutkan kegiatan makan.

Setelah diterapkan solusi menggunakan semaphore dan pembatasan jumlah filosof yang dapat mengakses sumber daya secara bersamaan, deadlock dapat dihindari. Mekanisme kontrol ini memutus kondisi circular wait dan mengurangi hold and wait, sehingga proses tetap berjalan secara bergilir dan teratur. Hasil modifikasi menunjukkan bahwa sinkronisasi yang tepat sangat penting untuk menjaga alokasi sumber daya agar tetap aman, efisien, dan bebas dari deadlock.

Secara keseluruhan, praktikum ini memberikan pemahaman tentang konsep deadlock, penyebab terjadinya, serta strategi pencegahan menggunakan teknik sinkronisasi seperti semaphore dan monitor.
---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.
  
- Pengecualian Bersama (persaingan untuk mendapatkan barang):

Ada sumber daya yang hanya bisa digunakan oleh satu orang atau proses saja. Jadi jika satu orang sudah menggunakannya, yang lainnya harus menunggu.

- Menahan dan Menunggu (sudah memiliki barang, masih meminta lebih):

Sebuah proses sudah memiliki satu sumber daya, tetapi masih meminta sumber daya lain. Sementara sumber daya lainnya sedang digunakan oleh proses yang berbeda.

- Tidak Ada Perampasan (barang tidak bisa diambil paksa):

Sumber daya yang sudah digunakan oleh suatu proses tidak boleh diambil secara paksa. Harus menunggu hingga proses tersebut selesai dan mengembalikannya secara sukarela.

- Antrian Melingkar (saling menunggu dalam siklus):

Terjadi keadaan "saling menunggu":
Proses A menunggu sumber daya yang dipegang oleh B, B menunggu C, C menunggu D, dan akhirnya D menunggu A. Hal ini menciptakan lingkaran menunggu.

2. Mengapa sinkronisasi diperlukan dalam sistem operasi?
   
* Menghindari Kekacauan Data (Race Condition)

Ketika dua proses mencoba untuk mengakses dan mengubah data yang sama secara bersamaan, hasilnya bisa menjadi tidak teratur. Sinkronisasi menjamin bahwa hanya satu proses yang dapat mengakses data penting pada satu waktu.

* Memastikan Keberlangsungan Data

Tanpa sinkronisasi, nilai data dapat berubah tanpa sesuai dengan logika program. Contoh: kedua proses dapat menambah saldo, namun hasil akhirnya keliru karena keduanya mengambil nilai yang lama.

* Mengelola Akses ke Sumber Daya Bersama

Beberapa sumber daya seperti file, memori, printer, dan buffer tidak dapat digunakan secara bersamaan. Sinkronisasi membuat proses harus menunggu gilirannya.

* Menghindari Deadlock dan Situasi Macet Lain

Dengan menggunakan mekanisme sinkronisasi yang tepat seperti mutex, semaphore, dan monitor, sistem bisa mencegah kondisi di mana proses saling menunggu dan menyebabkan sistem terhenti.

* Memfasilitasi Eksekusi Paralel yang Aman

Tujuan utama dari multiprogramming dan multicore adalah untuk melaksanakan banyak tugas secara bersamaan. Sinkronisasi memastikan bahwa semua tugas tersebut berjalan dengan aman, teratur, dan tidak merusak data.
     
3. Jelaskan perbedaan antara semaphore dan monitor.  

Semaphore (seperti cara mengantre)

Semaphore adalah seperti mengantre menggunakan nomor.

* Ada angka yang menunjukkan berapa banyak orang yang bisa masuk.

* Jika nomornya masih ada → kamu bisa masuk.

* Jika sudah habis → kamu harus menunggu.

* Kamu sendiri yang harus ingat untuk “mengambil nomor” dan “mengembalikan nomor”.

Kesimpulannya:
Semaphore adalah sistem antrean yang perlu kamu atur sendiri.

Monitor (seperti ruangan dengan pintu otomatis)

Monitor itu seperti ruangan dengan pintu yang mengunci sendiri.

* Hanya satu orang yang dapat masuk.

* Saat kamu masuk, pintunya langsung terkunci otomatis.

* Ketika kamu keluar, pintunya otomatis terbuka.

* Kamu tidak perlu mengurus kuncinya sendiri.

Kesimpulannya:
Monitor adalah sistem yang mengurus kuncinya sendiri, sehingga lebih aman dan mudah.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
