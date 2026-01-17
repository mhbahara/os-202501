import csv

# Baca dataset
processes = []
allocation = {}
request = {}

with open("dataset_deadlock.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row["Process"]
        processes.append(p)
        allocation[p] = row["Allocation"]
        request[p] = row["Request"]

# Bangun graph wait-for
graph = {}
for p in processes:
    graph[p] = []

for p1 in processes:
    for p2 in processes:
        if request[p1] == allocation[p2]:
            graph[p1].append(p2)

# Deteksi cycle (DFS)
visited = set()
stack = set()
deadlock_processes = set()

def dfs(node):
    if node in stack:
        deadlock_processes.add(node)
        return True
    if node in visited:
        return False

    visited.add(node)
    stack.add(node)

    for neighbor in graph[node]:
        if dfs(neighbor):
            deadlock_processes.add(node)
            return True

    stack.remove(node)
    return False

for p in processes:
    if dfs(p):
        pass

# Output
print("=== HASIL DETEKSI DEADLOCK ===")
if deadlock_processes:
    print("Deadlock TERDETEKSI")
    print("Proses yang terlibat:")
    for p in sorted(deadlock_processes):
        print("-", p)
else:
    print("Tidak terjadi deadlock")