
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : [Mohammad Fatikh Mahsun]  
- **NIM**   : [250202952]  
- **Kelas** : [1IKRB]

---

### Judul

### Analisis Komparatif Performa Algoritma Penjadwalan First-Come First-Served (FCFS) dan Shortest Job First (SJF) terhadap Rata-rata Waktu Tunggu (Average Waiting Time).

---

## 1. Introduction (Pendahuluan)
### 1.1 Latar Belakang

Dalam sistem komputer multiprogramming, CPU merupakan sumber daya paling berharga yang harus dikelola dengan efisien. Karena jumlah proses yang ingin berjalan sering kali lebih banyak daripada jumlah inti CPU yang tersedia, sistem operasi memerlukan mekanisme pengaturan antrean yang disebut dengan penjadwalan CPU (CPU Scheduling). Efisiensi dari algoritma penjadwalan ini menjadi penentu utama dalam produktivitas sistem, terutama dalam menjaga agar waktu tunggu proses di dalam antrean tetap minimal.

Algoritma First-Come, First-Served (FCFS) merupakan metode penjadwalan paling dasar yang bekerja berdasarkan prinsip antrean linear. Namun, pada praktiknya, FCFS sering kali menghadapi kendala efisiensi yang dikenal sebagai Convoy Effect. Fenomena ini terjadi ketika proses dengan waktu eksekusi (burst time) yang besar menempati CPU dalam waktu lama, sehingga menyebabkan proses-proses kecil di belakangnya tertahan secara tidak proporsional. Masalah ini berdampak buruk pada Average Waiting Time (AWT) sistem secara keseluruhan.

Sebagai solusi optimal secara teoritis, algoritma Shortest Job First (SJF) diperkenalkan untuk memperbaiki kelemahan tersebut dengan mendahulukan proses yang memiliki durasi paling singkat. Meskipun SJF mampu menghasilkan rata-rata waktu tunggu yang lebih rendah, implementasinya di dunia nyata memiliki kompleksitas tersendiri, terutama dalam memprediksi durasi proses sebelum dieksekusi. Oleh karena itu, diperlukan sebuah pengujian praktikum untuk membandingkan secara langsung sejauh mana perbedaan performa antara FCFS dan SJF dalam menangani beban kerja proses yang bervariasi.

## 1.2 Rumusan Masalah

1.Bagaimana perbandingan mekanisme eksekusi proses antara algoritma First-Come, First-Served (FCFS) dan Shortest Job First (SJF) dalam simulasi antrean?

2.Sejauh mana pengaruh urutan kedatangan dan durasi proses (burst time) terhadap Average Waiting Time (AWT) pada kedua algoritma tersebut?

3.Apakah algoritma SJF selalu menghasilkan performa yang lebih baik dibandingkan FCFS dalam berbagai variasi beban kerja proses?

---

## 1.3 Tujuan

1.Memahami secara mendalam cara kerja algoritma penjadwalan FCFS dan SJF melalui pengujian data.

2.Mengukur dan menganalisis nilai rata-rata waktu tunggu (Average Waiting Time) yang dihasilkan oleh masing-masing algoritma.

3.Membuktikan secara empiris keunggulan dan keterbatasan dari penggunaan algoritma FCFS dan SJF dalam manajemen proses.

---

## 2. Methods (Metode)
## 2.1 Lingkungan Pengujian

Pengujian dilakukan dalam lingkungan terkontrol untuk meminimalkan variabel eksternal. Spesifikasi lingkungan pengujian adalah sebagai berikut:

Perangkat Keras (Hardware): 

Laptop/PC dengan prosesor setingkat  : Intel Core i5/Ryzen 5 dan RAM : 8GB

Perangkat Lunak (Software):

Sistem Operasi: Windows 11 / Ubuntu 22.04.

Simulator/Interpreter:  Python 3.x, Compiler C++, atau Spreadsheet/Excel untuk perhitungan manual.

Alat Dokumentasi: Visual Studio Code sebagai editor Markdown.

Objek Pengujian: Kumpulan proses (process set) yang terdiri dari sejumlah identitas proses (p1), waktu kedatangan (Arrival Time), dan durasi eksekusi (Burst Time).


### 2.2 Langkah-Langkah Eksperimen

Langkah-langkah yang dilakukan dalam praktikum ini meliputi:

1.Pendefinisian Dataset: Menentukan 5 sampel proses dengan variasi Burst Time yang berbeda untuk memicu kondisi Convoy Effect.

2.Simulasi Penjadwalan FCFS: Menghitung waktu mulai (start time) dan waktu selesai (finish time) setiap proses berdasarkan urutan kedatangan pertama.

