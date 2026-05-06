#yang dilakukan pada laman ini : 
# UI (sidebar) → ambil data → hitung indikator → tampilkan grafik → tampilkan insight
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.loader import load_data

st.set_page_config(page_title="Visualisasi IHSG", page_icon="📉", layout="wide")

def main():
    st.title("📉 Visualisasi Saham IHSG")

    # =========================
    # 🎛️ SIDEBAR
    # =========================
    st.sidebar.header("⚙️ Pengaturan")

    ###Pilih saham pake fungsi sidebar.selectbox###
    stock = st.sidebar.selectbox(
        "Pilih Saham",
        ["AALI", "BBCA", "ADRO", "TLKM", "ANTM"]
    )

    #User bisa nyalakan MA atau tidak dan merubah periode MA
       ###Pilih saham pake fungsi sidebar.checkbox###
    show_ma = st.sidebar.checkbox("Moving Average", True)
       ###Pilih saham pake fungsi sidebar.sliderbox###
    ma_period = st.sidebar.slider("MA Period", 5, 50, 20)

    #Checkbox untuk rsi ditampilkan atau tidak
    show_rsi = st.sidebar.checkbox("RSI", True)

    # =========================
    # 📥 LOAD DATA
    # =========================
    with st.spinner("📥 Mengambil data..."):
        df = load_data(stock)
        df = df.tail(100)

    if df.empty:
        st.error("Data tidak tersedia")
        return

    # =========================
    # 📊 INDIKATOR
    # =========================
    if show_ma:
        #rata-rata harga dalam periode tertentu
        df['ma'] = df['close'].rolling(ma_period).mean() 
        #Interpretasi:
        #harga di atas MA → tren naik 
        #harga di bawah MA → tren turun 
    if show_rsi:
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean() #naik (gain)
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean() #turun (loss)
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs)) #Hasil akhir RSI (rangenya 0-100)

    # =========================
    # 📈 CANDLESTICK
    # grafik yang menunjukkan pergerakan harga dalam 1 periode waktu
    # =========================
    fig = go.Figure()
    #Buat grafik candlestick berdasarkan data harga saham dari waktu ke waktu
    fig.add_trace(go.Candlestick( 
       #fig.add_trace = Tambahkan grafik ke dalam figure
       #go.Candlestick itu tipe grafik dari plotly
        x=df['date'],
        open=df['open'], #harga awal 
        high=df['high'], #harga tertinggi
        low=df['low'], #Harga terendah
        close=df['close'], #harga saat selesai
        name="Price"
    ))
    #Moving average kalau aktif
    if show_ma:
        fig.add_trace(go.Scatter( #go.scatter warna default biru
            x=df['date'],
            y=df['ma'],
            name=f"MA {ma_period}"
        ))
    # Fix Y-axis (biar candle keliatan)
    y_min = df['low'].min()
    y_max = df['high'].max()

    fig.update_layout(
    yaxis=dict(range=[y_min * 0.98, y_max * 1.02]), #Mengatur batas bawah dan atas sumbu Y (harga) secara manual
    height=600)
    ###Pake komponen st.plotly_chart() untuk menampilkan candlestick dan RSI###
    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # 📊 RSI
    # =========================
    if show_rsi:
        st.subheader("📊 RSI Indicator")

        fig_rsi = go.Figure()

        fig_rsi.add_trace(go.Scatter(
            x=df['date'],
            y=df['rsi'],
            name="RSI"
        ))

        fig_rsi.add_hline(y=70)
        fig_rsi.add_hline(y=30)

        st.plotly_chart(fig_rsi, use_container_width=True)

    # =========================
    # 📌 METRICS
    # =========================
    st.subheader("📌 Statistik")

    col1, col2, col3 = st.columns(3)

    col1.metric("Harga Terakhir", f"{df['close'].iloc[-1]:,.2f}")
    col2.metric("Harga Tertinggi", f"{df['high'].max():,.2f}")
    col3.metric("Harga Terendah", f"{df['low'].min():,.2f}")

    # =========================
    #  INSIGHT
    # =========================
    st.subheader("Insight")

    if show_rsi:
        #Ambil nilai RSI paling terakhir (data terbaru)
        rsi_last = df['rsi'].iloc[-1] #.iloc ialah cara akses data berdasarkan posisi index
        
        if rsi_last > 70:
            st.error("⚠️ Overbought (potensi turun)")
        elif rsi_last < 30:
            st.success("💡 Oversold (potensi naik)")
        else:
            st.info("📊 Normal")

    # =========================
    # 📋 DATA
    # =========================

    ###st.expander() untuk menyembuntikan/menampilkan data###
    with st.expander("📋 Lihat Data"):
        st.dataframe(df.tail(100))


if __name__ == "__main__":
    main()