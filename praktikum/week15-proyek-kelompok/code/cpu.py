import os
from tabulate import tabulate

def solve_fcfs(file_path):
    print(f"\n[INFO] Menjalankan CPU Scheduling (FCFS)...")
    
    # Cek file dulu
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' tidak ditemukan!")
        print(f"Posisi folder saat ini: {os.getcwd()}")
        return

    processes = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Bersihkan spasi dan enter
                clean_line = line.strip()
                # Jika baris kosong, lewati (biar gak error)
                if not clean_line:
                    continue
                
                parts = clean_line.split(',')
                # Pastikan ada 3 kolom (Nama, Arrival, Burst)
                if len(parts) == 3:
                    processes.append({
                        'pid': parts[0], 
                        'at': int(parts[1]), 
                        'bt': int(parts[2])
                    })
    except Exception as e:
        print(f"Error saat membaca file: {e}")
        return

    if not processes:
        print("Error: Data kosong atau format salah!")
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
    print(tabulate(results, headers=["Process", "Arrival", "Burst", "Finish", "Turnaround", "Waiting"], tablefmt="fancy_grid"))
    
    print(f"\n> Rata-rata Turnaround Time : {total_tat / len(processes):.2f} ms")
    print(f"> Rata-rata Waiting Time    : {total_wt / len(processes):.2f} ms")
