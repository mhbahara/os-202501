import os
import csv
from tabulate import tabulate

def detect_deadlock(processes, allocation, request, available):
    finished = [False] * len(processes)
    work = available.copy()
    safe_sequence = []

    while True:
        found = False
        for i, proc in enumerate(processes):
            if not finished[i]:
                can_allocate = True
                for res in request[proc]:
                    if work.get(res, 0) < 1:
                        can_allocate = False
                        break
                if can_allocate:
                    for res in allocation[proc]:
                        work[res] += 1
                    finished[i] = True
                    safe_sequence.append(proc)
                    found = True
        if not found:
            break

    deadlocked_processes = [processes[i] for i in range(len(processes)) if not finished[i]]
    return len(deadlocked_processes) == 0, deadlocked_processes, safe_sequence

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, "dataset_deadlock.csv")

    processes = []
    allocation = {}
    request = {}
    resources = set()

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            proc = row['Proses']
            processes.append(proc)
            allocation[proc] = row['Allocation'].split(',') if row['Allocation'] else []
            request[proc] = row['Request'].split(',') if row['Request'] else []
            resources.update(allocation[proc])
            resources.update(request[proc])

    # otomatis: semua resource dianggap punya 1 instance
    total_resources = {res: 1 for res in resources}

    allocated_count = {res: 0 for res in total_resources}
    for alloc in allocation.values():
        for res in alloc:
            allocated_count[res] += 1
    available = {res: total_resources[res] - allocated_count[res] for res in total_resources}

    dataset_table = [[proc, ', '.join(allocation[proc]), ', '.join(request[proc])] for proc in processes]
    print("=== DATASET DEADLOCK ===")
    print(tabulate(dataset_table, headers=["Proses", "Allocation", "Request"], tablefmt="grid"))
    print(f"Available: {available}\n")

    is_safe, deadlocked, safe_seq = detect_deadlock(processes, allocation, request, available)

    result_table = [[proc, "Tidak Deadlock" if proc not in deadlocked else "Deadlock"] for proc in processes]
    print("=== HASIL DETEKSI DEADLOCK ===")
    print(tabulate(result_table, headers=["Proses", "Status"], tablefmt="grid"))

    if is_safe:
        print(f"\n>>> Sistem aman, tidak ada deadlock. Safe Sequence: {safe_seq}")
    else:
        print(f"\n>>> Deadlock terdeteksi! Proses yang terlibat: {deadlocked}")

if __name__ == "__main__":
    main()