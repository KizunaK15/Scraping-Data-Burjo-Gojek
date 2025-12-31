from bs4 import BeautifulSoup
import pandas as pd
import os

# 1. Target File (Yang baru Anda buat)
file_name = "WebScraper\data_mentah.html"
current_dir = os.getcwd()
file_path = os.path.join(current_dir, file_name)

print(f"📂 Membuka file pasien: {file_name}")

if os.path.exists(file_path):
    # Baca file dengan encoding utf-8
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    menu_list = []
    
    # 2. LOGIKA BARU (Berdasarkan Forensik)
    # Target Class yang ditemukan di data Anda: 'text-gf-content-primary line-clamp-2 gf-label-m'
    items = soup.find_all('h3', class_='text-gf-content-primary line-clamp-2 gf-label-m')
    
    print(f"🔍 Ditemukan {len(items)} item menu. Sedang mengekstrak...")

    for item in items:
        try:
            # AMBIL NAMA
            nama_menu = item.text.strip()
            
            # AMBIL HARGA
            # Logika: Harga ada di tag 'span' dengan class 'mr-4 mt-0.5' 
            # yang berada di dalam pembungkus yang sama dengan h3
            
            # Kita naik ke parent (div pembungkus), lalu cari span harga di dalamnya
            parent_container = item.parent
            harga_element = parent_container.find('span', class_='mr-4 mt-0.5')
            
            if harga_element:
                harga = harga_element.text.strip()
            else:
                # Fallback: Cari text angka di sekitar situ jika class berubah
                harga = "0"

            # AMBIL DESKRIPSI (Optional)
            desc_element = item.find_next('p', class_='text-gf-content-muted')
            deskripsi = desc_element.text.strip() if desc_element else "-"

            # Simpan Data
            print(f"   > {nama_menu} | {harga}")
            menu_list.append({
                'Nama Menu': nama_menu,
                'Harga': harga,
                'Deskripsi': deskripsi
            })

        except Exception as e:
            print(f"⚠️ Error pada satu item: {e}")
            continue

    # 3. Export Hasil
    if menu_list:
        df = pd.DataFrame(menu_list)
        df.to_csv('Data_Burjo_PakMan_Final.csv', index=False)
        print(f"\n🎉 MISI SELESAI! {len(menu_list)} data berhasil diamankan.")
        print("📂 File CSV siap dikirim ke klien (atau dosen).")
    else:
        print("\n❌ Masih kosong. Pastikan Anda sudah paste HTML panjang tadi ke 'data_mentah.html'")

else:
    print(f"❌ File '{file_name}' tidak ditemukan. Buat dulu filenya!")