
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas
- **Nama**  : Faiq Atha Rulloh 
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---
## Identitas Kelompok 
- **Nama**, **NIM Mahasiswa**, **Tugas** :
1. Hendra Farid Hidayat, (250320572), Dokumentasi
2. Abdi Hanafi Alghifari, (250320570), Implementasi
3. Faiq Atha Rulloh, (250320571), Analisis
4. Alfan Nur Fadzillah, (250320575), Analisis 
- **Kelas** : 1DSRA

---

## A. Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme sinkronisasi proses dan penanganan deadlock** dalam sistem operasi.  
Tujuan utamanya adalah memahami bagaimana beberapa proses dapat berjalan secara bersamaan (concurrent) tanpa menyebabkan konflik data atau kebuntuan sumber daya (*deadlock*).

Mahasiswa akan melakukan studi kasus berbasis **Dining Philosophers Problem**, yaitu permasalahan klasik sinkronisasi yang menggambarkan bagaimana proses harus berbagi sumber daya terbatas (chopstick, mutex, semaphore) tanpa menimbulkan deadlock.  

Eksperimen ini dilakukan secara berkelompok, difokuskan pada:
- Analisis kondisi terjadinya deadlock.
- Implementasi solusi sinkronisasi menggunakan *semaphore* atau *monitor*.
- Dokumentasi perbandingan versi deadlock dan versi fixed.

---

## B. Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengidentifikasi empat kondisi penyebab deadlock (*mutual exclusion, hold and wait, no preemption, circular wait*).  
2. Menjelaskan mekanisme sinkronisasi menggunakan *semaphore* atau *monitor*.  
3. Menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Menyajikan hasil studi kasus secara sistematis.  

---

## C. Pendahuluan
 **Latar Belakang**
 -  *Concurrency generally means ‘multiple things going on at the same time* atau konkruensi secara umum didefiniskan sebagai 'hal-hal yang dikerjakan dalam waktu bersamaan', (OSTEP, 2018).
 -  Konkruensi terjadi di dalam sistem operasi karena banyaknya tugas-tugas dilakukan secara bersamaan di dalam program. Deadlock memiliki pengertian, *a set of blocked processes each holding a resource and waiting to acquire a resource held by another process in the set* atau seperangkat proses yang diblokir, masing-masing memegang sebuah sumber daya dan menunggu untuk memperoleh sumber daya yang dimiliki oleh proses lain dalam himpunan tersebut, (Silberschatz, Galvin & Gagne, Operating System Concepts, 10th Edition, Wiley, 2018).
 -  Buku itu juga menjelaskan bahwa terdapat empat kondisi yang memenuhi syarat terjadinya deadlock, yaitu,
    -  *Mutual exclusion*, setidaknya satu sumber daya tidak bisa dibagi atau hanya satu proses pada satu waktu.
    -  *Hold and wait*, sebuah proses memegang satu atau lebih sumber daya, sambil menunggu sumber daya lain yang dipegang oleh proses lain.
    -  *No preemption*, sumber daya yang sudah dipegang proses tidak bisa direbut paksa; hanya dilepas secara sukarela oleh proses yang memegangnya.
    -  *Circular wait*, terdapat rangkaian proses {P0, P1, …, Pn} dimana P0 menunggu sumber daya yang dipegang P1, P1 menunggu dari P2, …, Pn menunggu dari P0. Jadi, konkruensi deadlock adalah sekumpulan tugas yang dilakukan dalam satu waktu dengan terpenuhinya keempat syarat, yaitu *mutual exclusion*; *hold and wait*; *no preemption*; dan *circular wait*, sehingga program tidak berjalan atau terjadi deadlock.
    
> Tugas kelompok ini diberikan dengan tujuan utama untuk mengetahui dan memahami konkruesi deadlock secara berkelompok. Pemberian tugas secara berkelompok juga memudahkan mahasiswa-mahasiswa yang terkait dan melatih kerja sama tim dalam menyelesaikan masalah-masalah IT.

---

## D. Dasar Teori
1. Pendekatan pembelajaran sistem operasi modern menunjukkan bahwa sinkronisasi harus sederhana, aman dari deadlock dan starvation, serta efisien dalam sistem multiprosesor. (OSTEP, 2018).
2. Deadlock terjadi ketika sekumpulan proses menunggu sumber daya yang dimiliki satu sama lain sehingga tidak ada proses yang dapat melanjutkan eksekusi. (Silberschatz, Galvin, & Gagne, 2018).
3. Empat syarat utama penyebab deadlock adalah mutual exclusion, hold and wait, no preemption, dan circular wait. (Silberschatz, Galvin, & Gagne, 2018).
4. Pengendalian deadlock dapat dilakukan melalui empat strategi: pencegahan (prevention), penghindaran (avoidance), deteksi (detection), dan pemulihan (recovery). (OSTEP, 2018).

