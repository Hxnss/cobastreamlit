import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Baca data saham
df = pd.read_csv('data_saham.csv')

# Tampilan aplikasi
st.title('Predict the Stocks')

# Input kode saham
kode_saham = st.text_input('Kode Saham')

# Jika tombol Predict ditekan
if st.button('Predict'):
    # Tampilkan grafik saham
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Tanggal'], df['Harga'])
    ax.set_title(f'Grafik Harga Saham {kode_saham}')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Harga')
    st.pyplot(fig)
