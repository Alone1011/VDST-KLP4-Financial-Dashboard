#file ini berfungsi untuk :
#Mengambil data → Membersihkan → Menstandarkan → Mengirim ke halaman lain
import os #ngatur path file
import pandas as pd #Olah data tabel
import streamlit as st  #buat tampilan & error message
import kagglehub #download dataset dari Kaggle

@st.cache_data #Menyimpan hasil load data di memori
def load_data(stock_code="AALI"): #pake AALI dulu kalo user blm milih kode saham
    try:
        # Download dataset
        path = kagglehub.dataset_download("muamkh/ihsgstockdata")

        # Masuk ke folder daily
        daily_path = os.path.join(path, "daily")

        # Path file saham
        file_path = os.path.join(daily_path, f"{stock_code}.csv") #nampilin data sesuai kode saham yang dopilih user

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{stock_code}.csv tidak ditemukan")

        df = pd.read_csv(file_path)

        # =========================
        # 🧹 NORMALISASI KOLOM
        # =========================
        df.columns = df.columns.str.lower()

        # =========================
        # 🔍 CARI KOLOM TANGGAL
        # =========================
        date_col = None
        for col in df.columns:
            if "date" in col or "time" in col:
                date_col = col
                break

        if date_col is None:
            raise Exception(f"Kolom tanggal tidak ditemukan. Kolom: {df.columns}")

        # Rename jadi 'date'
        df.rename(columns={date_col: 'date'}, inplace=True)

        # Convert ke datetime
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values(by='date')       # urutkan berdasarkan waktu
        df = df.reset_index(drop=True)       # rapihin index
        return df

    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return pd.DataFrame()