import streamlit as st

# Judul aplikasi
st.title("🍚 Kalkulator Kebutuhan Karbohidrat dan Makronutrien")
st.write("""
Kalkulator ini membantu Anda menghitung kebutuhan karbohidrat, protein, dan lemak berdasarkan berat badan,
tingkat aktivitas, dan tujuan diet.
""")

# Input data pengguna
berat_badan = st.number_input("Masukkan berat badan (kg)", min_value=30, max_value=200, value=70)
tingkat_aktivitas = st.selectbox("Pilih tingkat aktivitas", ["Sedentari (kurang aktif)", "Ringan", "Sedang", "Berat"])
tujuan_diet = st.selectbox("Pilih tujuan diet", ["Pemeliharaan Berat Badan", "Penurunan Berat Badan", "Peningkatan Berat Badan"])

# Tentukan faktor aktivitas (berdasarkan tingkat aktivitas)
if tingkat_aktivitas == "Sedentari (kurang aktif)":
    faktor_aktivitas = 1.2
elif tingkat_aktivitas == "Ringan":
    faktor_aktivitas = 1.375
elif tingkat_aktivitas == "Sedang":
    faktor_aktivitas = 1.55
else:
    faktor_aktivitas = 1.725

# Tentukan kebutuhan kalori berdasarkan tujuan diet
if tujuan_diet == "Pemeliharaan Berat Badan":
    kalori_harian = 25 * berat_badan * faktor_aktivitas  # Kalori untuk pemeliharaan
elif tujuan_diet == "Penurunan Berat Badan":
    kalori_harian = 20 * berat_badan * faktor_aktivitas  # Kalori untuk penurunan
else:
    kalori_harian = 30 * berat_badan * faktor_aktivitas  # Kalori untuk peningkatan

# Hitung kebutuhan makronutrien (Karbohidrat, Protein, Lemak)
# Karbohidrat 50-60% dari total kalori
karbohidrat_per_hari = kalori_harian * 0.55 / 4  # 1 gram karbohidrat = 4 kalori
# Protein 15-25% dari total kalori
protein_per_hari = kalori_harian * 0.2 / 4  # 1 gram protein = 4 kalori
# Lemak 20-30% dari total kalori
lemak_per_hari = kalori_harian * 0.25 / 9  # 1 gram lemak = 9 kalori

# Porsi makanan untuk setiap makronutrien
karbo_per_porsi = 30  # Karbohidrat per porsi makanan (misal nasi 1 porsi = 30g karbohidrat)
protein_per_porsi = 10  # Protein per porsi makanan (misal ayam 1 porsi = 10g protein)
lemak_per_porsi = 10  # Lemak per porsi makanan (misal alpukat 1 porsi = 10g lemak)

# Hasil kalkulasi
st.subheader("Hasil Perhitungan Kebutuhan Makronutrien Anda")
st.write(f"Total kalori yang dibutuhkan per hari: **{kalori_harian:.2f} kkal**")
st.write(f"Kebutuhan karbohidrat per hari: **{karbohidrat_per_hari:.2f} gram**")
st.write(f"Kebutuhan protein per hari: **{protein_per_hari:.2f} gram**")
st.write(f"Kebutuhan lemak per hari: **{lemak_per_hari:.2f} gram**")

# Porsi makanan
st.subheader("Porsi Makanan yang Diperlukan untuk Memenuhi Kebutuhan")
st.write(f"Porsi makanan untuk karbohidrat: **{karbohidrat_per_hari / karbo_per_porsi:.2f} porsi** (misal nasi)")
st.write(f"Porsi makanan untuk protein: **{protein_per_hari / protein_per_porsi:.2f} porsi** (misal ayam)")
st.write(f"Porsi makanan untuk lemak: **{lemak_per_hari / lemak_per_porsi:.2f} porsi** (misal alpukat)")

# Pilihan makanan berdasarkan karbohidrat
makanan_karbo = {
    "Nasi Putih": 28, "Kentang Rebus": 20, "Roti Tawar": 49, "Mie Instan Rebus": 50, "Apel": 14, "Pisang": 23
}

# Pilihan makanan berdasarkan protein
makanan_protein = {
    "Ayam Goreng": 27, "Tempe Goreng": 18, "Tahu Goreng": 14, "Telur Rebus": 13, "Sate Ayam": 14
}

# Pilihan makanan berdasarkan lemak
makanan_lemak = {
    "Alpukat": 15, "Kacang Almond": 49, "Susu Full Cream": 3.2, "Keju": 25, "Minyak Zaitun": 100
}

st.subheader("Pilihan Makanan yang Dapat Membantu Menyusun Diet Anda")
st.write("**Makanan dengan Karbohidrat Tinggi**:")
st.write(makanan_karbo)
st.write("**Makanan dengan Protein Tinggi**:")
st.write(makanan_protein)
st.write("**Makanan dengan Lemak Tinggi**:")
st.write(makanan_lemak)

# Footer
st.markdown("---")
st.caption("Dibuat oleh Mahasiswa Jurusan Pangan | Streamlit Kalkulator Kebutuhan Makronutrien 2025")