---

## E. Rumusan Masalah
1. Kenapa deadlock bisa terjadi?
2. Apa mekanisme pencegahan deadlock?
3. Bagaimana cara mengatasi kasus deadlock? 

---

## F. Metode
-  Metode yang digunakan dalam menyelesaikan tugas ini adalah metode eksperimen dengan menggunakan bahasa pemrograman Python. Python cenderung lebih mudah dibandingkan bahasa-bahasa pemrograman yang lainnya sehingga dipilih untuk menuangkan bahasa pseudocode ke dalam bahasa Python.

---


## G. Hasil 
1. Laporan tugas di file laporan.md masing-masing anggota.
2. Screenshots pada file praktikum screenshots masing-masing anggota.
3. Screenshoots hasil :
- Versi Deadlock 
![Screenshot hasil](<screenshots/cd7_kelompok_DEADLOCK.png>)

- Versi Fixed (Semaphore)
![Screenshot hasil](<screenshots/cd7_kelompok_FIXED.png>)
---

## H. Analisis

1. Kode inti dalam pseudocode:
```bash
while true:
  think()
  pick_left_fork()
  pick_right_fork()
  eat()
  put_left_fork()
  put_right_fork()
```

2. Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)
```bash
import threading
import time
import random

N = 5  # jumlah filosof
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        print(f"Philosopher {i} thinking...")
        time.sleep(random.random())

        print(f"Philosopher {i} tries to pick LEFT fork {left}")
        forks[left].acquire()  # pick_left_fork()

        print(f"Philosopher {i} tries to pick RIGHT fork {right}")
        forks[right].acquire()  # pick_right_fork()

        print(f"Philosopher {i} eating...")
        time.sleep(random.random())

        forks[left].release()  # put_left_fork()
        forks[right].release()  # put_right_fork()
        print(f"Philosopher {i} finished eating, forks released.\n")

# Menjalankan simulasi
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.daemon = True
    threads.append(t)
    t.start()

# Biarkan berjalan beberapa waktu
time.sleep(5)
print("Simulasi selesai (DEADLOCK!)")
```
- Identifikasi waktu dan alasan deadlock terjadi
> Deadlock terjadi ketika kelima filosof secara bersamaan berhasil mengambil garpu di kiri mereka, tetapi semuanya belum mendapatkan garpu di kanan mereka. Sehingga semua *philosopher* menunggu. Deadlock terjadi.
- Deadlock tidak akan terjadi apabila tidak dipenuhinya empat alasan deadlock. Alasan terjadinya deadlock dalam bentuk tabel: 

| Kondisi          | Penjelasan                                                                   |
| ---------------- | ---------------------------------------------------------------------------- |
| Mutual Exclusion | Garpu hanya bisa dipegang satu filosof pada satu waktu (Lock).               |
| Hold and Wait    | Filosof sudah memegang garpu kiri sambil menunggu garpu kanan.               |
| No Preemption    | Garpu tidak bisa diambil paksa — hanya dilepas oleh pemilik lock.            |
| Circular Wait    | F0 menunggu F1 → F1 menunggu F2 → … → F4 menunggu F0 (sirkular).             |

3. Eksperimen 2 - Versi Fixed (Menggunakan Semaphore / Monitor)
```bash
import threading
import time
import random

N = 5  # jumlah filosof
forks = [threading.Lock() for _ in range(N)]
waiter = threading.Semaphore(N - 1)  # memastikan tidak semua filosof mengambil garpu simultan

def philosopher(i):
    left = i
    right = (i + 1) % N

    while True:
        print(f"Philosopher {i} thinking...")
        time.sleep(random.random())

        print(f"Philosopher {i} waiting for permission (semaphore)")
        waiter.acquire()  # izin untuk mengambil garpu

        print(f"Philosopher {i} picks LEFT fork {left}")
        forks[left].acquire()

        print(f"Philosopher {i} picks RIGHT fork {right}")
        forks[right].acquire()

        print(f"Philosopher {i} eating...")
        time.sleep(random.random())

        forks[left].release()
        forks[right].release()
        waiter.release()  # izin dikembalikan

        print(f"Philosopher {i} finished eating, forks released.\n")

# Menjalankan simulasi
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.daemon = True
    threads.append(t)
    t.start()

time.sleep(10)
print("FIXED")
```
- Deadlock bisa dicegah karena adanya penggunaan *semaphore*
```bash
waiter = threading.Semaphore(N - 1)  # memastikan tidak semua filosof mengambil garpu simultan
```
- Bukti bahwa deadlock bisa diatasi, yaitu semua filosof tidak bisa memegang satu garpu sekaligus, karena *semaphore* membatasi hanya 4 filsuf yang boleh mengambil garpu.
Maka, setidaknya 1 filosof pasti akan makan, lalu melepas garpu sehingga sistem tetap bergerak.

