import sys
sys.dont_write_bytecode = True

from kasir_FCFS import simulasi_kasir
from page import simulasi_lru

def menu():
    while True:
        print("\n=== MENU SIMULASI SISTEM OPERASI ===")
        print("1. Simulasi FCFS (Kasir)")
        print("2. Simulasi Page Replacement LRU")
        print("3. Jalankan Semua Simulasi")
        print("0. Keluar")
        print("-" * 35)

        pilihan = input("Pilih menu (0-3): ")

        if pilihan == "1":
            simulasi_kasir()
        elif pilihan == "2":
            simulasi_lru()
        elif pilihan == "3":
            simulasi_kasir()
            simulasi_lru()
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    menu()
