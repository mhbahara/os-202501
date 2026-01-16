from tabulate import tabulate

def solve_lru(file_path, capacity=3):
    print(f"\n[INFO] Menjalankan Memory Management (LRU) - Frame: {capacity}")
    
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            # Handle pemisah spasi
            pages = content.split()
    except FileNotFoundError:
        print("Error: File dataset tidak ditemukan di folder data/.")
        return

    frames = []
    page_faults = 0
    history = []

    for page in pages:
        status = ""
        if page not in frames:
            status = "MISS"
            page_faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0) # Hapus elemen pertama (LRU)
                frames.append(page)
        else:
            status = "HIT"
            frames.remove(page)
            frames.append(page) # Pindah ke paling baru
        
        history.append([page, str(frames), status])

    hit_ratio = ((len(pages) - page_faults) / len(pages)) * 100
    
    print(tabulate(history, headers=["App Request", "RAM Frames", "Status"], tablefmt="simple"))
    print(f"\n> Total Requests : {len(pages)}")
    print(f"> Total Page Faults: {page_faults}")
    print(f"> Hit Ratio        : {hit_ratio:.2f}%")
