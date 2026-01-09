
# Laporan Praktikum Minggu [13]
Topik: **Docker – Resource Limit (CPU & Memori)**

---

## Identitas
- **Nama**  : [Miftakhul Lisna Esa Baehaqi]  
- **NIM**   : [250202951]  
- **Kelas** : [1 IKRB]

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan CPU dan memori.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.
---

## Dasar Teori

1. Docker & Containerization

Container adalah teknologi virtualisasi tingkat OS yang memungkinkan aplikasi berjalan di lingkungan terisolasi tetapi tetap menggunakan kernel host. Container lebih ringan dibanding VM karena:

- Tidak membutuhkan Guest OS.

- Startup cepat.

- Overhead rendah.

Docker menyediakan mekanisme packaging aplikasi beserta dependensinya ke dalam image, lalu dijalankan sebagai container.

2. Isolasi Resource dengan cgroups

Linux cgroups digunakan oleh Docker untuk:

- Mengatur batas CPU

- Mengatur batas memori

- Monitoring penggunaan resource

Contoh parameter Docker:

- --cpus="0.5" → membatasi maksimal 50% CPU core

- --memory="256m" → membatasi memori maksimum 256MB

Jika aplikasi melewati batas:

- CPU akan diperlambat (throttling)

- Memori berlebih dapat menyebabkan error Out of Memory (OOM)

3. Perbedaan Tanpa Limit vs Dengan Limit.

| Kondisi             | Perilaku                                                          |
| ------------------- | ----------------------------------------------------------------- |
| Tanpa limit         | Proses berjalan maksimal mengikuti kemampuan CPU & RAM            |
| Dengan limit CPU    | Program tetap berjalan tetapi lebih lambat                        |
| Dengan limit Memori | Program bisa gagal jika membutuhkan memori lebih besar dari batas |


---

## Langkah Praktikum
1. 1. Persiapan

docker version
docker ps

Pastikan Docker berjalan:

2. Program Uji

Program dibuat untuk:

- melakukan komputasi intensif (CPU),

- mengalokasikan memori bertahap.  

3. Dockerfile.
```python
# Menggunakan Python 3.11 slim sebagai base image
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Install psutil untuk monitoring resource
RUN pip install --no-cache-dir psutil

# Copy aplikasi ke container
COPY app.py .

# Make script executable
RUN chmod +x app.py

# Set default command
CMD ["python", "app.py"]
```
Build image

docker build -t week13-resource-limit .



4. Menjalankan Tanpa Limit.
```python
docker run --rm week13-resource-limit
```
Pengamatan:

- Program berjalan cepat

- Memori bertambah terus

- Potensi memenuhi RAM host jika dibiarkan

5. Menjalankan Dengan Limit Resource
```python
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```


Pengamatan:

- Eksekusi lebih lambat (CPU throttling)

- Saat memori mencapai batas 256MB, container berhenti / error OOM

- Sistem host tetap aman karena batas memori dilindungi oleh cgroups

6. Monitoring


---

