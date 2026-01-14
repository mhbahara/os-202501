
# Laporan Praktikum Minggu [X]
Topik: [Arsitektur Sistem Operasi dan Kernel]

---

## Identitas
- **Nama**  : {Ayu Ida Nuraini]  
- **NIM**   : [250320588]  
- **Kelas** : [1DSRA]

---**#DESKRIPSI SINGKAT**
# Mode Eksekusi, System Call, dan Arsitektur OS

## Perbedaan Kernel Mode dan User Mode

**Kernel Mode (Supervisor/Privileged Mode):**
- Memiliki akses penuh ke semua instruksi CPU dan hardware
- Dapat mengeksekusi instruksi privileged (I/O operations, manajemen memori, interrupt handling)
- Akses langsung ke seluruh address space sistem
- Kode OS inti berjalan di mode ini
- Kesalahan fatal dapat menyebabkan system crash (kernel panic/BSOD)

**User Mode (Unprivileged Mode):**
- Akses terbatas hanya ke instruksi non-privileged
- Tidak dapat mengakses hardware atau memori kernel secara langsung
- Aplikasi user berjalan dalam restricted environment
- Harus menggunakan system call untuk meminta layanan kernel
- Kesalahan hanya mempengaruhi aplikasi tersebut (isolation)

**Tujuan Pemisahan:**
- Melindungi integritas sistem dari aplikasi yang error atau malicious
- Mencegah aplikasi user mengakses memori aplikasi lain
- Memastikan resource sharing yang adil dan aman

---

## Mekanisme System Call

System call adalah interface antara user space dan kernel space yang memungkinkan aplikasi meminta layanan OS.

**Proses System Call:**

1. **Inisiasi** - Aplikasi memanggil library function (contoh: `read()`, `write()`, `fork()`)

2. **Parameter Setup** - Parameter disimpan di register CPU atau stack

3. **Trap Instruction** - CPU mengeksekusi software interrupt (INT instruction) yang memicu mode switch

4. **Mode Transition** - CPU beralih dari user mode ke kernel mode dan melompat ke interrupt handler

5. **Identifikasi System Call** - Kernel mengidentifikasi system call yang diminta melalui system call number

6. **Eksekusi** - Kernel mengeksekusi fungsi yang sesuai dengan privilege penuh

7. **Return** - Hasil dikembalikan ke user space dan CPU kembali ke user mode

**Contoh System Call:**
- **File operations**: `open()`, `read()`, `write()`, `close()`
- **Process control**: `fork()`, `exec()`, `wait()`, `exit()`
- **Memory management**: `brk()`, `mmap()`
- **Communication**: `socket()`, `send()`, `recv()`

**Overhead:**
Context switching antara user-kernel mode memiliki cost (save/restore state, cache flushing), sehingga system call yang terlalu frequent dapat mengurangi performa.

---

## Perbandingan Model Arsitektur OS

### 1. Monolithic Kernel

**Karakteristik:**
- Semua komponen OS berjalan dalam satu address space di kernel mode
- Tight integration antara komponen (scheduler, memory manager, file system, drivers)
- Komunikasi antar-komponen melalui function calls langsung

**Kelebihan:**
- Performa sangat tinggi (minimal overhead)
- Komunikasi antar-komponen efisien
- Akses hardware cepat

**Kekurangan:**
- Kompleksitas tinggi dan sulit di-maintain
- Bug dalam satu komponen dapat crash seluruh sistem
- Security risk lebih besar
- Code base besar dan monolitik

**Contoh:** Linux, Unix, MS-DOS

**Variasi Modern:** Linux menggunakan modular monolithic - kernel dapat load/unload modules dinamis tanpa reboot

---

### 2. Layered Approach

**Karakteristik:**
- OS dibagi dalam hierarki layer (biasanya 5-7 layer)
- Setiap layer hanya berinteraksi dengan layer adjacent
- Layer bawah menyediakan abstraksi untuk layer atas

