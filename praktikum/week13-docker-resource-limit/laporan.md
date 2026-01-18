
# Laporan Praktikum Minggu [13]
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

1.Melakukan inisialisasi lingkungan kerja dengan memverifikasi instalasi Docker melalui docker version dan menyiapkan struktur folder sesuai ketentuan teknis.

2.Mengembangkan skrip uji app.py yang dirancang untuk memberikan beban komputasi pada CPU serta alokasi memori progresif, kemudian membungkusnya menggunakan Dockerfile berbasis python:3.9-slim.

3.Membangun image Docker dengan perintah docker build -t week13-resource-limit . hingga proses build selesai sepenuhnya.

4.Menjalankan kontainer dalam kondisi tanpa batasan menggunakan docker run --rm week13-resource-limit untuk mengamati kapasitas maksimal yang diberikan sistem host (default sekitar 3.6 GB).

5.Menjalankan kembali kontainer dengan parameter pembatasan spesifik melalui perintah docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit.

6.Melakukan monitoring secara real-time menggunakan docker stats untuk memverifikasi bahwa penggunaan CPU tertahan di kisaran 46-50% dan limit memori terkunci ketat pada angka 256 MiB.

7.Commit Message yang Digunakan

git add .
git commit -m "Minggu 13 - Docker Resource Limit"
git push origin main

---

## Kode / Perintah

```bash
FROM python:3.9-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]

# Membangun image dari folder code
docker build -t week13-resource-limit .

# Menjalankan dengan limit
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit

#Menjalankan Container Tanpa Limit
docker run --rm week13-resource-limit


```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Week13.1.png)

![Screenshot hasil](screenshots/Week13.2.png)

![Screenshot hasil](screenshots/Week13.3.png)

![Screenshot hasil](screenshots/Week13.4.png)

---

## Analisis

1.Tanpa Limit (Default)
Pada tahap ini, container dijalankan secara standar tanpa tambahan parameter pembatas.

-Perintah: docker run --rm week13-resource-limit.

-Batas Memori: Pada monitoring, terlihat LIMIT memori sebesar 3.674 GiB. Ini adalah total kapasitas RAM yang dialokasikan oleh sistem host (Windows) untuk Docker Desktop secara keseluruhan.

-Perilaku Aplikasi: Program berhasil mengisi RAM hingga target 500 MB tanpa hambatan karena batas atas (3.6 GB) masih sangat jauh.

-Penggunaan CPU: Terpantau penggunaan CPU berada di angka 29.26%.

2. Dengan Limit (Resource Quotas)

Pada tahap ini, diterapkan batasan ketat menggunakan flag --cpus dan --memory.

-Perintah: docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit.

-Batas Memori: Kolom LIMIT kini terkunci tepat pada angka 256 MiB.

-Batas CPU: Dengan jatah 0.5 core, penggunaan CPU terpantau naik menjadi 46.48%. Hal ini menunjukkan container bekerja hampir maksimal sesuai jatah kecil yang diberikan (mendekati 50% dari 1 core).

-Perilaku Aplikasi: Meskipun aplikasi mencoba mengisi RAM hingga 500 MB, sistem Docker akan membatasi atau mematikan container jika penggunaan riil menembus angka 256 MB guna menjaga stabilitas sistem utama.

 Perbedaan utama dari kedua kondisi ini terletak pada tingkat keamanan dan kontrol sumber daya. Pada kondisi Tanpa Limit, prioritas diberikan pada performa aplikasi sehingga ia bisa mengambil apa pun yang tersedia di host, namun stabilitas sistem induk menjadi taruhannya. Sebaliknya, pada kondisi Dengan Limit, prioritas dialihkan pada stabilitas sistem secara keseluruhan dengan mengisolasi container ke dalam jatah sumber daya yang kecil dan pasti. Jika aplikasi dalam kondisi limit ini dipaksa untuk terus menambah data melebihi 256 MB, sistem Docker akan menjalankan protokol keamanan dengan mematikan container tersebut secara otomatis guna mencegah dampak kerusakan yang lebih luas pada perangkat

---

## Kesimpulan
Berdasarkan pengujian yang telah dilakukan, menunjukkan bahwa tanpa limitasi, container menggunakan batas memori default sistem sebesar 3.674 GiB, sehingga aplikasi stress test dapat berjalan bebas mencapai target 500 MB. Kondisi ini berisiko tinggi karena ketiadaan isolasi memori dapat menyebabkan container menghabiskan seluruh sumber daya host dan mengganggu stabilitas sistem operasi utama.

Sebaliknya, penerapan limitasi --cpus="0.5" dan --memory="256m" secara efektif mengunci penggunaan sumber daya. Statistik menunjukkan beban CPU tertahan di 46.48% dan memori dibatasi ketat pada angka 256 MiB, meskipun aplikasi tetap mencoba meminta kapasitas lebih besar. Hal ini membuktikan bahwa fitur Resource Quotas berfungsi sebagai pengaman otomatis yang melindungi stabilitas sistem dengan memaksa container tetap berada dalam koridor penggunaan yang aman.

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
