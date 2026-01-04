
# Laporan Praktikum Minggu [10]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Mohammad Ftikh Mahsun
- **NIM**   : 250202952
- **Kelas** : 1IKRB

---

## Tujuan
•Memahami konsep manajemen memori virtual pada sistem operasi, khususnya mekanisme page replacement yang digunakan ketika terjadi page fault.

•Menerapkan dan mengimplementasikan algoritma page replacement FIFO (First-In First-Out) dan LRU (Least Recently Used) ke dalam sebuah program simulasi berbasis terminal.

•Mensimulasikan proses penggantian halaman menggunakan dataset yang telah ditentukan serta jumlah frame memori tertentu untuk melihat alur kerja masing-masing algoritma.

•Menghitung, mencatat, dan menganalisis jumlah page fault yang dihasilkan oleh algoritma FIFO dan LRU selama proses simulasi berlangsung.

•Membandingkan performa algoritma FIFO dan LRU berdasarkan hasil simulasi untuk mengetahui algoritma mana yang lebih efisien dan efektif dalam pengelolaan memori.

---

## Dasar Teori
1.Manajemen memori virtual adalah teknik yang digunakan oleh sistem operasi untuk mengatur penggunaan memori agar program dapat berjalan dengan efisien, meskipun kapasitas memori fisik terbatas. Sistem ini bekerja dengan membagi memori ke dalam satuan kecil yang disebut page, sehingga proses pemindahan data antara memori utama dan penyimpanan sekunder dapat dilakukan secara teratur.

2.Ketika suatu proses membutuhkan halaman yang belum tersedia di memori utama, maka akan terjadi kondisi yang disebut  page fault. Pada kondisi ini, sistem operasi harus memilih salah satu halaman yang sudah ada di memori untuk digantikan, sehingga diperlukan algoritma page replacement untuk menentukan halaman mana yang akan dikeluarkan.

3.Algoritma FIFO (First-In First-Out) merupakan algoritma page replacement paling sederhana, di mana halaman yang pertam kali masuk ke memori akan menjadi halaman pertama yang diganti. Algoritma ini tidak memperhatikan frekuensi maupun        waktu terakhir penggunaan halaman, sehingga dalam beberapa kasus dapat menghasilkan jumlah page fault yang cukup besar.

4.Algoritma LRU (Least Recently Used) bekerja dengan mengganti halaman yang paling lama tidak diakses berdasarkan riwayat penggunaan. Dengan mempertimbangkan pola akses halaman, algoritma ini lebih mendekati perilaku penggunaan memori secara nyata, sehingga halaman yang sering digunakan dapat dipertahankan lebih lama di memori.

5.Perbedaan cara kerja antara algoritma FIFO dan LRU menyebabkan perbedaan hasil pada simulasi page replacement. Umumnya, LRU menghasilkan jumlah page fault yang lebih sedikit dibandingkan FIFO karena algoritma ini lebih adaptif terhadap pola akses program, sehingga pengelolaan memori menjadi lebih efisien.

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
 potongan ko
mes
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
Berdasarkan hasil simulasi page replacement menggunakan reference string yang telah ditentukan dengan jumlah 3 frame memori, diperoleh perbedaan jumlah page fault antara algoritma FIFO dan LRU. Pada algoritma FIFO, jumlah page fault yang dihasilkan lebih banyak dibandingkan dengan algoritma LRU. Hal ini terjadi karena FIFO mengganti halaman berdasarkan urutan kedatangan tanpa mempertimbangkan apakah halaman tersebut masih sering digunakan atau tidak.

Pada simulasi FIFO, halaman yang pertama kali masuk ke memori akan digantikan terlebih dahulu ketika terjadi page fault. Akibatnya, beberapa halaman yang sebenarnya masih dibutuhkan kembali justru dikeluarkan dari memori, sehingga menyebabkan terjadinya page fault tambahan. Kondisi ini menunjukkan bahwa FIFO kurang efektif dalam mengikuti pola akses halaman pada program.

Sementara itu, algoritma LRU menghasilkan jumlah page fault yang lebih sedikit karena mengganti halaman yang paling lama tidak digunakan. Dengan mempertimbangkan riwayat akses halaman, LRU mampu mempertahankan halaman yang sering diakses agar tetap berada di memori. Hal ini membuat proses penggantian halaman menjadi lebih efisien dan sesuai dengan perilaku penggunaan memori secara nyata.

Perbedaan hasil antara FIFO dan LRU menunjukkan bahwa algoritma page replacement yang mempertimbangkan pola penggunaan halaman cenderung memberikan performa yang lebih baik. Oleh karena itu, berdasarkan hasil percobaan ini, algoritma LRU dapat dikatakan lebih efisien dibandingkan FIFO dalam mengelola memori untuk dataset yang digunakan.

---

## Kesimpulan
Berdasarkan hasil praktikum yang telah dilakukan, dapat disimpulkan bahwa algoritma page replacement FIFO dan LRU memiliki perbedaan cara kerja dalam mengganti halaman di memori. Hasil simulasi menunjukkan bahwa algoritma FIFO menghasilkan jumlah page fault yang lebih banyak karena tidak mempertimbangkan pola penggunaan halaman. Sebaliknya, algoritma LRU mampu mengelola memori dengan lebih baik karena mengganti halaman yang paling lama tidak digunakan. Oleh karena itu, algoritma LRU terbukti lebih efisien dibandingkan FIFO dalam pengelolaan memori pada percobaan yang telah dilakukan.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?

Perbedaan utama antara algoritma FIFO dan LRU terletak pada cara menentukan halaman yang akan diganti ketika terjadi page fault. Algoritma FIFO mengganti halaman berdasarkan urutan kedatangan, yaitu halaman yang pertama kali masuk ke memori akan menjadi halaman pertama yang dikeluarkan. Algoritma ini tidak memperhatikan seberapa sering atau seberapa baru halaman tersebut digunakan. Sebaliknya, algoritma LRU mengganti halaman yang paling lama tidak diakses dengan mempertimbangkan riwayat penggunaan halaman. Dengan demikian, LRU lebih menyesuaikan diri dengan pola akses program dibandingkan FIFO.

2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?

FIFO dapat menghasilkan Belady’s Anomaly karena penambahan jumlah frame memori tidak selalu berdampak pada penurunan jumlah page fault. Hal ini terjadi karena FIFO tidak mempertimbangkan tingkat kepentingan atau frekuensi penggunaan suatu halaman. Akibatnya, meskipun jumlah frame ditambah, halaman yang masih sering digunakan tetap bisa tergantikan hanya karena halaman tersebut masuk lebih awal ke memori. Kondisi ini menyebabkan jumlah page fault justru bisa meningkat, yang dikenal sebagai Belady’s Anomaly.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?

LRU umumnya menghasilkan performa yang lebih baik dibandingkan FIFO karena algoritma ini mengganti halaman berdasarkan waktu terakhir penggunaan. Dengan mempertahankan halaman yang sering diakses di dalam memori, LRU dapat mengurangi kemungkinan terjadinya page fault. Selain itu, algoritma LRU lebih mendekati pola penggunaan memori secara nyata pada program, di mana halaman yang baru digunakan biasanya akan digunakan kembali dalam waktu dekat. Oleh karena itu, LRU 
cenderung lebih efisien dan stabil dibandingkan FIFO dalam pengelolaan memori.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
