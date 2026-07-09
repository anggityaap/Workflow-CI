import requests
import pandas as pd

# 1. Menyiapkan data sampel untuk prediksi
# Kita mengganti 'Time' dan 'Amount' menjadi 'scaled_amount' dan 'scaled_time'
kolom_fitur = ['scaled_amount', 'scaled_time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
               'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
               'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']

df_sample = pd.DataFrame([[0.0] * 30], columns=kolom_fitur)

# 2. Mengubah data ke format yang diterima oleh MLflow Serving API
data_json = {"dataframe_split": df_sample.to_dict(orient="split")}

# 3. Mengirimkan HTTP POST Request ke Model
url = "http://127.0.0.1:5002/invocations"
headers = {"Content-Type": "application/json"}

print("Mengirim data ke model di", url, "...")
response = requests.post(url, json=data_json, headers=headers)

# 4. Menampilkan Hasil
if response.status_code == 200:
    print("✅ Prediksi Berhasil!")
    print("Hasil Prediksi (Class):", response.json())
else:
    print("❌ Gagal melakukan prediksi.")
    print("Status Code:", response.status_code)
    print("Pesan Error:", response.text)