## Kode / Perintah
1. Program Uji Resource (Python)
```python
#!/usr/bin/env python3
"""
Program Uji Resource Limit Docker
Menguji penggunaan CPU dan Memori
"""

import time
import psutil
import os
from datetime import datetime

def print_resource_info():
    """Menampilkan informasi penggunaan resource saat ini"""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    
    print(f"\n{'='*60}")
    print(f"Waktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"PID: {os.getpid()}")
    print(f"Memory RSS: {mem_info.rss / 1024 / 1024:.2f} MB")
    print(f"Memory VMS: {mem_info.vms / 1024 / 1024:.2f} MB")
    print(f"CPU Percent: {process.cpu_percent(interval=1):.2f}%")
    print(f"{'='*60}\n")

def cpu_intensive_task(duration=5):
    """
    Task yang menggunakan CPU intensif
    Args:
        duration: durasi dalam detik
    """
    print(f"[CPU TEST] Memulai komputasi intensif selama {duration} detik...")
    start_time = time.time()
    counter = 0
    
    while time.time() - start_time < duration:
        # Operasi matematika untuk menggunakan CPU
        result = sum([i**2 for i in range(1000)])
        counter += 1
    
    print(f"[CPU TEST] Selesai. Iterasi: {counter:,}")
    return counter

def memory_intensive_task(target_mb=200, step_mb=50):
    """
    Task yang mengalokasikan memori bertahap
    Args:
        target_mb: target memori yang akan dialokasikan (MB)
        step_mb: step alokasi per tahap (MB)
    """
    print(f"\n[MEMORY TEST] Mengalokasikan memori bertahap...")
    print(f"Target: {target_mb} MB, Step: {step_mb} MB")
    
    data_chunks = []
    allocated = 0
    
    try:
        while allocated < target_mb:
            # Alokasikan chunk memori (1 MB = 1024*1024 bytes)
            chunk_size = min(step_mb, target_mb - allocated)
            chunk = bytearray(chunk_size * 1024 * 1024)
            data_chunks.append(chunk)
            allocated += chunk_size
            
            print(f"  → Dialokasikan: {allocated} MB")
            print_resource_info()
            time.sleep(1)
        
        print(f"[MEMORY TEST] Berhasil mengalokasikan {allocated} MB")
        print("Menahan memori selama 3 detik...")
        time.sleep(3)
        
    except MemoryError:
        print(f"[MEMORY TEST] ❌ MemoryError! Hanya berhasil alokasi {allocated} MB")
    except Exception as e:
        print(f"[MEMORY TEST] ❌ Error: {e}")
    finally:
        print(f"[MEMORY TEST] Membersihkan memori...")
        data_chunks.clear()

def main():
    print("\n" + "="*60)
    print("DOCKER RESOURCE LIMIT TEST")
    print("="*60)
    
    # Informasi awal
    print("\n[INFO] Resource awal:")
    print_resource_info()
    
    # Test 1: CPU Intensive
    print("\n" + "-"*60)
    print("TEST 1: CPU INTENSIVE")
    print("-"*60)
    cpu_intensive_task(duration=5)
    print_resource_info()
    
    # Test 2: Memory Intensive
    print("\n" + "-"*60)
    print("TEST 2: MEMORY INTENSIVE")
    print("-"*60)
    memory_intensive_task(target_mb=200, step_mb=50)
    print_resource_info()
    
    # Test 3: Kombinasi CPU + Memory
    print("\n" + "-"*60)
    print("TEST 3: KOMBINASI CPU + MEMORY")
    print("-"*60)
    print("[KOMBINASI] Menjalankan CPU dan Memory test bersamaan...")
    
    # Alokasi memori 100 MB
    data = bytearray(100 * 1024 * 1024)
    print(f"  → Alokasi 100 MB memori")
    
    # CPU intensive dengan memori terpakai
    cpu_intensive_task(duration=3)
    print_resource_info()
    
    # Cleanup
    del data
    
    print("\n" + "="*60)
    print("SEMUA TEST SELESAI")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()

```

2. kode perintah yang dijalankan
- Container Tanpa Limit
Perintah: 
docker run --rm week13-resource-limit
- Container dengan CPU Limit (0.5 CPU)
Perintah
```python
docker run --rm --cpus="0.5" week13-resource-limit
```
 - Container dengan Memory Limit (256 MB)
Perintah:
```python
docker run --rm --memory="256m" week13-resource-limit
```
- Container dengan CPU & Memory Limit
Perintah:
``` python
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
- Monitoring dengan docker stats
```python
# Terminal 1: Jalankan container (tanpa --rm agar bisa dimonitor)
docker run --name test-resource --cpus="0.5" --memory="256m" week13-resource-limit