**Struktur Tipikal:**
- Layer 0: Hardware
- Layer 1: Memory management
- Layer 2: Process scheduling
- Layer 3: I/O management
- Layer 4: File system
- Layer 5: User programs

**Kelebihan:**
- Modularitas tinggi dan well-organized
- Mudah di-debug (dapat test per layer)
- Information hiding yang baik
- Maintenance lebih mudah

**Kekurangan:**
- Performa lebih lambat (harus traverse multiple layers)
- Sulit menentukan layer yang tepat untuk setiap fungsi
- Fungsi yang saling bergantung antar layer menjadi masalah

**Contoh:** THE OS (Dijkstra), MULTICS, lapisan awal Windows NT

---

### 3. Microkernel

**Karakteristik:**
- Kernel minimal hanya berisi fungsi esensial
- Layanan lainnya berjalan sebagai server di user space
- Komunikasi via message passing (IPC)

**Komponen di Kernel:**
- IPC mechanism
- Basic scheduling
- Low-level memory management
- Basic I/O primitives

**Komponen di User Space:**
- Device drivers
- File systems
- Network protocols
- GUI servers

**Kelebihan:**
- Reliabilitas tinggi (fault isolation)
- Security lebih baik (least privilege)
- Mudah extend dan customize
- Portability lebih baik
- Cocok untuk distributed systems

**Kekurangan:**
- Performa lebih lambat (frequent context switching)
- Overhead message passing
- Kompleksitas komunikasi antar-komponen

**Contoh:** MINIX, QNX, Mach, L4, seL4

---

## Tabel Perbandingan

| Aspek | Monolithic | Layered | Microkernel |
|-------|-----------|---------|-------------|
| **Performa** | Sangat tinggi | Sedang | Rendah-sedang |
| **Keamanan** | Rendah | Sedang | Tinggi |
| **Reliabilitas** | Rendah | Sedang | Sangat tinggi |
| **Kompleksitas** | Tinggi | Sedang | Rendah (kernel) |
| **Maintainability** | Sulit | Mudah | Mudah |
| **Flexibility** | Rendah | Sedang | Sangat tinggi |
| **Code Size** | Besar | Sedang | Kecil (kernel) |

---

## Tren Modern: Hybrid Kernel

Kebanyakan OS modern menggunakan **hybrid approach** yang mengombinasikan kelebihan berbagai arsitektur:

**Windows NT/XP/10:**
- Microkernel core dengan beberapa komponen di kernel space untuk performa
- Executive services di kernel, subsystems di user space

**macOS/iOS:**
- Mach microkernel sebagai basis
- BSD components dan drivers di kernel space
- Hybrid untuk balance performa dan modularitas

**Linux (Modular Monolithic):**
- Monolithic core untuk performa
- Loadable kernel modules untuk fleksibilitas
- Best of both worlds

**Kesimpulan:** Tidak ada arsitektur yang sempurna untuk semua kasus. Pemilihan bergantung pada prioritas: performa (monolithic), reliabilitas (microkernel), atau modularitas (layered/hybrid).

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid
  
1. Berikut peran-peran pentingnya:
     1. Manajemen Sumber Daya
         OS mengatur dan mengalokasikan sumber daya hardware seperti CPU, memori, dan perangkat I/O kepada berbagai proses yang berjalan.
     2. Abstraksi Hardware
          os menyembunyikan kompleksitas hardware dan menyediakan interface yang mudah digunakan untuk aplikasi, sehingga programmer tidak perlu memahami detail teknis setiap       perangkat keras.
     3. Keamanan dan Proteksi
     OS melindungi sistem dari akses tidak sah dan memastikan proses tidak saling mengganggu.
    4. Koordinasi Eksekusi Program
     OS mengelola eksekusi program secara bersamaan (multitasking) dan memastikan setiap program mendapat waktu CPU yang adil.
 
 2. Komponen Utama Sistem Operasi
1. Kernel
Kernel adalah inti dari sistem operasi yang berjalan di mode privileged (kernel mode). Fungsi utamanya meliputi:

Manajemen proses dan thread
Manajemen memori (paging, segmentasi)
Scheduling CPU
Komunikasi antar-proses (IPC)

2. System Call
System call adalah interface pemrograman yang memungkinkan aplikasi meminta layanan dari kernel. Contohnya: open(), read(), write(), fork(), exec(). System call bekerja sebagai gerbang antara user mode dan kernel mode.
3. Device Driver
Driver adalah software khusus yang memungkinkan OS berkomunikasi dengan perangkat keras tertentu seperti printer, disk, kartu grafis, dan network adapter. Driver menerjemahkan perintah generik OS menjadi instruksi spesifik untuk hardware.
4. File System
File system mengorganisir data di media penyimpanan dalam bentuk file dan direktori. Contoh file system: NTFS (Windows), ext4 (Linux), APFS (macOS). File system menangani operasi seperti membaca, menulis, menghapus, dan mengatur permission file.

3.Perbandingan Model Arsitektur OS
1. Monolithic Kernel
Semua layanan OS (manajemen proses, memori, file system, driver) berjalan dalam satu ruang kernel yang sama.
Kelebihan:

Performa tinggi karena komunikasi antar komponen sangat cepat
Akses langsung ke semua resource sistem

Kekurangan:

Kurang modular, sulit di-maintain
Satu bug di komponen bisa crash seluruh sistem
Ukuran kernel besar

Contoh: Linux tradisional, Unix klasik
2. Layered Architecture
OS dibagi menjadi beberapa layer, di mana setiap layer hanya berkomunikasi dengan layer di atas dan di bawahnya.
Kelebihan:

Modular dan terstruktur dengan baik
Lebih mudah di-debug dan di-maintain
Setiap layer dapat dikembangkan independen

Kekurangan:

Overhead performa karena harus melewati banyak layer
Sulit menentukan pembagian layer yang tepat
Kurang fleksibel

Contoh: THE (Technische Hogeschool Eindhoven), Windows NT awal
3. Microkernel
Hanya fungsi-fungsi paling esensial yang ada di kernel (IPC, scheduling dasar, manajemen memori low-level). Layanan lain seperti file system dan driver berjalan di user space.
Kelebihan:

Lebih stabil dan aman (bug di layanan tidak crash kernel)
Mudah di-extend dan di-maintain
Portabilitas tinggi

Kekurangan:

Performa lebih rendah karena banyak context switching
Komunikasi antar komponen lebih lambat
Kompleksitas desain tinggi

Contoh: MINIX, QNX, Mach (basis macOS/iOS)

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

1. **Prinsip Isolasi dan Protection Rings** - Sistem operasi menggunakan mekanisme hardware protection (kernel mode vs user mode) untuk memisahkan privilege level. Teori ini mendasari bagaimana kernel melindungi sumber daya kritsis dari akses langsung aplikasi user, memastikan stabilitas sistem melalui controlled access via system calls dan context switching.

2. **Trade-off antara Performa dan Modularitas** - Teori desain sistem menunjukkan bahwa komunikasi antar-komponen memiliki cost. Monolithic kernel meminimalkan overhead dengan tight coupling (komunikasi langsung dalam address space sama), sementara microkernel memaksimalkan modularitas dengan loose coupling (IPC dan message passing) dengan konsekuensi overhead lebih tinggi. Percobaan membuktikan tidak ada "silver bullet" - setiap pilihan arsitektur adalah kompromi.

