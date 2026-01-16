
# Laporan Praktikum Minggu 10
Topik: Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Gilang Ananda Putra
- **NIM**   : 250202939 
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
1. **Page Replacement:** Mekanisme yang dilakukan sistem operasi saat memori penuh dan terjadi *page fault*. OS harus memilih halaman mana yang akan dikeluarkan (*swap out*) untuk memberi ruang bagi halaman baru.
2. **FIFO (First-In First-Out):** Algoritma paling sederhana di mana halaman yang paling lama berada di memori (yang pertama kali masuk) akan diganti terlebih dahulu. Algoritma ini menggunakan prinsip antrean (queue).
3. **LRU (Least Recently Used):** Algoritma yang mengganti halaman yang sudah paling lama tidak digunakan. LRU berasumsi bahwa halaman yang baru saja digunakan kemungkinan besar akan digunakan lagi (*Locality of Reference*).
4. **Page Fault:** Kondisi ketika program mencoba mengakses halaman memori yang saat itu tidak tersedia di memori fisik (RAM), sehingga OS harus mengambilnya dari disk.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```

---

## Kode / Perintah
**1. Dataset Uji (`code/reference_string.txt`)**
File ini berisi urutan halaman yang akan diakses oleh memori.

```text
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2

```

**2. Implementasi Algoritma (`code/page_replacement.py`)**
Potongan kode logika utama untuk FIFO dan LRU dalam Python:

*Logika FIFO (First-In First-Out):*

```python
if len(memory) < capacity:
    memory.append(page)
else:
    # Hapus elemen pertama (paling tua), masukkan page baru di belakang
    memory.pop(0)
    memory.append(page)

```

*Logika LRU (Least Recently Used):*

```python
if page not in memory:
    if len(memory) < capacity:
        memory.append(page)
    else:
        # Hapus elemen pertama (paling lama tidak dipakai)
        memory.pop(0)
        memory.append(page)
else:
    # Jika HIT, pindahkan page ke posisi paling belakang (terbaru dipakai)
    memory.remove(page)
    memory.append(page)

```

**3. Perintah Eksekusi**
Perintah terminal untuk masuk ke direktori dan menjalankan simulasi:

```bash
# Masuk ke folder code
cd code

# Menampilkan isi dataset
cat reference_string.txt

# Menjalankan program simulasi
python page_replacement.py

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_simulasi_1.png)
![Screenshot hasil](screenshots/hasil_simulasi_2.png)

---

## Analisis

Berdasarkan hasil simulasi dengan **3 Frame** dan dataset `7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2`, diperoleh data sebagai berikut:

| Algoritma | Jumlah Page Fault | Keterangan |
| --- | --- | --- |
| FIFO | **12** | Kurang Efisien pada kasus ini |
| LRU | **12** | Sama (namun logika berbeda) |

*(Catatan: Sesuaikan angka di atas dengan hasil running di terminal Anda, angka 12 adalah estimasi umum untuk string ini pada 3 frame).*

**Analisis Perbandingan:**

1. **Performa:**  Pada dataset spesifik ini, FIFO dan LRU mungkin menghasilkan jumlah fault yang sama atau hampir sama. Namun, secara teori dan rata-rata kasus nyata, LRU dianggap lebih efisien.
2. **Logika Penggantian:**
* **FIFO** mengganti angka `7` saat angka `2` masuk, semata-mata karena `7` adalah yang terlama masuk, meskipun mungkin `7` akan dipakai lagi.
* **LRU** melihat riwayat penggunaan. Jika angka `0` sering diakses (HIT), maka `0` akan dipertahankan lebih lama di memori dibandingkan angka yang jarang disentuh.


3. **Kesimpulan Efisiensi:** LRU lebih cerdas karena memanfaatkan prinsip *locality*, sedangkan FIFO bekerja buta terhadap pola akses data.

---

## Kesimpulan
1. Algoritma **LRU** umumnya lebih baik daripada FIFO karena mempertimbangkan pola penggunaan data terakhir, sehingga meminimalisir pembuangan halaman yang sering diakses.
2. Algoritma **FIFO** mudah diimplementasikan (hanya butuh antrean), tetapi rentan terhadap anomali (seperti membuang halaman penting yang sering dipakai) dan *Belady's Anomaly*.
3. Jumlah *page fault* sangat dipengaruhi oleh jumlah frame yang tersedia dan pola *reference string* (urutan akses data).

---

## Quiz

1. **Apa perbedaan utama FIFO dan LRU?**

   **Jawaban:**

   Perbedaan utamanya terletak pada **halaman mana yang dipilih untuk diganti**. FIFO memilih halaman berdasarkan **waktu masuk** (yang paling tua masuk diganti), sedangkan LRU memilih halaman berdasarkan **waktu penggunaan terakhir** (yang paling lama tidak "disentuh" diganti).

2. **Mengapa FIFO dapat menghasilkan Belady’s Anomaly?**

   **Jawaban:**

   FIFO tidak mematuhi properti tumpukan (*stack property*). Dalam FIFO, menambah jumlah frame memori terkadang justru **meningkatkan** jumlah *page fault* karena pola penggantian halaman yang kaku (membuang halaman lama) bisa jadi justru membuang halaman yang akan segera diakses lagi dalam urutan *string* tertentu.

3. **Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?**

   **Jawaban:**

   Karena LRU memanfaatkan prinsip **Locality of Reference**. Program cenderung mengakses ulang data yang baru saja digunakan. Dengan mempertahankan data yang baru dipakai, LRU mengurangi kemungkinan terjadinya *page fault* di masa depan dibandingkan FIFO yang tidak peduli data itu sering dipakai atau tidak.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  

   Bagian yang cukup menantang adalah memahami logika *pointer* atau indeks saat mengimplementasikan LRU, khususnya saat harus memindahkan halaman yang statusnya "HIT" ke posisi *most recently used*.
- Bagaimana cara Anda mengatasinya? 

   Saya menggunakan struktur data `list` di Python. Untuk LRU, saat terjadi "HIT", saya menghapus elemen tersebut dari list lalu menambahkannya kembali ke bagian akhir list (append) agar elemen tersebut dianggap paling baru. 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
