import os
import csv

def read_processes(filename):
    processes = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data', filename)

    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                processes.append({
                    'ProcessID': row['ProcessID'],
                    'ArrivalTime': int(row['ArrivalTime']),
                    'BurstTime': int(row['BurstTime'])
                })
        return processes
    except Exception as e:
        print(f"Error: {e}")
        return []

def fcfs_algorithm(data_proses):
    data_proses.sort(key=lambda x: x['ArrivalTime'])

    print("\n" + "="*55)
    print(f"{'ID':<10} | {'Arrival':<8} | {'Burst':<6} | {'Exit':<6}")
    print("-" * 55)

    current_time = 0
    for p in data_proses:
        if current_time < p['ArrivalTime']:
            current_time = p['ArrivalTime']
        
        start_time = current_time
        exit_time = start_time + p['BurstTime']
        
        print(f"{p['ProcessID']:<10} | {p['ArrivalTime']:<8} | {p['BurstTime']:<6} | {exit_time:<6}")
        
        current_time = exit_time
    print("="*55)