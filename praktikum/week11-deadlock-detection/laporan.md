
# Laporan Praktikum Minggu 11
Topik:  Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : NOVIA SAFITRI
- **NIM**   : 250202923
- **Kelas** : 1IKRA

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi kebuntuan.

2. Garis simulasi deteksi kebuntuan dengan dataset uji.

3. Menyajikan analisis hasil kebuntuan dalam bentuk tabel.

4. Memberikan interpretasi hasil uji secara logistik dan sistematis.

5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
Deadlock adalah kondisi di mana beberapa proses saling menunggu sumber daya sehingga tidak ada yang bisa berjalan. 

Simulasi deadlock dilakukan untuk meniru alokasi sumber daya dan melihat kapan deadlock bisa terjadi. 

Deteksi deadlock adalah cara menemukan deadlock setelah terjadi dengan memeriksa alokasi sumber daya dan menelusuri siklus saling menunggu, kemudian sistem melakukan pemulihan dengan membebaskan atau menghentikan proses tertentu.

---

## Langkah Praktikum
`1. • Kumpulan data

Gunakan dataset sederhana yang berisi:

    * Daftar proses
    * Alokasi Sumber Daya
    * Permintaan/Kebutuhan Sumber Daya

Contoh tabel:

|Proses|	Alokasi	|Meminta|
|:---|:---|:---|
P1|	R1|	R2|
Halaman 2|	R2|	R3|
P3|	R3|	R1|

2. Implementasi Algoritma Deteksi Deadlock

Program minimal harus:
   * Membaca data proses dan sumber daya.
    * Menentukan apakah sistem berada dalam kondisi deadlock.
    * Menampilkan proses mana saja yang terlibat deadlock.

3.Eksekusi & Validasi
    * Jalankan program dengan dataset uji.
   * Validasi hasil deteksi dengan analisis manual/logis.
    * Simpan hasil eksekusi dalam bentuk screenshot.

4. Analisis Hasil

    * Sajikan hasil deteksi dalam tabel (proses deadlock/tidak).
    * Menjelaskan mengapa kebuntuan terjadi atau tidak terjadi.
    *  Kaitkan hasil dengan teori deadlock (empat kondisi).

5. Berkomitmen & Berusaha

          git add .
          git commit -m "Minggu 11 - Deadlock Detection"
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
1. Apa perbedaan antara pencegahan , penghindaran , dan deteksi kebuntuan ?

    **Jawaban:**
   |Aspek|Pencegahan|Penghindaran|Deteksi kebutuhan|
   |:---|:---|:---|:---|
   Tujuan|Mencegah deadlock terjadi sejak awal|Memastikan sistem tidak masuk kondisi deadlock|Mengizinkan deadlock terjadi tapi siap mendeteksi dan menanganinya|
   Cara kerja|Membatasi penggunaan sumber daya atau memaksa urutan tertentu|Mengecek setiap permintaan sumber daya dan memutuskan aman/tidak|memantau dan memeriksa apakah deadlock terjadi|
   Kelebihan|Deadlock pasti tidak terjadi|Lebih fleksibel daripada pencegahan|Tidak membatasi sistem, lebih efisien saat sumber daya banyak|
   Kekurangan|Bisa membatasi kinerja atau penggunaan sumber daya|Memerlukan perhitungan tambahan|Deadlock tetap bisa terjadi sementara, perlu pemulihan|
     
3. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?

    **Jawaban:**  Deteksi deadlock tetap diperlukan dalam sistem operasi karena  karena terkadang mencegah atau menghindari deadlock terlalu membatasi sistem. Dengan deteksi, sistem bisa tetap berjalan normal dan hanya menangani deadlock jika terjadi.

5. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
 
   **Jawaban:**
   Aspek|Kekurangan|Kelebihan|
   |:---|:---|:---|
   Deteksi deadlock|Deadlock tetap bisa terjadi sementara,memerlukan algoritma untuk mendeteksi,dan perlu mekanisme pemulihan, bisa kompleks|Tidak membatasi penggunaan sumber daya,tetap fleksibel dan deadlock bisa ditangani jika terjadi|
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
