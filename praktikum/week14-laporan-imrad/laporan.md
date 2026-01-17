
# Laporan Praktikum Minggu 14
Topik:  Penyusunan Laporan Praktikum Format IMRAD


---

## Identitas
- **Nama**  : NOVIA SAFITRI
- **NIM**   : 250202923
- **Kelas** : 1IKRA

---

## 1 PENDAHULUAN 
## 1.1 Latar Belakang  

Manajemen memori merupakan bagian penting dari sistem operasi dalam mengatur penggunaan memori utama yang jumlahnya terbatas. Oleh karena itu, sistem operasi menggunakan mekanisme paging dan page replacement untuk menentukan halaman yang harus diganti ketika memori penuh.(Silberschatz et al., 2018).

Dua algoritma page replacement yang umum digunakan adalah FIFO dan LRU.Algoritma FIFO mengganti halaman berdasarkan urutan kedatangan ke memori,sehingga halaman yang masuk lebih awal akan diganti terlebih dahulu tanpa mempertimbangkan apakah halaman tersebut masih sering digunakan.Meskipun sederhana,metode ini dapat menyebabkan halaman yang masih dibutuhkan ikut tergantikan.Berbeda dengan FIFO,algoritma LRU mengganti halaman yang paling lama tidak diakses dengan melihat riwayat penggunaan halaman.Pendekatan ini bertujuan untuk mempertahankan halaman yang sering digunakan agar tetap berada di memori sehingga jumlah page fault dapat dikurangi. Namun, penerapan LRU lebih kompleks karena membutuhkan pencatatan aktivitas penggunaan setiap halaman.(Tanenbaum & Bos, 2015).

Perbedaan cara kerja antara algoritma FIFO dan LRU menunjukkan bahwa masing-masing memiliki kelebihan dan kekurangan dalam pengelolaan memori.Oleh karena itu,praktikum ini dilakukan untuk membandingkan kinerja kedua algoritma tersebut berdasarkan jumlah page fault yang dihasilkan.

## 1.2 Rumusan Masalah 
 1. Bagaimana cara kerja algoritma penggantian halaman FIFO dan LRU dalam manajemen memori?
 2. Apa perbedaan kinerja antara algoritma FIFO dan LRU berdasarkan jumlah page fault yang dihasilkan?
 3. Algoritma manakah yang lebih efektif digunakan dalam pengelolaan memori utama pada kondisi pengujian tertentu?
## 1.3 Tujuan 
1. Mengetahui cara kerja algoritma FIFO dan LRU dalam proses penggantian halaman.

2. Membandingkan kinerja algoritma FIFO dan LRU berdasarkan jumlah page fault.

3. Menganalisis efektivitas masing-masing algoritma dalam pengelolaan memori utama.
---

## 2. METODE
## 2.1 Lingkungan Uji
   
 * Sistem Operasi : Windows 10  
 *  Bahasa Pemrograman : Python  
 * Jumlah frame : 3 frame  
 *  Reference string : 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
## 2.2 Langkah Eksperimen 
1. Menyiapkan dataset

   * Dataset :
    * string referensi(7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2)
2. Implemenstasik algoritma FIFO

    *  Simulasikan
    * Catat setiap page hit dan page fault
    * Hitung total page fault .
3. Implementasi LRU

   * Simulasikan penggantian halaman menggunakan algoritma LRU.
   * Catat setiap page hit dan page fault
   * Hitung total page fault .
4. Eksekusi & Validasi

  * Jalankan program untuk FIFO dan LRU.
  * Pastikan hasil simulasi logistik dan konsistensi.
  * Simpan tangkapan layar hasil eksekusi.

## 2.3 Cara Pengukuran 
Pengukuran kinerja algoritma dilakukan dengan cara:
   * Menjalankan simulasi penggantian halaman menggunakan dataset dan jumlah frame yang sama
   * Catat jumlah page fault yang terjadi setiap kali halaman yang diakses tidak tersedia di memori
   * Amati  jumlah page hit juga sebagai indikator efisiensi penggunaan memori



