import pandas as pd

# 1. Load Data (KUNCI PERBAIKAN DI SINI)
# dtype=str memaksa Python membaca "24.000" sebagai Teks, bukan Angka 24.0
file_input = 'Data_Burjo_PakMan_Final.csv'
print("🔧 Sedang memperbaiki format angka...")

try:
    df = pd.read_csv(file_input, dtype={'Harga': str})

    # 2. PEMBERSIHAN
    # Hapus titik "." dari teks "24.000" -> "24000"
    df['Harga'] = df['Harga'].str.replace('.', '', regex=False)
    
    # Ubah jadi angka murni (Integer)
    df['Harga'] = pd.to_numeric(df['Harga'], errors='coerce').fillna(0).astype(int)

    # Rapikan Teks lain
    df['Nama Menu'] = df['Nama Menu'].str.title()
    df['Deskripsi'] = df['Deskripsi'].str.replace('-', 'Tidak ada deskripsi')

    # Urutkan dari termahal
    df_sorted = df.sort_values(by='Harga', ascending=False)

    # 3. SIMPAN LANGSUNG KE EXCEL (Biar kolom otomatis rapi)
    output_excel = 'Laporan_Burjo_Final.xlsx'
    
    # Kita gunakan engine xlsxwriter jika ada, atau default
    df_sorted[['Nama Menu', 'Harga', 'Deskripsi']].to_excel(output_excel, index=False)
    
    print(f"\n✅ BERHASIL! Ribuan sudah kembali.")
    print(f"📊 Cek file: {output_excel}")
    print("💡 Tips: Buka Excel -> Blok Kolom Harga -> Ctrl+Shift+1 untuk format Rupiah.")

except FileNotFoundError:
    print("❌ File CSV tidak ditemukan.")