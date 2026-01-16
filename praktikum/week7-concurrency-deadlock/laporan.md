
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock  

---

## Nama Anggota :

- Gilang Ananda Putra [250202939]
- Faizal Muzaki [250202937]
- Rivan Ahmad Ardiansyah [220202715]
 
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengidentifikasi empat kondisi penyebab deadlock (*mutual exclusion, hold and wait, no preemption, circular wait*).  
2. Menjelaskan mekanisme sinkronisasi menggunakan *semaphore* atau *monitor*.  
3. Menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Menyajikan hasil studi kasus secara sistematis.  

---

## Dasar Teori
### 1. Sinkronisasi dan Kondisi Kritis

- **Kondisi Kritis (Critical Section)** adalah bagian dari kode di mana sebuah proses mengakses **sumber daya bersama (shared resource)**.  
- Sinkronisasi diperlukan untuk menjamin **Saling Eksklusi (Mutual Exclusion)**:  
  - Hanya **satu proses** yang diizinkan berada di Kondisi Kritis pada satu waktu  
  - Mencegah **race condition** dan **inkonsistensi data**
- **Mekanisme sinkronisasi** yang umum digunakan:  
  - **Mutex:** untuk saling eksklusi biner  
  - **Semaphore:** untuk mengontrol jumlah akses ke sumber daya

---

### 2. Definisi dan Kondisi Deadlock

- **Deadlock** adalah kebuntuan permanen di mana sekumpulan proses **saling menunggu sumber daya** yang dipegang oleh proses lain dalam set yang sama.  
- **Deadlock terjadi jika keempat kondisi Coffman berikut terpenuhi secara simultan:**

| Kondisi Coffman             | Penjelasan |
|------------------------------|------------|
| **Saling Eksklusi**         | Sumber daya tidak dapat dibagi, hanya satu proses yang bisa menggunakannya pada satu waktu. |
| **Kepemilikan dan Tunggu (Hold and Wait)** | Proses menahan sumber daya yang sudah dimiliki sambil menunggu sumber daya tambahan. |
| **Tidak Ada Prempsi (No Preemption)** | Sumber daya tidak dapat direbut paksa dari proses yang memilikinya. |
| **Tunggu Melingkar (Circular Wait)** | Terdapat rantai proses tertutup di mana setiap proses menunggu sumber daya yang dipegang oleh proses berikutnya. |

---

### 3. Masalah Filosof Makan dan Pencegahan

- **Masalah Lima Filosof Makan (Dining Philosophers Problem)** adalah model klasik untuk menggambarkan deadlock.  
  - Setiap filosof (proses) membutuhkan **dua garpu (sumber daya)** yang dipegang oleh tetangganya.  
  - Implementasi yang tidak terkoordinasi akan menciptakan **Tunggu Melingkar (Circular Wait)**.
- **Pencegahan Deadlock** dilakukan dengan membatalkan setidaknya satu dari empat kondisi Coffman (biasanya kondisi 2 atau 4).  
- **Solusi umum dalam masalah ini:**
  1. **Pembatasan Akses:**  
     - Menggunakan **Semaphore penghitung** untuk membatasi jumlah filosof yang boleh makan menjadi $N-1$.  
  2. **Pengurutan Sumber Daya:**  
     - Memaksakan urutan pengambilan sumber daya (garpu) secara konsisten, atau  
     - Asimetris: membuat satu filosof mengambil garpu dalam urutan terbalik untuk memecah circular wait.

---

## Langkah Praktikum
1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

---


---

## Hasil Eksekusi dan Analisis

### Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)

- **kode**

```python
import threading
import time

N = 5  
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    while True:
        print(f"Filosof {i} sedang berpikir...")
        time.sleep(1)

        forks[i].acquire()
        print(f"Filosof {i} mengambil garpu kiri {i}")

        forks[(i+1) % N].acquire()
        print(f"Filosof {i} mengambil garpu kanan {(i+1)%N}")

        print(f"Filosof {i} sedang makan...")
        time.sleep(2)

        forks[i].release()
        forks[(i+1) % N].release()
        print(f"Filosof {i} selesai makan dan meletakkan garpu")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
```

