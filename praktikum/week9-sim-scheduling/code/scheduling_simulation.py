import csv

# PATH ABSOLUT DATASET (PAKAI PATH KAMU)
path = r"C:\praktikum\os-202501-250202938\praktikum\week9-sim-scheduling\code\dataset.csv"

processes = []
with open(path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pid = row["Proses"]
        arrival = int(row["Arrival Time"])
        burst = int(row["Burst Time"])
        processes.append([pid, arrival, burst])

# FCFS
processes.sort(key=lambda x: x[1])

time = 0
total_wait = 0
total_turn = 0

print("Proses\tArrival\tBurst\tWaiting\tTurnaround")

for p in processes:
    pid, arrival, burst = p

    if time < arrival:
        time = arrival

    waiting = time - arrival
    time += burst
    turnaround = time - arrival

    total_wait += waiting
    total_turn += turnaround

    print(f"{pid}\t{arrival}\t{burst}\t{waiting}\t{turnaround}")

n = len(processes)
print("\nRata-rata Waiting Time    :", total_wait / n)
print("Rata-rata Turnaround Time :", total_turn / n)