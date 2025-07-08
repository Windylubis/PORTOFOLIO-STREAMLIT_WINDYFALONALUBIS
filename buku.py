import pandas as pd
import streamlit as st

def show():
    # Set judul halaman
    st.set_page_config(page_title="Portofolio Buku", layout="wide")
    st.markdown("""
        <style>
        .stApp {
            background-color: #fff9db;
        }
        </style>
    """, unsafe_allow_html=True)
    st.title("📚 Rak Buku Windy: Kisah, Kata, dan Rasa ✨")

    # Load data dari file CSV
    df = pd.read_csv("data_10_buku_self_improvement.csv")

    # Deskripsi pembuka
    st.write("""
    Di sini kamu bisa menemukan daftar buku self-improvement yang sudah aku baca,  
    lengkap dengan **review pribadi**, **harga saat aku beli**, dan tentu saja **rating dari hatiku** 🌷

    Semoga bisa jadi referensi buat kamu yang juga suka menumbuhkan diri lewat buku 📖
    """)

    # Loop tampilkan semua buku
    for index, row in df.iterrows():
        st.markdown("---")
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(row["Link Gambar"], width=100)
        with col2:
            st.subheader(f"📖 {row['Judul']} — *{row['Penulis']}*")
            st.write(f"💸 **Harga saat kubeli:** {row['Harga']}")
            st.write(f"⭐ **Rating Versiku:** {row['Rating']}/5")
            st.markdown(f"📝 _{row['Review']}_")