- **Analisis**

   Kode pertama adalah implementasi standar dan paling sederhana dari masalah **Lima Filosof Makan**.

- **Strategi**

   Semua filosof mengikuti aturan yang sama:
   - Selalu mengambil **garpu kiri** terlebih dahulu  
   - Kemudian mengambil **garpu kanan**

-  **Risiko Deadlock: Sangat Tinggi**

   Deadlock bisa terjadi jika semua 5 filosof (P0 hingga P4) secara bersamaan berhasil mengambil garpu kiri mereka (F0 hingga F4).  
   Ini menyebabkan kondisi **tunggu melingkar (circular wait)**:

   - Setiap filosof memegang satu garpu (garpu kiri)
   - Mereka menunggu garpu kanan yang sedang dipegang oleh tetangganya
   - Tidak ada yang bisa melanjutkan → **deadlock**

---

- **Analisis Berdasarkan Kondisi Coffman**

| Kondisi Coffman            | Status | Keterangan |
|----------------------------|--------|------------|
| **Saling Eksklusi**        | Ya     | Garpu (lock) hanya bisa dipakai 1 filosof. |
| **Kepemilikan & Tunggu**  | Ya     | Filosof memegang 1 garpu sambil menunggu garpu lain. |
| **Tidak Ada Prempsi**     | Ya     | Garpu tidak bisa direbut paksa. |
| **Tunggu Melingkar**       | Ya     | $P_0$ menunggu $F_1$, $P_1$ menunggu $F_2$, ..., $P_4$ menunggu $F_0$. |

Semua kondisi Coffman terpenuhi → **deadlock pasti dapat terjadi**.

### Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)

- **kode**

```python
import threading
import time

N = 5
forks = [threading.Lock() for _ in range(N)]
semaphore = threading.Semaphore(N-1)

def philosopher(i):
    while True:
        print(f"Filosof {i} sedang berpikir...")
        time.sleep(1)

        semaphore.acquire()

        if i == N-1:
            forks[(i+1) % N].acquire()
            print(f"Filosof {i} mengambil garpu kanan {(i+1)%N}")
            forks[i].acquire()
            print(f"Filosof {i} mengambil garpu kiri {i}")
        else:
            forks[i].acquire()
            print(f"Filosof {i} mengambil garpu kiri {i}")
            forks[(i+1) % N].acquire()
            print(f"Filosof {i} mengambil garpu kanan {(i+1)%N}")

        print(f"Filosof {i} sedang makan...")
        time.sleep(2)


        forks[i].release()
        forks[(i+1) % N].release()
        semaphore.release()
        print(f"Filosof {i} selesai makan dan meletakkan garpu")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
```

- **Analisis**
 
   Kode kedua adalah implementasi yang telah dimodifikasi untuk **mencegah deadlock** dengan menggunakan dua strategi utama: **Semaphore** dan **pengurutan pengambilan sumber daya yang asimetris**.

- **Pencegahan 1: Menggunakan Semaphore**

   - ```semaphore = threading.Semaphore(N-1)``` 
      Membatasi hanya **N-1 (4) filosof** yang diizinkan masuk ke "ruang makan" (yaitu, mencoba mengambil garpu) pada satu waktu.  
   - **Hasil:**  
      - Tidak mungkin semua 5 filosof memegang garpu secara bersamaan.  
      - Jika 4 filosof masuk dan memegang 4 garpu, selalu ada **1 garpu bebas** yang memungkinkan salah satu filosof menyelesaikan aksinya → **memecah lingkaran tunggu**.

   - **Risiko Deadlock: Sangat Rendah (Aman dari Deadlock).**

