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

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

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

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

![Screenshot hasil](<screenshots/>)

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

![Screenshot hasil](<screenshots/>)

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

![Screenshot hasil](<screenshots/>)

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit cpu
     docker run --rm week13-resource-limit mem
     ```
   - Catat output/hasil pengamatan.

![Screenshot hasil](<screenshots/>)

5. **Menjalankan Container Dengan Limit Resource**

   - Jalankan container dengan batasan resource (contoh):
     ```bash
     docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
     ```
   - Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

![Screenshot hasil](<screenshots/>)

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

![Screenshot hasil](<screenshots/>)

---

## Tugas & Quiz
### Tugas
1. Buat Dockerfile sederhana dan program uji di folder `code/`.
2. Build image dan jalankan container **tanpa limit**.
3. Jalankan container dengan limit **CPU** dan **memori**.
4. Sajikan hasil pengamatan dalam tabel/uraian singkat di `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa container perlu dibatasi CPU dan memori?
***Jawaban***
Untuk mencegah  efek Noisy Neighbor
Untuk melindungi sistem utama
Untuk keamanan dari serangan DoS

2. Apa perbedaan VM dan container dalam konteks isolasi resource?
***Jawaban***
jika butuh keamanan maksimal atau ingin menjalankan OS berbeda (misal: jalankan Windows di dalam Linux) Gunakan VM.
jika  ingin menjalankan banyak aplikasi dengan cepat dan hemat memori di satu sistem yang sama gunakan Container.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?
***Jawaban***
dampak limit memori terhadap aplikasi yang boros memori disebabkan oleh mekanisme manajemen sumber daya di dalam sistem operasi menjadikannya:
Kinerja Melambat
Gagal menjalankan fungsi tertentu
Eksekusi hukuman mati (OOM kill)

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
***Jawaban***
   - Bagian yang paling menantang adalah Menjalankan Container Dengan Limit Resource
- Bagaimana cara Anda mengatasinya?
***Jawaban***
   - cara mengatasinya dengan menyesuaikan nilai limit (Up-scaling)
---

**Credit:**
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