4. Eksperimen 3 - Analisis Deadlock
- Tabel perbedaan ketika terjadinya deadlock dengan teratasinya deadlock

| Syarat Deadlock                                                      | Kode Awal (Deadlock Terjadi)                                                                                                | Kode Dengan Semaphore (Tidak Deadlock)                                                                                            |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **1. Mutual Exclusion** (resource hanya bisa dipakai 1 thread)       | Garpu menggunakan `threading.Lock()`, eksklusif                                                                            | Sama, garpu tetap eksklusif                                                                                       |
| **2. Hold and Wait** (memegang 1 resource sambil menunggu yang lain) | Filosof mengambil garpu kiri sambil menunggu garpu kanan                                                                    | Filosof masih menunggu garpu lainnya, namun tidak semua filosof dapat memasuki fase mengambil garpu karena dicegah oleh semaphore |
| **3. No Preemption** (resource tidak bisa dipaksa dilepas)           | Garpu tidak bisa direbut paksa                                                                                              | Tetap sama atau tidak ada preemption                                                                                             |
| **4. Circular Wait** (siklus tunggu melingkar)                       | Semua filosof dapat mengambil garpu kiri dan menunggu garpu kanan | Tidak terjadi, karena semaphore menahan 1 filosof agar tidak mengambil garpu, sehingga siklus tunggu terputus                     |

- Deadlock tidak terjadi karena teratasinya salah satu masalah yang menjadi salah satu syarat dari keempat syarat yang harus terpenuhi, yaitu **circular wait**. Saat deadlock terjadi, semua filosof mengambil dapat mengambil garpu kiri dan menunggu garpu kanan. Sedangkan, sistem dengan *semaphore* menahan 1 filosof agar tidak mengambil garpu.
 
---

## I. Kesimpulan
1. Deadlock hanya akan terjadi apabila keempat syaratnya terpenuhi, jika satu dari keempat syarat sudah diatasi, maka deadlock bisa dihindari.
2. *Semaphore* dapat digunakan untuk mengatasi deadlock dengan cara kerja menahan salah satu filosof untuk tidak mengambil garpu. Dengan kata lain, *semaphore* digunakan dengan cara mengurangi jumlah atau N - x, N adalah jumlah filosof sebelum dikurangi dan x adalah bilangan variabel yang menjadi pengurang.

---

## J. Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.
   - *Mutual exclusion* (saling mengunci / eksklusif), *hold and wait* (menahan dan menunggu), *no preemption* (tidak bisa dipaksa lepas), *circular wait* (menunggu secara melingkar).  
2. Mengapa sinkronisasi diperlukan dalam sistem operasi?
   -  Sinkronisasi sangat penting dalam sistem operasi karena pada lingkungan multitasking/multiprocessing, banyak proses dapat mengakses data yang sama secara bersamaan. Tanpa mekanisme sinkronisasi, operasi paralel/*multiprocessing*/*multitasking* dapat menyebabkan kekacauan, inkonsistensi data, deadlock, atau bahkan kegagalan sistem. Beberapa fungsi dari sinkronisasi dalam sistem operasi, diantaranya :
       - Menghindari mengakses dan memodifikasi data bersama secara bersamaan.
       - Menjamin konsistensi data, sinkronisasi diperlukan sehingga ketika terdapat proses pengubahan suatu data, proses lain tidak akan terkait dengan data yang sedang diproses.
       - Koordinasi kerja antar proses, beberapa program memerlukan kolaborasi dan komunikasi. Sinkronisasi mengatur kapan suatu proses harus menunggu atau melanjutkan.
3. Jelaskan perbedaan antara *semaphore* dan *monitor*.  
- Di dalam tabel perbedaan
  
| Semaphore                                           | Monitor                                                                                 |
| --------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Mekanisme sinkronisasi berbasis variabel penghitung | Mekanisme sinkronisasi berbasis objek yang mengelola akses otomatis ke critical section |
| Menggunakan operasi `wait()` dan `signal()`         | Menggunakan *mutual exclusion* internal + *condition variables*                         |
| Bersifat *low-level*                                | Bersifat *high-level*                                                                   |

---

## K. Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  -  Yang paling menantang bagi saya adalah memahami bagaimana deadlock benar-benar terjadi dalam kode dan mengapa solusi tertentu berhasil sementara yang lain tidak.
- Bagaimana cara Anda mengatasinya?
  -  Pokoknya Kuncinya adalah Pahami bahwa deadlock semua saling tunggu tanpa akhir, dan solusinya pastikan selalu ada yang bisa maju.



---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
