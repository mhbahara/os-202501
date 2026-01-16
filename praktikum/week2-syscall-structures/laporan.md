
# Laporan Praktikum Minggu [2]
Topik: Struktur System Call dan Fungsi Kernel

---

## Identitas
- **Nama**  : Gilang Ananda Putra  
- **NIM**   : 250202939  
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

1. **System Call** adalah mekanisme yang menyediakan antarmuka antara *user mode* dengan *kernel mode*. Sistem Call memungkinkan program untuk mengakses layanan kernel, seperti manajemen file, proses, dan perangkat keras secara aman. System call berfungsi sebagai "gerbang" yang diatur ketat.

2. **Dual Mode Operation (User Mode dan Kernel Mode)**
   - User Mode adalah program aplikasi yang berjalan di mode ini. Dalam mode ini, akses instruksi atau memori yang sensitif dibatasi untuk mencegah kerusakan sistem.

   - Kernel Mode adalah mode yang memiliki hak akses istimewa penuh dan dapat mengeksekusi instruksi apa pun serta mengakses bagian memori dan perangkat keras. Transisi dari user mode ke kernel mode hanya terjadi melalui mekanisme yang terkontrol, salah satunya adalah system call.

3. **Mekanisme Eksekusi System Call** adalah ketika sebuah program memanggil sebuah fungsi pustaka (library function) yang memerlukan layanan OS, fungsi tersebut akan memicu sebuah trap atau interrupt software. Hal ini menyebabkan CPU beralih dari user mode ke kernel mode.



---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

3. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. **Diagram Alur System Call**
   - Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
   - Gunakan draw.io / mermaid.
   - Simpan di:
     ```
     praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
- perintah ```strace ls```
   - menghasilkan
   ```bash
   execve("/usr/bin/ls", ["ls"], 0x7fffd17fe190 /* 62 vars */) = 0
   brk(NULL)                               = 0x566d144a2000
   mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7dc688836000
   access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
   openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
   fstat(3, {st_mode=S_IFREG|0644, st_size=35463, ...}) = 0
   mmap(NULL, 35463, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7dc68882d000
   close(3)                                = 0
   openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libselinux.so.1", O_RDONLY|O_CLOEXEC) = 3
   read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
   fstat(3, {st_mode=S_IFREG|0644, st_size=174472, ...}) = 0
   mmap(NULL, 181960, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7dc688800000
   mmap(0x7dc688806000, 118784, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x6000) = 0x7dc688806000
   mmap(0x7dc688823000, 24576, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x23000) = 0x7dc688823000
   mmap(0x7dc688829000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x29000) = 0x7dc688829000
   mmap(0x7dc68882b000, 5832, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7dc68882b000
   close(3)                                = 0
   openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
   read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\243\2\0\0\0\0\0"..., 832) = 832
   pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
   fstat(3, {st_mode=S_IFREG|0755, st_size=2125328, ...}) = 0
   pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
   mmap(NULL, 2170256, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7dc6885ee000
   mmap(0x7dc688616000, 1605632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x28000) = 0x7dc688616000
   mmap(0x7dc68879e000, 323584, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b0000) = 0x7dc68879e000
   mmap(0x7dc6887ed000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1fe000) = 0x7dc6887ed000
   mmap(0x7dc6887f3000, 52624, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7dc6887f3000
   close(3)                                = 0
   openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpcre2-8.so.0", O_RDONLY|O_CLOEXEC) = 3
   read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
   fstat(3, {st_mode=S_IFREG|0644, st_size=625344, ...}) = 0
   mmap(NULL, 627472, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7dc688554000
   mmap(0x7dc688556000, 450560, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x7dc688556000
   mmap(0x7dc6885c4000, 163840, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x70000) = 0x7dc6885c4000
   mmap(0x7dc6885ec000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x97000) = 0x7dc6885ec000
   close(3)                                = 0
   mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7dc688551000
   arch_prctl(ARCH_SET_FS, 0x7dc688551800) = 0
   set_tid_address(0x7dc688551ad0)         = 1695
   set_robust_list(0x7dc688551ae0, 24)     = 0
   rseq(0x7dc688552120, 0x20, 0, 0x53053053) = 0
   mprotect(0x7dc6887ed000, 16384, PROT_READ) = 0
   mprotect(0x7dc6885ec000, 4096, PROT_READ) = 0
   mprotect(0x7dc688829000, 4096, PROT_READ) = 0
   mprotect(0x566ceb25f000, 8192, PROT_READ) = 0
   mprotect(0x7dc68886e000, 8192, PROT_READ) = 0
   prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
   munmap(0x7dc68882d000, 35463)           = 0
   statfs("/sys/fs/selinux", 0x7ffc1aa51cf0) = -1 ENOENT (No such file or directory)
   statfs("/selinux", 0x7ffc1aa51cf0)      = -1 ENOENT (No such file or directory)
   getrandom("\x73\xdd\xce\xf2\x16\xe5\xea\x07", 8, GRND_NONBLOCK) = 8
   brk(NULL)                               = 0x566d144a2000
   brk(0x566d144c3000)                     = 0x566d144c3000
   openat(AT_FDCWD, "/proc/filesystems", O_RDONLY|O_CLOEXEC) = 3
   fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
   read(3, "nodev\tsysfs\nnodev\ttmpfs\nnodev\tbd"..., 1024) = 390
   read(3, "", 1024)                       = 0
   close(3)                                = 0
   access("/etc/selinux/config", F_OK)     = -1 ENOENT (No such file or directory)
   openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
   fstat(3, {st_mode=S_IFREG|0644, st_size=3055776, ...}) = 0
   mmap(NULL, 3055776, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7dc688266000
   close(3)                                = 0
   ioctl(1, TCGETS, {c_iflag=ICRNL|IXON|IUTF8, c_oflag=NL0|CR0|TAB0|BS0|VT0|FF0|OPOST|ONLCR, c_cflag=B38400|CS8|CREAD, c_lflag=ISIG|ICANON|ECHO|ECHOE|ECHOK|IEXTEN|ECHOCTL|ECHOKE, ...}) = 0
   ioctl(1, TIOCGWINSZ, {ws_row=9, ws_col=82, ws_xpixel=0, ws_ypixel=0}) = 0
   openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
   fstat(3, {st_mode=S_IFDIR|0750, st_size=4096, ...}) = 0
   getdents64(3, 0x566d144a8ce0 /* 16 entries */, 32768) = 528
   getdents64(3, 0x566d144a8ce0 /* 0 entries */, 32768) = 0
   close(3)                                = 0
   fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(0x88, 0x1), ...}) = 0
   write(1, "README-cloudshell.txt\n", 22README-cloudshell.txt
   ) = 22
   close(1)                                = 0
   close(2)                                = 0
   exit_group(0)                           = ?
   +++ exited with 0 +++
   ```
---
- perintah ```strace -e trace=open,read,write,close cat /etc/passwd```
   - menghasilkan
   ```bash
   close(3)                                = 0
   read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\243\2\0\0\0\0\0"..., 832) = 832
   close(3)                                = 0
   close(3)                                = 0
   read(3, "root:x:0:0:root:/root:/bin/bash\n"..., 131072) = 1439
   write(1, "root:x:0:0:root:/root:/bin/bash\n"..., 1439root:x:0:0:root:/root:/bin/bash
   daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
   bin:x:2:2:bin:/bin:/usr/sbin/nologin
   sys:x:3:3:sys:/dev:/usr/sbin/nologin
   sync:x:4:65534:sync:/bin:/bin/sync
   games:x:5:60:games:/usr/games:/usr/sbin/nologin
   man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
   lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
   mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
   news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
   uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
   proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
   www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
   backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
   list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
   irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
   _apt:x:42:65534::/nonexistent:/usr/sbin/nologin
   nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
   systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
   messagebus:x:100:101::/nonexistent:/usr/sbin/nologin
   polkitd:x:997:997:User for polkitd:/:/usr/sbin/nologin
   syslog:x:101:102::/nonexistent:/usr/sbin/nologin
   dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
   dhcpcd:x:102:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
   redis:x:103:104::/var/lib/redis:/usr/sbin/nologin
   sshd:x:104:65534::/run/sshd:/usr/sbin/nologin
   postgres:x:105:106:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
   gilanganandaputra12:x:1000:1000::/home/gilanganandaputra12:/bin/bash
   ) = 1439
   read(3, "", 131072)                     = 0
   close(3)                                = 0
   close(1)                                = 0
   close(2)                                = 0
   +++ exited with 0 +++
   ```
---
- perintah ```dmesg | tail -n 10```
   - menghasilkan
   ```bash
   [ 1921.207577] sd 0:0:2:0: [sdb] Mode Sense: 1f 00 00 08
   [ 1921.207981] sd 0:0:2:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
   [ 1921.599060]  sdb: sdb1
   [ 1921.601986] sd 0:0:2:0: [sdb] Attached SCSI disk
   [ 1921.859972] EXT4-fs (sdb1): mounted filesystem b9f0e455-8c03-483b-a0d6-629a47561fb9 r/w with ordered data mode. Quota mode: none.
   [ 1923.235653] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/ipv4/netfilter/iptable_nat.ko" pid=2119 cmdline="/sbin/modprobe -q -- iptable_nat"
   [ 1923.380378] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netlink/netlink_diag.ko" pid=2140 cmdline="/sbin/modprobe -q -- net-pf-16-proto-4-type-16"
   [ 1926.129705] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netfilter/ipset/ip_set.ko" pid=2420 cmdline="/sbin/modprobe -q -- ipt_set"
   [ 1926.153347] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netfilter/xt_set.ko" pid=2420 cmdline="/sbin/modprobe -q -- ipt_set"
   [ 1926.193060] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/ipv6/netfilter/ip6table_nat.ko" pid=2426 cmdline="/sbin/modprobe -q -- ip6table_nat"
   ```

# Table Observasi Eksperimen Sistem Call

| **Eksperimen** | **Perintah yang Dijalankan** | **System Call / Output Utama yang Diamati** | **Fungsi dan Analisis** |
|----------------|-------------------------------|---------------------------------------------|---------------------------|
| **1. Analisis System Call (ls)** | `strace ls` | 1. `execve("/bin/ls", ["ls"], ...)` | Memuat dan menjalankan program `ls`. Ini adalah system call fundamental untuk eksekusi proses baru. |
| | | 2. `brk(NULL)` | Mengatur batas data segment program. Digunakan untuk alokasi memori awal. |
| | | 3. `access("/etc/ld.so.preload", R_OK)` | Memeriksa apakah file pre-load shared libraries ada dan dapat dibaca. |
| | | 4. `openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/...", O_RDONLY, O_CLOEXEC)` | Membuka file library untuk dibaca. |
| | | 5. `fstat(3, {st_mode=S_IFREG, 0644, ...})` | Mengambil metadata file (ukuran, mode, izin, dll). |
| | | 6. `mmap(...)` | Memetakan shared library yang dibuka ke dalam ruang alamat memori proses `ls`. |
| | | 7. `close(3)` | Menutup file descriptor setelah shared library selesai dimuat. |
| | | 8. `getdents64(1, ..., 32768)` | Membaca entri direktori (nama file/folder) dari file descriptor direktori saat ini. |
| | | 9. `write(1, "file1.txt\nfile2.txt\n", 20)` | Menulis hasil pembacaan direktori ke stdout (layar). |
| | | 10. `exit_group(0)` | Mengakhiri semua thread dalam proses secara bersih. |
| **2. Menelusuri File I/O (cat)** | `strace -e trace=open,read,write,close cat /etc/passwd` | 1. `openat(AT_FDCWD, "/etc/passwd", O_RDONLY)` | Membuka file `/etc/passwd` hanya untuk dibaca (`O_RDONLY`). Kernel mengembalikan file descriptor positif (misalnya 3). |
| | | 2. `read(3, "root:x:0:0:root:/root:/bin/bash\n...", 32768)` | Membaca data isi file dari file descriptor 3 ke buffer proses. |
| | | 3. `write(1, "root:x:0:0:root:/root:/bin/bash\n...", 32768)` | Menuliskan data yang dibaca ke stdout (terminal). |
| | | 4. `read(3, "", 32768)` | Membaca lagi, tetapi mengembalikan 0 → End-of-File (EOF). |
| | | 5. `close(3)` | Menutup file descriptor 3 dan melepaskan sumber daya kernel. |
| **3. Mode User vs. Kernel (dmesg)** | `dmesg` atau `tail -n 10 /var/log/kern.log` | 1. `[ 12.345678] usb 1-1: new high-speed USB device number 5 using xhci_hcd` | Menampilkan log aktivitas kernel seperti inisialisasi driver, pesan boot, dan error perangkat keras. Program user tidak dapat menghasilkan log seperti ini karena dijalankan di mode kernel. |




---

## Hasil Eksekusi
#### Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/strace_ls.png)
---

## Analisis Hasil Percobaan dan Keterkaitannya dengan Teori
### A. makna hasil percobaan

   Percobaan menggunakan ```strace``` dan ```dmesg``` berhasil memvisualisasikan **interaksi yang dimediasi** antara program aplikasi dan kernel, sehingga membuktikan adanya **Dual Mode Operation** pada OS.

   1. **Siklus Hidup Proses (strace ls)**
      - Setiap langkah program ```ls```(dari inisialisasi dengan ```execve()```, manajeman memori dengan ```brk()``` dan ```mmap()```, I/O file dengan ```openat()``` dan ```getdents64()```, sehingga output dengan ```write(1,...)``` adalah permintaan layanan kepada kernel.

      - Maknanya, program aplikasi tidak bisa melakukan operasi kritis sendiri, melainkan harus menggunakan **System Call** sebagai gerbang untuk memasuki **Kernel Mode**.

   2. **Operasi File I/O yang Terkontrol (strace cat)**
      - Alur ```openat() \rightarrow read() \rightarrow write() \rightarrow close()``` menunjukkan bahwa setiap akses data diatur oleh kernel.

      - Ini memastikan bahwa satu program tidak dapat merusak atau mengakses file sensitif prtogram lain tanpa izin.

   3. **Perbedaan Mode Operasi (dmesg)**
      - Kebutuhan untuk menggunakan ```sudo``` pada ```dmesg``` untuk melihat log kernel menunjukkan pemisahan ketat antara **User Mode** dan **Kernel Mode**.
      - Log kernel berisikan informasi tingkat rendah, yang merupakan domain eksklusif kernel dan dilindungi dari akses langsung user untuk **stabilitas dan keamanan sistem**.


### B. Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).

   | **Konsep Teori**        | **Keterkaitan dengan Hasil Percobaan (strace, dmesg)**                       | **Penjelasan**                                                                                                                                                                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **System Call**           | Output `strace` (e.g., `execve`, `read`, `write`)                           | Setiap baris System Call pada `strace` mewakili *software interrupt* yang berfungsi sebagai mekanisme transisi yang aman, mengalihkan kendali eksekusi dari program *user* ke *Kernel Mode*.                                                                                                 |
| **Fungsi Kernel**         | System Call Manajerial (e.g., `mmap`, `execve`, `openat`)                    | Kernel berperan sebagai *Resource Manager* utama. System call ini adalah permintaan resmi kepada kernel untuk mengelola sumber daya kritis seperti memori (`mmap`), proses (`execve`), dan sistem file (`openat`). Semua operasi sensitif harus melalui kernel.                                 |
| **Arsitektur Dual Mode**  | Kebutuhan `sudo` pada `dmesg` dan peran System Call                         | Membuktikan pemisahan antara *User Mode* (hak terbatas) dan *Kernel Mode* (hak istimewa). System call adalah cara terkontrol untuk mencapai keamanan sistem, memastikan program *User Mode* hanya dapat meminta layanan, bukan mengeksekusi instruksi istimewa secara langsung.                 |

### C. Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)? 

| **Fitur**               | **Linux (Unix-like)**                                                                                     | **Windows (NT Kernel)**                                                                                                            |
|--------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| **Antarmuka System Call** | Disediakan oleh **Linux Kernel**. Nama → *POSIX-style* (e.g., `execve`, `mmap`).                         | Disediakan oleh **NT Executive** (*Kernel Windows*). Nama → *Native API* (e.g., `NtCreateFile`, `NtAllocateVirtualMemory`).         |
| **Library Penghubung**   | Fungsi di **C Library (libc)** yang memetakan ke *system call* bernomor.                                 | Fungsi di **Win32 API** (e.g., `CreateProcess`, `ReadFile`) yang kemudian memanggil *Native API* kernel.                           |
| **Alat Trace**           | `strace`                                                                                                 | **Process Monitor (Procmon)** atau **xperf** (*Windows Performance Recorder*).                                                     |
| **Log Kernel**           | Dapat diakses melalui `dmesg` (membutuhkan hak akses tinggi).                                            | Log kernel disimpan di **Event Viewer** atau **Debug View**, dan memerlukan alat debugging khusus.                                 |

## Analisis Kritis Peran System Call 

1. **Mengapa System Call Penting Untuk Keamanan dan Stabilitas OS**

*System call* merupakan antarmuka terprogram yang diekspos oleh *kernel* ke *user space*, dan berfungsi sebagai batas keamanan fundamental dalam sistem operasi (OS) modern. Peran kritis *system call* terletak pada **Prinsip Pemisahan Hak Istimewa** melalui arsitektur *Dual Mode Operation.*
Arsitektur prosesor membedakan dua mode eksekusi yaitu *user mode* di mana aplikasi berjalan dengan hak istimewa terbatas, dan *kernel mode* dengan akses terbatas ke sumber daya sistem. Aplikasi di *user mode* tidak dapat menjalankan instruksi istimewa, mengakses memori kernel, atau secara langsung berinteraksi dengan perangkat keras (I/O). *System call* adalah salah-satunya gerbang yang diizinkan bagi program *user* untuk meminta layanan *kernel*, seperti manajemen berkas.
Mekanisme ini memastikan keamanan dan stabilitas OS dengan:
    - **Mengisolasi Sumber Daya Kritis**. *System call* menyediakan lapisan abstraksi, melindungi komponen vital sistem seperti CPU dan memori dari kesalahan program atau serangan terarah yang berasal dari *user space*.
    - **Membatasi Akses Langsung ke Perangkat Keras** dengan mewajibkan semua permintaan akses perangkat keras melalui *kernel* di Ring 0, *system call* menjamin bahwa operasi I/O dilakukan secara terorganisasi dan aman, mencegah akses tidak sah.

---

2. **Mekanisme Proteksi Transisi User ke Kernel Mode**

OS memastikan transisi dari *user mode* ke *kernel mode* berjalan aman melalui serangkaian mekanisme proteksi yang memanfaatkan fitur arsitektur prosesor, termasuk *interrupt* atau *trap*. Transisi dipicu ketika proses user memanggil *system call*, yang diimplementasikan melalui **trap** (software interrupt). Ini menyebabkan mesin (CPU) mentransfer *kontrol* ke *kernel*. Transfer kontrol ini bersifat **Atomik** dilakukan dalam satu instruksi untuk secara serentak mengubah status CPU, termasuk:
    - Mengatur **Privilege Level** ke kernel mode
    - Mengubah *Program Counter* (PC) untuk mengarahkan eksekusi ke *handler* kernel yang sudah terdaftar di Interrupt Vector Table (IVT).
    - Mengubah *Stack Pointer* (SP) dan proteksi memori, memastikan *handler* berjalan pada *stack kernel* yang aman

Setelah *kernel* mengambil alih kontrol, proteksi segera ditegakkan melalui **Validasi Parameter**. Teknik *system call checking* (misalnya Seccomp di Linux) memeriksa ID *system call* dan integritas nilai argumen yang diserahkan oleh proses *user* di register. Validasi yang tidak memadai, seperti *incomplete parameter validation*, dapat menciptakan celah keamanan (misalnya *argument races* atau pemodifikasian yang ilegal). Oleh karena itu, kernel harus membandingkan *system call* yang masuk dengan daftar yang diizinkan *(whitelist)* dan memverifikasi argumen sebelum melanjutkan eksekusi layanan.

---

3. **Contoh System Call Kritis Linux dan Relevansi Keamanan**

*System call* adalah titik penerapan kebijakan kontrol akses, seperti *Mandatory Access Control* (MAC) melalui *Linux Security Module* (LSM). Beberapa *system call* umum memiliki implikasi keamanan tinggi di Linux:
    - **execve (Execute Program)**: Digunakan untuk menjalankan program baru, menggantikan program yang sedang berjalan. Ini adalah blok bangunan krusial dalam serangan eskalasi hak istimewa *(privilege escalation)* dan *control-flow hijacking*. Penerapan **Principle of Least Privilege (PoLP)** sangat penting di sini. Mekanisme adaptif seperti SysXCHG memungkinkan pertukaran filter *system call* secara dinamis selama execve, memastikan program berjalan hanya dengan hak istimewa minimum yang dibutuhkan.
    - **open dan openat (File Access)**: Digunakan untuk membuka dan mengakses sumber daya *filesystem*. Relevansi keamanannya adalah tempat di mana izin pengguna *(permissions)* dan kebijakan MAC diperiksa untuk menegakkan kontrol akses.
    - **mprotect (Memory Protection):** Berfungsi mengubah izin pada halaman memori. *System call* ini sensitif karena sering disalahgunakan pasca eksploitasi *memory corruption* untuk menandai segmen memori sebagai dapat dieksekusi, memfasilitasi injeksi kode berbahaya. Penelitian modern berfokus pada penegakan **Integritas *System Call*** untuk memastikan penggunaan mprotect yang sah.



---

## Kesimpulan
1. System Call Adalah Antarmuka Aman ke Kernel. System Call berfungsi sebagai gerbang wajib yang memungkinkan program aplikasi di **User Mode** untuk meminta dan mendapatkan layanan sensitif dari **Kernel Mode** (seperti I/O file, manajemen memori, dan kontrol proses) secara terstruktur. Analisis ```strace``` membuktikan bahwa setiap operasi tingkat rendah pada OS dikoordinasikan melalui System Call (```execve```, ```read```, ```write```, dll.).

2. Pembuktian Arsitektur Dual Mode (Keamanan OS). Hasil percobaan menegaskan adanya pemisahan ketat antara User Mode dan Kernel Mode. Kebutuhan untuk menggunakan hak istimewa (```sudo```) saat mengakses log kernel via ```dmesg``` menunjukkan bahwa Kernel terlindungi dan beroperasi di tingkat hak akses yang lebih tinggi untuk menjamin stabilitas dan keamanan seluruh sistem.

3. Siklus Hidup Proses Terkendali Kernel: Eksekusi program, dari pemuatan awal (loading) hingga terminasi (```execve``` hingga ```exit_group```), sepenuhnya dikelola oleh Kernel. Kernel bertanggung jawab penuh dalam alokasi sumber daya (seperti memetakan shared library menggunakan ```mmap``` dan ```brk```) sebelum program dapat menjalankan logika intinya.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?  
   
   
   **Jawaban:**  
   Fungsi utama System Call adalah menyediakan antarmuka terprogram antara program aplikasi yang berjalan di User Mode dengan Kernel Mode sistem operasi. Fungsi ini memungkinkan aplikasi untuk mengakses sumber daya dan layanan kernel (seperti I/O file, manajemen memori, dan kontrol perangkat keras) secara aman, terstruktur, dan terkontrol.
2. Sebutkan 4 kategori system call yang umum digunakan 
   
   
   **Jawaban:**  
   - Process Control: Mengatur eksekusi program (misalnya: ```execve```, ```fork```, ```exit```).
   - File Management: Mengelola file (misalnya: ```open```, ```read```, ```write```, ```close```).

   - Device Management: Mengatur perangkat keras (misalnya: ```ioctl```, ```read```, ```write``` pada device).

   - Information Maintenance: Mengambil atau mengatur informasi sistem (misalnya: ```time```, ```getpid```, ```chmod```).

   - (Kategori tambahan yang sering diakui: Communication, misalnya: ```pipe```, ```shmget```)
3. Mengapa system call tidak bisa dipanggil langsung oleh user program? 
   
   
   **Jawaban:**  
   System Call tidak dapat dipanggil langsung karena alasan keamanan, stabilitas, dan hak istimewa (privilege) yang melekat pada Arsitektur Dual Mode (User Mode vs. Kernel Mode). System call memerlukan transisi mode dari User Mode ke Kernel Mode. Jika program user diizinkan memanggilnya langsung, program tersebut dapat:

   - Melanggar Keamanan: Mengakses atau mengubah data sensitif kernel atau program lain.

   - Menyebabkan Kerusakan (Crash): Mengeksekusi instruksi istimewa (privilege instructions) yang dapat membuat seluruh sistem operasi berhenti bekerja.

   Oleh karena itu, System Call hanya dapat diakses melalui mekanisme software interrupt atau trap yang telah didefinisikan oleh kernel, memastikan kontrol beralih ke kode kernel yang terpercaya.

---

## Refleksi Diri
Tuliskan secara singkat:
- Tidak bisa menggunakan WSL (terclose sendiri)
- menggunakan  Cloud Shell Editor dan menginstal ulang WSL menggunakan powershell ```wsl --install -d Ubuntu```

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
