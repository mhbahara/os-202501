import time

data = []
i = 0

print("Program berjalan...")
while True:
    for _ in range(10_000_000):
        pass

    data.append("X" * 10_000_000)
    i += 1
    print(f"Iterasi {i}, alokasi memori ~ {i * 10} MB")
    time.sleep(1)