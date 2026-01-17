import csv

processes = []

# Menggunakan encoding utf-8-sig untuk menghindari karakter aneh di awal file
with open("dataset.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        processes.append({
            "process": row["Process"],
            "arrival": int(row["ArrivalTime"]),
            "burst": int(row["BurstTime"])
        })

# Sort berdasarkan Arrival Time (FCFS)
processes.sort(key=lambda x: x["arrival"])

current_time = 0
total_waiting_time = 0
total_turnaround_time = 0
gantt_chart = [] # Untuk menyimpan urutan proses
time_stamps = [0] # Untuk menyimpan penanda waktu

print("\nHasil Simulasi FCFS Scheduling")
print("Process | Arrival | Burst | Waiting | Turnaround")
print("-----------------------------------------------")

for p in processes:
    # Jika CPU idle (menunggu proses tiba)
    if current_time < p["arrival"]:
        gantt_chart.append("IDLE")
        current_time = p["arrival"]
        time_stamps.append(current_time)

    waiting = current_time - p["arrival"]
    turnaround = waiting + p["burst"]

    print(f"{p['process']:>7} | {p['arrival']:>7} | {p['burst']:>5} | {waiting:>7} | {turnaround:>10}")

    total_waiting_time += waiting
    total_turnaround_time += turnaround
    
    # Tambahkan ke Gantt Chart
    gantt_chart.append(p['process'])
    current_time += p["burst"]
    time_stamps.append(current_time)

n = len(processes)
print("-----------------------------------------------")
print(f"Average Waiting Time    : {total_waiting_time / n:.2f}")
print(f"Average Turnaround Time : {total_turnaround_time / n:.2f}")

# --- VISUALISASI GANTT CHART ---
print("\nVisualisasi Gantt Chart:")
print("-" * (len(gantt_chart) * 8))

# Baris Nama Proses
chart_row = "|"
for p in gantt_chart:
    chart_row += f"  {p}  |"
print(chart_row)

print("-" * (len(gantt_chart) * 8))

# Baris Penanda Waktu
time_row = ""
for t in time_stamps:
    time_row += f"{t:<7}"
print(time_row)