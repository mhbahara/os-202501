# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine

---

## Identitas
- *Nama*  :
1. M. Habibi Nur Ramadhan (250202949)
3. Farhan Ramdhani (250202938)
4. Yusuf Anwar (250202971)
- *Kelas* : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).  
2. Membuat dan menjalankan sistem operasi guest di dalam VM.  
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).  
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.  
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

Virtual Machines (VM) adalah representasi virtual atau emulasi komputer fisik yang menggunakan perangkat lunak, bukan perangkat keras, untuk menjalankan program dan menerapkan aplikasi.
Dengan menggunakan sumber daya dari satu mesin fisik, seperti memori, CPU, antarmuka jaringan, dan penyimpanan, VM memungkinkan bisnis untuk menjalankan beberapa mesin secara virtual dengan sistem operasi yang berbeda pada satu perangkat.

Konsep utama dalam virtualisasi sistem operasi melibatkan tiga komponen penting, yaitu Host OS, Guest OS, dan Hypervisor.
1. *Host Operating System (Host OS)*
sistem operasi host bekerja dengan mesin runtime kontainer, seperti Docker atau Kubernetes , untuk mengelola siklus hidup kontainer. Berperan dalam menjaga keamanan dan kontrol akses untuk aplikasi yang dikontainerisasi. Sistem operasi host menerapkan kebijakan keamanan, otentikasi, dan otorisasi untuk melindungi sistem dari akses tidak sah atau memiliki potensi ancaman. Selain itu, sistem operasi host membantu dalam memantau dan mencatat aktivitas kontainer, memberikan wawasan berharga tentang kinerja dan potensi masalah.
2. *Guest Operating System (Guest OS)*
Sistem operasi tamu adalah sistem operasi yang diinstal pada mesin virtual ( VM ) atau disk yang dipartisi . Biasanya berbeda dari sistem operasi host (OS). Sederhananya, OS host berjalan pada perangkat keras sedangkan OS tamu berjalan pada VM.
Sistem operasi yang terpasang pada komputer yang memungkinkan komputer berkomunikasi dengan berbagai elemen perangkat keras dan perangkat lunaknya disebut sistem operasi host. Sebagai sistem operasi yang terpasang sejak awal, sistem operasi host adalah sistem operasi "utama" dari sistem tersebut.
3. *Hypervisor*
Hypervisor adalah perangkat lunak yang dapat digunakan untuk menjalankan beberapa mesin virtual pada satu mesin fisik. Setiap mesin virtual memiliki sistem pengoperasian dan aplikasinya sendiri. Hypervisor mengalokasikan sumber daya komputasi fisik dasar seperti CPU dan memori ke mesin virtual individu sesuai kebutuhan. Jadi, hypervisor mendukung penggunaan optimal infrastruktur IT fisik.

---

## Langkah Pengerjaan
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

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```

---

## Hasil Eksekusi

## 1. Instalasi VM
![alt text](/praktikum/week12-virtual-machine/screenshots/instalasi_vm.png.png)
## 2. OS Running
![alt text](/praktikum/week12-virtual-machine/screenshots/os_guest_running.png.png)
## 3. Konfigurasi sebelum diubah
![alt text](/praktikum/week12-virtual-machine/screenshots/konfigurasi_resource_sebelum_ubah.png.png)
![alt text](/praktikum/week12-virtual-machine/screenshots/konfigurasi_resource_sebelum_ubah2.png.png)
## 4. Performa sebelum diubah
![alt text](/praktikum/week12-virtual-machine/screenshots/performa_konfigurasi_sebelum_diubah.png.png)
![alt text](/praktikum/week12-virtual-machine/screenshots/performa_konfigurasi_sebelum_diubah2.png.png)
## 5. Konfigurasi setelah diubah
![alt text](/praktikum/week12-virtual-machine/screenshots/konfigurasi_resource_setelah_ubah.png.png)
![alt text](/praktikum/week12-virtual-machine/screenshots/konfigurasi_resource_setelah_ubah2.png.png)
## 6. Performa setelah diubah
![alt text](/praktikum/week12-virtual-machine/screenshots/performa_konfigurasi_setelah_diubah.png.png)
![alt text](/praktikum/week12-virtual-machine/screenshots/performa_konfigurasi_setelah_diubah2.png.png)

---

## Analisis
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  

   **Jawaban:** Virtual Machine (VM) menyediakan isolasi antara sistem host dan guest dengan menggunakan hypervisor yang mengatur serta membatasi akses guest terhadap sumber daya perangkat keras. Guest OS dijalankan dalam lingkungan virtual yang terpisah sehingga tidak dapat mengakses atau memengaruhi sistem host secara langsung. Isolasi ini membuat gangguan atau serangan yang terjadi pada guest tidak berdampak pada host maupun VM lain yang berjalan.
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

   **Jawaban:** Konsep isolasi pada VM berkaitan erat dengan sandboxing karena VM menciptakan lingkungan terbatas dan terkontrol untuk menjalankan sistem operasi dan aplikasi. Selain itu, VM juga mendukung hardening sistem operasi dengan mengurangi permukaan serangan, membatasi layanan yang berjalan, serta memungkinkan pengelolaan keamanan yang lebih ketat tanpa memengaruhi sistem utama.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
- Virtualisasi memungkinkan menjalankan beberapa sistem operasi secara bersamaan dalam satu perangkat keras fisik.
- Konfigurasi resource (CPU, RAM, storage) sangat memengaruhi performa dan stabilitas VM.
- VM menyediakan isolasi yang baik antara host dan guest sehingga meningkatkan keamanan sistem.


---

## Quiz
1. Apa perbedaan antara host OS dan guest OS?  

   **Jawaban:**  Host OS merupakan sistem operasi utama yang langsung berjalan di atas perangkat keras fisik dan mengelola seluruh resource komputer. Di sisi lain Guest OS merupakan sistem operasi yang berjalan di dalam Virtual Machine (VM) di atas host OS melalui hypervisor, menggunakan resource yang dialokasikan secara virtual dan tidak berinteraksi langsung dengan hardware fisik.
2. Apa peran hypervisor dalam virtualisasi?    

   **Jawaban:**  Hypervisor merupakan lapisan perangkat lunak yang mengelola dan mengendalikan virtual machine. Hypervisor mengalokasikan resource fisik seperti CPU, RAM, dan storage kepada setiap guest OS, serta menjaga isolasi antar VM agar satu sistem tidak saling mengganggu.
3. Mengapa virtualisasi meningkatkan keamanan sistem? 

   **Jawaban:**  Virtualisasi meningkatkan keamanan sistem karena menyediakan isolasi antara host OS dan guest OS maupun antar guest OS. Jika terjadi kesalahan, crash, atau serangan pada satu VM, dampaknya hanya terbatas pada VM tersebut dan tidak langsung memengaruhi sistem lain atau host. Selain itu, virtualisasi menerapkan konsep sandboxing, sehingga aktivitas berbahaya dapat dibatasi dalam lingkungan virtual.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
