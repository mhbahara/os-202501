# =====================================
# Simulasi Algoritma Page Replacement
# FIFO dan LRU
# =====================================

# Fungsi simulasi FIFO (First In First Out)
def fifo(reference, frame_size):
    frames = []            # Menyimpan halaman di memori
    page_fault = 0         # Menghitung jumlah page fault
    index = 0              # Penunjuk halaman yang akan diganti (FIFO)

    print("FIFO Simulation")

    # Membaca halaman satu per satu dari reference string
    for page in reference:
        # Jika halaman tidak ada di memori → page fault
        if page not in frames:
            page_fault += 1
            if len(frames) < frame_size:
                # Jika frame belum penuh, langsung tambahkan halaman
                frames.append(page)
            else:
                # Jika frame penuh, ganti halaman paling awal masuk
                frames[index] = page
                index = (index + 1) % frame_size
            status = "Fault"
        else:
            # Jika halaman sudah ada di memori → hit
            status = "Hit"

        print(f"Page: {page} | Frames: {frames} | {status}")

    return page_fault


# Fungsi simulasi LRU (Least Recently Used)
def lru(reference, frame_size):
    frames = []            # Menyimpan halaman di memori
    recent = {}            # Menyimpan waktu terakhir halaman digunakan
    page_fault = 0
    time = 0               # Penanda waktu akses halaman

    print("\nLRU Simulation")

    # Membaca halaman satu per satu dari reference string
    for page in reference:
        time += 1

        # Jika halaman tidak ada di memori → page fault
        if page not in frames:
            page_fault += 1
            if len(frames) < frame_size:
                # Jika frame belum penuh, langsung tambahkan halaman
                frames.append(page)
            else:
                # Mengganti halaman yang paling lama tidak digunakan
                lru_page = min(recent, key=recent.get)
                frames[frames.index(lru_page)] = page
                recent.pop(lru_page)
            status = "Fault"
        else:
            # Jika halaman sudah ada di memori → hit
            status = "Hit"

        # Memperbarui waktu terakhir halaman digunakan
        recent[page] = time
        print(f"Page: {page} | Frames: {frames} | {status}")

    return page_fault


# =====================================
# Program Utama
# =====================================
if __name__ == "__main__":
    # Reference string halaman
    reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

    # Jumlah frame memori
    frame_size = 3

    # Menjalankan simulasi FIFO dan LRU
    fifo_fault = fifo(reference, frame_size)
    lru_fault = lru(reference, frame_size)

    # Menampilkan ringkasan hasil simulasi
    print("\nRingkasan Hasil")
    print(f"FIFO Page Fault  : {fifo_fault}")
    print(f"LRU Page Fault   : {lru_fault}")