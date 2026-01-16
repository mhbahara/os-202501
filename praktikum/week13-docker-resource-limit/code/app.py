import time
import os
import sys

def stress_cpu(n):
    """
    Fungsi untuk membebani CPU dengan perhitungan bilangan prima.
    """
    print(f"--- [CPU TEST] Memulai perhitungan bilangan prima hingga {n} ---")
    start_time = time.time()
    
    count = 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            
    end_time = time.time()
    duration = end_time - start_time
    print(f"--- [CPU TEST] Selesai. Ditemukan {count} bilangan prima.")
    print(f"--- [CPU TEST] Durasi: {duration:.4f} detik ---\n")

def stress_memory(size_in_mb):
    """
    Fungsi untuk membebani Memory dengan mengalokasikan variabel besar.
    """
    print(f"--- [MEM TEST] Mencoba mengalokasikan memori sebesar {size_in_mb} MB ---")
    try:
        # Mengalokasikan string bytes (1 byte per karakter)
        # 1024 * 1024 bytes = 1 MB
        dummy_data = b' ' * (size_in_mb * 1024 * 1024)
        print(f"--- [MEM TEST] Berhasil! Ukuran data: {len(dummy_data) / (1024*1024)} MB")
        
        # Tahan memori sebentar agar bisa dicek di 'docker stats'
        print("--- [MEM TEST] Tidur selama 5 detik (cek docker stats sekarang)...")
        time.sleep(5)
        print("--- [MEM TEST] Selesai melepas memori ---\n")
    except MemoryError:
        print("--- [MEM TEST] GAGAL: Memory Error! Tidak cukup RAM. ---\n")
    except Exception as e:
        print(f"--- [MEM TEST] GAGAL: {e} ---\n")

if __name__ == "__main__":
    print(f"Container ID/Hostname: {os.environ.get('HOSTNAME', 'unknown')}")
    print("Mulai Pengujian Resource Limit...\n")

    # 1. Uji CPU (Menghitung prima sampai 50.000 biasanya cukup berat)
    # Jika CPU di-limit, durasi ini akan naik drastis.
    stress_cpu(50000)

    # 2. Uji Memory (Alokasi 150MB)
    # Jika container dilimit 128MB, ini akan menyebabkan OOM Killed atau MemoryError.
    stress_memory(150)

    print("Pengujian Selesai.")