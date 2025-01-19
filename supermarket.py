# Daftar produk supermarket dan harga
produk = {
    "Apel": 10000,
    "Pisang": 8000,
    "Jeruk": 12000,
    "Mangga": 15000,
    "Semangka": 20000
}

# Fungsi untuk menampilkan daftar produk
def tampilkan_produk():
    print("\nDaftar Produk Supermarket:")
    for nama, harga in produk.items():
        print(f"{nama}: Rp {harga}")

# Fungsi untuk menambah barang ke keranjang
def tambah_ke_keranjang(keranjang, produk, jumlah):
    if produk in keranjang:
        keranjang[produk] += jumlah
    else:
        keranjang[produk] = jumlah

# Fungsi untuk menghitung total belanjaan
def hitung_total(keranjang):
    total = 0
    for produk, jumlah in keranjang.items():
        total += produk[produk] * jumlah
    return total

def main():
    keranjang = {}
    while True:
        tampilkan_produk()
        pilihan = input("\nMasukkan nama produk yang ingin dibeli (atau ketik 'selesai' untuk keluar): ").capitalize()
        
        if pilihan == 'Selesai':
            break
        
        if pilihan not in produk:
            print("Produk tidak tersedia. Silakan pilih produk yang ada.")
            continue
        
        jumlah = int(input(f"Berapa banyak {pilihan} yang ingin Anda beli? "))
        
        tambah_ke_keranjang(keranjang, pilihan, jumlah)
        
    print("\nKeranjang Belanja Anda:")
    total = 0
    for produk, jumlah in keranjang.items():
        print(f"{produk}: {jumlah} x Rp {produk[produk]} = Rp {produk[produk] * jumlah}")
        total += produk[produk] * jumlah
        
    print(f"\nTotal Belanja: Rp {total}")

if __name__ == "__main__":
    main()