
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : FAIQ ATHA RULLOH  
- **NIM**   : 250320571  
- **Kelas** : 1DSRA

---

## Topik
**Manajemen Memori – Page Replacement (FIFO & LRU)**

---

## 1. Pendahuluan (Introduction)
### 1.1 Latar belakang
Dalam sistem operasi modern, mekanisme virtual memory memungkinkan proses dapat dijalankan meskipun ukuran program lebih besar dibanding kapasitas memori fisik. Virtual memory umumnya menggunakan konsep demand paging, yaitu halaman hanya dimuat ke memori ketika diperlukan. Ketika memori utama sudah penuh dan terjadi page fault, sistem harus menentukan halaman mana yang akan diganti menggunakan page-replacement algorithm. Oleh karena itu, pemilihan algoritma page replacement menjadi sangat penting karena berpengaruh langsung terhadap jumlah page fault dan kinerja sistem secara keseluruhan (Silberschatz et al., 2018).

Salah satu algoritma yang sering digunakan adalah _First-In First-Out (FIFO)_. Algoritma ini mengganti halaman yang paling lama berada di memori. Walaupun sederhana dan mudah diterapkan, kelemahan FIFO adalah tidak mempertimbangkan frekuensi maupun waktu terakhir halaman digunakan, sehingga tidak selalu mencerminkan kebutuhan akses memori yang sebenarnya dan dapat menghasilkan jumlah page fault yang tinggi. Bahkan, dalam beberapa kondisi FIFO dapat mengalami peningkatan jumlah page fault meskipun jumlah frame ditambah (Silberschatz et al., 2018).

Sebaliknya, algoritma _Least Recently Used (LRU)_ memilih halaman yang paling lama tidak digunakan. Algoritma ini dianggap lebih mendekati perilaku optimal karena berdasarkan pada histori penggunaan halaman, sehingga lebih sesuai dengan prinsip locality pada sistem memori. Secara umum, LRU mampu menghasilkan page fault yang lebih sedikit dibanding FIFO. Namun, implementasinya lebih kompleks karena membutuhkan mekanisme pencatatan akses memori yang efisien dan terkadang memerlukan dukungan perangkat keras tambahan (Silberschatz et al., 2018).

---

### 1.2 Rumusan masalah
Rumusan masalah dalam praktikum ini adalah sebagai berikut:
1. Bagaimana mekanisme kerja algoritma FIFO dan LRU dalam proses page replacement?
2. Berapa jumlah page fault yang dihasilkan oleh masing-masing algoritma pada kondisi kapasitas frame tertentu?
3. Algoritma manakah yang lebih efisien berdasarkan jumlah page fault dan bagaimana kesesuaiannya dengan teori pada literatur Sistem Operasi?

---

### 1.3 Tujuan
Tujuan dari praktikum ini adalah :
1. Menganalisis kinerja algoritma page replacement FIFO dan LRU dalam pengelolaan memori virtual.
2. Membandingkan jumlah page fault yang dihasilkan oleh masing-masing algoritma pada reference string tertentu.
3. Mengidentifikasi algoritma yang lebih efisien berdasarkan hasil simulasi.
4. Memverifikasi apakah hasil simulasi sesuai

---

## 2. Metode (Methods)
### 2.1 Lingkungan uji
- **Perangkat Keras**:
    - System Manufacturer:	Acer
    - System Model : Veriton X
    - System Type :	x64-based PC
    - Processor	: Intel(R) Core(TM) i5-14400, 2500 Mhz, 10 Core(s), 16 Logical Processor(s)
    - Installed Physical Memory (RAM) : 8,00 GB
    - Installed Physical Disk (ROM) : 512 GB / SSD
    
- **Perangkat Lunak**:
    - OS Name :	Microsoft Windows 11 Home Single Language
    - Version Windows : 25H2

- **Bahasa Pemrograman**:
    - `Python 3.12.11`

- **Alat Pendukung**:
    - `Visual Studio Code 1.108.0 x64`
    
