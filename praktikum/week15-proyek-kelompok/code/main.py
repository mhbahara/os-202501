import os
from utils import load_processes, load_pages
from memory import fifo_algorithm
from scheduling import fcfs_algorithm, read_processes

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        # clear_screen()
        print("\n" + "="*45)
        print("   SISTEM SIMULASI OS - KELOMPOK [NAMA]   ")
        print("="*45)
        print("1. Simulasi Penjadwalan CPU (FCFS)")
        print("2. Simulasi Manajemen Memori (FIFO)")
        print("3. Keluar")
        print("-" * 45)
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            print("\n--- Menjalankan FCFS ---")
            data = read_processes("processes.csv")
            if data:
                print(f"Berhasil memuat {len(data)} proses.")
                # PASTIKAN BARIS INI ADA DAN SEJAJAR:
                fcfs_algorithm(data)
            else:
                print("Gagal memuat data proses.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == '2':
            print("\n--- Menjalankan FIFO Memory ---")
            data = load_pages("pages.csv") 
            if data:
                fifo_algorithm(data, capacity=3)
            else:
                print("Data halaman tidak ditemukan atau kosong!")
            input("\nTekan Enter untuk kembali...") 

        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk mencoba lagi...")

if __name__ == "__main__":
    main_menu()