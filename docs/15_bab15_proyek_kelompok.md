# Tugas Praktikum Minggu 15  
Topik: Proyek Kelompok – Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)

---

## A. Deskripsi Singkat
Pada pertemuan ini, mahasiswa mengerjakan **proyek kelompok** untuk mengintegrasikan materi praktikum sebelumnya menjadi satu mini-aplikasi yang **bisa didemokan dan dipresentasikan**.

Setiap kelompok membangun aplikasi berbasis terminal yang:
1. Mensimulasikan minimal **2 konsep OS** (contoh: CPU scheduling + page replacement, atau scheduling + deadlock detection).
2. Menyediakan input dataset sederhana dan menampilkan output berupa tabel/ringkasan metrik.
3. Dapat dijalankan melalui **Docker** untuk memastikan reproducible environment.

---

## B. Tujuan
Setelah menyelesaikan proyek ini, mahasiswa mampu:
1. Bekerja kolaboratif dalam tim dengan pembagian peran yang jelas.
2. Mengintegrasikan beberapa konsep sistem operasi dalam satu aplikasi sederhana.
3. Mengelola proyek menggunakan Git (branch/PR/commit yang rapi).
4. Menyusun dokumentasi dan laporan proyek yang sistematis.
5. Melakukan presentasi dan demo hasil proyek.

---

## C. Ketentuan Teknis
- **Kelompok:** 3–5 mahasiswa.
- Bahasa pemrograman bebas (Python / C / Java / lainnya), aplikasi berbasis terminal.
- Wajib menggunakan Git kolaboratif (minimal: pembagian branch per fitur dan merge terkontrol).
- Wajib menyediakan cara jalan yang mudah (minimal `README.md` + perintah run) dan **demo via Docker**.

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week15-proyek-kelompok/
├─ code/
│  ├─ (source code proyek)
│  ├─ Dockerfile
│  ├─ README.md
│  └─ data/ (opsional)
├─ screenshots/
│  ├─ demo_run.png
│  └─ hasil_tabel.png
└─ laporan.md
```

---

## D. Spesifikasi Proyek & Langkah Pengerjaan
### 1) Pilih Paket Fitur (wajib minimal 2 modul)
Pilih **minimal 2 modul** berikut (boleh 3 untuk nilai tambahan analisis):
- **Modul A – CPU Scheduling:** FCFS dan/atau SJF (non-preemptive). Output: waiting time, turnaround time, rata-rata.
- **Modul B – Page Replacement:** FIFO dan/atau LRU. Output: page fault, hit ratio.
- **Modul C – Deadlock Detection:** deteksi proses deadlock pada dataset (allocation/request). Output: status deadlock + daftar proses terlibat.

### 2) Ketentuan Aplikasi
Aplikasi minimal harus memiliki:
1. **CLI/menu** untuk memilih modul dan parameter (mis. jumlah frame, dataset file).
2. Input dataset dari file (CSV/TXT sederhana) + contoh dataset di repo.
3. Output hasil dalam bentuk **tabel** (boleh ASCII table) dan ringkasan metrik.
4. Dokumentasi penggunaan di `code/README.md`.

### 3) Workflow Tim (wajib)
- Tentukan peran minimal:

  - **Project Lead/Integrator:** koordinasi, merge PR, memastikan build jalan.
  - **Developer 1:** implementasi Modul A atau B.
  - **Developer 2:** implementasi Modul B atau C.
  - **Dokumentasi & QA:** uji dataset, rapikan README, siapkan screenshot.
- Terapkan aturan Git:

  - Branch per fitur (contoh: `feat/scheduling`, `feat/pagerepl`, `docs/readme`).
  - Minimal 1 PR/merge per anggota.
  - Commit message jelas dan konsisten.

### 4) Dockerisasi
- Buat `Dockerfile` agar aplikasi bisa dijalankan via:

  - build image
  - run container
- Pastikan `code/README.md` memuat langkah run di host dan via Docker.

### 5) Bukti Proyek
- Minimal 2 screenshot:

  - hasil running aplikasi
  - hasil tabel/metrik (atau `docker stats` jika relevan)

---

## E. Presentasi (Wajib)
Setiap kelompok melakukan presentasi singkat dengan format:
- **Durasi:** 7–10 menit presentasi + 3–5 menit tanya jawab.
- **Materi minimal:**

  1. Latar belakang & tujuan proyek.
  2. Arsitektur aplikasi (modul dan alur data).
  3. Demo langsung menjalankan aplikasi (lebih baik via Docker).
  4. Hasil pengujian (tabel/metrik) + analisis singkat.
  5. Pembagian peran dan kontribusi tiap anggota.

### Tugas & Quiz
#### Tugas
1. Implementasikan proyek sesuai spesifikasi (minimal 2 modul).
2. Sediakan dataset contoh dan dokumentasi run (`code/README.md`).
3. Buat `Dockerfile` dan pastikan demo berjalan.
4. Tulis laporan proyek pada `laporan.md`.

#### Quiz (jawab di laporan)
1. Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?
2. Mengapa Docker membantu proses demo dan penilaian proyek?
3. Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? Jelaskan.

---

## F. Output yang Diharapkan
- Source code, `Dockerfile`, dan `README.md` di `praktikum/week15-proyek-kelompok/code/`.
- Screenshot demo dan hasil uji di `praktikum/week15-proyek-kelompok/screenshots/`.
- Laporan kelompok di `praktikum/week15-proyek-kelompok/laporan.md` berisi:

  - ringkasan proyek, arsitektur, cara menjalankan, hasil uji, analisis, kontribusi anggota.
- Semua hasil telah di-*commit* dan siap dipresentasikan.

---

## G. Referensi
1. Silberschatz, A., Galvin, P., Gagne, G. *Operating System Concepts*, 10th Ed.
2. Tanenbaum, A. *Modern Operating Systems*, 4th Ed.
3. OSTEP – Scheduling / Virtual Memory / Deadlocks (sesuai modul yang dipilih).