# Terminal 2: Monitor
docker stats test-resource
```
---

## Hasil Eksekusi

 Build Docker Image
 ![Screenshot hasil](./screenshots/build%20docker.png)

## Eksperimen 1: Container Tanpa Limit
Perintah: docker run --rm week13-resource-limit
![Screenshot hasil](./screenshots/Container%20Tanpa%20Limit%201.png)
![Screenshot hasil](./screenshots/Container%20Tanpa%20Limit%202.png)
![Screenshot hasil](./screenshots/Container%20Tanpa%20Limit%203.png)

## Eksperimen 2: Container dengan CPU Limit (0.5 CPU)
Perintah
``` python
docker run --rm --cpus="0.5" week13-resource-limit
```
![Screenshot hasil](./screenshots/Container%20dengan%20CPU%20Limit%20(0.5%20CPU)%201.png)
![Screenshot hasil](./screenshots/Container%20dengan%20CPU%20Limit%20(0.5%20CPU)%202.png)
![Screenshot hasil](./screenshots/Container%20dengan%20CPU%20Limit%20(0.5%20CPU)%203.png)
![Screenshot hasil](./screenshots/Container%20dengan%20CPU%20Limit%20(0.5%20CPU)%204.png)

## Eksperimen 3: Container dengan Memory Limit (256 MB)
Perintah:
``` python
bashdocker run --rm --memory="256m" week13-resource-limit
```
![Screenshot hasil](./screenshots/Container%20dengan%20Memory%20Limit%20(256%20MB)1.png)
![Screenshot hasil](./screenshots/Container%20dengan%20Memory%20Limit%20(256%20MB)2.png)
![Screenshot hasil](./screenshots/Container%20dengan%20Memory%20Limit%20(256%20MB)3.png)

## Eksperimen 4: Container dengan CPU & Memory Limit
Perintah:
```python
bashdocker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
![Screenshot hasil](./screenshots/Container%20dengan%20CPU%20&%20Memory%20Limit1.png)
![Screenshot hasil](./screenshots/Container%20dengan%20CPU%20&%20Memory%20Limit2.png)
![Screenshot hasil](./screenshots/Container%20dengan%20CPU%20&%20Memory%20Limit3.png)

## Monitoring dengan docker stats
Perintah:
```python
# Terminal 1: Jalankan container (tanpa --rm agar bisa dimonitor)
docker run --name test-resource --cpus="0.5" --memory="256m" week13-resource-limit

# Terminal 2: Monitor
docker stats test-resource
Perintah

# Terminal 1: Jalankan container (tanpa --rm agar bisa dimonitor)
docker run --name test-resource --cpus="0.5" --memory="256m" week13-resource-limit

# Terminal 2: Monitor
docker stats test-resource
```
![Screenshot hasil](./screenshots/Monitoring%20dengan%20docker%20stats1%20(1).png)
![Screenshot hasil](./screenshots/Monitoring%20dengan%20docker%20stats1%20(2).png)
![Screenshot hasil](./screenshots/Monitoring%20dengan%20docker%20stats1%20(3).png)







---

## Analisis
1. CPU Limiting

- Docker membatasi CPU dengan cgroups melalui mekanisme cpu quota.

- --cpus="0.5" = container hanya boleh pakai 50% dari satu core.

Dampak:

- Performa turun linear (≈50% lebih lambat).

- Tetap stabil, predictable, dan tanpa overhead berarti.

- Scheduler Linux (CFS) memastikan pembagian CPU adil.

2. Memory Limiting

- Dibatasi dengan --memory (hard limit) + opsi swap.

- Jika penggunaan melebihi limit → OOM Killer menghentikan container.

Penyebab kegagalan:

- Tidak ada ruang buffer (runtime + GC juga butuh memori tambahan).

Kesimpulan:

- Memory limit bersifat keras / absolut, tidak ada “kasihan”.

3. Kombinasi CPU + Memory

Dengan --cpus="0.5" dan --memory="256m":

- CPU: performa turun setengah.

- Memory: aplikasi gagal jika butuh memori lebih besar.

Efeknya bukan hanya lambat, tapi juga mempersempit pilihan algoritma dan perilaku aplikasi.

4. Dampak Sistem

- Tanpa limit → risiko “noisy neighbor”, sistem host bisa berat.

- Dengan limit → penggunaan resource lebih adil, stabil, dan aman.

5. Insight Penting

- CPU limit → efisien dan predictable.

- Memory limit → keras dan berpotensi fatal jika salah sizing.

- Monitoring sangat penting (docker stats, metrics CPU & memory).

- Harus ada buffer memori 30–50% di atas kebutuhan aplikasi asli.

