import time
import random
from prometheus_client import start_http_server, Summary, Counter, Gauge

# Membuat 3 metrik sesuai kriteria:
# 1. Counter: Menghitung total prediksi/request
REQUEST_COUNT = Counter('model_request_count', 'Total prediksi yang dilakukan')
# 2. Summary: Mengukur waktu yang dibutuhkan untuk prediksi (latensi)
MODEL_LATENCY = Summary('model_latency_seconds', 'Waktu yang dibutuhkan untuk prediksi')
# 3. Gauge: Mengukur fluktuasi akurasi model
MODEL_ACCURACY = Gauge('model_accuracy', 'Akurasi model saat ini')

def process_request():
    """Fungsi ini mensimulasikan sebuah request prediksi ke model"""
    REQUEST_COUNT.inc()
    time.sleep(random.uniform(0.1, 0.5)) # Simulasi waktu proses 0.1 - 0.5 detik
    MODEL_ACCURACY.set(random.uniform(0.85, 0.98)) # Simulasi akurasi 85% - 98%

if __name__ == '__main__':
    # Memulai server metrik di port 8000
    start_http_server(8000)
    print("Prometheus exporter berjalan di http://localhost:8000/metrics")
    
    # Loop untuk terus mengirimkan data metrik simulasi
    while True:
        with MODEL_LATENCY.time():
            process_request()
        time.sleep(2) # Kirim data metrik setiap 2 detik