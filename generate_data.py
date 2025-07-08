import pandas as pd

data_buku_10 = {
    "Judul": [
        "Atomic Habits",
        "The Power of Now",
        "Deep Work",
        "The 7 Habits of Highly Effective People",
        "Think and Grow Rich",
        "Grit",
        "Mindset",
        "Dare to Lead",
        "Ikigai",
        "The Subtle Art of Not Giving a F*ck"
    ],
    "Penulis": [
        "James Clear",
        "Eckhart Tolle",
        "Cal Newport",
        "Stephen R. Covey",
        "Napoleon Hill",
        "Angela Duckworth",
        "Carol S. Dweck",
        "Brené Brown",
        "Héctor García & Francesc Miralles",
        "Mark Manson"
    ],
    "Harga": [
        "Rp125.000", "Rp110.000", "Rp135.000", "Rp120.000", "Rp115.000",
        "Rp130.000", "Rp119.000", "Rp140.000", "Rp100.000", "Rp128.000"
    ],
    "Review": [
        "Buku ini memberikan pendekatan praktis dalam mengubah kebiasaan buruk menjadi kebiasaan produktif. Mudah dipahami dan sangat aplikatif.",
        "Mengajak kita untuk hidup di masa kini dengan penuh kesadaran. Buku ini sangat dalam dan reflektif.",
        "Panduan penting untuk bekerja fokus di era yang penuh distraksi digital. Cocok untuk siapa saja yang ingin produktif.",
        "Klasik sepanjang masa. Mengajarkan prinsip-prinsip dasar untuk menjadi pribadi yang efektif dalam kehidupan pribadi maupun profesional.",
        "Buku motivasi legendaris yang membakar semangat sukses dan membentuk pola pikir untuk bertumbuh.",
        "Menekankan pentingnya kegigihan dan semangat pantang menyerah. Cocok untuk kamu yang sedang berjuang mencapai tujuan.",
        "Mengubah cara pandang kita tentang kecerdasan. Menanamkan bahwa kemampuan bisa dikembangkan lewat usaha.",
        "Mendorong kepemimpinan yang berani dan penuh empati. Buku ini sangat menyentuh dan menginspirasi.",
        "Filosofi Jepang tentang hidup panjang dan bermakna. Buku ini menenangkan dan mengajak kita refleksi hidup.",
        "Gaya bahasanya blak-blakan tapi jujur. Buku ini menantang kita untuk berpikir ulang soal makna kebahagiaan dan prioritas hidup."
    ],
    "Rating": [4.9, 4.8, 4.7, 4.9, 4.8, 4.7, 4.8, 4.9, 4.6, 4.7],
    "Link Gambar": [
        "at.JPG",
        "https://images-na.ssl-images-amazon.com/images/I/71XShy1zLAL.jpg",
        "https://media.karousell.com/media/photos/products/2022/8/22/the_power_of_now__a_guide_of_s_1661177181_17973c81.jpg",
        "https://impartiallyderivative.com/wp-content/uploads/2018/10/DeepWork-6.jpg",
        "https://img.drz.lazcdn.com/static/pk/p/7a1ca0c15aed51a56334f033cb9cb961.jpg_720x720q80.jpg",
        "https://hlbookstore.in/wp-content/uploads/2022/06/Think-And-Grow-Rich-By-Napoleon-Hill-1.jpg",
        "https://i.pinimg.com/originals/89/f0/b7/89f0b74dad7af0b52071f9094a59ea84.jpg",
        "https://parentotheca.com/wp-content/uploads/2020/12/IMG_9026-scaled.jpg",
        "https://images.squarespace-cdn.com/content/v1/59c82ac46f4ca30b86d179bf/1626355058421-1N61AQSEDMKGTJ7CMLV7/34.bookreview.daretolead.tpr.jpg",
        "https://www.bigw.com.au/medias/sys_master/images/images/hd4/h19/14654977703966.jpg"
        "https://5.imimg.com/data5/SELLER/Default/2023/2/KU/GR/TV/147952517/mark-manson-book-500x500.jpeg"
    ]
}

df = pd.DataFrame(data_buku_10)
df.to_csv("data_10_buku_self_improvement.csv", index=False)
