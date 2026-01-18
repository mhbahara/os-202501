import csv

def simulasi_lru():
    frame = 3
    pages = []

    with open("data/aplikasi.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            pages.append(row["aplikasi"])

    memory = []
    page_fault = 0

    print("\n=== PAGE REPLACEMENT LRU - MEMORI LAPTOP ===")
    print("-" * 63)
    print(f"| {'Aplikasi':<10} | {'Isi RAM':<30} | {'Page Fault':<12} |")
    print("-" * 63)

    for p in pages:
        fault = "No"
        if p in memory:
            memory.remove(p)
            memory.append(p)
        else:
            page_fault += 1
            fault = "Yes"
            if len(memory) < frame:
                memory.append(p)
            else:
                memory.pop(0)
                memory.append(p)

        ram_str = ", ".join(memory)
        print(f"| {p:<10} | {ram_str:<30} | {fault:<12} |")

    print("-" * 63)
    print(f"\nTotal Page Fault : {page_fault}")
