
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine  

---

## Identitas
- **Nama**  : FAIQ ATHA RULLOH
- **NIM**   : 250320571
- **Kelas** : 1DSRA

---
## Deskripsi Singkat
Pada praktikum minggu ini, mahasiswa akan mempelajari konsep **virtualisasi sistem operasi** dengan menggunakan **Virtual Machine (VM)**.  
Mahasiswa diarahkan untuk menginstal dan menjalankan sistem operasi guest di atas host OS menggunakan perangkat lunak virtualisasi seperti **VirtualBox** atau **VMware**.

Praktikum ini menekankan pemahaman hubungan antara **host OS**, **guest OS**, dan **hypervisor**, serta bagaimana konfigurasi resource (CPU, memori, dan storage) memengaruhi kinerja dan isolasi sistem.

---

## Tujuan
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
1. Host OS adalah sistem operasi utama di komputer di fisik
2. Guest OS adalah sistem operasi virtual yang berjalan diatasnya
3. Hypervisor adalah perangkat lunak perantara (VirtualBox atau VMware)
4. VM (Virtual Machine) adalah komputer virtual berbasis perangkat lunak yang berjalan di dalam komputer fisik (host)
5. VirtualBox dan VMware adalah perangkat lunak virtualisasi yang memungkinkan Anda menjalankan "komputer di dalam komputer"


---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

---

## Hasil Eksekusi
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.

![Screenshot hasil](<screenshots/instalasi_vm.png(1).png>)


![Screenshot hasil](<screenshots/instalasi_vm.png (2).png>)

   - Pengecekan fitur virtualisasi (VT-x / AMD-V) tanpa ke BIOS.

![Screenshot hasil](<screenshots/Pastikan fitur virtualisasi.png>)

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest

![Screenshot hasil](<screenshots/os_guest_running.png.png>)

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.
   - Pastikan OS guest dapat login dan berjalan normal.

![Screenshot hasil](<screenshots/Instalasi Sistem Operasi (1).png>)

![Screenshot hasil](<screenshots/Instalasi Sistem Operasi (2).png>)

![Screenshot hasil](<screenshots/Instalasi Sistem Operasi (3).png>)

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.

![Screenshot hasil](<screenshots/konfigurasi_resource.png>)

   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

![Screenshot hasil](<screenshots/perbedaan performa sebelum dan sesudah.png>)


---
## Analisis Proteksi OS
- Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.
    - Virtual Machine (VM) menyediakan isolasi antara host dan guest dengan cara memisahkan sumber daya, eksekusi, dan akses sistem melalui lapisan virtualisasi:
    - 1. Memisahkan sumber daya (resources)
         - VM tidak menggunakan hardware secara langsung.
         - CPU, memori, disk, dan jaringan dibagi dan dialokasikan oleh hypervisor.
         - Guest hanya “melihat” sumber daya virtual (vCPU, RAM virtual, disk virtual).
    - 2. Memisahkan eksekusi (execution)
         - Kode dan instruksi dari guest OS tidak dieksekusi langsung di hardware.
    - 3. lapisan virtualisasi (hypervisor)
         - Lapisan virtualisasi bertindak sebagai perantara dan pengawas
         - Menjamin keamanan dan stabilitas host
- Kaitkan dengan konsep *sandboxing* dan *hardening* OS.
    - Konsep hardering:
        - VM membantu Hardening dengan cara memisahkan yang penting dari yang tidak penting.
    - Konsep sandboxing:
        - Jika Guest OS hancur terkena virus, virus tersebut tetap terperangkap di dalam VM dan tidak bisa keluar ke Host OS (sistem utama).

---

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Apa perbedaan antara host OS dan guest OS?  
***jawaban***
- Host OS (Sistem Operasi Induk) adalah sistem operasi utama yang terpasang langsung pada komputer fisik Anda (misalnya Windows 10 atau macOS), sementara Guest OS (Sistem Operasi Tamu) adalah sistem operasi "kedua" yang berjalan di dalam mesin virtual (VM) yang di-hosting oleh Host OS.

2. Apa peran hypervisor dalam virtualisasi?  
***Jawaban***
- Sebagai pembagi sumber daya fisik dari komputer
- Sebagai isolasi berjalan setiap VM berjalan di lingkungan sendiri
- Sebagai komunikasi antar perangkat keras fisik

3. Mengapa virtualisasi meningkatkan keamanan sistem?  
***Jawaban***
- Karena adanya integritas memori yang melindungi dan mengeraskan sistem operasi dengan menjalankan integritas kode mode kernel dalam lingkungan virtualisasi yang terisolasi.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
***Jawaban***
   - Menurut saya yang paling menantang minggu ini adalah mengamati perbedaan performa sebelum dan sesudah perubahan resource.
- Bagaimana cara Anda mengatasinya?  
***Jawaban***
   - Cara mengatasinya adalah membandingkan dengan angka lihat perbedaan rata-rata , puncak, dan latensi pada metrik kunci.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
