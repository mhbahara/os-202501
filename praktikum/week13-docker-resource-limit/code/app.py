#!/usr/bin/env python3
"""
Program Uji Resource Limit Docker
Menguji penggunaan CPU dan Memori
"""

import time
import psutil
import os
from datetime import datetime

def print_resource_info():
    """Menampilkan informasi penggunaan resource saat ini"""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    
    print(f"\n{'='*60}")
    print(f"Waktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"PID: {os.getpid()}")
    print(f"Memory RSS: {mem_info.rss / 1024 / 1024:.2f} MB")
    print(f"Memory VMS: {mem_info.vms / 1024 / 1024:.2f} MB")
    print(f"CPU Percent: {process.cpu_percent(interval=1):.2f}%")
    print(f"{'='*60}\n")

def cpu_intensive_task(duration=5):
    """
    Task yang menggunakan CPU intensif
    Args:
        duration: durasi dalam detik
    """
    print(f"[CPU TEST] Memulai komputasi intensif selama {duration} detik...")
    start_time = time.time()
    counter = 0
    
    while time.time() - start_time < duration:
        # Operasi matematika untuk menggunakan CPU
        result = sum([i**2 for i in range(1000)])
        counter += 1
    
    print(f"[CPU TEST] Selesai. Iterasi: {counter:,}")
    return counter

def memory_intensive_task(target_mb=200, step_mb=50):
    """
    Task yang mengalokasikan memori bertahap
    Args:
        target_mb: target memori yang akan dialokasikan (MB)
        step_mb: step alokasi per tahap (MB)
    """
    print(f"\n[MEMORY TEST] Mengalokasikan memori bertahap...")
    print(f"Target: {target_mb} MB, Step: {step_mb} MB")
    
    data_chunks = []
    allocated = 0
    
    try:
        while allocated < target_mb:
            # Alokasikan chunk memori (1 MB = 1024*1024 bytes)
            chunk_size = min(step_mb, target_mb - allocated)
            chunk = bytearray(chunk_size * 1024 * 1024)
            data_chunks.append(chunk)
            allocated += chunk_size
            
            print(f"  → Dialokasikan: {allocated} MB")
            print_resource_info()
            time.sleep(1)
        
        print(f"[MEMORY TEST] Berhasil mengalokasikan {allocated} MB")
        print("Menahan memori selama 3 detik...")
        time.sleep(3)
        
    except MemoryError:
        print(f"[MEMORY TEST] ❌ MemoryError! Hanya berhasil alokasi {allocated} MB")
    except Exception as e:
        print(f"[MEMORY TEST] ❌ Error: {e}")
    finally:
        print(f"[MEMORY TEST] Membersihkan memori...")
        data_chunks.clear()

def main():
    print("\n" + "="*60)
    print("DOCKER RESOURCE LIMIT TEST")
    print("="*60)
    
    # Informasi awal
    print("\n[INFO] Resource awal:")
    print_resource_info()
    
    # Test 1: CPU Intensive
    print("\n" + "-"*60)
    print("TEST 1: CPU INTENSIVE")
    print("-"*60)
    cpu_intensive_task(duration=5)
    print_resource_info()
    
    # Test 2: Memory Intensive
    print("\n" + "-"*60)
    print("TEST 2: MEMORY INTENSIVE")
    print("-"*60)
    memory_intensive_task(target_mb=200, step_mb=50)
    print_resource_info()
    
    # Test 3: Kombinasi CPU + Memory
    print("\n" + "-"*60)
    print("TEST 3: KOMBINASI CPU + MEMORY")
    print("-"*60)
    print("[KOMBINASI] Menjalankan CPU dan Memory test bersamaan...")
    
    # Alokasi memori 100 MB
    data = bytearray(100 * 1024 * 1024)
    print(f"  → Alokasi 100 MB memori")
    
    # CPU intensive dengan memori terpakai
    cpu_intensive_task(duration=3)
    print_resource_info()
    
    # Cleanup
    del data
    
    print("\n" + "="*60)
    print("SEMUA TEST SELESAI")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()