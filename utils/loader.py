import os
import glob
import pandas as pd
import streamlit as st
import kagglehub

@st.cache_data
def load_data():
    """
    Mengunduh dan memuat dataset IHSG dari Kaggle.
    Dataset di-cache oleh Streamlit agar tidak perlu diunduh/dibaca ulang.
    """
    try:
        # Mengunduh dataset menggunakan kagglehub
        path = kagglehub.dataset_download("muamkh/ihsgstockdata")
        
        # Mencari file .csv dalam direktori hasil unduhan
        csv_files = glob.glob(os.path.join(path, "*.csv"))
        
        if not csv_files:
            raise FileNotFoundError("Tidak ada file CSV yang ditemukan dalam dataset.")
            
        # Membaca file CSV pertama yang ditemukan
        file_path = csv_files[0]
        df = pd.read_csv(file_path)
        
        return df
        
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return pd.DataFrame() # Mengembalikan DataFrame kosong jika terjadi error
