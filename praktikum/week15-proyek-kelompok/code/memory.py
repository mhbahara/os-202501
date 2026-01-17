from collections import deque

def fifo_algorithm(pages, capacity=3):
    """
    Simulasi algoritma FIFO (First-In-First-Out) untuk Page Replacement.
    """
    memory = deque(maxlen=capacity)
    page_faults = 0
    
    print(f"\n[Konfigurasi: Kapasitas Frame = {capacity}]")
    print(f"{'Step':<5} | {'Page':<5} | {'Memory Frame':<20} | {'Status'}")
    print("-" * 60)

    for step, page in enumerate(pages, 1):
        if page in memory:
            status = "HIT"
        else:
            status = "MISS (Fault)"
            page_faults += 1
            memory.append(page)
        
        # Konversi deque ke list untuk tampilan yang rapi
        mem_display = list(memory)
        print(f"{step:<5} | {page:<5} | {str(mem_display):<20} | {status}")

    total = len(pages)
    hits = total - page_faults
    hit_ratio = (hits / total) * 100

    print("-" * 60)
    print(f"Ringkasan Eksekusi:")
    print(f" - Total Page Faults : {page_faults}")
    print(f" - Total Page Hits   : {hits}")
    print(f" - Hit Ratio         : {hit_ratio:.2f}%")

if __name__ == "__main__":
    # Data input
    referensi_halaman = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
    kapasitas_frame = 3
    
    fifo_algorithm(referensi_halaman, kapasitas_frame)