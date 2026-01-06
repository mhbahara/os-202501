
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Rizky Iqbal Hisyam  
- **NIM**   : 250202926  
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
Deadlock adalah kondisi ketika dua atau lebih proses saling menunggu sumber daya yang sedang digunakan oleh proses lain sehingga tidak ada proses yang dapat melanjutkan eksekusi. Deadlock dapat terjadi jika empat kondisi terpenuhi secara bersamaan, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait.
Pendekatan deadlock detection memungkinkan sistem operasi membiarkan deadlock terjadi, kemudian mendeteksinya menggunakan algoritma tertentu, seperti resource allocation graph atau deadlock detection algorithm, sebelum mengambil tindakan pemulihan.

---

## Langkah Praktikum
1. Sesuaikan struktur folder seperti berikut:
```
praktikum/week11-deadlock-detection/
├─ code/
│  ├─ deadlock_detection.py
│  └─ dataset_deadlock.csv
├─ screenshots/
│  └─ hasil_deteksi.png
└─ laporan.md
```
2. Siapkan dataset berisi daftar proses, resource allocation, dan resource request.
   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |
3. Implementasi Algoritma Deteksi Deadlock (program harus membaca data proses dan resource, menentukan sistem deadlock atau tidak, menampilkan proses mana yang terlibat deadlock).
4. Jalankan program dengan dataset dan simpan hasil screenshots.
5. Analisis hasil.
6. Commit dan push.
   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```


---

## Kode / Perintah
Kode ada di folder praktikum/week11-deadlock-detection/code/deadlock_detection.py

---

## Hasil Eksekusi
Hasil eksekusi/simulasi:
![Screenshot hasil](./screenshots/hasil_eksekusi.png)

---

## Analisis
- Tabel hasil deteksi deadlock:

   | Proses | Status   |
   | ------ | -------- |
   | P1     | Deadlock |
   | P2     | Deadlock |
   | P3     | Deadlock |

- Alasan terjadinya deadlock
   
   Deadlock terjadi karena setiap proses memegang satu sumber daya dan pada saat yang sama meminta sumber daya lain yang sedang digunakan oleh proses berbeda. Kondisi ini membentuk circular wait, di mana P1 menunggu sumber daya dari P2, P2 menunggu sumber daya dari P3, dan P3 menunggu sumber daya dari P1, sehingga tidak ada proses yang dapat melanjutkan eksekusi.

- Kaitannya dengan teori deadlock (4 kondisi)

   Hasil simulasi sesuai dengan teori deadlock karena keempat kondisi deadlock terpenuhi, yaitu mutual exclusion (sumber daya hanya dapat digunakan oleh satu proses), hold and wait (proses memegang sumber daya sambil menunggu yang lain), no preemption (sumber daya tidak dapat diambil paksa), dan circular wait (terdapat siklus ketergantungan antar proses). Terpenuhinya keempat kondisi tersebut menyebabkan sistem berada dalam keadaan deadlock.

---

## Kesimpulan
Berdasarkan praktikum yang dilakukan, dapat disimpulkan bahwa deadlock detection merupakan pendekatan yang efektif untuk mengidentifikasi deadlock setelah kondisi tersebut terjadi. Melalui simulasi, mahasiswa dapat memahami proses pendeteksian deadlock secara lebih nyata dan logis. Meskipun memiliki overhead tambahan, pendekatan ini memberikan fleksibilitas bagi sistem operasi dalam mengelola sumber daya.

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?  
   **Jawaban:**  Perbedaan antara deadlock prevention, deadlock avoidance, dan deadlock detection terletak pada waktu dan cara sistem operasi menangani deadlock. Deadlock prevention berusaha mencegah deadlock sejak awal dengan menghilangkan satu atau lebih dari empat kondisi deadlock, namun cara ini sering membatasi penggunaan sumber daya. Deadlock avoidance menghindari deadlock dengan memeriksa kondisi sistem sebelum mengalokasikan sumber daya, sehingga hanya memberikan alokasi yang berada dalam keadaan aman (safe state), tetapi memerlukan informasi lengkap tentang kebutuhan proses. Sementara itu, deadlock detection membiarkan deadlock terjadi, lalu mendeteksinya menggunakan algoritma tertentu dan mengambil tindakan pemulihan, sehingga lebih fleksibel tetapi menimbulkan overhead tambahan.
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   **Jawaban:**  Deteksi deadlock tetap diperlukan dalam sistem operasi karena tidak semua deadlock dapat dicegah atau dihindari secara efisien. Pada sistem yang kompleks dan dinamis, pembatasan ketat seperti pada *deadlock prevention* atau kebutuhan informasi lengkap seperti pada *deadlock avoidance* sering kali tidak praktis. Oleh karena itu, sistem operasi membiarkan proses berjalan secara normal dan menggunakan **deadlock detection** untuk mengidentifikasi deadlock yang benar-benar terjadi, sehingga sistem tetap fleksibel dan sumber daya dapat dimanfaatkan secara optimal sebelum dilakukan pemulihan.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?   
   **Jawaban:**  Pendekatan deteksi deadlock memiliki kelebihan karena **lebih fleksibel** dan tidak membatasi alokasi sumber daya sejak awal. Sistem hanya menangani deadlock ketika benar-benar terjadi. Namun, pendekatan ini memiliki kekurangan berupa **overhead tambahan** untuk proses deteksi dan risiko gangguan sistem saat dilakukan pemulihan, seperti penghentian proses yang terlibat.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  sempat beberapa kali eror pada program deadlock detection yang saya buat
- Bagaimana cara Anda mengatasinya?  mencari letak kesalahan kode dan memperbaikinya

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
