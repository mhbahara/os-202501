def simulasi_fifo_game(daftar_klik_game, kapasitas_ram=3):
    memori_ram = []
    page_faults = 0
    
    print(f"\nKapasitas RAM HP: {kapasitas_ram} Slot Game")
    print(f"{'Step':<5} | {'Game Dibuka':<15} | {'Isi RAM Sekarang':<45} | {'Status'}")
    print("-" * 90)

    for step, game in enumerate(daftar_klik_game, 1):
        status = ""
        # 1. Cek: Apakah game sudah ada di RAM?
        if game not in memori_ram:
            page_faults += 1
            status = "MISS (Loading Ulang)"
            
            # 2. Jika RAM Penuh (3 slot terisi)
            if len(memori_ram) >= kapasitas_ram:
                # 3. FIFO: Tendang game yang pertama kali masuk (index 0)
                game_dibuang = memori_ram.pop(0) 
                memori_ram.append(game)
                status += f" -> {game_dibuang} DIBUANG"
            else:
                # Jika masih ada slot kosong
                memori_ram.append(game)
        else:
            # 4. Jika game sudah ada di RAM (HIT)
            status = "HIT (Lancar)"
        
        print(f"{step:<5} | {game:<15} | {str(memori_ram):<45} | {status}")

    # Statistik Performa HP Master
    total = len(daftar_klik_game)
    hits = total - page_faults
    print("-" * 90)
    print(f"Hasil Akhir: HP Anda mengalami {page_faults} kali loading ulang dan {hits} kali lancar.")
    print(f"Skor Kelancaran (Hit Ratio): {(hits/total)*100:.2f}%")

# Data dari file pages.csv Master
urutan_game = ["PUBG", "Delta Force", "Arena Breakout", "War Thunder", "PUBG", "Delta Force", "War Thunder"]

# Jalankan!
simulasi_fifo_game(urutan_game)
