import csv

def simulasi_kasir():
    nama = []
    waktu_layanan = []

    with open("pelanggan.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            nama.append(row["nama"])
            waktu_layanan.append(int(row["waktu_layanan"]))

    jumlah = len(nama)
    waktu_tunggu = [0] * jumlah
    waktu_selesai = [0] * jumlah

    for i in range(1, jumlah):
        waktu_tunggu[i] = waktu_tunggu[i - 1] + waktu_layanan[i - 1]

    for i in range(jumlah):
        waktu_selesai[i] = waktu_tunggu[i] + waktu_layanan[i]

    print("\n=== SIMULASI FCFS (KASIR) ===")
    print("-" * 51)
    print(f"| {'Nama':<10} | {'Waktu Layanan':<8} | {'Waktu Tunggu':<8} | {'Selesai':<8} |")
    print("-" * 51)

    for i in range(jumlah):
        print(f"| {nama[i]:<10} | {waktu_layanan[i]:<13} | {waktu_tunggu[i]:<12} | {waktu_selesai[i]:<8} |")

    print("-" * 51)

