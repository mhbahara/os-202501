import csv

processes = []

with open("dataset.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # ⬅️ LEWATI HEADER

    for row in reader:
        pid = row[0]
        arrival = int(row[1])
        burst = int(row[2])
        processes.append([pid, arrival, burst])

# FCFS → urut berdasarkan arrival time
processes.sort(key=lambda x: x[1])

time = 0
total_wait = 0
total_tat = 0

print("Proses | Arrival | Burst | Waiting | Turnaround")
print("---------------------------------------------")

for p in processes:
    pid, arrival, burst = p

    if time < arrival:
        time = arrival

    waiting = time - arrival
    turnaround = waiting + burst

    time += burst

    total_wait += waiting
    total_tat += turnaround

    print(f"{pid:^6} | {arrival:^7} | {burst:^5} | {waiting:^7} | {turnaround:^10}")

n = len(processes)
print("---------------------------------------------")
print(f"Rata-rata Waiting Time   : {total_wait / n:.2f}")
print(f"Rata-rata Turnaround Time: {total_tat / n:.2f}")

