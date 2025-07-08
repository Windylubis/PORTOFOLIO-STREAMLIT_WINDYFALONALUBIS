# streamlit_app.py
import streamlit as st
import buku
import kontak

st.set_page_config(page_title= "Jejak Baca Windy: Kisah, Rating, dan Rasa", layout="wide")

# Sidebar Navigasi
st.sidebar.title("📚 Jelajahi Ceritaku")
page = st.sidebar.radio("Mau ke mana hari ini? ✨", ["🏠 Halaman Utama", "📚 Rak Buku Windy", "💌 Kirim Pesan Manis"])

# Halaman BERANDA
if page == "🏠 Halaman Utama":
    st.markdown("""
        <style>
        .stApp { background-color: #ffe6f0; }
        </style>
    """, unsafe_allow_html=True)

    st.title("📘 Jejak Baca Windy: Kisah, Rating, dan Rasa 💕")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("Captureff.JPG", width=200)
    with col2:
        st.markdown("### Halo! Aku Windy Falona Lubis 🌸")
        st.write("Pencinta buku self-improvement dan pengagum kata-kata indah ✨")
        st.markdown("> *“Membaca buatku seperti ngobrol diam-diam dengan dunia.”* – Windy 💖")


    st.write(""" 
    Aku suka banget membaca buku.  
    Buatku, membaca bukan cuma soal menamatkan halaman demi halaman.  
    Tapi tentang **merasakan perjalanan**, **mendapatkan sudut pandang baru**, dan **mengenal dunia lewat kata-kata**.

    Lewat portofolio ini, aku ingin berbagi daftar buku yang pernah aku baca — beserta **pendapat**, **kesan**, bahkan **harga bukunya**.

    Semoga bisa jadi inspirasi atau referensi buat kamu yang juga suka membaca ✨  
    Selamat menjelajahi koleksi bacaan pribadiku! 📖
    """)

    st.markdown("""
    - 🖋️ Review pribadi  
    - 💰 Harga bukunya  
    - 📸 Sampulnya  
    - ⭐ Rating dan rekomendasinya  
    """)

    st.markdown("---")

    # 🌟 KUTIPAN INSPIRATIF
    st.markdown("> *“Reading is essential for those who seek to rise above the ordinary.” – Jim Rohn*")

    # 📊 STATISTIK SINGKAT
    with st.container():
       st.markdown("### 📊 Statistik Koleksi Buku")
       st.markdown("""
       - 📚 **Total Buku:** 10  
       - 🧠 **Topik Dominan:** Self-Improvement  
       - ⭐ **Rata-rata Rating:** 4.8  
       """)


    # 💖 BUKU FAVORIT
    st.markdown("#### 📖 Buku Favoritku")
    st.image("https://cf.shopee.co.id/file/sg-11134201-22120-fr1ys5gc3ukvd5", width=150, caption="Ikigai — Héctor García & Francesc Miralles")
    st.write("Buku ini mengubah cara pandangku tentang tujuan hidup. Ringan, tapi menyentuh banget. Rasanya seperti diajak mengenal diri sambil menikmati teh hangat di pagi hari.")

    st.markdown("Terima kasih sudah mampir! 🌷 Selamat menemukan buku yang menyentuh hatimu 💕")

    st.markdown("---")
    

# Halaman BUKU
elif page == "📚 Rak Buku Windy":
    buku.show()

# Halaman KONTAK
elif page == "💌 Kirim Pesan Manis":
    kontak.show()

