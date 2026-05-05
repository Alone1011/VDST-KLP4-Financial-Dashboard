import streamlit as st
from utils.loader import load_data

# Konfigurasi halaman untuk Overview
st.set_page_config(page_title="Overview Data IHSG", page_icon="📊", layout="wide")

def main():
    st.title("📊 Data Overview")
    st.markdown("Halaman ini menampilkan ringkasan dataset historis IHSG yang berhasil dimuat.")
    st.markdown("---")
    
    with st.spinner("Memuat data dari Kaggle..."):
        df = load_data()
        
    if not df.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(label="Total Baris Data", value=f"{df.shape[0]:,}")
            
        with col2:
            st.metric(label="Total Kolom", value=f"{df.shape[1]}")
            
        st.markdown("### Cuplikan Data")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Data tidak tersedia. Silakan periksa koneksi atau perbaiki pipeline data.")

if __name__ == "__main__":
    main()
