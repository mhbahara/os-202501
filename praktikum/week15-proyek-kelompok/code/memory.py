import os

def run_fifo(page_reference, frame_count):
    """
    Simulasi Algoritma Page Replacement FIFO.
    """
    frames = []
    page_faults = 0
    hits = 0
    
    # Header Tabel
    print(f"\n{'='*45}")
    print(f" SIMULASI PAGE REPLACEMENT: FIFO ")
    print(f" Kapasitas Frame: {frame_count} ")
    print(f"{'='*45}")
    print(f"{'Step':<5} | {'Page':<5} | {'Current Frames':<18} | {'Status':<8}")
    print("-" * 45)

    for step, page in enumerate(page_reference, 1):
        status = ""
        if page not in frames:
            status = "FAULT"
            page_faults += 1
            # Logika FIFO: Jika penuh, hapus yang paling lama (indeks 0)
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames.pop(0) 
                frames.append(page)
        else:
            status = "HIT"
            hits += 1
        
        # Format tampilan frame agar rapi
        frame_display = str(frames)
        print(f"{step:<5} | {page:<5} | {frame_display:<18} | {status:<8}")

    # Perhitungan Metrik
    total_requests = len(page_reference)
    hit_ratio = (hits / total_requests) * 100 if total_requests > 0 else 0
    
    print("-" * 45)
    print(f"HASIL ANALISIS:")
    print(f"Total Page Faults : {page_faults}")
    print(f"Total Page Hits   : {hits}")
    print(f"Hit Ratio         : {hit_ratio:.2f}%")
    print(f"{'='*45}\n")
    
    return {"faults": page_faults, "hit_ratio": hit_ratio}

# Bagian ini hanya berjalan jika Master menjalankan file ini secara langsung (bukan di-import)
if __name__ == "__main__":
    # Contoh data simulasi
    example_pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
    example_capacity = 3
    
    run_fifo(example_pages, example_capacity)