3. **Layering dan Abstraction Hierarchy** - Konsep fundamental computer science bahwa kompleksitas dapat dikelola melalui abstraksi berlapis. Setiap layer menyembunyikan detail implementasi dari layer di atasnya, memungkinkan separation of concerns. Teori ini mendasari mengapa layered architecture memudahkan development dan debugging, meskipun menambah overhead komunikasi antar-layer yang harus dipertimbangkan dalam implementasi praktis.
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
Tuliskan ringkasan (±500 kata) mencakup:
Perbedaan monolithic kernel, microkernel, dan layered architecture.
Contoh OS yang menerapkan tiap model.
Analisis: model mana yang paling relevan untuk sistem modern.
Arsitektur Sistem Operasi: Perbandingan dan Relevansi di Era Modern
Arsitektur kernel merupakan fondasi desain sistem operasi yang menentukan bagaimana komponen-komponen OS berinteraksi dan diorganisasi. Tiga model utama yang berkembang adalah monolithic kernel, microkernel, dan layered architecture, masing-masing dengan filosofi dan karakteristik berbeda.
Monolithic Kernel
Monolithic kernel menempatkan seluruh layanan sistem operasi dalam satu address space di kernel mode. Semua komponen seperti device drivers, file system, memory management, dan network stack berjalan dalam privilege level tertinggi dengan akses langsung ke hardware. Pendekatan ini menghasilkan komunikasi antar-komponen yang sangat cepat karena tidak memerlukan context switching atau message passing.
Kelebihan utamanya adalah performa tinggi karena overhead komunikasi minimal. Namun, kelemahannya terletak pada kompleksitas kode yang besar, kesulitan maintenance, dan risiko keamanan yang lebih tinggi. Satu bug dalam driver dapat menyebabkan crash seluruh sistem. Contoh implementasi meliputi Linux, Unix tradisional, dan MS-DOS. Linux modern sebenarnya menggunakan pendekatan modular monolithic, di mana komponen dapat dimuat atau dihapus secara dinamis sebagai loadable kernel modules.
Microkernel
Microkernel mengadopsi filosofi minimalis dengan hanya menyimpan fungsi paling esensial di kernel space, seperti IPC (Inter-Process Communication), basic scheduling, dan low-level memory management. Layanan lain seperti device drivers, file systems, dan network protocols dijalankan sebagai server terpisah di user space.
Arsitektur ini menawarkan stabilitas superior karena kegagalan satu komponen tidak akan menghancurkan seluruh sistem. Keamanan lebih baik karena principle of least privilege diterapkan ketat. Namun, performa menjadi trade-off karena frequent context switching dan message passing antar komponen. Contoh implementasi termasuk MINIX (yang menginspirasi Linux), QNX (digunakan dalam otomotif dan embedded systems), dan Mach (basis dari macOS).
Layered Architecture
Layered architecture mengorganisasi OS dalam hierarki lapisan, di mana setiap layer hanya berinteraksi dengan layer tepat di atas atau di bawahnya. Layer terbawah menangani hardware, sedangkan layer tertinggi menyediakan user interface. Desain ini mempromosikan modularitas dan memudahkan debugging karena setiap layer dapat diuji independen.
Kelemahannya adalah kompleksitas dalam menentukan lapisan yang tepat untuk setiap fungsi dan potensi overhead performa karena harus melewati multiple layers. THE (Technische Hogeschool Eindhoven) adalah contoh awal implementasi ini, dan Windows NT menggunakan modifikasi pendekatan layered dalam arsitekturnya.
Analisis untuk Sistem Modern
Untuk sistem modern, tidak ada satu model yang ideal untuk semua kasus. Hybrid kernel menjadi solusi paling relevan, mengombinasikan kekuatan berbagai arsitektur. Windows NT dan macOS menggunakan pendekatan hybrid ini.
Untuk server dan desktop computing, monolithic modular seperti Linux tetap paling relevan karena menawarkan performa tinggi yang dibutuhkan untuk workload modern, sambil menjaga fleksibilitas melalui loadable modules. Ekosistem driver yang matang dan community support yang kuat menjadi nilai tambah.
Untuk sistem embedded, real-time, dan IoT, microkernel seperti QNX lebih unggul karena predictability, keandalan, dan footprint kecil yang krusial untuk resource-constrained devices.
Tren ke depan menunjukkan minat pada unikernel dan library OS untuk cloud computing, di mana aplikasi dan OS minimal dikompilasi menjadi satu image untuk efisiensi maksimal. Namun, untuk general-purpose computing, hybrid architecture yang mengombinasikan performa monolithic dengan keamanan microkernel akan terus mendominasi lanskap sistem operasi modern.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
# Kesimpulan Arsitektur Sistem Operasi

