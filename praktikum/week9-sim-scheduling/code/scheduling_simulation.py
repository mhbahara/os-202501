import csv

# baca data dari CSV
processes = []
with open("dataset.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # lewati header

    for name, arrival, burst in reader:
        processes.append([name, int(arrival), int(burst)])

# urutkan berdasarkan arrival time (FCFS)
processes.sort(key=lambda x: x[1])

time = 0
total_wait = 0
total_turn = 0

print("\nHasil Simulasi FCFS")
print("Proses | Arrival | Burst | Waiting | Turnaround")
print("-" * 45)

for p in processes:
    if time < p[1]:
        time = p[1]

    waiting = time - p[1]
    turnaround = waiting + p[2]

    time += p[2]

    total_wait += waiting
    total_turn += turnaround

    print(f"{p[0]:6} | {p[1]:7} | {p[2]:5} | {waiting:7} | {turnaround:10}")

print("-" * 45)
print("Rata-rata Waiting Time   :", total_wait / len(processes))
print("Rata-rata Turnaround Time:", total_turn / len(processes))