---

## DOKUMENTASI 
Algoritma FIFO DAN LRU
![alt tekx](<screenshots/week14.png>)


## 3. HASIL 
*FIFO Page Replacement* 

Page: 7 -> Frames: [7] (Fault)

Page: 0 -> Frames: [7, 0] (Fault)

Page: 1 -> Frames: [7, 0, 1] (Fault)

Page: 2 -> Frames: [2, 0, 1] (Fault)

Page: 0 -> Frames: [2, 0, 1] (Hit)

Page: 3 -> Frames: [2, 3, 1] (Fault)

Page: 0 -> Frames: [2, 3, 0] (Fault)

Page: 4 -> Frames: [4, 3, 0] (Fault)

Page: 2 -> Frames: [4, 2, 0] (Fault)

Page: 3 -> Frames: [4, 2, 3] (Fault)

Page: 0 -> Frames: [0, 2, 3] (Fault)

Page: 3 -> Frames: [0, 2, 3] (Hit)

Page: 2 -> Frames: [0, 2, 3] (Hit)
Total Page Fault FIFO: 10

*LRU Page Replacement*
Page: 7 -> Frames: [7] (Fault)

Page: 0 -> Frames: [7, 0] (Fault)

Page: 1 -> Frames: [7, 0, 1] (Fault)

Page: 2 -> Frames: [2, 0, 1] (Fault)

Page: 0 -> Frames: [2, 0, 1] (Hit)

Page: 3 -> Frames: [2, 0, 3] (Fault)

Page: 0 -> Frames: [2, 0, 3] (Hit)

Page: 4 -> Frames: [4, 0, 3] (Fault)

Page: 2 -> Frames: [4, 0, 2] (Fault)

Page: 3 -> Frames: [4, 3, 2] (Fault)

Page: 0 -> Frames: [0, 3, 2] (Fault)

Page: 3 -> Frames: [0, 3, 2] (Hit)

Page: 2 -> Frames: [0, 3, 2] (Hit)

Total Page Fault LRU : 9

Berdasarkan hasil simulasi penggantian halaman dengan jumlah frame sebanyak 3, algoritma FIFO menghasilkan total 10 page fault, sedangkan algoritma LRU menghasilkan 9 page fault. Hal ini menunjukkan bahwa algoritma LRU memiliki kinerja yang lebih baik dibandingkan FIFO pada skenario pengujian yang dilakukan.

Perbedaan jumlah page fault terjadi karena algoritma FIFO mengganti halaman berdasarkan urutan kedatangan tanpa mempertimbangkan frekuensi penggunaan, sehingga beberapa halaman yang masih sering diakses ikut tergantikan. Sebaliknya, algoritma LRU mempertahankan halaman yang lebih sering digunakan dengan mengganti halaman yang paling lama tidak diakses, sehingga mampu mengurangi jumlah page fault.

## 4. PEMBAHASAN 
## 4.1 Interpretasi hasil
|Aspek Perbandingan|	FIFO	|LRU|
|:---|:---|:---|
Dasar penggantian halaman	|Urutan kedatangan halaman	Waktu |terakhir halaman digunakan|
|Pertimbangan pola akses	|Tidak memperhatikan	|Memperhatikan riwayat akses|
|Jumlah page fault|	Lebih banyak|	Lebih sedikit|
Efisiensi penggunaan memori|	Kurang optimal	|Lebih optimal|
|Kinerja pada pengujian	|Lebbih rendah	|Lebih baik|

Dari tabel diatas menunjukkan adanya perbedaan kinerja antara algoritma FIFO dan LRU:
Hasil simulasi menunjukkan adanya perbedaan kinerja antara algoritma FIFO dan LRU. Algoritma LRU menghasilkan jumlah page fault yang lebih sedikit karena mampu mempertahankan halaman yang sering digunakan dengan mengganti halaman yang paling lama tidak diakses. Sebaliknya, FIFO mengganti halaman berdasarkan urutan kedatangan tanpa mempertimbangkan pola akses, sehingga kinerjanya kurang optimal pada skenario pengujian ini.

