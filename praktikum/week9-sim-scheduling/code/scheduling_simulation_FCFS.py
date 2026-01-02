```bash
def main():
    # ---  DATASET  ---
    proses_list = [
        {'id': 'P1', 'arrival': 0, 'burst': 6},
        {'id': 'P2', 'arrival': 1, 'burst': 8},
        {'id': 'P3', 'arrival': 2, 'burst': 7},
        {'id': 'P4', 'arrival': 3, 'burst': 3}
    ]

    # --- 2. LOGIKA FCFS (First-Come First-Served) ---
    # Urutkan berdasarkan waktu datang (Arrival Time) biar aman
    proses_list.sort(key=lambda x: x['arrival'])

    waktu_sekarang = 0
    total_waiting = 0
    total_turnaround = 0

    print("\n=== SIMULASI CPU SCHEDULING (FCFS) ===")
    print(f"{'Proses':<8} {'Arrival':<8} {'Burst':<8} {'Waiting':<8} {'Turnaround':<10}")
    print("-" * 50)

    for p in proses_list:
        # Cek apakah CPU harus menunggu proses datang (Idle time)
        if waktu_sekarang < p['arrival']:
            waktu_sekarang = p['arrival']

        # Proses dimulai & selesai
        start_time = waktu_sekarang
        finish_time = start_time + p['burst']

        # Hitung Metrics
        turnaround = finish_time - p['arrival']
        waiting = turnaround - p['burst']

        # Akumulasi untuk rata-rata
        total_waiting += waiting
        total_turnaround += turnaround
        
        # Update waktu sistem
        waktu_sekarang = finish_time

        # Tampilkan baris data
        print(f"{p['id']:<8} {p['arrival']:<8} {p['burst']:<8} {waiting:<8} {turnaround:<10}")

    # --- 3. HASIL AKHIR ---
    rata_waiting = total_waiting / len(proses_list)
    rata_turnaround = total_turnaround / len(proses_list)

    print("-" * 50)
    print(f"Rata-rata Waiting Time    : {rata_waiting:.2f} ms")
    print(f"Rata-rata Turnaround Time : {rata_turnaround:.2f} ms")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
```
