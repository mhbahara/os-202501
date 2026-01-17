import csv
import time
from colorama import Fore, Style, init
init(autoreset=True)

# ===============================
# Membaca Dataset
# ===============================
def baca_data_gudang(nama_file):
    data = []
    with open(nama_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


# ===============================
# Pengecekan Deadlock (Circular Wait)
# ===============================
def cek_deadlock(peta_tunggu):
    sudah_dicek = set()

    for f in peta_tunggu:
        jalur = f
        rantai = []

        while jalur not in sudah_dicek:
            sudah_dicek.add(jalur)
            rantai.append(jalur)

            if jalur not in peta_tunggu:
                break

            jalur = peta_tunggu[jalur]

            # Jika kembali ke awal → DEADLOCK
            if jalur == f:
                return True, rantai

    return False, []


# ===============================
# Simulasi Deteksi Deadlock
# ===============================
def simulasi_deteksi():
    catatan = baca_data_gudang("dataset_forklift.csv")

    print(Fore.CYAN + "\nSISTEM MONITORING GUDANG OTOMATIS\n")

    # Mapping Gate yang sedang ditempati siapa
    posisi_gate = {row['Gate_Current']: row['Forklift'] for row in catatan}

    peta_tunggu = {}
    print(Fore.YELLOW + "[!] Sistem memantau pergerakan Forklift:\n")

    for row in catatan:
        forklift = row['Forklift']
        gate_asal = row['Gate_Current']
        gate_tujuan = row['Gate_Target']

        print(f"{Fore.WHITE}{forklift} berada di {Fore.GREEN}{gate_asal} "
              f"{Fore.WHITE}ingin pindah ke {Fore.BLUE}{gate_tujuan}")

        if gate_tujuan in posisi_gate:
            penghalang = posisi_gate[gate_tujuan]
            peta_tunggu[forklift] = penghalang
            print(f"   {Fore.RED}>> Tertahan! {gate_tujuan} sedang dipakai {Fore.MAGENTA}{penghalang}")
        else:
            print(f"   {Fore.GREEN}>> Gate tujuan kosong, aman.")

        time.sleep(0.5)

    print(Fore.YELLOW + "\n[!] Sistem menganalisis potensi deadlock...")

    status, rantai = cek_deadlock(peta_tunggu)

    print("\nKESIMPULAN SISTEM:")
    if status:
        print(Fore.WHITE + "STATUS: " + Fore.RED + "TERDETEKSI DEADLOCK")
        print(Fore.WHITE + "Forklift yang saling mengunci: " + Fore.MAGENTA + ", ".join(rantai))
        print(Fore.YELLOW + "Tindakan: Supervisor perlu mengeluarkan salah satu forklift agar alur terbuka.")
    else:
        print(Fore.GREEN + "STATUS: TIDAK ADA DEADLOCK")
        print("Semua forklift dapat bergerak tanpa saling mengunci.")


# ===============================
# Main
# ===============================
if __name__ == "__main__":
    simulasi_deteksi()





import csv
import time

# ===============================
# Membaca Dataset Gudang
# ===============================
def baca_data_gudang(nama_file):
    data = []
    with open(nama_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


# ===============================
# Cek Circular Deadlock
# ===============================
def cek_deadlock(peta_tunggu):
    sudah_dicek = set()

    for f in peta_tunggu:
        jalur = f
        rantai = []

        while jalur not in sudah_dicek:
            sudah_dicek.add(jalur)
            rantai.append(jalur)

            if jalur not in peta_tunggu:
                break

            jalur = peta_tunggu[jalur]

            if jalur == f:
                return True, rantai

    return False, []


# ===============================
# Proses Recovery Deadlock
# ===============================
def recovery_deadlock():
    data = baca_data_gudang("dataset_forklift.csv")

    print("\nSISTEM PEMULIHAN KEMACETAN GUDANG (DEADLOCK RECOVERY)")
    print("=====================================================\n")

    posisi_gate = {row['Gate_Current']: row['Forklift'] for row in data}
    peta_tunggu = {}

    for row in data:
        forklift = row["Forklift"]
        gate_tujuan = row["Gate_Target"]

        if gate_tujuan in posisi_gate:
            peta_tunggu[forklift] = posisi_gate[gate_tujuan]

    status, rantai = cek_deadlock(peta_tunggu)

    if not status:
        print("Status: Tidak ada deadlock. Semua forklift aman bergerak.")
        return

    print(f"[!] Deadlock terdeteksi melibatkan: {', '.join(rantai)}\n")

    # Pilih forklift pertama untuk dikeluarkan
    forklift_dikeluarkan = rantai[0]

    print(f"Langkah Pemulihan:")
    print(f"- Supervisor memutuskan untuk mengeluarkan {forklift_dikeluarkan} dari area gate...")
    time.sleep(1)
    print(f"- {forklift_dikeluarkan} dipindahkan secara manual keluar jalur.")
    time.sleep(1)

    print("\nHasil Setelah Recovery:")
    print("- Rantai tunggu terputus.")
    print("- Forklift lain kini dapat bergerak normal.")
    print("\nKESIMPULAN: Deadlock berhasil diatasi. Gudang kembali beroperasi normal.")


# ===============================
# Main Program
# ===============================
if __name__ == "__main__":
    recovery_deadlock()
