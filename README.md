# os-202501-250202930
Repository praktikum Sistem Operasi (os-202501), Program Studi Ilmu Komputer UPB. Berisi panduan, materi, dan artefak praktikum bertumbuh mingguan.
```mermaid
flowchart TD
    User1[User 1] --> Software
    User2[User 2] --> Software
    Usern[User 3] --> Software

    Software --> Sys[System Softwares]
    Software --> App[Application Softwares]

    Sys --> OS[Operating System]
    App --> OS[Operating System]

    OS --> Hardware
    Hardware --> CPU
    Hardware --> RAM
    Hardware --> IO[I/O]
