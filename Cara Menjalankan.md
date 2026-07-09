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