## 4.2 Keterbatasan 
Dalam praktikum ini memiliki beberapa keterbatasan:
   * Pengujian hanya dilakukan menggunakan satu dataset dengan jumlah frame memori yang terbatasa 
   * hasil yang diperoleh belum tentu mewakili semua kondisi penggunaan memori
   *  simulasi dilakukan secara sederhana tanpa mempertimbangkan faktor lain seperti ukuran halaman
   *   variasi pola akses yang lebih kompleks, serta overhead implementasi algoritma dalam sistem operasi nyata.
## 4.3 Perbandingan teori/ekspektasi
Secara teori, algoritma LRU dianggap lebih baik dibandingkan FIFO karena mampu menyesuaikan diri dengan pola akses halaman yang bersifat lokalitas. LRU berupaya mempertahankan halaman yang sering digunakan dan mengganti halaman yang sudah lama tidak diakses, sehingga diharapkan dapat menghasilkan jumlah page fault yang lebih sedikit.

Hasil praktikum yang diperoleh menunjukkan bahwa algoritma LRU memang menghasilkan jumlah page fault lebih rendah dibandingkan FIFO. Temuan ini sesuai dengan teori yang dikemukakan oleh Silberschatz serta Tanenbaum, yang menyatakan bahwa algoritma berbasis riwayat penggunaan umumnya lebih efektif dalam pengelolaan memori. Dengan demikian, hasil eksperimen yang diperoleh telah memenuhi ekspektasi awal dan memperkuat pemahaman mengenai perbedaan kinerja antara algoritma FIFO dan LRU.


## KESIMPULAN 
Berdasarkan hasil praktikum yang telah dilakukan, dapat disimpulkan bahwa algoritma FIFO dan LRU memiliki cara kerja yang berbeda dalam proses penggantian halaman. Algoritma FIFO lebih sederhana dalam implementasi, namun cenderung menghasilkan jumlah page fault yang lebih banyak karena tidak mempertimbangkan frekuensi penggunaan halaman. Sebaliknya, algoritma LRU mampu mengurangi jumlah page fault dengan mempertahankan halaman yang sering diakses, meskipun memiliki tingkat kompleksitas yang lebih tinggi. Dengan demikian, algoritma LRU menunjukkan kinerja yang lebih baik dibandingkan FIFO dalam pengelolaan memori pada kondisi pengujian yang dilakukan.


## Quiz
1.Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?
   
   **Jawaban:**  Format IMRAD membantu membuat laporan praktikum lebih ilmiah karena menyajikan isi laporan secara terstruktur dan runtut, mulai dari latar belakang,hingga kesimpulan.Format IMRAD memudahkan pembaca memahami alur penelitian seperti tujuan, metode, hasil, serta analisis yang dilakukan.

2.Apa perbedaan antara bagian Hasil dan Pembahasan ?
 
   **Jawaban:** Bagian Hasil berisi data yang diperoleh dari percobaan,seperti tabel atau hasil simulasi,menunjukan apa yang terjadi selama eksperimen,Sedangkan bagian
   pembahasan berisi penjelaskan dan penafsiran dari bagian hasil tersebut,serta menerapkan dengan teori yang dipelajari.

3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?

   **Jawaban:**  Sitasi dan daftar pustaka penting untuk laporan praktikum karena untuk menunjukkan sumber teori dan referensi yang menjadi dasar pelaksanaan praktikum.
   Dengan mencantumkan sitasi, dapat menunjukkan bahwa materi yang digunakan tidak berasal dari pendapat pribadi semata, melainkan didukung oleh sumber yang jelas dan dapat dipercaya. 

---

## Daftar Pustaka 
1. Silberschatz, A., Galvin, P., Gagne, G. Konsep Sistem Operasi , Edisi ke-10

2. Tanenbaum, A. Sistem Operasi Modern , Edisi ke-4.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
