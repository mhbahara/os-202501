import csv
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path_dataset = os.path.join(base_dir, 'dataset.csv')

proses_list = []

try:
    with open(path_dataset, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for baris in reader:
            proses_list.append({
                'id' : baris['Proses'],
                'at' : int(baris['Arrival_Time']), 
                'bt' : int(baris['Burst_Time']),
                'start' : 0,
                'finish' : 0,
                'tat' : 0,
                'wt' : 0
            })
except FileNotFoundError:
    print(f"ERROR: File tidak ditemukan di: {path_dataset}")
    exit()

proses_list.sort(key=lambda x: x['at'])
waktu_sekarang = 0

print("\n=== LOG EKSEKUSI FCFS ===")
for p in proses_list:
    if waktu_sekarang < p['at']:
        print(f"Waktu {waktu_sekarang:02d} - {p['at']:02d}: CPU Idle")
        waktu_sekarang = p['at']

    p['start'] = waktu_sekarang
    waktu_sekarang += p['bt']
    p['finish'] = waktu_sekarang

    p['tat'] = p['finish'] - p['at']
    p['wt'] = p['tat'] - p['bt']
    
    print(f"Waktu {p['start']:02d} - {p['finish']:02d}: {p['id']} Berjalan")

print(f"\n{'Proses':<7} | {'AT':<4} | {'BT':<4} | {'Mulai':<6} | {'Selesai':<8} | {'TAT':<5} | {'WT':<5}")
print("-" * 60)

for p in proses_list:
    print(f"{p['id']:<7} | {p['at']:<4} | {p['bt']:<4} | {p['start']:<6} | {p['finish']:<8} | {p['tat']:<5} | {p['wt']:<5}")

avg_tat = sum(p['tat'] for p in proses_list) / len(proses_list)
avg_wt = sum(p['wt'] for p in proses_list) / len(proses_list)

print("-" * 60)
print(f"Rata-rata Turnaround Time : {avg_tat:.2f} ms")
print(f"Rata-rata Waiting Time    : {avg_wt:.2f} ms\n")