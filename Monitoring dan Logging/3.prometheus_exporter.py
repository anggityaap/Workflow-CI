from flask import Flask, request, jsonify, Response
import time
import psutil  # Pastikan library ini sudah terinstal (pip install psutil)
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Metrik untuk API model
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')  # Total request yang diterima
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP Request Latency')  # Waktu respons API
THROUGHPUT = Counter('http_requests_throughput', 'Total number of requests per second')  # Throughput

# Metrik untuk sistem
CPU_USAGE = Gauge('system_cpu_usage', 'CPU Usage Percentage')  # Penggunaan CPU
RAM_USAGE = Gauge('system_ram_usage', 'RAM Usage Percentage')  # Penggunaan RAM

# Endpoint untuk Prometheus mengambil (scrape) metrik
@app.route('/metrics', methods=['GET'])
def metrics():
    # Update metrik sistem secara real-time
    CPU_USAGE.set(psutil.cpu_percent())
    RAM_USAGE.set(psutil.virtual_memory().percent)
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Endpoint simulasi untuk menerima request prediksi
@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    
    # Mencatat request masuk
    REQUEST_COUNT.inc()
    THROUGHPUT.inc()
    
    # (Di sini biasanya adalah proses model ML Anda bekerja)
    time.sleep(0.1) # Simulasi waktu proses model
    
    # Mencatat latensi (waktu respons)
    latency = time.time() - start_time
    REQUEST_LATENCY.observe(latency)
    
    return jsonify({"status": "success", "message": "Prediksi berhasil"})

if __name__ == '__main__':
    # Menjalankan servis di port 8000
    app.run(host='127.0.0.1', port=8000)