---

### 2.2 langkah eksperimen
Eksperimen dilakukan ada tahapan utama:
1. **Menyiapkan Dataset**
   - Menyiapkan Dataset: Menetapkan reference string  `[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]` 
   - Jumlah Frame: `3`

2. **Persiapan Lingkungan**
   - Alat Pendukungnya : `Visual Studio Code`
   - Bahasa Pemrograman : `Python`

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

---

### 2.3 Dataset
Dataset yang digunakan dalam eksperimen ini adalah:

- Reference String: `[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2] `
- Jumlah Frame: `3`
- Metode Algoritma:
   - _FIFO (First-In first-out)_.
   - _LRU (Least Recently Used)_.

---
## 2.4 Program
```bash
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3


def print_process_table(title, steps):
    print(f"\n{title}")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")
    print("| Page   | Frame 1  | Frame 2  | Frame 3  | Status   |")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")
    
    for page, mem, status in steps:
        print(f"| {page:<6} | {mem[0]:<8} | {mem[1]:<8} | {mem[2]:<8} | {status:<8} |")
    
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")


# ================= FIFO =================
def fifo_page_replacement(ref, frames):
    memory = ['-'] * frames
    fifo_index = 0
    steps = []
    page_fault = 0

    for page in ref:
        if page in memory:
            steps.append((page, memory.copy(), "HIT"))
        else:
            page_fault += 1
            memory[fifo_index] = page
            fifo_index = (fifo_index + 1) % frames
            steps.append((page, memory.copy(), "FAULT"))

    return page_fault, steps


# ================= LRU =================
def lru_page_replacement(ref, frames):
    memory = ['-'] * frames
    last_used = {}
    steps = []
    page_fault = 0

    for time, page in enumerate(ref):
        if page in memory:
            steps.append((page, memory.copy(), "HIT"))
        else:
            page_fault += 1
            if '-' in memory:
                index = memory.index('-')
            else:
                lru_page = min(last_used, key=last_used.get)
                index = memory.index(lru_page)
                del last_used[lru_page]

            memory[index] = page
            steps.append((page, memory.copy(), "FAULT"))

        last_used[page] = time

    return page_fault, steps


# ================= EKSEKUSI =================
fifo_fault, fifo_steps = fifo_page_replacement(reference_string, frames)
lru_fault, lru_steps = lru_page_replacement(reference_string, frames)

print_process_table("PROSES FIFO (First-In First-Out)", fifo_steps)
print_process_table("PROSES LRU (Least Recently Used)", lru_steps)

# ================= RINGKASAN =================
print("\nRINGKASAN HASIL AKHIR")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
print("| Algoritma | Jumlah Frame | Page Fault   |")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
print(f"| FIFO      | {frames:^12} | {fifo_fault:^12} |")
print(f"| LRU       | {frames:^12} | {lru_fault:^12} |")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
```

---

### 2.5 Cara pengukuran
1. Program membaca halaman satu per satu dari `reference_string`.
2. Setiap halaman dicek apakah sudah ada di memori:

    ```
    if page in memory
    ```

3. Jika halaman ada maka dicatat sebagai HIT
4. Jika halaman tidak ada maka dicatat sebagai FAULT dan nilai bertambah 1:

    ```
    page_fault += 1
    ```

5. Jika terjadi FAULT dan memori penuh:
    - FIFO = mengganti halaman yang paling lama masuk.
    - LRU = mengganti halaman yang paling lama tidak digunakan.
6. Setiap langkah (halaman, isi frame, dan status HIT/FAULT) disimpan dan ditampilkan dalam tabel proses.

7. Setelah semua halaman selesai diproses, total `page_fault` untuk FIFO dan LRU dihitung.

8. Hasil akhir dibandingkan:
    - Algoritma dengan jumlah page fault lebih sedikit dianggap lebih efisien.

