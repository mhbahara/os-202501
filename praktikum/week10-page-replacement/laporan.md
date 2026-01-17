
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Faiq Atha Rulloh
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---
## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **manajemen memori virtual**, khususnya mekanisme **page replacement**.  
Fokus utama praktikum adalah memahami bagaimana sistem operasi mengganti halaman (*page*) di memori utama ketika terjadi *page fault*, serta membandingkan performa algoritma **FIFO (First-In First-Out)** dan **LRU (Least Recently Used)**.

Mahasiswa akan mengimplementasikan **program simulasi page replacement**, menjalankan dataset uji, dan menyajikan hasil dalam bentuk tabel atau grafik.

---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---


## Dasar Teori
1. FIFO (First-In, First-Out)
Algoritma ini adalah yang paling sederhana. Logikanya mirip dengan antrean: halaman yang pertama kali masuk ke memori adalah yang pertama kali akan diganti.
2. LRU (Least Recently Used)
LRU lebih cerdas dibanding FIFO karena didasarkan pada prinsip lokalitas temporal. Algoritma ini berasumsi bahwa halaman yang baru saja digunakan kemungkinan besar akan digunakan lagi dalam waktu dekat.

---
## Langkah Pengerjaan
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

## Kode / Perintah
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

## Hasil Eksekusi

![Screenshot hasil](<screenshots/Eksperimen_Simulsi FIFO dan LRU_Week_10.png>)

---

## Analisis
**Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | 10 | paling lama masuk akan diganti lebih dulu |
   | LRU | 9 | paling lama tidak digunakan akan diganti lebih dulu.|


- Jelaskan mengapa jumlah *page fault* bisa berbeda.
    - **jawaban** : Karena kedua algortima tersebut memiliki cara kerja yang berbeda. 
    >misalkan pada algoritma FIFO disitu penggantian angka, yang paling lama tidak dipakai akan diganti tanpa mematuhi urutan halaman sedangkan algoritma LRU  disitu penggantian angka, yang paling lama tidak dipakai akan diganti namun harus mematuhi urutan halaman.

- Analisis algoritma mana yang lebih efisien dan alasannya.
  
   - **Jawaban** : Menurut saya yang paling efisien adalah algoritma FIFO karena pada algoritma tersebut memiliki implementasi yang sederhana.

---


## Tugas
1. Buat program simulasi page replacement FIFO dan LRU. &#10003;
2. Jalankan simulasi dengan dataset uji. &#10003;
3. Sajikan hasil simulasi dalam tabel atau grafik. &#10003;
4. Tulis laporan praktikum pada `laporan.md`. &#10003;

## Quiz
Jawab pada bagian **Quiz** di laporan:
1. Apa perbedaan utama FIFO dan LRU?
- Perbedaanya adalah pada prinsip dasar kalau FIFO berdasarkan Waktu kedatangan, sedangkan LRU berdasarkan Waktu penggunaan terakhir.
2. Mengapa FIFO dapat menghasilkan *Belady’s Anomaly*?
- karena penyebab Utama anomaly belady  adalah karena FIFO tidak memiliki (inclusion property) = manajemen memori yang menjamin bahwa performa sistem tidak akan memburuk jika kita menambah kapasitas RAM.
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
- karena LRU bekerja berdasarkan perilaku nyata dari sebuah program, sedangkan FIFO hanya bekerja berdasarkan urutan Waktu tanpa logika kegunaan.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
   - paling menantang pada minggu ini adalah memahami inclusion property dan belady's anomaly
- Bagaimana cara Anda mengatasinya?  
   - cara mengatasinya dengan visualisasi dengan tabel dan menggunakan analogi sederhana untuk memahami inclusion property dan belady's anomaly.


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
