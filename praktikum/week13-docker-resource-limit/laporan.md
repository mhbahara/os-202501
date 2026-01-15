
# Laporan Praktikum Minggu [X]
Topik: [Docker – Resource Limit (CPU & Memori)]

---

## Identitas
- **Nama**  : [Mohammad FATIKH Mahsun]  
- **NIM**   : [250202952]  
- **Kelas** : [1IKRB]

---

## Tujuan
1.Memahami konsep dasar containerization serta cara kerja Docker dalam menjalankan aplikasi di dalam container.

2.Melatih kemampuan menulis Dockerfile sederhana untuk menjalankan program atau skrip berbasis terminal.

3.Mampu melakukan proses build image dan menjalankan container Docker dengan benar.

4.Menerapkan pembatasan penggunaan sumber daya berupa CPU dan memori pada container.

5.Mengamati dan membandingkan perilaku serta kinerja aplikasi saat dijalankan tanpa limit dan dengan limit resource.

6.Menarik kesimpulan mengenai pentingnya pengelolaan sumber daya pada lingkungan berbasis container.

---

## Dasar Teori
•Docker adalah teknologi containerization yang memungkinkan aplikasi dijalankan dalam lingkungan terisolasi tanpa memerlukan sistem operasi terpisah, sehingga lebih ringan dan efisien dibandingkan virtual machine.

•Docker memanfaatkan fitur sistem operasi Linux seperti namespace untuk isolasi dan control groups (cgroups) untuk mengatur serta membatasi penggunaan sumber daya seperti CPU dan memori pada container.

•Pembatasan CPU bertujuan agar sebuah container tidak menggunakan seluruh kapasitas prosesor, sehingga proses lain atau container lain tetap dapat berjalan dengan baik.

•Pembatasan memori berfungsi untuk mencegah aplikasi menggunakan memori secara berlebihan yang dapat menyebabkan error atau membuat sistem menjadi tidak stabil.

•Penerapan limit resource pada container penting untuk menjaga kestabilan, keadilan penggunaan sumber daya, dan performa 
sistem terutama ketika menjalankan banyak aplikasi secara bersamaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?

Container perlu dibatasi CPU dan memori agar penggunaan sumber daya pada sistem dapat terkontrol dengan baik. Tanpa adanya pembatasan, sebuah container berpotensi menggunakan CPU dan memori secara berlebihan sehingga mengganggu kinerja container lain yang berjalan pada sistem yang sama. Pembatasan ini juga membantu menjaga kestabilan sistem serta memastikan pembagian sumber daya yang lebih adil antar aplikasi.

2. Apa perbedaan VM dan container dalam konteks isolasi resource?

Virtual Machine memiliki tingkat isolasi resource yang lebih tinggi karena setiap VM menjalankan sistem operasi sendiri dengan alokasi sumber daya yang relatif terpisah. Hal ini membuat VM lebih aman namun membutuhkan sumber daya yang lebih besar. Sebaliknya, container berbagi kernel dengan sistem operasi host sehingga lebih ringan dan cepat dijalankan, sementara isolasi resource pada container diatur menggunakan mekanisme seperti cgroups.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?

Penerapan limit memori dapat membatasi aplikasi yang boros memori agar tidak menggunakan sumber daya secara berlebihan. Jika penggunaan memori melebihi batas yang ditentukan, aplikasi dapat mengalami penurunan kinerja, error, atau bahkan dihentikan oleh sistem. Dengan adanya limit memori, risiko kehabisan memori pada sistem dapat diminimalkan sehingga sistem tetap berjalan dengan stabil.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
