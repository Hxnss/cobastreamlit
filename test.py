# import streamlit as st

# Judul = st.title("Hello World!", anchor='right')
# Sub = st.subheader("The World is so beautifull.")
# st.header("World is so complex.")
# st.text("Earth is Our World. So if the earth not match with our condition anymore, we would die.")
# st.markdown("[YouTube](https://www.youtube.com/@gurugembul)")
# st.image('Hitam dan Emas Elegan Modern Sampul Buku Yasin.png')

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Judul aplikasi
st.title("Visualisasi Data Saham")

# Input untuk simbol saham
stock_symbol = st.text_input("Masukkan simbol saham (contoh: GOTO.JK untuk GoTo, BBCA.JK untuk BCA):", "GOTO.JK")

# Input untuk rentang waktu
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Tanggal Mulai", datetime.now() - timedelta(days=365))
with col2:
    end_date = st.date_input("Tanggal Akhir", datetime.now())

# Tombol untuk memuat data
if st.button("Tampilkan Grafik"):
    try:
        # Mengambil data saham
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        
        if len(stock_data) > 0:
            # Membuat grafik candlestick
            fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                               open=stock_data['Open'],
                                               high=stock_data['High'],
                                               low=stock_data['Low'],
                                               close=stock_data['Close'])])
            
            # Mengatur layout grafik
            fig.update_layout(
                title=f'Grafik Saham {stock_symbol}',
                yaxis_title='Harga (IDR)',
                xaxis_title='Tanggal',
                template='plotly_dark'
            )
            
            # Menampilkan grafik
            st.plotly_chart(fig, use_container_width=True)
            
            # Menampilkan statistik dasar
            st.subheader("Statistik Saham")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Harga Pembukaan Terakhir", f"Rp {stock_data['Open'][-1]:,.2f}")
            with col2:
                st.metric("Harga Penutupan Terakhir", f"Rp {stock_data['Close'][-1]:,.2f}")
            with col3:
                st.metric("Volume Perdagangan Terakhir", f"{stock_data['Volume'][-1]:,}")
            
            # Menampilkan data mentah
            if st.checkbox("Tampilkan Data Mentah"):
                st.write(stock_data)
                
    except Exception as e:
        st.error(f"Terjadi kesalahan: {str(e)}")
