# Simulasi Page Replacement
# Algoritma FIFO dan LRU

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3


def fifo(reference, frame_size):
    frames = []
    page_fault = 0

    print("FIFO")
    for page in reference:
        if page not in frames:
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        print(f"Page: {page} Frames: {frames}")

    return page_fault


def lru(reference, frame_size):
    frames = []
    page_fault = 0
    recent = []

    print("\nLRU")
    for page in reference:
        if page not in frames:
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                lru_page = recent.pop(0)
                frames.remove(lru_page)
                frames.append(page)
        else:
            recent.remove(page)

        recent.append(page)
        print(f"Page: {page} Frames: {frames}")

    return page_fault


fifo_fault = fifo(reference_string, frame_size)
lru_fault = lru(reference_string, frame_size)

print("\nTotal Page Fault")
print(f"FIFO: {fifo_fault}")
print(f"LRU : {lru_fault}")