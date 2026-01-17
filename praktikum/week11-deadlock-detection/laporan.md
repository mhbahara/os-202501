
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
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(BASE_DIR, "dataset_deadlock.csv")

proses = []
alokasi = {}
request = {}

# Baca dataset
try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            
            if line == "" or line.lower().startswith("proses"):
                continue

            p, a, r = line.split(",")
            proses.append(p)
            alokasi[p] = a
            request[p] = r

except FileNotFoundError:
    print("ERROR: File dataset_deadlock.csv tidak ditemukan!")
    print("Path dicari:", filename)
    exit()

# Deteksi circular wait (deadlock)
deadlock = set()

for p in proses:
    visited = set()
    current = p

    while current not in visited:
        visited.add(current)
        res_diminta = request[current]

        
        next_process = None
        for q in proses:
            if alokasi[q] == res_diminta:
                next_process = q
                break

        if next_process is None:
            break

        if next_process == p:
            deadlock.update(visited)
            break

        current = next_process

print("=== Data Proses ===")
print("Proses | Alokasi | Request")
print("---------------------------")
for p in proses:
    print(f"{p:5} | {alokasi[p]:7} | {request[p]}")

if deadlock:
    print("\nKondisi Sistem: DEADLOCK TERDETEKSI")
    print("Terlibat deadlock:", ", ".join(sorted(deadlock)))
else:
    print("\nKondisi Sistem: AMAN (Tidak ada deadlock)")

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
Tabel hasil deteksi
|Proses|	Alokasi	|Meminta|Status|
|:---|:---|:---|:---|
P1|	R1|	R2|deadlock|
Halaman 2|	R2|	R3|deadlock|
P3|	R3|	R1|deadlock|

Dari haisl simulasi semua proses berada dalam keadaan deadlock.Deadlock terjadi karena setiap proses memegang satu resource dan menunggu resource lain yang dipegang proses berbeda, sehingga terbentuk circular wait P1 → P2 → P3 → P1 dan tidak ada proses yang dapat melanjutkan eksekusi.

   * P1 memegang R1 dan menunggu R2
   * P2 memegang R2 dan menunggu R3
   * P3 memegang R3 dan menunggu R1

Kaitkan hasil dengan teori deadlock
 * Mutual Exclusion -> Hanya satu proses yang dapat menggunakan suatu resource pada satu waktu dan proses lain harus menunggu hingga resource tersebut dilepaskan.
 * Hold and Wait -> Proses memegang satu resource sambil menunggu resource lain.
 * No Preemption -> Resource yang sudah diberikan kepada suatu proses tidak dapat diambil kembali secara paksa oleh sistem. Resource tersebut hanya dapat dilepaskan setelah proses selesai menggunakannya.
 * Circular Wait -> Terjadi siklus menunggu antar proses (P1 → P2 → P3 → P1) sehingga menyebabkan deadlock

---

## Kesimpulan
   * Program deteksi deadlock berhasil mengidentifikasi kondisi kebuntuan pada sistem dengan menelusuri hubungan alokasi dan permintaan sumber daya antar proses.
   * Berdasarkan hasil simulasi, seluruh proses berada dalam kondisi deadlock karena memenuhi keempat syarat deadlock, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait.

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
  Bagian  yang paling menantang dalam minggu ini menentukan deadlock yang benar  
- Bagaimana cara Anda mengatasinya?
  mencari referensi di website

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
