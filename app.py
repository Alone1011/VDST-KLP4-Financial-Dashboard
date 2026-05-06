import streamlit as st
import pandas as pd
from utils.loader import load_data

# Konfigurasi Awal
st.set_page_config(page_title="IHSG Dashboard", page_icon="📈", layout="wide")

def main():
    # === SIDEBAR MODERN ===
    with st.sidebar:
        
        st.success("💡 **Tip:** Aktifkan *Dark Theme* di menu pengaturan (ujung kanan atas) agar visual grafik lebih elegan dan modern.")
        
        st.markdown("---")
        st.caption("👨‍💻 **Tim Pengembang (VDST Kelompok 4):**")
        st.markdown("""
        - **Rifki Y.** *(Core Architect)*
        - **Sherly S.** *(Logic & Viz)*
        - **M. Hafiz** *(Form Developer)*
        """)
        
        st.markdown("---")
        st.markdown("<div style='text-align: center; font-size: 12px; color: gray;'>v1.0.0 | Data by Kagglehub</div>", unsafe_allow_html=True)
    # =======================

    # Bagian 1: Hero Section (Welcome)
    st.title("🚀 Financial & Equity Dashboard")
    st.write("Aplikasi ini memvisualisasikan data historis Indeks Harga Saham Gabungan (IHSG) yang diambil secara otomatis dari Kaggle.")
    
    st.markdown("""
    ### 🧑‍💻 Tim Pengembang
    - **1. Core Architect** (Rifki Yuliandra - 2311532011)
    - **2. Logic & Visualization Engineer** (Sherly Sukmadira Putri - 2311532015)
    - **3. Interactive Form Developer** (Muhammad Hafiz - 2311532007)
    """)
    
    st.info("👈 Silakan mengeksplorasi fitur grafik dan kalkulator di sidebar sebelah kiri.")
    
    # Bagian 2: Data Overview
    st.markdown("---")
    st.subheader("📊 Ringkasan Dataset IHSG")
    
    with st.spinner("Memuat data dari Kaggle..."):
        df = load_data()
        
    if not df.empty:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="Total Baris Data", value=f"{df.shape[0]:,}")
            
        with col2:
            st.metric(label="Total Kolom", value=f"{df.shape[1]}")
            
        with col3:
            if 'Date' in df.columns:
                min_date = str(df['Date'].min())[:10]
                max_date = str(df['Date'].max())[:10]
                st.metric(label="Rentang Waktu", value=f"{min_date} / {max_date}")
            else:
                st.metric(label="Status Data", value="Tersedia")
                
        st.write("**Cuplikan Tabel Data Mentah (100 Baris Pertama):**")
        st.dataframe(df.head(100), use_container_width=True)
        
    else:
        st.error("Data tidak tersedia atau gagal dimuat dari Kaggle.")

if __name__ == "__main__":
    main()
