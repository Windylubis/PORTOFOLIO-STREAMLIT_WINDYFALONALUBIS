import streamlit as st
import buku
import kontak

# ==== KONFIGURASI DASAR APLIKASI ====
st.set_page_config(
    page_title="Jejak Baca Windy: Kisah, Rating, dan Rasa",
    layout="wide"
)

# ==== GANTI WARNA SIDEBAR JADI BIRU LAUT ====
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #d0f0f9;
    }
    </style>
""", unsafe_allow_html=True)

# ==== SIDEBAR NAVIGASI ====
st.sidebar.title("📚 Jelajahi Ceritaku")
page = st.sidebar.radio("Mau ke mana hari ini? ✨", [
    "🏠 Halaman Utama", 
    "📚 Rak Buku Windy", 
    "💌 Kirim Pesan Manis"
])

# ========== HALAMAN BERANDA ==========
if page == "🏠 Halaman Utama":
    # Background pink lembut
    st.markdown("""
        <style>
        .stApp { background-color: #ffe6f0; }
        </style>
    """, unsafe_allow_html=True)

    # ==== HEADER UTAMA ====
    st.title("📘 Jejak Baca Windy: Kisah, Rating, dan Rasa 💕")

    # ==== PROFIL & INTRO ====
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("Captureff.JPG", width=200)
    with col2:
        st.markdown("### 🌸 Halo! Aku Windy Falona Lubis")
        st.markdown("> *“Membaca buatku seperti ngobrol diam-diam dengan dunia.”* – Windy 💖")

    # ==== DESKRIPSI JEJAK BACA ====
    st.write("""
    Aku suka banget membaca buku.  
    Buatku, membaca bukan cuma soal menamatkan halaman demi halaman,  
    tetapi tentang **merasakan perjalanan**, **mendapatkan sudut pandang baru**,  
    dan **mengenal dunia lewat kata-kata** 📖

    Lewat portofolio ini, aku ingin berbagi daftar buku yang pernah aku baca —  
    lengkap dengan **pendapat**, **kesan**, bahkan **harga bukunya**.

    Semoga bisa jadi inspirasi buat kamu yang juga suka membaca ✨
    """)

    st.markdown("""
    - 🖋️ Review pribadi  
    - 💰 Harga bukunya  
    - 📸 Sampulnya  
    - ⭐ Rating dan rekomendasinya  
    """)

    st.markdown("---")

    # ==== KUTIPAN INSPIRATIF ====
    st.markdown("> *“Reading is essential for those who seek to rise above the ordinary.” – Jim Rohn*")

    # ==== STATISTIK KOLEKSI BUKU ====
    with st.container():
        st.markdown("### 📊 Statistik Koleksi Buku")
        st.markdown("""
        - 📚 **Total Buku:** 10  
        - 🧠 **Topik Dominan:** Self-Improvement  
        - ⭐ **Rata-rata Rating:** 4.8  
        """)

    # ==== BUKU TERBARU ====
    st.markdown("### 📌 Buku Terbaru Windy")
    col3, col4 = st.columns([1, 4])
    with col3:
        st.image("https://i0.wp.com/www.rukita.co/stories/wp-content/uploads/2021/09/aku-ingin-pulang-meski-sudah-di-rumah-tweet-1.jpg?w=1000&ssl=1", width=100)
    with col4:
        st.markdown("**Aku Ingin Pulang, Meski Sudah di Rumah** – Won Ji-hyun")
        st.write("🌙 Setelah membaca: Kamu tidak langsung sembuh. Tapi kamu mulai mengizinkan dirimu terluka tanpa merasa bersalah. Dan dari situ, perjalanan pulang bisa dimulai. 🌱")
        st.write("⭐ Rating Windy: 4.9")

    # ==== BUKU FAVORIT ====
    st.markdown("### 📖 Buku Favoritku")
    st.image("https://cf.shopee.co.id/file/sg-11134201-22120-fr1ys5gc3ukvd5", width=150, caption="Ikigai — Héctor García & Francesc Miralles")
    st.write("Buku ini mengubah cara pandangku tentang tujuan hidup. Ringan, tapi menyentuh banget. Rasanya seperti diajak mengenal diri sambil menikmati teh hangat di pagi hari.")


    # ==== FOOTER ====
    st.markdown("---")
    st.markdown("Terima kasih sudah mampir! 🌷 Selamat menemukan buku yang menyentuh hatimu 💕")

# ========== HALAMAN RAK BUKU ==========
elif page == "📚 Rak Buku Windy":
    buku.show()

# ========== HALAMAN KONTAK ==========
elif page == "💌 Kirim Pesan Manis":
    kontak.show()

