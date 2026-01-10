# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : FAIQ ATHA RULLOH
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---
## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa mempelajari konsep **containerization** menggunakan Docker, serta bagaimana sistem operasi membatasi pemakaian sumber daya proses melalui mekanisme isolasi dan kontrol resource (mis. *cgroups* pada Linux).

Fokus praktikum adalah:
1. Membuat **Dockerfile sederhana** untuk menjalankan aplikasi/skrip.
2. Menjalankan container dengan **pembatasan resource** (CPU dan memori).
3. Mengamati dampak pembatasan resource melalui output program dan monitoring sederhana.

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.
---

## Dasar Teori
1. Docker adalah Aplikasi yang  Membagi 1 OS jadi banyak "wadah" terisolasi untuk aplikasi
2. Containerization adalah proses memaketkan perangkat lunak agar bisa dikirim dan dijalankan dengan cepat, aman dan tanpa eror karena beda perangkat
3. cgroup mengaitkan sekumpulan tugas dengan sekumpulan parameter untuk satu atau lebih subsistem.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   - Jalankan container dengan batasan resource (contoh):
     ```bash
     docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
     ```
   - Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

---

## Kode / Perintah
```bash
import sys
import time

def jalankan_tes():
    # Mengambil mode (cpu/mem) dari perintah terminal
    mode = sys.argv[1].lower() if len(sys.argv) > 1 else "cpu"
    
    print("\n" + "="*50)
    print(f"    PENGUJIAN RESOURCE DOCKER: {mode.upper()}")
    print("="*50)

    if mode == "cpu":
        print(f"{'Waktu':<10} | {'Total Iterasi CPU':<20} | {'Status'}")
        print("-" * 50)
        
        iterasi = 0
        start_time = time.time()
        last_report = time.time()
        
        try:
            while True:
                # Operasi beban CPU
                _ = 500 * 500
                iterasi += 1
                
                # Tampilkan output setiap 1 detik agar perubahan terlihat jelas
                curr_time = time.time()
                if curr_time - last_report >= 1:
                    durasi = int(curr_time - start_time)
                    print(f"{durasi:>3} detik  | {iterasi:>20,} | Running...")
                    last_report = curr_time
        except KeyboardInterrupt:
            print("\n[!] Pengujian CPU dihentikan manual.")

    elif mode == "mem":
        print(f"{'Waktu':<10} | {'Penggunaan RAM':<20} | {'Visual'}")
        print("-" * 50)
        
        data = []
        start_time = time.time()
        try:
            while True:
                # Tambah 20MB tiap detik
                data.append(bytearray(20 * 1024 * 1024))
                total_mb = len(data) * 20
                durasi = int(time.time() - start_time)
                
                # Visualisasi bar sederhana
                bar = "█" * (total_mb // 20)
                print(f"{durasi:>3} detik  | {total_mb:>17} MB | {bar}")
                
                time.sleep(1)
        except:
            # Jika limit memory tersentuh, Docker akan mematikan container
            print("\n" + "!"*50)
            print(" [!!!] KILLED: PENGGUNAAN MEMORI MELEBIHI LIMIT")
            print("!"*50)

if __name__ == "__main__":
    jalankan_tes()
```
---

## Hasil Eksekusi
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.✅
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

![Screenshot hasil](<screenshots/docker version and ps.png>)

- Pengecekkan pada aplikasi docker
  
![Screenshot hasil](<screenshots/docker.png>)

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

![Screenshot hasil](<screenshots/app.png>)

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

