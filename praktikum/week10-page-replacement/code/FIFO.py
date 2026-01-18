def fifo_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0
    hits = 0
    pointer = 0

    print("=== FIFO Page Replacement ===")
    for page in reference_string:
        if page in memory:
            hits += 1
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % frames

        print(f"Page {page} -> {memory} ({status})")

    print(f"\nTotal Page Faults (FIFO): {page_faults}")
    return page_faults


def lru_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0
    hits = 0

    print("\n=== LRU Page Replacement ===")
    for page in reference_string:
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        print(f"Page {page} -> {memory} ({status})")

    print(f"\nTotal Page Faults (LRU): {page_faults}")
    return page_faults


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    fifo_faults = fifo_page_replacement(reference_string, frames)
    lru_faults = lru_page_replacement(reference_string, frames)
