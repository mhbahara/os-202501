import sys
import os
import cpu      # Import langsung (karena satu folder)
import memory   # Import langsung

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("==========================================")
        print("   OS SIMULATION TOOL - KELOMPOK KITA     ")
        print("==========================================")
        print("1. CPU Scheduling (FCFS)")
        print("2. Memory Management (LRU)")
        print("3. Keluar")
        print("==========================================")
        
        choice = input("Pilih menu [1-3]: ")
        
        if choice == '1':
            # Pastikan file data ada di folder data/
            cpu.solve_fcfs('data/cpu_data.csv')
        elif choice == '2':
            try:
                frames = int(input("Masukkan jumlah Frame RAM (misal: 3): "))
                memory.solve_lru('data/mem_data.txt', capacity=frames)
            except ValueError:
                print("Input harus angka!")
        elif choice == '3':
            print("Terima kasih!")
            sys.exit()
        else:
            print("Pilihan tidak valid.")
        
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main_menu()
