
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Penggantian Halaman (FIFO & LRU)

---

## Identitas
- **Nama**  : NOVIA SAFITRI
- **NIM**   :250202923
- **Kelas** :1IKRA
---

## Tujuan
1. Mengimplementasikan algoritma penggantian halaman FIFO dalam program.

2. Mengimplementasikan algoritma penggantian halaman LRU dalam program.

3. Batasan simulasi penggantian halaman dengan dataset tertentu.

4. Membandingkan performa FIFO dan LRU berdasarkan jumlah pagefault .

5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
Manajemen memori adalah proses sistem operasi yang berfungsi untuk  mengatur penggunaan RAM agar efisien, termasuk melalui memori virtual yang membagi memori menjadi halaman (page) dan frame. Saat halaman yang dibutuhkan tidak ada di RAM, terjadi page fault, sehingga perlu dilakukan penggantian halaman. 
Dua algoritma umum yaitu :
* FIFO (First In First Out), yang mengganti halaman paling lama masuk, sederhana tapi kadang tidak efisien
*  LRU (Least Recently Used), yang mengganti halaman paling lama tidak digunakan, lebih efisien tetapi lebih kompleks. Pemilihan algoritma tergantung pola akses memori dan kebutuhan sistem.

---

## Langkah Praktikum
1. • Kumpulan data

Gunakan string referensi berikut sebagai contoh:

      7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2

Jumlah frame memori: 3 frame .

2. Implementasi FIFO

   * Simulasikan penempatan halaman menggunakan algoritma FIFO.
   * Catat setiap halaman hit dan halaman kesalahan .
   * Hitung total page fault .

3. Implementasi LRU

   * Simulasikan penempatan halaman menggunakan algoritma LRU.
   * Catat setiap halaman hit dan halaman kesalahan .
   * Hitung total page fault .

4. Eksekusi & Validasi

   * Jalankan program untuk FIFO dan LRU.
   * Pastikan hasil simulasi logistik dan konsistensi.
   * Simpan tangkapan layar hasil eksekusi.

5. Analisis Perbandingan

Buat tabel perbandingan seperti berikut:

|Algoritm|	Jumlah Kesalahan Halaman|	Keterangan|
|:---|:---|:---|
|FIFO|	...|	...|
|LRU	|...|	...|
  * Menjelaskan mengapa jumlah kesalahan halaman bisa berbeda.
  * Analisis algoritma mana yang lebih efisien dan nyaman.

6. Berkomitmen & Berusaha

         git add .
         git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
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
1. Apa perbedaan utama FIFO dan LRU?

 **Jawaban:** 
|Aspek|FIFO(First In First Out)|LRU(Least Recently Used)|
|:---|:---|:---|
Prinsip utama|Mengganti halaman yang paling lama masuk|Mengganti halaman yang paling lama tidak pernah digunakan|
Fokus penggantian|berdasarkan urutan masuk|Berdasarkan urutan penggunaan terakhir|
Kelebihan|Sederhana dan mudah diimplementasikan|Lebih efisien, page fault lebih rendah|
Kekurangan|Tidak mempertimbangkan penggunaan, bisa terjadi Belady’s Anomaly|Lebih kompleks, perlu catatan akses halaman|

3. Mengapa FIFO dapat menghasilkan Belady's Anomaly ?

    **Jawaban:**  FIFO dapat menghasilkan Belady’s Anomaly karena hanya fokus dengan  mengganti halaman yang paling lama masuk memori, tanpa memperhatikan apakah halaman itu sering dipakai atau tidak. Akibatnya, kadang menambah jumlah memori justru meningkatkan page fault karena halaman yang masih dibutuhkan diganti terlalu cepat.

5. Mengapa LRU umumnya menghasilkan kinerja lebih baik dibandingkan FIFO?

   **Jawaban:**  LRU biasanya lebih baik daripada FIFO karena mengganti halaman yang paling lama tidak digunakan, sehingga halaman yang masih sering dipakai tetap di memori dan jumlah page fault lebih rendah.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
