import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.loader import load_data

st.set_page_config(page_title="Kalkulator Saham", page_icon="🧮", layout="wide")

def main():
    st.title("🧮 Target Calculator")
    st.markdown("Simulasikan target keuntungan (*take profit*) dan batas kerugian (*stop loss*) Anda.")
    st.markdown("---")

    # Load data
    df = load_data()

    # Ambil harga terakhir (close)
    if not df.empty and 'close' in df.columns:
        harga_default = float(df['close'].iloc[-1])
    else:
        harga_default = 100000.0

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📥 Input Data")

        harga_beli = st.number_input(
            "Harga Beli (Rp)",
            min_value=0.0,
            value=harga_default,
            step=10000.0
        )

        target_profit = st.slider(
            "Target Profit (%)",
            min_value=0,
            max_value=100,
            value=10
        )

        stop_loss = st.slider(
            "Stop Loss (%)",
            min_value=0,
            max_value=50,
            value=5
        )

    with col2:
        st.subheader("📊 Hasil Simulasi")

        if harga_beli <= 0:
            st.error("Harga beli harus lebih dari 0.")
            return

        # Perhitungan
        harga_target = harga_beli * (1 + target_profit / 100)
        harga_cutloss = harga_beli * (1 - stop_loss / 100)

        keuntungan = harga_target - harga_beli
        kerugian = harga_beli - harga_cutloss

        # Risk Reward Ratio
        rr_ratio = keuntungan / kerugian if kerugian != 0 else 0

        st.metric(
            "🎯 Harga Target",
            f"Rp {harga_target:,.2f}",
            f"+Rp {keuntungan:,.2f}"
        )

        st.metric(
            "🛑 Stop Loss",
            f"Rp {harga_cutloss:,.2f}",
            f"-Rp {kerugian:,.2f}"
        )

        st.markdown("---")

        # Highlight Risk Reward
        if rr_ratio >= 2:
            st.success(f"💰 Risk/Reward Ratio: {rr_ratio:.2f} (Bagus 👍)")
        elif rr_ratio >= 1:
            st.warning(f"⚖️ Risk/Reward Ratio: {rr_ratio:.2f} (Cukup)")
        else:
            st.error(f"⚠️ Risk/Reward Ratio: {rr_ratio:.2f} (Kurang baik)")

        st.info(f"""
        📌 **Ringkasan:**
        - Harga beli: Rp {harga_beli:,.2f}
        - Target profit: {target_profit}%
        - Stop loss: {stop_loss}%
        """)

if __name__ == "__main__":
    main()