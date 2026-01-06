import csv

# =====================================
# Membaca dataset deadlock dari CSV
# =====================================
def load_dataset(filename):
    processes = []

    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes.append({
                "process": row["Proses"],
                "alloc": row["Allocation"],
                "req": row["Request"]
            })

    return processes


# =====================================
# Menampilkan tabel data proses
# =====================================
def tampilkan_tabel_proses(processes):
    print("\nTabel Data Proses")
    print("Proses | Allocation | Request")
    print("-" * 30)

    for p in processes:
        print(f"{p['process']:<6} | {p['alloc']:<10} | {p['req']}")


# =====================================
# Deteksi deadlock + ambil siklus
# =====================================
def detect_deadlock(processes):
    allocation_map = {p["alloc"]: p["process"] for p in processes}
    graph = {}

    for p in processes:
        if p["req"] in allocation_map:
            graph[p["process"]] = allocation_map[p["req"]]

    for start in graph:
        path = []
        current = start

        while current in graph:
            if current in path:
                cycle = path[path.index(current):] + [current]
                return cycle
            path.append(current)
            current = graph[current]

    return None


# =====================================
# Menampilkan hasil deteksi deadlock
# =====================================
def tampilkan_hasil(processes, cycle):
    print("\nHasil Deteksi Deadlock")

    if cycle:
        print("Status Sistem : DEADLOCK\n")

        print("Tabel Status Proses")
        print("Proses | Status")
        print("-" * 20)

        for p in processes:
            status = "Deadlock" if p["process"] in cycle else "Aman"
            print(f"{p['process']:<6} | {status}")

        print("\nSiklus Deadlock:")
        print(" → ".join(cycle))

    else:
        print("Status Sistem : TIDAK DEADLOCK")


# =====================================
# Program Utama
# =====================================
if __name__ == "__main__":
    data = load_dataset("dataset_deadlock.csv")

    tampilkan_tabel_proses(data)

    cycle = detect_deadlock(data)

    tampilkan_hasil(data, cycle)