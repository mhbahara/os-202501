
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Miftakhul Lisna Esa Baehaqi]  
- **NIM**   : [250202951]  
- **Kelas** : [1 IKRB]

---

## Tujuan
1. Mengimplementasikan algoritma Page Replacement FIFO (First-In First-Out) dan LRU (Least Recently Used) menggunakan bahasa pemrograman.
2. Memahami konsep Page Fault (kegagalan halaman) dan Page Hit.
3. Membandingkan efisiensi algoritma FIFO dan LRU berdasarkan jumlah page fault yang dihasilkan.

---

## Dasar Teori
Manajemen memori virtual memungkinkan eksekusi proses yang ukurannya lebih besar dari memori fisik yang tersedia. Ketika CPU membutuhkan halaman (page) yang tidak ada di memori utama (RAM), terjadi Page Fault. Sistem operasi harus memuat halaman tersebut dari disk ke memori. Jika memori penuh, OS harus memilih salah satu halaman untuk diganti (swap out).

1. FIFO (First-In First-Out): Algoritma paling sederhana. Halaman yang paling awal masuk ke memori adalah yang pertama kali diganti. Sistem menggunakan antrian (queue) atau pointer melingkar untuk melacak halaman tertua.

2. LRU (Least Recently Used): Algoritma ini mengganti halaman yang sudah paling lama tidak digunakan. Asumsinya adalah halaman yang sering digunakan baru-baru ini kemungkinan akan digunakan lagi (Locality of Reference).

---

## Langkah Praktikum

1. Membuat folder praktikum/week10-page-replacement/ dengan subfolder code dan screenshots.

2. Membuat file reference_string.txt berisi data uji: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2 dan menetapkan jumlah frame = 3.

3. Membuat program Python (page_replacement.py) yang membaca file dataset, mensimulasikan antrian frame untuk FIFO, dan stack penggunaan untuk LRU.

4. Menjalankan program di terminal dan mencatat setiap kali status MISS (Page Fault) terjadi.

5. Mendokumentasikan seluruh hasil simulasi, perhitungan, dan analisis dalam file laporan.md.
---

## Kode / Perintah

```python
def fifo_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0
    hits = 0
    pointer = 0

    print("=== FIFO Page Replacement ===")
    for page in reference_string:
        if page in memory:
            hits += 1
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % frames

        print(f"Page {page} -> {memory} ({status})")

    print(f"\nTotal Page Faults (FIFO): {page_faults}")
    return page_faults


def lru_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0
    hits = 0

    print("\n=== LRU Page Replacement ===")
    for page in reference_string:
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        print(f"Page {page} -> {memory} ({status})")

    print(f"\nTotal Page Faults (LRU): {page_faults}")
    return page_faults


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    fifo_faults = fifo_page_replacement(reference_string, frames)
    lru_faults = lru_page_replacement(reference_string, frames)

```

---

## Hasil Eksekusi
Berikut adalah output program saat dijalankan dengan dataset uji:

![Screenshot hasil](./screenshots/hasil%20uji.png)

---

## Analisis
1. Analisis Perbandingan

| Algoritma | Jumlah Page Fault | Keterangan                                                                   |
| --------- | ----------------- | ---------------------------------------------------------------------------- |
| FIFO      | 10                | Mengganti halaman paling lama masuk tanpa memperhatikan frekuensi penggunaan |
| LRU       | 9                 | Mengganti halaman yang paling lama tidak digunakan                           |

2. Analisis Perbedaan Page Fault

Berdasarkan hasil simulasi menggunakan reference string
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2 dengan 3 frame memori, diperoleh hasil bahwa algoritma FIFO menghasilkan jumlah page fault lebih banyak dibandingkan LRU.

- Perbedaan jumlah page fault terjadi karena cara masing-masing algoritma menentukan halaman yang akan diganti ketika memori penuh.
- Algoritma FIFO (First-In First-Out) mengganti halaman yang pertama kali masuk ke memori, tanpa memperhatikan apakah halaman tersebut masih sering digunakan atau tidak. Akibatnya, FIFO dapat menghapus halaman yang sebenarnya masih dibutuhkan dalam waktu dekat, sehingga meningkatkan kemungkinan terjadinya page fault berikutnya.

Sebaliknya, LRU (Least Recently Used) mengganti halaman yang paling lama tidak digunakan. Algoritma ini memanfaatkan informasi riwayat penggunaan halaman, sehingga halaman yang sering diakses tetap dipertahankan di memori. Hal ini menyebabkan jumlah page fault pada LRU lebih sedikit dibanding FIFO.

3. Analisis Efisiensi: Mengapa LRU Lebih Baik?

Algoritma LRU dianggap lebih efisien dibanding FIFO karena lebih sesuai dengan pola akses memori program, di mana halaman yang baru saja digunakan cenderung akan digunakan kembali dalam waktu dekat (locality of reference).

Beberapa alasan utama mengapa LRU lebih efisien:

-  Mempertahankan halaman yang sering digunakan
LRU tidak mengganti halaman yang baru diakses, sehingga mengurangi kemungkinan page fault berulang pada halaman penting.

- Mengurangi penggantian halaman yang tidak perlu
FIFO dapat mengganti halaman aktif hanya karena halaman tersebut masuk lebih awal ke memori, sedangkan LRU menghindari hal ini.

- Tidak mengalami Belady’s Anomaly
LRU merupakan algoritma stack-based, sehingga penambahan jumlah frame tidak akan meningkatkan jumlah page fault, berbeda dengan FIFO yang dapat mengalami anomali tersebut.

- Lebih mendekati algoritma optimal
LRU mendekati perilaku algoritma optimal (OPT) karena menggunakan informasi penggunaan masa lalu sebagai pendekatan prediksi kebutuhan di masa depan.

- Dengan pertimbangan tersebut, LRU menghasilkan performa yang lebih stabil dan efisien, terutama pada sistem dengan pola akses memori yang dinamis dan berulang.

"Catatan Penting: Meskipun LRU lebih efisien secara hasil, ia membutuhkan pemrosesan yang lebih kompleks (seperti memperbarui stack atau timestamp setiap kali ada akses) dibandingkan FIFO yang hanya memerlukan pointer sederhana."


---

## Kesimpulan
Berdasarkan hasil simulasi, algoritma LRU menghasilkan jumlah page fault lebih sedikit dibanding FIFO. Hal ini karena LRU mengganti halaman yang paling lama tidak digunakan, sehingga lebih sesuai dengan pola akses memori. Sementara itu, FIFO mengganti halaman berdasarkan urutan masuk tanpa mempertimbangkan frekuensi penggunaan, sehingga kurang efisien. Oleh karena itu, LRU lebih efektif dalam manajemen memori virtual dibanding FIFO.

---

## Quiz
**1. Apa perbedaan utama FIFO dan LRU?**  
FIFO berdasarkan urutan masuk, LRU berdasarkan terakhir digunakan.

**2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?**  
Karena penambahan frame justru bisa meningkatkan page fault akibat strategi yang tidak adaptif.

**3. Mengapa LRU lebih baik dari FIFO?**  
Karena mempertimbangkan pola penggunaan halaman sehingga lebih optimal.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
jarang bertemu pembelajaran tatap muka
- Bagaimana cara Anda mengatasinya?
tetap mengerjakan  dan tetap semangat

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
