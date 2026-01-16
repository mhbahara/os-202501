import csv
import os

def load_processes(file_name):
    # Karena folder 'data' ada di dalam folder yang sama dengan 'utils.py'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, 'data', file_name)

    data = []
    if not os.path.exists(target_path):
        print(f"[DEBUG] File TIDAK ADA di: {target_path}")
        return data

    with open(target_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                data.append({
                    'ProcessID': row['ProcessID'],
                    'ArrivalTime': int(row['ArrivalTime']),
                    'BurstTime': int(row['BurstTime'])
                })
            except Exception as e:
                print(f"[ERROR] Data bermasalah: {e}")
    return data

def load_pages(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, 'data', file_name)

    if not os.path.exists(target_path):
        return []
    with open(target_path, mode='r') as file:
        content = file.read().strip()
        if not content: return []
        import re
        nums = re.split(r'[,\s\n]+', content)
        return [int(x) for x in nums if x.isdigit()]

if __name__ == "__main__":
    print("\n" + "="*40)
    print("=== DEBUGGING DATA ENGINEER (ANGGOTA 5) ===")
    
    # Menangani kemungkinan nama file double .csv.csv
    proses = load_processes("processes.csv")
    if not proses:
        proses = load_processes("processes.csv.csv")
        
    halaman = load_pages("pages.csv")
    if not halaman:
        halaman = load_pages("pages.csv.csv")
    
    if proses:
        print(f"-> BERHASIL! Ditemukan {len(proses)} proses.")
        for p in proses: print(f"   {p}")
    else:
        print("-> GAGAL: File tidak ditemukan di dalam folder data.")

    if halaman:
        print(f"-> BERHASIL! Data Pages: {halaman}")
    
    print("="*40)