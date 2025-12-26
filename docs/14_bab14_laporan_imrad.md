# Tugas Praktikum Minggu 14  
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## A. Deskripsi Singkat
Pada pertemuan ini, mahasiswa menyusun **laporan praktikum ilmiah** secara sistematis menggunakan format **IMRAD** (*Introduction, Methods, Results, and Discussion*) yang ditutup dengan **Kesimpulan**.

Laporan IMRAD digunakan untuk merangkum praktikum-praktikum sebelumnya (mis. scheduling, page replacement, deadlock detection, VM/Docker) agar hasil uji dapat dipahami, direplikasi, dan dievaluasi secara akademik.

---

## B. Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menyusun laporan praktikum dengan struktur ilmiah (Pendahuluan–Metode–Hasil–Pembahasan–Kesimpulan).
2. Menyajikan hasil uji dalam bentuk tabel dan/atau grafik yang jelas.
3. Menuliskan analisis hasil dengan argumentasi yang logis.
4. Menyusun sitasi dan daftar pustaka dengan format yang konsisten.
5. Mengunggah draft laporan ke repositori dengan rapi dan tepat waktu.

---

## C. Ketentuan Teknis
- Laporan ditulis dalam `Markdown` pada file `laporan.md`.
- Topik laporan boleh memilih salah satu dari praktikum sebelumnya:
  - Scheduling (FCFS/SJF)
  - Page Replacement (FIFO/LRU)
  - Deadlock Detection
  - VM/Docker (resource management)
- Wajib menyertakan minimal:
  - 1 tabel hasil (atau lebih)
  - 1 gambar (screenshot, diagram, atau grafik)
  - sitasi dan daftar pustaka

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week14-laporan-imrad/
├─ code/
│  └─ (opsional) file kode/data pendukung
├─ screenshots/
│  ├─ (wajib) bukti hasil uji
│  └─ (opsional) grafik/diagram
└─ laporan.md
```

---

## D. Langkah Pengerjaan
1. **Menentukan Topik Laporan**

   Pilih 1 topik dari praktikum sebelumnya (mis. Minggu 9/10/11/13) dan tetapkan tujuan eksperimen yang ingin disampaikan.

2. **Menyiapkan Bahan**

   - Kode/program yang digunakan.
   - Dataset/parameter uji (jika ada).
   - Bukti hasil eksekusi (screenshot) dan/atau grafik.

3. **Menulis Laporan dengan Struktur IMRAD**

   Tulis `praktikum/week14-laporan-imrad/laporan.md` dengan struktur minimal berikut:
   - **Pendahuluan (Introduction):** latar belakang, rumusan masalah/tujuan.
   - **Metode (Methods):** lingkungan uji, langkah eksperimen, parameter/dataset, cara pengukuran.
   - **Hasil (Results):** tabel/grafik hasil uji, ringkasan temuan.
   - **Pembahasan (Discussion):** interpretasi hasil, keterbatasan, perbandingan teori/ekspektasi.
   - **Kesimpulan:** 2–4 poin ringkas menjawab tujuan.

4. **Menyajikan Tabel/Grafik**

   - Tabel harus diberi judul/keterangan singkat.
   - Jika menggunakan grafik: jelaskan sumbu dan arti grafik.

5. **Sitasi dan Daftar Pustaka**

   - Cantumkan referensi minimal 2 sumber.
   - Gunakan format konsisten (mis. daftar bernomor).

6. **Commit & Push Draft**

   ```bash
   git add .
   git commit -m "Minggu 14 - Draft Laporan IMRAD"
   git push origin main
   ```

---

## E. Tugas & Quiz
### Tugas
1. Susun laporan praktikum format IMRAD di `praktikum/week14-laporan-imrad/laporan.md`.
2. Sertakan minimal 1 tabel dan 1 gambar (screenshot/grafik).
3. Sertakan sitasi dan daftar pustaka.
4. Pastikan struktur folder rapi sesuai ketentuan.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?
2. Apa perbedaan antara bagian **Hasil** dan **Pembahasan**?
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?

---

## F. Output yang Diharapkan
- File `praktikum/week14-laporan-imrad/laporan.md` berisi laporan format IMRAD.
- Bukti hasil uji (screenshot/grafik) tersimpan di `praktikum/week14-laporan-imrad/screenshots/`.
- (Opsional) kode/data pendukung di `praktikum/week14-laporan-imrad/code/`.
- Semua perubahan telah di-*commit* dan di-*push*.

---

## G. Referensi
1. Silberschatz, A., Galvin, P., Gagne, G. *Operating System Concepts*, 10th Ed.
2. Tanenbaum, A. *Modern Operating Systems*, 4th Ed.
3. OSTEP – referensi sesuai topik praktikum yang dipilih.
