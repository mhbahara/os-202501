import os

def load_reference_string(filename):
    """Membaca reference string dari file txt."""
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            # Menghapus spasi dan memisahkan berdasarkan koma
            pages = [int(x) for x in content.replace(' ', '').split(',')]
        return pages
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return []

def print_step(step, page, memory, status):
    """Fungsi helper untuk mencetak langkah simulasi."""
    # Formatting output agar rapi
    mem_str = str(memory).ljust(15) 
    print(f"Step {step:2d} | Page: {page} | Mem: {mem_str} | {status}")

def fifo_algorithm(pages, capacity):
    print(f"\n{'='*20} SIMULASI FIFO {'='*20}")
    print(f"Total Frames: {capacity}")
    print("-" * 60)
    
    memory = []
    page_faults = 0
    step = 1

    for page in pages:
        status = ""
        if page not in memory:
            status = "MISS (Fault)"
            page_faults += 1
            
            if len(memory) < capacity:
                memory.append(page)
            else:
                # FIFO: Hapus elemen pertama (index 0), masukkan baru di belakang
                memory.pop(0)
                memory.append(page)
        else:
            status = "HIT"
        
        print_step(step, page, memory, status)
        step += 1

    print("-" * 60)
    print(f"Total Page Faults (FIFO): {page_faults}")
    return page_faults

def lru_algorithm(pages, capacity):
    print(f"\n{'='*20} SIMULASI LRU  {'='*20}")
    print(f"Total Frames: {capacity}")
    print("-" * 60)
    
    memory = []
    page_faults = 0
    step = 1

    for page in pages:
        status = ""
        if page not in memory:
            status = "MISS (Fault)"
            page_faults += 1
            
            if len(memory) < capacity:
                memory.append(page)
            else:
                # LRU: Elemen di index 0 dianggap paling lama tidak dipakai
                memory.pop(0)
                memory.append(page)
        else:
            status = "HIT"
            # LRU Logic: Jika Hit, pindahkan page tersebut ke posisi paling belakang
            # (menandakan baru saja dipakai/most recently used)
            memory.remove(page)
            memory.append(page)
        
        print_step(step, page, memory, status)
        step += 1

    print("-" * 60)
    print(f"Total Page Faults (LRU): {page_faults}")
    return page_faults

def main():
    # Konfigurasi
    FILENAME = 'reference_string.txt'
    FRAMES = 3
    
    # Cek apakah file ada di direktori yang sama
    if not os.path.exists(FILENAME):
        # Fallback jika user lupa membuat file, gunakan data default soal
        print("File tidak ditemukan, menggunakan data default...")
        pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    else:
        pages = load_reference_string(FILENAME)

    if not pages:
        return

    print(f"Reference String: {pages}")
    
    # Jalankan Simulasi
    fifo_faults = fifo_algorithm(pages, FRAMES)
    lru_faults = lru_algorithm(pages, FRAMES)

    # Tampilkan Perbandingan Akhir
    print("\n" + "="*40)
    print("HASIL PERBANDINGAN AKHIR")
    print("="*40)
    print(f"{'Algoritma':<10} | {'Page Faults':<12} | {'Keterangan'}")
    print("-" * 40)
    
    diff = fifo_faults - lru_faults
    if diff > 0:
        note_lru = "Lebih Efisien"
        note_fifo = ""
    elif diff < 0:
        note_lru = ""
        note_fifo = "Lebih Efisien"
    else:
        note_lru = "Sama"
        note_fifo = "Sama"

    print(f"{'FIFO':<10} | {fifo_faults:<12} | {note_fifo}")
    print(f"{'LRU':<10} | {lru_faults:<12} | {note_lru}")
    print("="*40)

if __name__ == "__main__":
    main()