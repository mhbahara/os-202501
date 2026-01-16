import time
import os

def heavy_computation():
    print("--- Memulai Komputasi Berat (CPU Stress) ---")
    start_time = time.time()
    result = 0
    for i in range(1, 10000000):
        result += i * i
    end_time = time.time()
    print(f"Selesai! Waktu eksekusi: {end_time - start_time:.4f} detik")

def memory_allocation():
    print("\n--- Memulai Alokasi Memori (RAM Stress) ---")
    try:
        dummy_data = []
        for i in range(10):
            dummy_data.append(' ' * (10**6 * 10)) 
            print(f"Alokasi memori tahap {i+1}: Total ~{(i+1)*10} MB")
            time.sleep(0.5)
        print("Alokasi memori berhasil tanpa error.")
    except Exception as e:
        print(f"\nTerhenti: {e}")

if __name__ == "__main__":
    print(f"Running on Process ID: {os.getpid()}")
    heavy_computation()
    memory_allocation()