### Eksperimen 3 – Analisis Deadlock

**1. Analisis Kondisi Deadlock pada Versi Deadlock**


   - **Mutual Exclusion (Saling Eksklusi)**

      - Setiap garpu hanya dapat digunakan oleh **satu** filosof pada satu waktu.  
      - Garpu adalah *shared resource* non-sharable → kondisi ME terpenuhi.

   - **Hold and Wait (Menahan & Menunggu)**

      - Setiap filosof memegang garpu kiri **sambil menunggu** garpu kanan.  
      - Setiap proses menahan sebagian resource → kondisi HE terpenuhi.

   - **No Preemption (Tidak Ada Preemption)**

      - Garpu tidak bisa direbut paksa dari filosof lain.  
      - Tidak ada mekanisme sistem untuk memaksa melepas resource.  
      - Proses hanya melepas garpu setelah selesai makan.

   - **Circular Wait**

      - Filosof 0 menunggu filosof 1  
      - Filosof 1 menunggu filosof 2  
      - …  
      - Filosof 4 menunggu filosof 0  
      - Terjadi lingkaran menunggu → syarat utama deadlock tercapai.

**2. Analisis Solusi pada Versi Fixed**

Pada versi fixed digunakan salah satu strategi, misalnya:

- **Semaphore room(4)** → hanya maksimal 4 filosof boleh mencoba mengambil garpu.  
- **Mengubah urutan pengambilan garpu**, misalnya filosof terakhir mengambil garpu kanan terlebih dahulu.  
- **Menambahkan mutex** saat proses mengambil garpu.  

Solusi ini menghilangkan satu atau lebih kondisi Coffman, sehingga deadlock dapat dicegah.

**3. Tabel Analisis Deadlock**

| **Kondisi Deadlock** | **Terjadi di Versi Deadlock?** | **Mengapa Terjadi?**                                                         | **Solusi di Versi Fixed**                                                                                            |
| -------------------- | ------------------------------ | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Mutual Exclusion** | Ya                             | Garpu hanya dapat dipegang oleh satu filosof                                 | Tetap ada, tetapi dikontrol dengan semaphore/mutex sehingga alurnya aman                                            |
| **Hold and Wait**    | Ya                             | Filosof menahan satu garpu sambil menunggu garpu berikutnya                  | Menghindari proses menahan sebagian resource tanpa jaminan ketersediaan (misal *waiter* atau `room=4`)               |
| **No Preemption**    | Ya                             | Tidak ada mekanisme melepas paksa garpu                                      | Garpu hanya boleh diambil jika *dua-duanya tersedia*, sehingga tidak perlu preemption                               |
| **Circular Wait**    | Ya                             | Semua filosof memegang garpu kiri dan menunggu garpu kanan → lingkaran penuh | Menghilangkan cycle: mengubah urutan pengambilan garpu atau membatasi jumlah filosof (room=4)                       |

---

## Kesimpulan
### 1. Kegagalan Sinkronisasi Mengakibatkan Deadlock
- Implementasi sederhana dari **Dining Philosophers Problem**, di mana semua proses (filosof) mencoba memperoleh sumber daya (garpu) dalam urutan yang sama, secara inheren **memenuhi empat kondisi Coffman**:  
  - Tunggu Melingkar  
  - Saling Eksklusi  
  - Kepemilikan dan Tunggu  
  - Tidak Ada Prempsi  
- Hal ini membuktikan bahwa **kegagalan dalam perencanaan urutan akses sumber daya** dalam lingkungan konkuren akan memicu **deadlock** dan menghentikan kemajuan sistem.

### 2. Pencegahan Deadlock Dapat Dicapai dengan Pembatasan Sumber Daya
- Deadlock dapat dihindari dengan memutus salah satu dari **empat kondisi Coffman**.  
- Dalam praktikum ini, pencegahan dilakukan melalui:  
  1. **Pembatasan Akses menggunakan Semaphore Penghitung**  
     - Membatasi maksimum **$N-1$ filosof** yang makan pada satu waktu  
  2. **Pengurutan Sumber Daya Asimetris**  
     - Mengubah urutan pengambilan garpu untuk satu filosof  