>“Metode pengukuran ini mengacu  pada konsep evaluasi page replacement yang dijelaskan oleh Silberschatz (2018) dan Tanenbaum (2015) yang menggunakan jumlah page fault sebagai metrik utama.”

---

## 3. Hasil (Results)

![Screenshot](screenshots/example.png)

### 3.1 Tabel/grafik hasil uji

- PROSES FIFO (First-In First-Out)
  
| Page | Frame 1 | Frame 2 | Frame 3 | Status |
| ---- | ------- | ------- | ------- | ------ |
| 7    | 7       | -       | -       | FAULT  |
| 0    | 7       | 0       | -       | FAULT  |
| 1    | 7       | 0       | 1       | FAULT  |
| 0    | 7       | 0       | 1       | HIT    |
| 2    | 2       | 0       | 1       | FAULT  |
| 0    | 2       | 0       | 1       | HIT    |
| 3    | 2       | 0       | 3       | FAULT  |
| 0    | 2       | 0       | 3       | HIT    |
| 4    | 2       | 4       | 3       | FAULT  |
| 2    | 2       | 4       | 3       | HIT    |
| 3    | 2       | 4       | 3       | HIT    |
| 0    | 0       | 4       | 3       | FAULT  |

- PROSES LRU (Least Recently Used)

| Page | Frame 1 | Frame 2 | Frame 3 | Status |
| ---- | ------- | ------- | ------- | ------ |
| 7    | 7       | -       | -       | FAULT  |
| 0    | 7       | 0       | -       | FAULT  |
| 1    | 7       | 0       | 1       | FAULT  |
| 0    | 7       | 0       | 1       | HIT    |
| 2    | 7       | 0       | 2       | FAULT  |
| 0    | 7       | 0       | 2       | HIT    |
| 3    | 7       | 0       | 3       | FAULT  |
| 0    | 7       | 0       | 3       | HIT    |
| 4    | 7       | 4       | 3       | FAULT  |
| 2    | 7       | 4       | 2       | FAULT  |
| 3    | 7       | 4       | 3       | HIT    |
| 0    | 0       | 4       | 3       | HIT    |

- HASIL AKHIR

| Algoritma | Jumlah Frame | Page Fault |
| --------- | ------------ | ---------- |
| FIFO      | 3            | 10         |
| LRU       | 3            | 9          |

---

### 3.2 Ringkasan temuan
Berdasarkan hasil simulasi penggantian halaman menggunakan 13 reference string dan kapasitas 3 frame, ditemukan beberapa poin utama sebagai berikut:

1. Perbandingan Total Page Fault:
    - Algoritma FIFO menghasilkan sebanyak 10 page fault.
    - Algoritma LRU menghasilkan sebanyak 9 page fault.
    - Temuan ini menunjukkan bahwa untuk dataset ini, LRU memiliki efisiensi yang lebih tinggi dibandingkan FIFO dengan selisih 1 fault.

## 4. Pembahasan  (Discussion)
### 4.1 Interpretasi hasil
> Hasil simulasi menunjukkan bahwa algoritma LRU menghasilkan jumlah page fault yang lebih sedikit dibandingkan FIFO. Hal ini mengindikasikan bahwa LRU memiliki kinerja yang lebih efisien karena mempertimbangkan riwayat akses halaman sehingga lebih sesuai dengan prinsip locality of reference dan mendekati algoritma optimal . Sebaliknya, FIFO mengganti halaman berdasarkan urutan kedatangan tanpa mempertimbangkan pola penggunaan, sehingga berpotensi menghasilkan page fault lebih tinggi dan pada kondisi tertentu dapat mengalami Belady’s Anomaly, sehingga performanya tidak selalu optimal Hasil ini sejalan dengan teori literatur dan sumber pendukung lain yang menyatakan bahwa LRU umumnya memberikan performa yang lebih baik dibandingkan FIFO (Silberschatz et al., 2018).

---