Kesimpulan Utama

Docker resource limit efektif, efisien, dan sangat penting untuk stabilitas sistem. Namun, penentuan limit harus direncanakan dengan benar—khususnya memori—agar aplikasi tidak sering mengalami OOM. Teknologi ini krusial untuk lingkungan production, DevOps, dan cloud-native.

---

## Kesimpulan
- Docker Resource Limit menggunakan Linux cgroups untuk membatasi CPU dan memori container secara efektif
- CPU Limit berdampak langsung pada performa komputasi - limit 0.5 CPU menurunkan throughput hingga 50%
- Memory Limit bersifat hard limit - aplikasi akan error/killed jika melebihi batas
- Resource Planning sangat penting - perlu memahami kebutuhan aplikasi dan set limit dengan buffer yang cukup
- Monitoring dengan docker stats membantu mengidentifikasi bottleneck dan optimasi resource
- Container dengan resource limit tepat memastikan multi-tenancy yang adil dan sistem yang stabil
---

## Quiz
1. [Mengapa container perlu dibatasi CPU dan memori?]  
   **Jawaban:**  
   container perlu dibatasi CPU dan memori karena beberapa alasan:
- Isolasi Resource: Mencegah satu container menghabiskan seluruh resource sistem dan mengganggu container lain (noisy neighbor problem)
- Stabilitas Sistem: Menjaga sistem host tetap stabil dan responsif
- Resource Planning: Membantu perencanaan kapasitas dan scheduling container di cluster (mis. Kubernetes)
- Billing & Cost Control: Dalam cloud computing, pembatasan resource membantu kontrol biaya
- Quality of Service (QoS): Memastikan setiap aplikasi mendapat resource yang dijanjikan
- Keamanan: Mencegah serangan DoS di mana container jahat menghabiskan resource sistem
2. [Apa perbedaan VM dan container dalam konteks isolasi resource]  
   **Jawaban:**  
Perbedaan Kunci:

- VM: Menggunakan hypervisor (KVM, VMware, Hyper-V) yang memvirtualisasi hardware. Setiap VM memiliki kernel OS sendiri yang sepenuhnya terisolasi. Resource dialokasikan secara eksklusif.

 Container: Menggunakan kernel Linux features seperti:
 
- cgroups (control groups): Membatasi dan mengukur resource usage
- namespaces: Mengisolasi process, network, filesystem
- Lebih efisien karena sharing kernel, tapi isolasi tidak se-ketat VM



Container cocok untuk microservices dan deployment cepat, VM cocok untuk isolasi keamanan maksimal atau menjalankan OS berbeda.

3. [Apa dampak limit memori terhadap aplikasi yang boros memori]  
   **Jawaban:**  

Dampak limit memori pada aplikasi yang boros memori:
1. Out of Memory (OOM) Kill

- Jika aplikasi mencoba menggunakan memori melebihi limit, Linux OOM Killer akan terminate container
- Tidak ada graceful shutdown, aplikasi langsung dihentikan
- Data di memory yang belum disimpan akan hilang

2. MemoryError Exception

- Aplikasi modern (Python, Java, dll) akan raise MemoryError saat gagal alokasi
- Aplikasi mungkin crash jika tidak handle exception dengan baik

3. Performance Degradation

- Jika mendekati limit, sistem akan mulai swapping (jika swap diaktifkan)
- Swapping sangat lambat, membuat aplikasi menjadi tidak responsif
- Thrashing: CPU sibuk melakukan swap, performa turun drastis

4. Unpredictable Behavior

- Memory allocation gagal bisa menyebabkan perilaku tidak terduga
- Null pointer, corrupted data, partial operation

Solusi Best Practice:

- Set memory limit 20-30% lebih tinggi dari kebutuhan normal
- Implement memory monitoring dan alerting
- Optimize aplikasi untuk efisien memori (object pooling, caching strategy)
- Gunakan memory profiler untuk menemukan memory leak
- Set memory request dan limit yang realistis di Kubernetes

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
pusingggggggggggggggggggggggg 
- Bagaimana cara Anda mengatasinya?  
tanya ke anak poltek

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
