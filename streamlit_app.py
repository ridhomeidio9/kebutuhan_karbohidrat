import streamlit as st
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Kalkulator Kebutuhan Karbohidrat", page_icon="🍚", layout="centered")

# Title with a nice emoji
st.title("🍚 Kalkulator Kebutuhan Karbohidrat dan Makronutrien")
st.write("""
Selamat datang di kalkulator kebutuhan karbohidrat yang membantu Anda menghitung kebutuhan karbohidrat, protein, dan lemak
berdasarkan berat badan, tingkat aktivitas, dan tujuan diet.
""")

# Custom CSS for styling
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        color: #4CAF50;
        font-weight: bold;
    }
    .highlight {
        color: #FF5722;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        padding: 20px;
        font-size: 14px;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

# Input data
berat_badan = st.number_input("Masukkan berat badan (kg)", min_value=30, max_value=200, value=70)
tingkat_aktivitas = st.selectbox("Pilih tingkat aktivitas", ["Sedentari (kurang aktif)", "Ringan", "Sedang", "Berat"])
tujuan_diet = st.selectbox("Pilih tujuan diet", ["Pemeliharaan Berat Badan", "Penurunan Berat Badan", "Peningkatan Berat Badan"])

# Aktivitas factors
aktivitas_faktor = {
    "Sedentari (kurang aktif)": 1.2,
    "Ringan": 1.375,
    "Sedang": 1.55,
    "Berat": 1.725
}

# Tentukan kebutuhan kalori berdasarkan tujuan diet
kalori_harian = 25 * berat_badan * aktivitas_faktor[tingkat_aktivitas] if tujuan_diet == "Pemeliharaan Berat Badan" else \
                20 * berat_badan * aktivitas_faktor[tingkat_aktivitas] if tujuan_diet == "Penurunan Berat Badan" else \
                30 * berat_badan * aktivitas_faktor[tingkat_aktivitas]

# Hitung kebutuhan karbohidrat, protein, lemak
karbohidrat_per_hari = kalori_harian * 0.55 / 4
protein_per_hari = kalori_harian * 0.2 / 4
lemak_per_hari = kalori_harian * 0.25 / 9

# Visualisasi grafik
st.subheader("🍽️ Kebutuhan Gizi Anda")
st.write(f"Total kalori yang dibutuhkan per hari: **{kalori_harian:.2f} kkal**")
st.write(f"Kebutuhan karbohidrat per hari: **{karbohidrat_per_hari:.2f} gram**")
st.write(f"Kebutuhan protein per hari: **{protein_per_hari:.2f} gram**")
st.write(f"Kebutuhan lemak per hari: **{lemak_per_hari:.2f} gram**")

# Pie chart untuk komposisi gizi
fig, ax = plt.subplots()
labels = ['Karbohidrat', 'Protein', 'Lemak']
sizes = [karbohidrat_per_hari, protein_per_hari, lemak_per_hari]
colors = ['#FF9999','#66B2FF','#99FF99']
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Tips & Informasi Diet
st.subheader("💡 Tips & Informasi Diet")
st.write("""
- **Pemeliharaan Berat Badan**: Jika tujuan Anda adalah mempertahankan berat badan saat ini.
- **Penurunan Berat Badan**: Jika tujuan Anda adalah menurunkan berat badan, dengan defisit kalori.
- **Peningkatan Berat Badan**: Jika tujuan Anda adalah menambah massa tubuh dengan surplus kalori.

Dengan menghitung makronutrien yang tepat, Anda dapat merencanakan pola makan yang lebih sehat dan sesuai dengan tujuan.
""")

# Saran makanan berdasarkan makronutrien
st.subheader("🍽️ Pilihan Makanan Berdasarkan Kebutuhan")
st.write("**Makanan dengan Karbohidrat Tinggi**: Nasi, Kentang, Roti, Mie Instan, Pisang")
st.write("**Makanan dengan Protein Tinggi**: Ayam, Tempe, Tahu, Telur Rebus, Ikan")
st.write("**Makanan dengan Lemak Tinggi**: Alpukat, Kacang Almond, Minyak Zaitun, Keju")

# Footer
st.markdown('<div class="footer">Dibuat oleh Mahasiswa Jurusan Pangan | Streamlit Kalkulator 2025</div>', unsafe_allow_html=True)
pip install streamlit matplotlib