### 4.2 Keterbatasan
1. Algoritma FIFO tidak mempertimbangkan pola maupun frekuensi akses halaman sehingga berpotensi menghasilkan jumlah page fault yang lebih tinggi dan pada kondisi tertentu dapat mengalami Belady’s Anomaly (Silberschatz et al., 2018).
2. Algoritma LRU, meskipun lebih efisien, memiliki tingkat kompleksitas implementasi yang tinggi karena memerlukan pencatatan riwayat akses memori secara kontinu, sehingga berpotensi menambah overhead sistem (Silberschatz et al., 2018).

---
### 4.3 Perbandingan teori
1. Di buku Silberschatz et al. (2018) (Operating System Concepts) menyatakan bahwa:
- FIFO :
    - Sederhana
    - Menggantikan halaman yang paling awal masuk
    - Dapat mengalami Belady’s Anomaly

- LRU :
    - Menggantikan halaman yang paling lama tidak digunakan
    - Lebih mendekati algoritma Optimal
    - Umumnya menghasilkan lebih sedikit page fault

2. Di Buku Tanenbaum (Modern Operating Systems) menyatakan bahwa:
  - FIFO tidak mempertimbangkan pola akses sehingga tidak selalu efisien
  - LRU memanfaatkan prinsip locality of reference
  - LRU biasanya lebih unggul dalam performa


---
### 4.4 Ekspektasi
Berdasarkan ekspetasi saya sebagai berikut:

1. FIFO
    - Sederhana dan mudah diimplementasikan.
    - Tidak mempertimbangkan riwayat penggunaan halaman.
    - Berpotensi mengalami Belady’s Anomaly (jumlah frame bertambah tetapi page fault meningkat).

2. LRU
    - Menggantikan halaman yang paling lama tidak digunakan.
    - Lebih mendekati algoritma optimal.
    - Biasanya menghasilkan lebih sedikit page fault dibanding FIFO.
    - Membutuhkan mekanisme pencatatan akses sehingga lebih kompleks.

---

## 5. Kesimpulan
Berdasarkan hasil simulasi dan analisis yang dilakukan, diperoleh kesimpulan sebagai berikut:

1. Algoritma FIFO dan LRU memiliki mekanisme kerja yang berbeda, di mana FIFO mengganti halaman paling awal masuk sedangkan LRU mengganti halaman yang paling lama tidak digunakan.
2. Pada pengujian menggunakan reference string `[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]` dengan `3 frame`, algoritma FIFO menghasilkan 10 page fault sedangkan LRU menghasilkan 9 page fault.
3. LRU terbukti lebih efisien dibanding FIFO pada skenario ini karena mempertimbangkan riwayat akses halaman, sehingga selaras dengan teori pada Silberschatz dan Tanenbaum.
4. Hasil praktikum ini konsisten dengan literatur bahwa LRU umumnya memberikan performa yang lebih baik dibandingkan FIFO, meskipun memiliki kompleksitas implementasi yang lebih tinggi.

---

## Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?
   - Karena strukturnya sistematis, agar memudahkan peneliti lain untuk mengulang/mengkaji percobaan, memverifikasi hasilnya dan hasil uji dapat dipahami, direplikasi, dan dievaluasi secara akademik.

2. Apa perbedaan antara bagian **Hasil** dan **Pembahasan**?
   - Hasil: Hanya menyajikan fakta/data apa adanya. 
   - Pembahasan: Menjelaskan makna data tersebut dan menghubungkannya dengan teori.
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?
   - Untuk menghindari plagiarisme dan memperkuat argumen laporan dengan dasar ilmiah yang valid.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
   - Menyusun data hasil praktikum dari minggu-minggu sebelumnya. 
- Bagaimana cara Anda mengatasinya?
   - Saya melakukan preview berulang kali agar struktur laporan tetap konsisten.  

---

## Daftar Pustaka
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts (10th ed.)*. Wiley.
2. Tanenbaum, A. Modern Operating Systems, 4th Ed.
3. GeeksforGeeks. (2023). *Page Replacement Algorithms in Operating Systems*. Retrieved from https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
