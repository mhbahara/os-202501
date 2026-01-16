# Gunakan image dasar Python yang ringan
FROM python:3.9-slim

# Set folder kerja di dalam container menjadi /app
WORKDIR /app

# Copy file app.py dari komputer ke dalam container
COPY app.py .

# Perintah yang dijalankan saat container start
CMD ["python", "app.py"]