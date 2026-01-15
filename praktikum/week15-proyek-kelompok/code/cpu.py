from tabulate import tabulate

def solve_fcfs(file_path):
    print(f"\n[INFO] Menjalankan CPU Scheduling (FCFS) dengan data: {file_path}")
    
    processes = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                # Format: NamaProses, Arrival, Burst
                processes.append({
                    'pid': parts[0], 
                    'at': int(parts[1]), 
                    'bt': int(parts[2])
                })
    except FileNotFoundError:
        print("Error: File dataset tidak ditemukan di folder data/.")
        return

    # Sort berdasarkan Arrival Time
    processes.sort(key=lambda x: x['at'])

    current_time = 0
    total_wt = 0
    total_tat = 0
    results = []

    for p in processes:
        if current_time < p['at']:
            current_time = p['at']
        
        start_time = current_time
        completion_time = start_time + p['bt']
        turnaround_time = completion_time - p['at']
        waiting_time = turnaround_time - p['bt']
        
        current_time = completion_time
        total_wt += waiting_time
        total_tat += turnaround_time
        
        results.append([p['pid'], p['at'], p['bt'], completion_time, turnaround_time, waiting_time])

    # Output Tabel
    headers = ["Process", "Arrival", "Burst", "Finish", "Turnaround", "Waiting"]
    print(tabulate(results, headers=headers, tablefmt="fancy_grid"))
    
    print(f"\n> Rata-rata Turnaround Time : {total_tat / len(processes):.2f} ms")
    print(f"> Rata-rata Waiting Time    : {total_wt / len(processes):.2f} ms")
