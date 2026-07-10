# Cara Menjalankan Project

Ikuti langkah-langkah di bawah ini untuk menjalankan MLflow server dan script pelatihan model:

## 1. Menjalankan MLflow Server
Server MLflow harus berjalan agar metrik dan model dapat dicatat. Jalankan perintah berikut di terminal:
```powershell
mlflow server --host 127.0.0.1 --port 5000
```
*Biarkan terminal ini tetap terbuka selama proses pelatihan.*

## 2. Menjalankan Pelatihan Model
Buka terminal baru (atau tab baru), lalu jalankan perintah berikut secara berurutan untuk masuk ke direktori model dan mengeksekusi script:

```powershell
# Masuk ke folder model
cd Membangun_model

# Mengaktifkan mode UTF-8 agar tidak error Unicode/Emoji di Windows Powershell
$env:PYTHONUTF8=1

# Menjalankan script modelling
python modelling.py
```





Jika komputer Anda di-restart, semua terminal yang sedang berjalan di latar belakang akan tertutup secara otomatis. Untuk melanjutkan pekerjaan atau menguji kembali sistem Anda, ada 4 layanan (services) yang perlu Anda jalankan ulang di terminal atau jendela yang berbeda-beda.
Berikut adalah daftar layanan, lokasi path (folder), dan perintah yang harus dijalankan:
1. MLflow Model Serving Layanan ini untuk menyalakan model Anda sebagai API agar bisa menerima data prediksi.
Path/Folder: C:\laragon\www\Eksperimen_SML_anggitya-ayu-pertiwi\Membangun_model
Perintah di Terminal:
2. Prometheus Exporter (Script Pembuat Metrik Python) Layanan ini untuk menghasilkan simulasi metrik (akurasi, latensi, jumlah request) agar bisa dibaca oleh Prometheus.
Path/Folder: C:\laragon\www\Eksperimen_SML_anggitya-ayu-pertiwi\Monitoring dan Logging
Perintah di Terminal:
3. Prometheus Server Aplikasi ini bertugas untuk menarik (scrape) data dari Exporter yang Anda jalankan di atas.
Path/Folder: Folder tempat Anda sebelumnya mengunduh dan mengekstrak aplikasi Prometheus (di luar folder proyek Anda).
Cara Menjalankan: Anda cukup masuk ke folder tersebut melalui File Explorer, lalu klik ganda (double click) file prometheus.exe
. (Tampilan terminal hitam akan muncul dan biarkan menyala).
4. Grafana Server Aplikasi ini bertugas untuk menampilkan visualisasi grafik dari data Prometheus di browser Anda.
Path/Folder: Folder tempat Anda mengekstrak Grafana, lalu masuk ke dalam folder bin
.
Cara Menjalankan: Di dalam folder bin tersebut, klik ganda file grafana-server.exe
. (Sama seperti Prometheus, biarkan jendela terminalnya tetap menyala).
Setelah keempat layanan ini menyala, sistem pemantauan Anda (http://localhost:3000 untuk Grafana dan port 5002 untuk Model) akan kembali aktif dan siap menerima uji coba dari file 7.inference.py seperti semula.