1. **Tidak Ada Arsitektur Universal** - Setiap model arsitektur (monolithic, microkernel, layered) memiliki trade-off antara performa, keamanan, dan kompleksitas. Pemilihan arsitektur bergantung pada kebutuhan spesifik: monolithic untuk performa tinggi, microkernel untuk reliabilitas dan keamanan, layered untuk modularitas dan maintainability.

2. **Hybrid Architecture sebagai Solusi Praktis** - Sistem operasi modern cenderung mengadopsi pendekatan hybrid yang mengombinasikan kelebihan berbagai arsitektur. Linux dengan modular monolithic dan Windows/macOS dengan hybrid kernel membuktikan bahwa fleksibilitas desain lebih penting daripada mengikuti satu model secara rigid.

3. **Evolusi Berkelanjutan Mengikuti Kebutuhan** - Arsitektur OS terus berkembang seiring perubahan teknologi dan use case. Dari mainframe ke mobile, cloud, dan IoT, setiap era membutuhkan optimasi berbeda. Tren seperti containerization, unikernel, dan microservices menunjukkan bahwa inovasi arsitektur OS akan terus berlanjut untuk memenuhi tuntutan komputasi masa depan.
---

## Quiz
**1. [Sebutkan tiga fungsi utama sistem operasi?]  
   **Jawaban:Tiga Fungsi Utama Sistem Operasi

1.Manajemen Proses - Mengatur pembuatan, penjadwalan, dan penghentian proses, serta mengelola alokasi CPU untuk berbagai program yang berjalan.
2.Manajemen Memori - Mengelola pengalokasian RAM untuk proses, termasuk virtual memory, dan memastikan setiap program memiliki ruang memori yang dibutuhkan tanpa saling mengganggu.
3.Manajemen I/O dan File System - Mengontrol akses ke perangkat keras seperti disk, printer, dan keyboard, serta mengelola penyimpanan dan organisasi file.
2. [Jelaskan perbedaan antara kernel mode dan user mode?]  
   **Jawaban:
   Perbedaan Kernel Mode dan User Mode
Kernel Mode:

Memiliki akses penuh ke semua sumber daya hardware dan instruksi CPU
Dapat mengeksekusi instruksi privileged (seperti I/O operations, manajemen memori)
Kode sistem operasi berjalan di mode ini
Kesalahan di mode ini bisa menyebabkan system crash

User Mode:

Akses terbatas ke hardware dan instruksi CPU tertentu
Aplikasi pengguna berjalan di mode ini
Harus meminta layanan OS melalui system call untuk mengakses hardware
Kesalahan di mode ini hanya mempengaruhi aplikasi tersebut, tidak seluruh sistem
3. [Sebutkan contoh OS dengan arsitektur monolithic dan micrrokernel?]  
   **Jawaban:**
   Contoh Arsitektur OS
Monolithic Kernel:

Linux - Semua komponen kernel (device drivers, file system, memory management) berjalan dalam satu address space di kernel mode
Unix tradisional - Arsitektur yang menjadi basis banyak OS modern

Microkernel:

MINIX - Hanya fungsi dasar di kernel, layanan lain berjalan sebagai server di user space
QNX - Digunakan dalam sistem embedded dan real-time
Mach - Menjadi basis untuk macOS/iOS (meskipun macOS menggunakan hybrid kernel)

Perbedaan utamanya: monolithic menempatkan hampir semua fungsi OS di kernel space untuk performa lebih cepat, sedangkan microkernel hanya menempatkan fungsi minimal di kernel untuk meningkatkan stabilitas dan keamanan.
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
- ngga ada 
- Bagaimana cara Anda mengatasinya?
- 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
