import streamlit as st

# Konfigurasi halaman wajib di baris pertama
st.set_page_config(page_title="IHSG Dashboard", page_icon="📈", layout="wide")

def main():
    st.title("📈 Financial & Equity Dashboard (IHSG Edition)")
    
    st.info("Aplikasi ini menggunakan dataset historis Indeks Harga Saham Gabungan (IHSG) yang diambil secara otomatis dari Kaggle.")
    
    st.markdown("""
    ### 🌟 Tentang Aplikasi
    Dashboard ini adalah aplikasi visualisasi data time-series yang dibangun menggunakan Streamlit. 
    Aplikasi ini secara otomatis mengambil dataset IHSG terbaru menggunakan `kagglehub`, memvisualisasikannya, dan menyediakan kalkulator sederhana untuk simulasi target.
    
    ---
    
    ### 🧑‍💻 Struktur Tim 
    - **1. Core Architect (UI & Data Pipeline)**
      *Fokus pada App Setup, otomatisasi data dari Kaggle, dan menampilkan ringkasan data.*
    - **2. Logic & Visualization Engineer**
      *Fokus merancang grafik interaktif (candlestick/line chart) dan filter data.*
    - **3. Interactive Form Developer**
      *Fokus membangun formulir kalkulator simulasi dengan logika matematika dasar.*
    """)

if __name__ == "__main__":
    main()
