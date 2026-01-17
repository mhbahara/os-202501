reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3


def print_process_table(title, steps):
    print(f"\n{title}")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")
    print("| Page   | Frame 1  | Frame 2  | Frame 3  | Status   |")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")
    
    for page, mem, status in steps:
        print(f"| {page:<6} | {mem[0]:<8} | {mem[1]:<8} | {mem[2]:<8} | {status:<8} |")
    
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")


# ================= FIFO =================
def fifo_page_replacement(ref, frames):
    memory = ['-'] * frames
    fifo_index = 0
    steps = []
    page_fault = 0

    for page in ref:
        if page in memory:
            steps.append((page, memory.copy(), "HIT"))
        else:
            page_fault += 1
            memory[fifo_index] = page
            fifo_index = (fifo_index + 1) % frames
            steps.append((page, memory.copy(), "FAULT"))

    return page_fault, steps


# ================= LRU =================
def lru_page_replacement(ref, frames):
    memory = ['-'] * frames
    last_used = {}
    steps = []
    page_fault = 0

    for time, page in enumerate(ref):
        if page in memory:
            steps.append((page, memory.copy(), "HIT"))
        else:
            page_fault += 1
            if '-' in memory:
                index = memory.index('-')
            else:
                lru_page = min(last_used, key=last_used.get)
                index = memory.index(lru_page)
                del last_used[lru_page]

            memory[index] = page
            steps.append((page, memory.copy(), "FAULT"))

        last_used[page] = time

    return page_fault, steps


# ================= EKSEKUSI =================
fifo_fault, fifo_steps = fifo_page_replacement(reference_string, frames)
lru_fault, lru_steps = lru_page_replacement(reference_string, frames)

print_process_table("PROSES FIFO (First-In First-Out)", fifo_steps)
print_process_table("PROSES LRU (Least Recently Used)", lru_steps)

# ================= RINGKASAN =================
print("\nRINGKASAN HASIL AKHIR")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
print("| Algoritma | Jumlah Frame | Page Fault   |")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
print(f"| FIFO      | {frames:^12} | {fifo_fault:^12} |")
print(f"| LRU       | {frames:^12} | {lru_fault:^12} |")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
