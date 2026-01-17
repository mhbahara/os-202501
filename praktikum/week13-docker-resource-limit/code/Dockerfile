# Menggunakan python versi ringan
FROM python:3.9-slim

# Set lokasi kerja di dalam container
WORKDIR /app

# Salin file app.py ke dalam container
COPY app.py .

# Jalankan skrip saat container dimulai
ENTRYPOINT ["python", "app.py"]
