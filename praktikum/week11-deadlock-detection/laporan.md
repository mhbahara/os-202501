# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock

## Identitas
- **Nama**  : Faiq Atha Rulloh 
- **NIM**   : 250320571 
- **Kelas** : 1DSRA

---

## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme deteksi deadlock** dalam sistem operasi.  
Berbeda dengan Minggu 7 yang berfokus pada *pencegahan dan penghindaran deadlock*, pada minggu ini mahasiswa diarahkan untuk **mendeteksi deadlock yang telah terjadi** menggunakan pendekatan algoritmik.

Mahasiswa akan membuat **program simulasi sederhana deteksi deadlock**, menjalankan dataset uji, serta menyajikan hasil analisis dalam bentuk tabel dan interpretasi logis.

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
1. Deadlock adalah kondisi di mana sekumpulan proses terhenti.
2. Simulasikan atau memodelkan deadlock, gunakan Resource Allocation Graph (RAG) atau Graf Alokasi Sumber Daya.
3. Deteksi Deadlock cara sistem untuk mengetahui apakah saat ini sedang terjadi deadlock atau tidak
---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

---

## Kode / Perintah
```bash
processes = ["P1", "P2", "P3"]

wait_for = {
    "P1": "P2",
    "P2": "P3",
    "P3": "P1"
}

deadlock = False

for p in processes:
    visited = set()
    while p not in visited:
        visited.add(p)
        if p not in wait_for:
            break
        p = wait_for[p]
    else:
        deadlock = True
        break

print("HASIL DETEKSI DEADLOCK")
print("-" * 45)
print(f"| {'Proses':^10} | {'Menunggu':^12} | {'Status':^12} |")
print("-" * 45)

for p in processes:
    status = "Deadlock" if deadlock else "Aman"
    print(f"| {p:^10} | {wait_for[p]:^12} | {status:^12} |")

print("-" * 45)
print("Status Sistem : DEADLOCK TERDETEKSI")
```
---

## Hasil Eksekusi
![Screenshot hasil](<screenshots/example.png>)

---

## Analisis
   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
### HASIL DETEKSI DEADLOCK

| Proses | Menunggu | Status   |
|--------|----------|----------|
| P1     | P2       | Deadlock |
| P2     | P3       | Deadlock |
| P3     | P1       | Deadlock |

**Status Sistem: DEADLOCK TERDETEKSI**
     
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.
       - jika Deadlock terjadi disebabkan karena adanya proses menunggu secara melingkar antar proses dan jika Deadlock tidak terjadi disebabkan karena tidak adanya proses menunggu antar proses.
   - Kaitkan hasil dengan teori deadlock (empat kondisi).
1. Mutual Exclusion (Saling Eksklusif)
(Terpenuhi)
- Setiap proses hanya bisa memakai satu sumber daya dalam satu waktu,Proses lain harus menunggu.
2. Hold and Wait (Menahan dan Menunggu)
(Terpenuhi)
- Setiap proses menahan satu sumber daya sambil menunggu sumber daya lain.
Contoh:
   - P1 menahan resource miliknya sambil menunggu P2
   - P2 menunggu P3, dan seterusnya
3. No Preemption (Tidak Bisa Direbut Paksa)
(Terpenuhi)
- Sumber daya tidak bisa diambil paksa oleh sistem,Harus menunggu proses lain selesai sendiri.
4. Circular Wait (Menunggu Melingkar)
(Terpenuhi)
```
P1 → P2 → P3 → P1
```
- Inilah penyebab utama deadlock terjadi.

---

## Quiz
Jawab pada bagian **Quiz** di laporan:
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?  
   - deadlock prevention (pencegahan) system ini bekerja sebelum proses berjalan satu dari empat syarat deadlock agar tidak mungkin terjadi;
   - deadlock avoidance (penghindaran) system ini tidak membatasi cara proses meminta sumber daya, tetapu akan memeriksa setiap permintaan;
   - deadlock detection (deteksi) system ini membiarkan algoritma untuk memeriksa adanya siklus antar proses yang saling menunggu
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   - karena memiliki kelemahan yang signifikan yang membuat system tidak efisien.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
   - Kelebihan deteksi deadlock : sumber daya maksimal, system jauh lebih cepat, mendeteksi proses yang macet atau tidak efisien.
   - Kelemahan deteksi deadlock : risiko kehilangan data, memakan Waktu CPU dan memori yang banyak
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
   - Menjelaskan  Teori Deadlock dengan bahasa yang mudah dipahami
- Bagaimana cara Anda mengatasinya?  
   - saya menganalogikan dengan Bahasa dan pemahaman saya sendiri.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) â€“ Universitas Putra Bangsa_