- Solusi ini **menghilangkan kondisi Tunggu Melingkar** dan menjamin sistem selalu memiliki **kemajuan (progress)**.

### 3. Pentingnya Mekanisme Sinkronisasi Tingkat Lanjut
- Masalah ini menegaskan perlunya mekanisme sinkronisasi tingkat lanjut (**Semaphore** atau **Monitor**) dalam sistem operasi.  
- Mekanisme ini:  
  - Menjamin **Saling Eksklusi** di Kondisi Kritis  
  - Memungkinkan **kontrol alokasi sumber daya** yang lebih halus  
  - Sangat krusial untuk **mencegah kebuntuan** dalam sistem kompleks dan multithreaded

---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock. 

   **Jawaban:**  

   1. **Saling Eksklusi (Mutual Exclusion):**  
      Sumber daya hanya dapat dipegang oleh **satu proses** pada satu waktu.

   2. **Kepemilikan dan Tunggu (Hold and Wait):**  
      Proses menahan setidaknya satu sumber daya sambil menunggu untuk memperoleh sumber daya tambahan yang sedang dipegang oleh proses lain.

   3. **Tidak Ada Prempsi (No Preemption):**  
      Sumber daya yang dipegang tidak dapat diambil secara paksa; hanya dapat dilepaskan secara sukarela oleh proses yang memegangnya.

   4. **Tunggu Melingkar (Circular Wait):**  
      Terdapat serangkaian proses tertutup di mana setiap proses dalam rantai menunggu sumber daya yang dipegang oleh proses berikutnya.


2. Mengapa sinkronisasi diperlukan dalam sistem operasi? 

   **Jawaban:**  

   1. **Mencegah Inkonsistensi Data (Data Inconsistency):**  
      - Dalam lingkungan multitasking atau multithreaded, banyak proses atau thread mungkin mengakses dan memodifikasi data bersama secara bersamaan.  
      - Tanpa sinkronisasi, urutan operasi dapat menyebabkan **race condition** yang menghasilkan nilai data salah atau tidak terduga.

   2. **Memastikan Saling Eksklusi:**  
      - Hanya **satu proses** yang berada di Kondisi Kritis (segmen kode yang mengakses sumber daya bersama) pada satu waktu, sehingga **integritas data terjaga**.


3. Jelaskan perbedaan antara *semaphore* dan *monitor*. 

   **Jawaban:**  

| Fitur               | Semaphore                                           | Monitor                                                      |
|--------------------|----------------------------------------------------|-------------------------------------------------------------|
| **Konsep**          | Mekanisme sinkronisasi tingkat rendah (variabel integer) | Konstruksi tingkat tinggi (struktur bahasa pemrograman)    |
| **Implementasi**    | Hanya memiliki dua operasi atomik: `wait()` (P) dan `signal()` (V) | Menggabungkan data bersama, prosedur (method) untuk memanipulasi data, dan mekanisme sinkronisasi ke dalam satu unit |
| **Akses**           | Kesalahan programmer (misal lupa memanggil `wait()` atau `signal()`) dapat merusak mekanisme saling eksklusi | Saling eksklusi dijamin otomatis oleh compiler/runtime; programmer tidak perlu mengelola lock secara eksplisit |
| **Kemudahan**       | Sulit diimplementasikan dengan benar, rentan deadlock atau kesalahan waktu | Lebih aman dan mudah digunakan karena menyederhanakan proses sinkronisasi |
 
 
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
  
   Kesulitan memahami deadlock

- Bagaimana cara Anda mengatasinya? 

   mempelajari dan memahami pengertian dan ciri-ciri deadlock

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
