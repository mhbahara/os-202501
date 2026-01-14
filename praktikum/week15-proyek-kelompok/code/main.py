def show_header():
    print("=" * 40)
    print(" MINI SIMULASI SISTEM OPERASI ")
    print("=" * 40)


def show_main_menu():
    print("\nMenu Utama:")
    print("1. CPU Scheduling")
    print("2. Page Replacement")
    print("3. Deadlock Detection")
    print("0. Keluar")


def run_cpu_scheduling():
    print("\n--- CPU Scheduling ---")
    print("Modul CPU Scheduling belum diimplementasikan.")
    input("Tekan Enter untuk kembali ke menu utama...")


def run_page_replacement():
    print("\n--- Page Replacement ---")
    print("Modul Page Replacement belum diimplementasikan.")
    input("Tekan Enter untuk kembali ke menu utama...")


def run_deadlock_detection():
    print("\n--- Deadlock Detection ---")
    print("Modul Deadlock Detection belum diimplementasikan.")
    input("Tekan Enter untuk kembali ke menu utama...")


def main():
    while True:
        show_header()
        show_main_menu()

        choice = input("Pilih menu: ")

        if choice == "1":
            run_cpu_scheduling()
        elif choice == "2":
            run_page_replacement()
        elif choice == "3":
            run_deadlock_detection()
        elif choice == "0":
            print("Keluar dari program. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk mencoba lagi...")


if __name__ == "__main__":
    main()