3.Simulasi Penjadwalan SJF: Mengurutkan proses berdasarkan Burst Time terkecil (Non-preemptive), kemudian menghitung waktu tunggu masing-masing.

4.Pengambilan Data: Mencatat Waiting Time (WT) setiap proses dengan rumus:
WT = Start\ Time - Arrival\ Time Kalkulasi Rata-rata: Menghitung Average Waiting Time (AWT) untuk kedua algoritma.

### 2.3 Variabel Pengukuran

1.Burst Time (BT): Variabel ini merupakan durasi waktu yang dibutuhkan oleh masing-masing proses untuk dieksekusi oleh CPU. Data ini ditentukan di awal sebagai input statis.

2.Waiting Time (WT): Saya menghitung variabel ini untuk mengetahui berapa lama suatu proses harus menunggu di dalam antrean sampai akhirnya mendapatkan jatah waktu CPU. Perhitungan yang  digunakan adalah selisih antara waktu mulai eksekusi dengan waktu kedatangan proses.

3.Average Waiting Time (AWT): Ini adalah variabel metrik utama yang digunakan untuk menentukan efisiensi algoritma. cara menghitungnya itu dengan menjumlahkan seluruh Waiting Time proses, lalu membaginya dengan jumlah total proses yang diuji.

4.Turnaround Time (TAT): Selain waktu tunggu, saya juga memperhatikan total waktu yang dihabiskan proses sejak masuk antrean hingga selesai dieksekusi. Variabel ini saya peroleh dengan menjumlahkan Waiting Time dan Burst Time.

---

## 3. Hasil (Results)

Disajikan data hasil pengujian algoritma penjadwalan FCFS dan SJF menggunakan dataset 5 proses dengan Arrival Time (waktu kedatangan) yang sama (AT = 0).

## 3.1 Dataset Pengujian
Dataset yang digunakan dalam simulasi ini adalah sebagai berikut:

P1: 12 ms

P2: 3 ms

P3: 8 ms

P4: 2 ms

P5: 5 ms

### 3.2 Tabel Perbandingan Output Terminal





---


## 3.2 Analisis Hasil Pengujian

1.Berdasarkan data yang telah disajikan pada tabel sebelumnya, berikut adalah analisis mendalam terhadap performa algoritma FCFS dan SJF:Dampak Urutan Eksekusi pada FCFS:Pada algoritma FCFS, proses P1 dengan burst time terbesar (12 ms) menempati urutan pertama eksekusi. Hal ini mengakibatkan proses-proses pendek lainnya (P2, P3, P4, P5) tertahan di dalam antrean untuk waktu yang lama. Fenomena ini dikenal sebagai Convoy Effect, di mana proses dengan durasi kecil mengalami hambatan yang signifikan akibat satu proses panjang di depannya. Akibatnya, rata-rata waktu tunggu (AWT) menjadi tinggi, yakni sebesar 15.0 ms.

2.Optimasi Waktu Tunggu pada SJF:Penerapan algoritma SJF merubah urutan eksekusi menjadi P4 $\rightarrow$ P2 $\rightarrow$ P5 $\rightarrow$ P3 $\rightarrow$ P1. Dengan memprioritaskan proses dengan burst time terpendek, beban antrean berkurang lebih cepat secara kolektif. Sebagai contoh, P4 yang pada FCFS memiliki waktu tunggu 23 ms, berkurang drastis menjadi 0 ms pada SJF. Pengaturan ulang urutan ini secara efektif menurunkan AWT hingga ke angka 7.0 ms.

3.Efisiensi Performa:Terdapat perbedaan waktu tunggu sebesar 8.0 ms antara kedua algoritma. Secara statistik, algoritma SJF menunjukkan peningkatan efisiensi sebesar 53,3% dibandingkan FCFS dalam meminimalkan waktu tunggu pada dataset yang sama.

4.Hubungan Karakteristik Proses dan Respon Sistem:Analisis menunjukkan bahwa pada FCFS, waktu tunggu sangat bergantung pada posisi kedatangan proses. Sebaliknya, pada SJF, waktu tunggu ditentukan oleh karakteristik durasi proses itu sendiri. Algoritma SJF terbukti lebih responsif bagi mayoritas proses dalam sistem karena mampu menyelesaikan lebih banyak tugas dalam rentang waktu yang lebih awal.

5.Interpretasi Gantt Chart:Visualisasi melalui Gantt Chart memperlihatkan bahwa pada SJF, utilisasi waktu di awal periode eksekusi digunakan untuk menuntaskan proses-proses kecil. Hal ini meminimalkan jumlah proses yang tertahan di ready queue secara bersamaan dibandingkan dengan alur pada FCFS.

---

### 4. Pembahasan (Discussion)

## 4.1 Analisis Perbandingan Algoritma

