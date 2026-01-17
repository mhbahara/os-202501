import sys
import time

def jalankan_tes():
    # Mengambil mode (cpu/mem) dari perintah terminal
    mode = sys.argv[1].lower() if len(sys.argv) > 1 else "cpu"
    
    print("\n" + "="*50)
    print(f"    PENGUJIAN RESOURCE DOCKER: {mode.upper()}")
    print("="*50)

    if mode == "cpu":
        print(f"{'Waktu':<10} | {'Total Iterasi CPU':<20} | {'Status'}")
        print("-" * 50)
        
        iterasi = 0
        start_time = time.time()
        last_report = time.time()
        
        try:
            while True:
                # Operasi beban CPU
                _ = 500 * 500
                iterasi += 1
                
                # Tampilkan output setiap 1 detik agar perubahan terlihat jelas
                curr_time = time.time()
                if curr_time - last_report >= 1:
                    durasi = int(curr_time - start_time)
                    print(f"{durasi:>3} detik  | {iterasi:>20,} | Running...")
                    last_report = curr_time
        except KeyboardInterrupt:
            print("\n[!] Pengujian CPU dihentikan manual.")

    elif mode == "mem":
        print(f"{'Waktu':<10} | {'Penggunaan RAM':<20} | {'Visual'}")
        print("-" * 50)
        
        data = []
        start_time = time.time()
        try:
            while True:
                # Tambah 20MB tiap detik
                data.append(bytearray(20 * 1024 * 1024))
                total_mb = len(data) * 20
                durasi = int(time.time() - start_time)
                
                # Visualisasi bar sederhana
                bar = "█" * (total_mb // 20)
                print(f"{durasi:>3} detik  | {total_mb:>17} MB | {bar}")
                
                time.sleep(1)
        except:
            # Jika limit memory tersentuh, Docker akan mematikan container
            print("\n" + "!"*50)
            print(" [!!!] KILLED: PENGGUNAAN MEMORI MELEBIHI LIMIT")
            print("!"*50)

if __name__ == "__main__":
    jalankan_tes()
