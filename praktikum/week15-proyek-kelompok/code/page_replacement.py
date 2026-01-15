import os
from collections import deque


def fifo(reference, frame_count):
    frames = []
    queue = deque()
    page_fault = 0
    page_hit = 0
    table = []

    for page in reference:
        if page in frames:
            status = "HIT"
            page_hit += 1
        else:
            status = "FAULT"
            page_fault += 1

            if len(frames) < frame_count:
                frames.append(page)
                queue.append(page)
            else:
                old = queue.popleft()
                idx = frames.index(old)
                frames[idx] = page
                queue.append(page)

        table.append((page, frames.copy(), status))

    return page_fault, page_hit, table


def print_table(title, table, frame_count):
    print(f"\n{title}")
    print("-" * 50)
    header = "Page\t" + "\t".join([f"F{i+1}" for i in range(frame_count)]) + "\tStatus"
    print(header)
    print("-" * 50)

    for page, frames, status in table:
        row = f"{page}\t"
        for i in range(frame_count):
            row += f"{frames[i] if i < len(frames) else '-'}\t"
        row += status
        print(row)



def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "reference_string.txt")

    with open(file_path, "r") as file:
        reference = list(map(int, file.read().split(",")))

    frame_count = 3

    fifo_fault, fifo_hits, fifo_table = fifo(reference, frame_count)
   
    total_references = len(reference)
    hit_ratio = (fifo_hits / total_references) * 100

    print_table("FIFO Page Replacement", fifo_table, frame_count)
    print(f"\nTotal Page Fault: {fifo_fault}")
    print(f"\nTOtal Page Hit: {fifo_hits}")
    print(f"\nHit Ratio: {hit_ratio}%")

if __name__ == "__main__":
    main()