Hasil pengujian menunjukkan perbedaan performa yang signifikan antara algoritma FCFS dan SJF dalam mengelola antrean proses:

1.Efisiensi Waktu Tunggu: Algoritma SJF terbukti lebih optimal dengan nilai AWT sebesar 7.0 ms, berbanding jauh dengan FCFS yang mencapai 15.0 ms. Penurunan waktu tunggu sebesar 53,3% ini mengonfirmasi bahwa memprioritaskan proses dengan burst time terpendek secara efektif meningkatkan responsivitas sistem secara keseluruhan.

2.Eliminasi Convoy Effect: Pada algoritma FCFS, ditemukan fenomena Convoy Effect di mana proses P1 (12 ms) menghambat proses-proses kecil di belakangnya. SJF berhasil mengeliminasi masalah ini dengan melakukan reorganisasi urutan eksekusi, sehingga proses ringan seperti P4 dapat selesai tanpa penundaan yang tidak perlu.

3.Kesesuaian Teoritis: Temuan ini sejalan dengan studi literatur (Indra dkk., 2025) yang menyatakan bahwa SJF adalah algoritma paling efisien untuk meminimalkan rata-rata waktu tunggu. Namun, secara praktis, FCFS tetap memiliki keunggulan dalam hal kesederhanaan implementasi dan rendahnya overhead karena tidak memerlukan estimasi durasi proses sebelumnya.

4.Optimalitas Sistem: Penggunaan SJF meningkatkan throughput sistem karena jumlah proses dalam antrean berkurang lebih cepat. Hal ini menunjukkan bahwa untuk beban kerja dengan variasi burst time yang tinggi, penjadwalan berbasis durasi jauh lebih unggul dibandingkan penjadwalan berbasis urutan kedatangan.

---

### Kesimpulan
Berdasarkan hasil pengujian dan analisis yang telah dilakukan, dapat ditarik kesimpulan sebagai berikut:

1.Efisiensi Algoritma: Algoritma Shortest Job First (SJF) terbukti secara signifikan lebih efisien dibandingkan First-Come First-Served (FCFS) dalam meminimalkan waktu tunggu, dengan penurunan Average Waiting Time (AWT) sebesar 53,3% (dari 15.0 ms menjadi 7.0 ms).

2.Karakteristik Penjadwalan: Algoritma FCFS sangat dipengaruhi oleh urutan kedatangan proses dan rentan terhadap Convoy Effect, sedangkan SJF mengoptimalkan performa sistem dengan memprioritaskan proses berdasarkan durasi burst time terpendek.

3.Implementasi Praktis: Meskipun SJF menawarkan hasil yang lebih optimal secara matematis, FCFS tetap memiliki relevansi dalam penggunaan praktis karena kesederhanaan logika serta rendahnya beban komputasi (overhead) sistem dibandingkan algoritma yang memerlukan pengurutan atau prediksi durasi proses.

---

## Daftar Pustaka

1.Indra, Z., dkk. (2025). Analisis Komparatif dan Evaluatif terhadap Algoritma First-Come First-Served (FCFS) dalam Penjadwalan CPU di Era Komputasi Modern. Jurnal Penelitian Inovatif (JUPIN), 5(4).

2.Fadhilah, I., & Siregar, H. (2025). Systematic Literature Review: Perbandingan Algoritma Round Robin dan Shortest Job First dalam Penjadwalan CPU. BIOS: Jurnal Teknologi Informasi dan Rekayasa Komputer, 6(2).

3.Rahman, R., dkk. (2024). Meningkatkan Responsivitas pada Sistem Operasi Android melalui Implementasi Algoritma Penjadwalan Mutakhir. Router: Jurnal Teknik Informatika dan Terapan, 2(3).

4.Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts. 10th Edition. John Wiley & Sons.

---

## Quiz
1.Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah?

Format IMRAD menyediakan struktur standar yang memisahkan data objektif (Hasil) dari analisis subjektif-ilmiah (Pembahasan), sehingga laporan menjadi lebih sistematis, logis, dan mudah dievaluasi oleh pihak lain.

2.Apa perbedaan antara bagian Hasil dan Pembahasan?

Bagian Hasil hanya menyajikan temuan data dalam bentuk tabel atau grafik tanpa interpretasi, sementara bagian Pembahasan menjelaskan makna dari data tersebut, menghubungkannya dengan teori, serta menganalisis mengapa hasil tersebut bisa terjadi.

3.Mengapa sitasi dan daftar pustaka penting?

Sitasi dan daftar pustaka berfungsi untuk memberikan pengakuan atas karya orang lain, menghindari plagiarisme, serta memberikan landasan teori yang kuat agar hasil praktikum memiliki kredibilitas akademik.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
