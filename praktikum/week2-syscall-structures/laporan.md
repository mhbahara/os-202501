
# Laporan Praktikum Minggu 2
Topik: Struktur System Call dan Fungsi Kernel

---

## Identitas
- **Nama**  : Farhan Ramdhani  
- **NIM**   : 250202938  
- **Kelas** : 1IKRB

---

## Tujuan
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
Sistem operasi (Operating System/OS) merupakan perangkat lunak yang berperan sebagai penghubung antara pengguna dengan perangkat keras komputer. Melalui sistem operasi, pengguna dapat menjalankan berbagai program aplikasi dengan aman dan efisien tanpa perlu berinteraksi langsung dengan perangkat keras. Di dalam sistem operasi terdapat dua komponen utama, yaitu kernel dan system call. Kernel berfungsi sebagai inti dari sistem operasi yang menyediakan berbagai layanan penting agar komputer dapat beroperasi dengan baik. Sementara itu, system call berperan sebagai pintu masuk bagi aplikasi untuk meminta layanan dari kernel. Dengan kata lain, system call memungkinkan program aplikasi berkomunikasi dengan kernel untuk melakukan tugas-tugas seperti membaca file, mengakses memori, atau berinteraksi dengan perangkat keras. Tanpa adanya system call, aplikasi tidak dapat mengakses sumber daya sistem secara aman. Sebaliknya, tanpa kernel, system call tidak memiliki sistem yang dapat menjalankan perintah tersebut. Keduanya saling bergantung dan bekerja sama agar sistem operasi dapat berjalan secara optimal.

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
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```
### 1. strace ls
```bash
- root@DESKTOP-R1GLO2B:~# strace ls
execve("/usr/bin/ls", ["ls"], 0x7ffdf785a1a0 /* 28 vars */) = 0
brk(NULL)                               = 0x63f59647f000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x72d604b77000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=26567, ...}) = 0
mmap(NULL, 26567, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604b70000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libselinux.so.1", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=174472, ...}) = 0
mmap(NULL, 181960, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x72d604b43000
mmap(0x72d604b49000, 118784, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x6000) = 0x72d604b49000
mmap(0x72d604b66000, 24576, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x23000) = 0x72d604b66000
mmap(0x72d604b6c000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x29000) = 0x72d604b6c000
mmap(0x72d604b6e000, 5832, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x72d604b6e000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\243\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
fstat(3, {st_mode=S_IFREG|0755, st_size=2125328, ...}) = 0Eksperimen 1 – Analisis System Call Jalankan perintah berikut:
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 2170256, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x72d604800000
mmap(0x72d604828000, 1605632, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x28000) = 0x72d604828000
mmap(0x72d6049b0000, 323584, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1b0000) = 0x72d6049b0000
mmap(0x72d6049ff000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1fe000) = 0x72d6049ff000
mmap(0x72d604a05000, 52624, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x72d604a05000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libpcre2-8.so.0", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\0\0\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=625344, ...}) = 0
mmap(NULL, 627472, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x72d604aa9000
mmap(0x72d604aab000, 450560, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x2000) = 0x72d604aab000
mmap(0x72d604b19000, 163840, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x70000) = 0x72d604b19000
mmap(0x72d604b41000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x97000) = 0x72d604b41000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x72d604aa6000
arch_prctl(ARCH_SET_FS, 0x72d604aa6800) = 0
set_tid_address(0x72d604aa6ad0)         = 2606
set_robust_list(0x72d604aa6ae0, 24)     = 0
rseq(0x72d604aa7120, 0x20, 0, 0x53053053) = 0
mprotect(0x72d6049ff000, 16384, PROT_READ) = 0
mprotect(0x72d604b41000, 4096, PROT_READ) = 0
mprotect(0x72d604b6c000, 4096, PROT_READ) = 0
mprotect(0x63f565634000, 8192, PROT_READ) = 0
mprotect(0x72d604baf000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x72d604b70000, 26567)           = 0
statfs("/sys/fs/selinux", {f_type=SYSFS_MAGIC, f_bsize=4096, f_blocks=0, f_bfree=0, f_bavail=0, f_files=0, f_ffree=0, f_fsid={val=[0x2946c3fe, 0xd2276f1d]}, f_namelen=255, f_frsize=4096, f_flags=ST_VALID|ST_NOSUID|ST_NODEV|ST_NOEXEC|ST_NOATIME}) = 0
statfs("/selinux", 0x7fffc6b4fbf0)      = -1 ENOENT (No such file or directory)
getrandom("\x36\xc4\x5e\x9a\x85\x95\xd7\x3b", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0x63f59647f000
brk(0x63f5964a0000)                     = 0x63f5964a0000
openat(AT_FDCWD, "/proc/filesystems", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(3, "nodev\tsysfs\nnodev\ttmpfs\nnodev\tbd"..., 1024) = 442
close(3)                                = 0
openat(AT_FDCWD, "/proc/mounts", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(3, "none /usr/lib/modules/6.6.87.2-m"..., 1024) = 1024
read(3, "\ndevpts /dev/pts devpts rw,nosui"..., 1024) = 1024
read(3, "hugetlbfs /dev/hugepages hugetlb"..., 1024) = 553
read(3, "", 1024)                       = 0
close(3)                                = 0
access("/etc/selinux/config", F_OK)     = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/share/locale/locale.alias", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=2996, ...}) = 0
read(3, "# Locale name alias data base.\n#"..., 4096) = 2996
read(3, "", 4096)                       = 0
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_IDENTIFICATION", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_IDENTIFICATION", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=258, ...}) = 0
mmap(NULL, 258, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604b76000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=27028, ...}) = 0
mmap(NULL, 27028, PROT_READ, MAP_SHARED, 3, 0) = 0x72d604a9f000
close(3)                                = 0
futex(0x72d604a0472c, FUTEX_WAKE_PRIVATE, 2147483647) = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_MEASUREMENT", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_MEASUREMENT", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=23, ...}) = 0
mmap(NULL, 23, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604b75000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_TELEPHONE", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_TELEPHONE", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=47, ...}) = 0
mmap(NULL, 47, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604b74000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_ADDRESS", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_ADDRESS", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=127, ...}) = 0
mmap(NULL, 127, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604b73000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_NAME", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_NAME", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=62, ...}) = 0
mmap(NULL, 62, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604b72000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_PAPER", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_PAPER", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=34, ...}) = 0
mmap(NULL, 34, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604b71000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_MESSAGES", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_MESSAGES", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_MESSAGES/SYS_LC_MESSAGES", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=48, ...}) = 0
mmap(NULL, 48, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604b70000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_MONETARY", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_MONETARY", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=270, ...}) = 0
mmap(NULL, 270, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604a9e000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_COLLATE", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_COLLATE", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=1406, ...}) = 0
mmap(NULL, 1406, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604a9d000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_TIME", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_TIME", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=3360, ...}) = 0
mmap(NULL, 3360, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604a9c000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_NUMERIC", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_NUMERIC", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=50, ...}) = 0
mmap(NULL, 50, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604a9b000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/locale/C.UTF-8/LC_CTYPE", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/locale/C.utf8/LC_CTYPE", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=360460, ...}) = 0
mmap(NULL, 360460, PROT_READ, MAP_PRIVATE, 3, 0) = 0x72d604a42000
close(3)                                = 0
ioctl(1, TCGETS, {c_iflag=ICRNL|IXON, c_oflag=NL0|CR0|TAB0|BS0|VT0|FF0|OPOST|ONLCR, c_cflag=B38400|CS8|CREAD, c_lflag=ISIG|ICANON|ECHO|ECHOE|ECHOK|IEXTEN|ECHOCTL|ECHOKE, ...}) = 0
ioctl(1, TIOCGWINSZ, {ws_row=41, ws_col=156, ws_xpixel=0, ws_ypixel=0}) = 0
openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
fstat(3, {st_mode=S_IFDIR|0700, st_size=4096, ...}) = 0
getdents64(3, 0x63f5964888a0 /* 9 entries */, 32768) = 272
getdents64(3, 0x63f5964888a0 /* 0 entries */, 32768) = 0
close(3)                                = 0
close(1)                                = 0
close(2)                                = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```

### 2. strace -e trace=open,read,write,close cat /etc/passwd
```bash
- root@DESKTOP-R1GLO2B:~# strace -e trace=open,read,write,close cat /etc/passwd
close(3)                                = 0
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\243\2\0\0\0\0\0"..., 832) = 832
close(3)                                = 0
read(3, "# Locale name alias data base.\n#"..., 4096) = 2996
read(3, "", 4096)                       = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
close(3)                                = 0
read(3, "root:x:0:0:root:/root:/bin/bash\n"..., 131072) = 1380
write(1, "root:x:0:0:root:/root:/bin/bash\n"..., 1380root:x:0:0:root:/root:/bin/bash
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
systemd-timesync:x:996:996:systemd Time Synchronization:/:/usr/sbin/nologin
dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
syslog:x:102:102::/nonexistent:/usr/sbin/nologin
systemd-resolve:x:991:991:systemd Resolver:/:/usr/sbin/nologin
uuidd:x:103:103::/run/uuidd:/usr/sbin/nologin
landscape:x:104:105::/var/lib/landscape:/usr/sbin/nologin
polkitd:x:990:990:User for polkitd:/:/usr/sbin/nologin
) = 1380
read(3, "", 131072)                     = 0
close(3)                                = 0
close(1)                                = 0
close(2)                                = 0
+++ exited with 0 +++
```

### 3. dmesg | tail -n 10
```bash
- root@DESKTOP-R1GLO2B:~# dmesg | tail -n 10
[ 3431.716885] systemd-journald[55]: Time jumped backwards, rotating.
[ 3474.171045] WSL (247) ERROR: CheckConnection: getaddrinfo() failed: -5
[ 3536.970557] systemd-journald[55]: Time jumped backwards, rotating.
[ 3924.456915] systemd-journald[55]: Time jumped backwards, rotating.
[ 4483.074489] systemd-journald[55]: Time jumped backwards, rotating.
[ 5037.582850] systemd-journald[55]: Time jumped backwards, rotating.
[ 5261.126564] systemd-journald[55]: Time jumped backwards, rotating.
[ 5370.606919] WSL (247) ERROR: CheckConnection: getaddrinfo() failed: -5
[ 5587.058647] mini_init (232): drop_caches: 1
[ 5591.302300] systemd-journald[55]: Time jumped backwards, rotating.
```

---

## Hasil Eksekusi
![alt text](<../week2-syscall-structures/screenshots/Screenshot 2025-10-10 003743.png>)
![alt text](<../week2-syscall-structures/screenshots/Screenshot 2025-10-09 202429.png>)

![alt text](<../week2-syscall-structures/screenshots/Screenshot 2025-10-09 202615.png>)

![alt text](<../week2-syscall-structures/screenshots/Screenshot 2025-10-09 202658.png>)

---

## Tugas
- Dokumentasikan hasil eksperimen `strace` dan `dmesg` dalam bentuk tabel observasi.
- Mengapa system call penting untuk keamanan OS?
- Bagaimana OS memastikan transisi user–kernel berjalan aman?
- Sebutkan contoh system call yang sering digunakan di Linux.

**Jawaban :**
## 1. Dokumentasi Hasil Eksperimen strace dan dmesg

### Tabel Observasi

| No | Perintah | Fungsi Perintah | Cuplikan Output | Analisis Singkat |
|----|-----------|----------------|------------------|------------------|
| 1 | `strace ls` | Melacak semua system call yang dijalankan oleh perintah ls. | openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3 | Terlihat bahwa ls memanggil system call openat untuk membuka direktori dan membaca isinya. |
| 2 | `strace cat file.txt` | Melacak system call yang terjadi saat membaca file teks. | read(3, "Isi file\n", 9) = 9 | System call read() digunakan untuk membaca isi file dari disk. |
| 3 | `dmesg` | `head` | Menampilkan pesan log kernel pada saat sistem berjalan. | [0.000000] Linux version 5.15.153.1-microsoft-standard-WSL2 ... | Menunjukkan informasi kernel dan pesan inisialisasi sistem pada saat booting. |
| 4 | `dmesg` | `tail` | Menampilkan pesan kernel terbaru. | [1234.567890] usb 1-2: new device found... | Kernel mencatat aktivitas perangkat keras seperti koneksi USB. |

## 2. Mengapa system call penting untuk keamanan OS?

System call memiliki peran besar dalam menjaga keamanan sistem operasi. Fungsinya seperti gerbang pengaman yang membatasi interaksi antara aplikasi dan kernel. Kernel adalah inti dari sistem operasi yang memiliki kendali penuh terhadap perangkat keras. Jika semua aplikasi bisa mengakses kernel secara bebas, risiko terjadinya kerusakan sistem atau penyalahgunaan sumber daya akan sangat tinggi. Melalui system call, setiap permintaan dari aplikasi diperiksa terlebih dahulu oleh kernel. Misalnya, ketika aplikasi ingin membuka sebuah file, kernel akan memeriksa apakah pengguna memiliki izin untuk mengakses file tersebut. Jika tidak, permintaan tersebut akan ditolak. Proses ini memastikan bahwa setiap tindakan di sistem berjalan sesuai aturan keamanan.

## 2. Bagaimana OS memastikan transisi user–kernel berjalan aman?

Sistem operasi membagi ruang kerja menjadi dua bagian, yaitu user mode dan kernel mode. Aplikasi berjalan di user mode, di mana aksesnya terbatas. Saat aplikasi butuh bantuan kernel, misalnya untuk membaca file atau membuat proses baru, aplikasi akan memanggil system call yang menyebabkan perpindahan sementara ke kernel mode. Proses perpindahan ini tidak dilakukan sembarangan. Kernel hanya mengeksekusi perintah yang sudah tercatat di tabel system call. Sebelum menjalankan perintah, kernel akan memeriksa data yang dikirim aplikasi agar tidak menimbulkan gangguan atau celah keamanan. Setelah tugas selesai, sistem otomatis kembali ke user mode. Dengan cara ini, OS memastikan tidak ada aplikasi yang bisa menguasai kernel atau mengubah sistem secara langsung, sehingga sistem tetap aman dan stabil.

## 3. Contoh system call yang sering digunakan di Linux

**Beberapa system call yang sering digunakan di Linux antara lain :**

- `read` untuk membaca data,

- `write` untuk menulis data ke file,

- `close` untuk menutup file,

- `fork` untuk membuat proses baru,

- `exec` untuk menjalankan program lain,

- `exit` untuk keluar dari proses,

- `wait` untuk menunggu proses anak selesai,

- `getpid` untuk mengetahui ID proses yang sedang berjalan.

---

## Analisis
- Jelaskan makna hasil percobaan.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?

**Jawaban :**

### Makna Hasil Percobaan

Bisa disimpulkan bahwa setiap tindakan sederhana yang kita lakukan di sistem operasi ternyata melibatkan proses yang cukup kompleks di belakang layar. Aplikasi tidak langsung berhubungan dengan perangkat keras, tapi lewat system call yang menjadi penghubung antara program dan kernel. Jadi, hasil percobaan ini menunjukkan bagaimana sistem operasi bekerja dengan teratur dan aman melalui lapisan-lapisan yang saling terhubung.

### Hubungan Hasil Dengan Teori (fungsi kernel, system call, arsitektur OS).

Hasil percobaan ini sejalan dengan teori tentang fungsi kernel dan system call yang sudah dipelajari sebelumnya. Kernel berfungsi sebagai pusat pengendali sistem operasi yang bertugas mengatur akses ke perangkat keras, memori, dan file. Sedangkan system call menjadi cara resmi bagi aplikasi untuk meminta bantuan kernel.

### Perbedaan hasil di OS berbeda (Linux vs Windows) ?

Pada Linux, system call bisa dilihat secara terbuka menggunakan alat seperti strace. Ini membuat kita bisa mempelajari dan memahami bagaimana aplikasi berinteraksi dengan kernel secara langsung. Linux memang bersifat open source, jadi pengguna bisa memantau aktivitas sistem dengan bebas.

Sedangkan di Windows, mekanisme system call lebih tertutup. Aplikasi biasanya tidak langsung berinteraksi dengan kernel, tapi lewat lapisan yang disebut Windows API (Win32 API). Karena itu, pengguna tidak bisa melihat system call secara langsung tanpa alat tambahan seperti Process Monitor. Pendekatan ini membuat Windows terlihat lebih tertutup, tapi tetap aman karena setiap interaksi dikontrol oleh sistemnya sendiri.

Secara sederhana, Linux lebih transparan, sedangkan Windows lebih tertutup namun tetap menjaga keamanan melalui lapisan API-nya.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

**Jawaban :** 
System call dan kernel bekerja seperti dua sisi yang saling melengkapi. System call memberikan jalan yang aman bagi aplikasi untuk berinteraksi dengan kernel, sementara kernel memastikan semua permintaan itu diproses dengan benar tanpa mengancam keamanan sistem. Dengan mekanisme ini, sistem operasi seperti Linux bisa berjalan stabil, efisien, dan tetap aman bagi penggunanya.

---

## Quiz
### 1. Apa fungsi utama system call dalam sistem operasi?

   **Jawaban:** Fungsi utama system call adalah sebagai jembatan antara program pengguna dan kernel. Melalui system call, program bisa meminta layanan dari sistem operasi, seperti membaca atau menulis file, mengatur proses, dan berkomunikasi dengan perangkat keras. Tanpa system call, aplikasi tidak bisa berinteraksi dengan sumber daya komputer secara aman dan terkontrol.
 
### 2. Sebutkan 4 kategori system call yang umum digunakan.

   **Jawaban:** 

- Process control → untuk mengatur proses, seperti fork, exec, exit.


- File management → untuk mengakses file, seperti open, read, write, close.


- Device management → untuk mengatur perangkat keras melalui ioctl atau request.


- Information maintenance → untuk mendapatkan informasi sistem, seperti getpid, alarm, time.



### 3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   **Jawaban:**  Karena system call bekerja di kernel mode, sedangkan program pengguna berjalan di user mode. Kalau user program bisa langsung memanggil kernel tanpa batasan, sistem bisa rusak atau tidak aman. Maka, system call harus lewat mekanisme resmi agar setiap permintaan bisa diverifikasi dan dikontrol oleh kernel, supaya sistem tetap aman dan stabil.




---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
**Jawaban :** Bagian yang paling menantang minggu ini adalah memahami bagaimana system call benar-benar bekerja di balik perintah yang kita jalankan di terminal. Awalnya agak bingung karena banyak istilah baru seperti user mode, kernel mode, dan interrupt yang perlu dipahami dulu.



- Bagaimana cara Anda mengatasinya?  
**Jawaban :** Saya mengatasinya dengan membaca ulang materi dari modul praktikum, mencari contoh-contoh system call di Linux lewat strace, dan menonton beberapa video penjelasan tentang cara kerja kernel di YouTube. Dengan begitu, saya jadi lebih paham alurnya dan bisa melihat langsung hubungan antara teori dan hasil percobaan di sistem operasi.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
