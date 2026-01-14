import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(BASE_DIR, "dataset_deadlock.csv")

proses = []
alokasi = {}
request = {}

# Baca dataset
try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            
            if line == "" or line.lower().startswith("proses"):
                continue

            p, a, r = line.split(",")
            proses.append(p)
            alokasi[p] = a
            request[p] = r

except FileNotFoundError:
    print("ERROR: File dataset_deadlock.csv tidak ditemukan!")
    print("Path dicari:", filename)
    exit()

# Deteksi circular wait (deadlock)
deadlock = set()

for p in proses:
    visited = set()
    current = p

    while current not in visited:
        visited.add(current)
        res_diminta = request[current]

        
        next_process = None
        for q in proses:
            if alokasi[q] == res_diminta:
                next_process = q
                break

        if next_process is None:
            break

        if next_process == p:
            deadlock.update(visited)
            break

        current = next_process

print("=== Data Proses ===")
print("Proses | Alokasi | Request")
print("---------------------------")
for p in proses:
    print(f"{p:5} | {alokasi[p]:7} | {request[p]}")

if deadlock:
    print("\nKondisi Sistem: DEADLOCK TERDETEKSI")
    print("Terlibat deadlock:", ", ".join(sorted(deadlock)))
else:
    print("\nKondisi Sistem: AMAN (Tidak ada deadlock)")
