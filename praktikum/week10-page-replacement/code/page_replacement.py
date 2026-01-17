def fifo(reference, frame_count):
    frames = []
    pointer = 0
    faults = 0

    print("=== FIFO Page Replacement ===")
    for page in reference:
        if page not in frames:
            faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frame_count
            status = "Fault"
        else:
            status = "Hit"

        print(f"Page: {page} -> Frames: {frames} ({status})")

    print("\n=== HASIL FIFO ===")
    print(f"Total Page Fault FIFO: {faults}\n")
    return faults


def lru(reference, frame_count):
    frames = []
    history = []
    faults = 0

    print("=== LRU Page Replacement ===")
    for page in reference:
        if page in frames:
            history.remove(page)
            history.append(page)
            status = "Hit"
        else:
            faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                old = history.pop(0)
                frames[frames.index(old)] = page
            history.append(page)
            status = "Fault"

        print(f"Page: {page} -> Frames: {frames} ({status})")

    print("\n=== HASIL LRU ===")
    print(f"Total Page Fault LRU : {faults}\n")
    return faults


# ================= MAIN =================

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 3

fifo_faults = fifo(reference_string, frame_count)
lru_faults = lru(reference_string, frame_count)
