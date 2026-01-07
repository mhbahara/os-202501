processes = ["P1", "P2", "P3"]

wait_for = {
    "P1": "P2",
    "P2": "P3",
    "P3": "P1"
}

deadlock = False

for p in processes:
    visited = set()
    while p not in visited:
        visited.add(p)
        if p not in wait_for:
            break
        p = wait_for[p]
    else:
        deadlock = True
        break

print("HASIL DETEKSI DEADLOCK")
print("-" * 45)
print(f"| {'Proses':^10} | {'Menunggu':^12} | {'Status':^12} |")
print("-" * 45)

for p in processes:
    status = "Deadlock" if deadlock else "Aman"
    print(f"| {p:^10} | {wait_for[p]:^12} | {status:^12} |")

print("-" * 45)
print("Status Sistem : DEADLOCK TERDETEKSI")
