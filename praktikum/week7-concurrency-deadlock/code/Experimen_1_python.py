import threading
import time

N = 5  
forks = [threading.Lock() for _ in range(N)]

def philosopher(i):
    while True:
        print(f"Filosof {i} sedang berpikir...")
        time.sleep(1)

        forks[i].acquire()
        print(f"Filosof {i} mengambil garpu kiri {i}")

        forks[(i+1) % N].acquire()
        print(f"Filosof {i} mengambil garpu kanan {(i+1)%N}")

        print(f"Filosof {i} sedang makan...")
        time.sleep(2)

        forks[i].release()
        forks[(i+1) % N].release()
        print(f"Filosof {i} selesai makan dan meletakkan garpu")

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
