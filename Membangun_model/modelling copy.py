import os
import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Mengatur nama user di MLflow secara default
os.environ["MLFLOW_USER"] = "anggitya"
os.environ["USERNAME"] = "anggitya"
os.environ["USER"] = "anggitya"

# 1. Mengatur Tracking URI ke localhost sesuai kriteria
mlflow.set_tracking_uri("http://127.0.0.1:5000/")

# 2. Membuat nama eksperimen
mlflow.set_experiment("Eksperimen_SML_Credit_Fraud")

# 3. Mengaktifkan fitur Autolog dari MLFlow
mlflow.autolog()

if __name__ == "__main__":
    print("Memuat dataset...")
    # Sesuaikan nama file ini jika Anda menyimpannya dengan nama atau di folder berbeda
    # Misalnya: '../namadataset_preprocessing/creditcard_clean.csv'
    df = pd.read_csv('creditcard_clean.csv') 

    # Memisahkan fitur dan target
    X = df.drop('Class', axis=1)
    y = df['Class']

    # Membagi data latih dan uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Memulai proses Run di MLFlow dan melatih model
    print("Memulai pelatihan model...")
    with mlflow.start_run():
        # Set user_id ke "anggitya" secara eksplisit
        mlflow.set_tag("mlflow.user", "anggitya")
        
        # Kita menggunakan Logistic Regression sebagai contoh yang cepat
        model = LogisticRegression(max_iter=1000)
        
        # Saat model.fit dijalankan, MLFlow autolog otomatis mencatat semuanya!
        model.fit(X_train, y_train)
        
        print("Pelatihan selesai! Artefak dan metrik telah dicatat oleh MLFlow.")