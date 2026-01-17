
# Laporan Praktikum Minggu 13
Topik: "Docker – Batasan Sumber Daya (CPU & Memori)"

---

## Identitas
- **Nama**  : Novia Safitri 
- **NIM**   : 250202923
- **Kelas** :1IKRA
---

## Tujuan
Setelah menyelesaikan tugas ini, siswa mampu:

1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.

2. Membangun image dan menjalankan container.

3. Jangkauan wadah dengan kekuatan CPU dan memori .

4. Mengamati dan menjelaskan perbedaan eksekusi kontainer dengan dan tanpa batas sumber daya.

5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
Docker adalah teknologi yang digunakan untuk menjalankan aplikasi di dalam container. Container ini bersifat terisolasi, tetapi tetap berbagi sumber daya dengan sistem operasi utama. Pada Docker, penggunaan CPU dan memori bisa dibatasi agar satu aplikasi tidak memakai sumber daya terlalu besar. Batas CPU mengatur seberapa banyak proses menggunakan prosesor, sedangkan batas memori mengatur jumlah memori yang boleh dipakai supaya sistem tetap stabil dan aplikasi lain tidak terganggu.

---

## Langkah Praktikum
1. Sesuaikan struktur folder seperti berikut:


           praktikum/week13-docker-resource-limit/
           ├─ code/
           │  ├─ Dockerfile
           │  └─ app.*
           ├─ screenshots/
           │  └─ hasil_limit.png
           └─ laporan.md

2. Siapkan Docker dan pastikan sudah berjalan: Verifikasi:

           docker version
           docker ps

3. Buat program sederhana di folder code/(bahasa bebas) yang:

    * Melakukan komputasi secara berulang (untuk mengamati batas CPU), dan/atau
    * Mengalokasikan memori secara bertahap (untuk mengamati batas memori).

4. Buat Dockerfile

    * Tulis Dockerfile untuk menjalankan program uji.
    *Buat gambar:
 
                 docker build -t week13-resource-limit .

5. Jalankan kontainer secara normal:

                docker run --rm week13-resource-limit
 
 Catat keluaran/hasil pengamatan.

6. Jalankan container dengan batasan sumber daya (contoh):

              docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit

Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

7. Berkomitmen & Berusaha

            git add .
            git commit -m "Minggu 13 - Docker Resource Limit"
            git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
docker build -t week13-resource-limit
docker run --rm week13-resource-limit
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
docker stats

* Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
CMD ["python", "-u", "app.py"]


* App
import time
import math

buffer = {}
counter = 0

print("Program stress test resource berjalan...")
print("Tekan Ctrl+C untuk menghentikan\n")

try:
    while True:
        # Beban CPU: operasi matematika
        nilai = 0
        for i in range(1, 300_000):
            nilai += math.sqrt(i)

        # Beban memori: simpan list integer
        buffer[counter] = [counter] * 1_000_000  # ±8 MB (tergantung sistem)

        counter += 1
        print(
            f"Siklus {counter} | Nilai CPU: {int(nilai)} | "
            f"Estimasi memori: {counter * 8} MB"
        

        )
        time.sleep(1)

except MemoryError:
    print("ERROR: Sistem kehabisan memori!")
except KeyboardInterrupt:
    print("\nProgram dihentikan secara manual.")

```

---

## Hasil Eksekusi
* Membangun citra 
![alt text](<screenshots/bangun_citra.png>)


* Pengujian tanpa limit
![alt text](<screenshots/tanpa batas.png>)

Hasil dari pengamatan :
    
   * Program bekerja sangat lancar dan responsi
   * Iterasi bertambah dengan cepat secara konsisten tanpa jeda
   * Tidak terjadi error selama berjalan
   * Penggunaan memori naik terus menerus tanpa ada batas 
   * Proggram akan berhenti ketika diberhentikan secara manual dengan ctrl+c
   
   Hal ini menunjukan bahwa container tanpa batas memori dapat mengeksploitasi seluruh resource host secara penuh dan tidak terkendali.   

* Pengujian menggunakan  limit 
![alt text](<screenshots/ada_batas.png>)

* Hasil dari pengamatan :

    * CPU dibatesin 0.5 core bikin iterasi lambat,program tetep aman tapi gak berjalan cepet seperti tanpa limit
     * Penggunaan memori mencapai 64MB trigger OOM killer Linux yang mematikan proses otomati

Hal ini menunjukan batasan CPU berpengaruh terhadap kecepatan eksekusi suatu program dan limit program dapat menyebabkan menghentikan proses jika sudah melampaui batas

---


## Kesimpulan

Praktikum ini membuktikan Docker efektif menjalankan aplikasi secara konsisten dalam kontainer terlindungi, bebas dari variasi konfigurasi sistem operasi host yang sering menyebabkan inkonsistensi penerapan.

Pengujian menunjukkan CPU 0.5 core secara signifikan memperlambat laju iterasi program dibandingkan tanpa batas, sementara batas memori 64MB memicu mekanisme OOM killer Linux untuk menghentikan proses dengan pesan otomatis "Killed" saat batas tercapai.

Penerapan batasan sumber daya pada Docker sangat penting untuk lingkungan produksi, memungkinkan kontrol yang tepat terhadap penggunaan sumber daya, menjaga stabilitas sistem secara keseluruhan, serta memastikan pembagian sumber daya yang adil antar beberapa container agar tidak ada satu aplikasi yang mendominasi host.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?

    **Jawaban:**  Container perlu dibatasi  CPU dan memori karena supaya  tidak memakan seluruh komponen komputer, yang bisa membuat sistem menjadi lambat atau bahkan crash. 
3. Apa perbedaan VM dan container dalam konteks isolasi sumber daya?

   **Jawaban:**  Virtual Machine (VM) bekerja dengan menjalankan sistem operasi lengkap sendiri, sehingga penggunaan CPU, memori, dan penyimpanan benar-benar terpisah dari sistem lain. Container berbeda karena hanya menjalankan aplikasi dan kebutuhannya saja dengan memanfaatkan kernel dari sistem host, sehingga lebih ringan dan cepat, tetapi isolasi sumber dayanya tidak sekuat VM.
5. Apa dampak limit memori terhadap aplikasi yang boros memori?

    **Jawaban:** Dampak limit memoeri terhadap aplikasi yang boros memori aplikasi tidak berjalan optimal atau bahkan berhenti.Ketika penggunaan memori mendekati atau melebihi batas yang ditentukan, aplikasi dapat mengalami kegagalan alokasi memori, performa menurun drastis, atau dihentikan secara paksa oleh sistem 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  Bagian yang paling menantang minggu ini saat menjalankan container tanpa batas 
- Bagaimana cara Anda mengatasinya?
  Cara mengatasinya menggunakan mencari di referensi website

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