![Screenshot hasil](<screenshots/docker build.png>)

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit cpu
     docker run --rm week13-resource-limit mem
     ```
   - Catat output/hasil pengamatan.

![Screenshot hasil](<screenshots/hasil_tanpa_limit_cpu.png>)

![Screenshot hasil](<screenshots/hasil_tanpa_limit_memori.png>)

| Aspek Pengamatan | Hasil Pengamatan (Output) | Perilaku Program                                                |
|------------------|---------------------------|-----------------------------------------------------------------|
| Iterasi CPU      | Sangat Tinggi (Maksimal)  | Program menggunakan seluruh daya CPU yang tersedia tanpa batas. |
| Alokasi Memori   | Terus bertambah (> 300MB) | Program tidak berhenti meskipun penggunaan RAM sangat besar.    |
| Docker Stats     | CPU % bisa di atas 100%   | Memory Limit menunjukkan total RAM komputer fisik.              |
| Kondisi Akhir    | Berjalan Terus (Running)  | Hanya berhenti jika ditekan Ctrl+C secara manual.               |

- Penjelasan perubahan perilaku program : Tanpa Limit Program memiliki akses 100% ke core CPU. Hasilnya, jumlah iterasi per detik sangat tinggi karena prosesor bekerja pada kecepatan penuh untuk menyelesaikan perhitungan matematika dalam kode.
5. **Menjalankan Container Dengan Limit Resource**

   - Jalankan container dengan batasan resource (contoh):
     ```bash
     docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit cpu
     docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit mem
     ```
   - Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

![Screenshot hasil](<screenshots/hasil_limit.png>)

![Screenshot hasil](<screenshots/hasil_limit_memory.png>)

| Aspek Pengamatan | Hasil Pengamatan (Output) | Perilaku Program                                          |
|------------------|---------------------------|-----------------------------------------------------------|
| Iterasi CPU      | Menurun Drastis (~50%)    | Melambat: Terjadi pembatasan waktu proses (Throttling).   |
| Alokasi Memori   | Terhenti di angka ~256 MB | Killed: Program dimatikan sistem saat batas RAM tercapai. |
| Docker Stats     | CPU % Terkunci di 50.00%  | Memory Limit terkunci tepat di angka 256 MiB.             |
| Kondisi Akhir    | Terhenti (OOM Killed)     | Docker berhasil mengisolasi resource agar tidak boros.    |


- Penjelasan perubahan perilaku program : Dengan Limit (0.5) Program tetap berstatus Running, namun angka iterasi CPU bertambah jauh lebih lambat (turun sekitar 50%).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

![Screenshot hasil](<screenshots/docker stats.png>)

---

### Analisis
1. Analisis Performa CPU (Dibatasi dengan Bebas)

- Tanpa Limit CPU
   - Program bekerja seperti **mobil yang dipacu dengan kecepatan maksimal**. Seluruh tenaga mesin (prosesor) digunakan, sehingga:
      - Jumlah perhitungan (iterasi) sangat tinggi
      - Waktu eksekusi sangat cepat
      - CPU digunakan tanpa batas

- Dengan Limit CPU (0.5 Core)
   - Program seperti **mobil dengan pembatas kecepatan**. Program tetap berjalan, tetapi:
      - Kecepatan proses dibatasi
      - Jumlah iterasi jauh lebih sedikit dalam waktu yang sama
      - Terjadi *CPU throttling*

- Kesimpulan CPU
   - Batasan CPU **tidak mematikan program**, tetapi **memperlambat eksekusi** secara signifikan.
  
2. Analisis Kapasitas Memori (Dibatasi dengan Bebas)

- Tanpa Limit Memori
   - Program seperti **gelas yang terus diisi air tanpa henti**. Selama masih ada RAM di sistem:
      - Penggunaan memori terus meningkat
      - Program tidak berhenti
      - Berpotensi menghabiskan seluruh RAM host

- Dengan Limit Memori (256 MB)
   - Program seperti **gelas dengan kapasitas tetap**.Ketika penggunaan memori:
      - Melewati batas 256 MB
      - Docker langsung menghentikan program (*OOM Killed*)

- Kesimpulan Memori
   - Batasan memori adalah **batas keras (hard limit)**. Jika terlampaui sedikit saja, program **langsung dimatikan demi stabilitas sistem**.

---
### Kesimpulan

> "Hasil pengujian menunjukkan bahwa Docker memanfaatkan fitur **control groups (cgroups)** untuk mengelola dan membatasi penggunaan sumber daya sistem. Penerapan **limit CPU** menyebabkan penurunan kecepatan eksekusi aplikasi (program tetap berjalan namun melambat), sedangkan penerapan **limit memori** mengakibatkan **penghentian paksa aplikasi (OOM Killed)** ketika penggunaan memori melebihi kapasitas yang telah ditentukan. Dengan demikian, pembatasan CPU berfungsi sebagai mekanisme pengendalian kinerja, sementara pembatasan memori bertindak sebagai mekanisme proteksi sistem untuk menjaga stabilitas dan mencegah pemborosan sumber daya."

---
### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa container perlu dibatasi CPU dan memori?
- Untuk mencegah  efek Noisy Neighbor
- Untuk melindungi sistem utama
- Untuk keamanan dari serangan DoS

2. Apa perbedaan VM dan container dalam konteks isolasi resource?
- jika butuh keamanan maksimal atau ingin menjalankan OS berbeda (misal: jalankan Windows di dalam Linux) Gunakan VM.
- jika  ingin menjalankan banyak aplikasi dengan cepat dan hemat memori di satu sistem yang sama gunakan Container.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?
- Dampak limit memori terhadap aplikasi yang boros memori disebabkan oleh mekanisme manajemen sumber daya di dalam sistem operasi menjadikannya:
   - Kinerja Melambat
   - Gagal menjalankan fungsi tertentu
   - Eksekusi hukuman mati (_OOM Killed_)

---

## Refleksi Diri
Tuliskan secara singkat:
1. Apa bagian yang paling menantang minggu ini?
  
  - Bagian yang paling menantang adalah Menjalankan Container Dengan Limit Resource
   
2. Bagaimana cara Anda mengatasinya?

  - cara mengatasinya dengan menyesuaikan nilai limit (Up-scaling)

---

**Credit:**
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
