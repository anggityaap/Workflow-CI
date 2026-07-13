import os
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1. Mengatur Tracking URI ke localhost
# BARIS DI BAWAH INI DIJADIKAN KOMENTAR ATAU DIHAPUS AGAR TIDAK ERROR DI GITHUB ACTIONS
# mlflow.set_tracking_uri("http://127.0.0.1:5000/") 

# 2. Membuat nama eksperimen
if "MLFLOW_RUN_ID" not in os.environ:
    mlflow.set_experiment("Eksperimen_SML_Credit_Fraud")

if __name__ == "__main__":
    print("Memuat dataset...")
    # Pastikan file dataset berada di folder yang sama (MLProject)
    df = pd.read_csv('creditcard_clean.csv') 

    # Memisahkan fitur dan target
    X = df.drop('Class', axis=1)
    y = df['Class']

    # Membagi data latih dan uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Mengaktifkan fitur Autolog KHUSUS Scikit-Learn
    mlflow.sklearn.autolog()

    # 4. Memulai proses Run di MLFlow dan melatih model
    print("Memulai pelatihan model...")
    with mlflow.start_run():
        model = LogisticRegression(max_iter=1000)
        
        # Proses fit ini yang akan dicatat otomatis oleh MLFlow
        model.fit(X_train, y_train)
        
        print("Pelatihan selesai! Artefak dan metrik telah dicatat oleh MLFlow.")