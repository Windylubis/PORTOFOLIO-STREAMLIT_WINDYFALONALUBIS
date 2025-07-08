import pandas as pd
import streamlit as st

def show():
    st.set_page_config(page_title="Portofolio Buku", layout="wide")
    st.title("💖 Bacaan Self-Improvement Versi Windy")

    df = pd.read_csv("data_10_buku_self_improvement.csv")

    for index, row in df.iterrows():
        st.markdown("---")
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(row["Link Gambar"], width=100)
        with col2:
            st.subheader(f"{row['Judul']} — *{row['Penulis']}*")
            st.write(f"**Harga:** {row['Harga']}  |  **Rating:** ⭐ {row['Rating']}")
            st.write(row["Review"])


