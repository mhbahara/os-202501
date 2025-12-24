import csv

# =====================================
# Membaca dataset dari file CSV
# =====================================
def load_dataset(nama_file):
    daftar_proses = []

    with open(nama_file, newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            daftar_proses.append({
                "proses": row["Proses"],
                "arrival": int(row["Arrival Time"]),
                "burst": int(row["Burst Time"])
            })

    return daftar_proses


# =====================================
# Algoritma First Come First Served (FCFS)
# =====================================
def fcfs(proses_list):
    waktu = 0
    hasil = []

    for p in sorted(proses_list, key=lambda x: x["arrival"]):
        if waktu < p["arrival"]:
            waktu = p["arrival"]

        waktu_tunggu = waktu - p["arrival"]
        waktu_selesai = waktu_tunggu + p["burst"]
        waktu += p["burst"]

        hasil.append({
            "proses": p["proses"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "waiting": waktu_tunggu,
            "turnaround": waktu_selesai
        })

    return hasil


# =====================================
# Algoritma Shortest Job First (Non-Preemptive)
# =====================================
def sjf(proses_list):
    waktu = 0
    selesai = []
    antrian = proses_list.copy()

    while antrian:
        tersedia = [p for p in antrian if p["arrival"] <= waktu]

        if not tersedia:
            waktu += 1
            continue

        terpendek = min(tersedia, key=lambda x: x["burst"])
        antrian.remove(terpendek)

        waktu_tunggu = waktu - terpendek["arrival"]
        waktu_selesai = waktu_tunggu + terpendek["burst"]
        waktu += terpendek["burst"]

        selesai.append({
            "proses": terpendek["proses"],
            "arrival": terpendek["arrival"],
            "burst": terpendek["burst"],
            "waiting": waktu_tunggu,
            "turnaround": waktu_selesai
        })

    return selesai


# =====================================
# Menghitung rata-rata Waiting & Turnaround
# =====================================
def hitung_rata_rata(data):
    total_waiting = sum(p["waiting"] for p in data)
    total_turnaround = sum(p["turnaround"] for p in data)

    rata_waiting = total_waiting / len(data)
    rata_turnaround = total_turnaround / len(data)

    return rata_waiting, rata_turnaround


# =====================================
# Menampilkan hasil simulasi
# =====================================
def tampilkan_hasil(judul, data):
    print(f"\n=== {judul} ===")
    print("Proses | Arrival | Burst | Waiting | Turnaround")
    print("-" * 55)

    for p in data:
        print(f"{p['proses']:>6} | {p['arrival']:>7} | {p['burst']:>5} |"
              f" {p['waiting']:>7} | {p['turnaround']:>10}")

    rata_wt, rata_tat = hitung_rata_rata(data)

    print("-" * 55)
    print(f"Rata-rata Waiting Time    : {rata_wt:.2f}")
    print(f"Rata-rata Turnaround Time : {rata_tat:.2f}")


# =====================================
# Program Utama
# =====================================
if __name__ == "__main__":
    dataset = load_dataset("dataset.csv")
    

    hasil_fcfs = fcfs(dataset)
    hasil_sjf = sjf(dataset)

    tampilkan_hasil("Simulasi FCFS", hasil_fcfs)
    tampilkan_hasil("Simulasi SJF Non-Preemptive", hasil_sjf)
