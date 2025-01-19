class Kasir:
    def __init__(self):
        self.daftar_barang = []
        self.total_harga = 0

    def tambah_barang(self, nama_barang, harga, jumlah):
        barang = {
            'nama': nama_barang,
            'harga': harga,
            'jumlah': jumlah,
            'total': harga * jumlah
        }
        self.daftar_barang.append(barang)
        self.total_harga += barang['total']
        print(f"{nama_barang} x{jumlah} ditambahkan ke daftar belanja.")

    def tampilkan_rincian(self):
        print("\n--- Rincian Belanja ---")
        for barang in self.daftar_barang:
            print(f"{barang['nama']} - Harga: {barang['harga']} - Jumlah: {barang['jumlah']} - Total: {barang['total']}")
        print(f"\nTotal Belanja: {self.total_harga}")

    def bayar(self, uang_dibayar):
        if uang_dibayar >= self.total_harga:
            kembalian = uang_dibayar - self.total_harga
            print(f"\nTotal yang harus dibayar: {self.total_harga}")
            print(f"Uang yang dibayar: {uang_dibayar}")
            print(f"Kembalian: {kembalian}")
        else:
            print("\nUang yang dibayar kurang dari total belanja. Transaksi dibatalkan.")

# Program utama
def main():
    kasir = Kasir()

    while True:
        print("\nMenu Kasir")
        print("1. Tambah barang")
        print("2. Tampilkan rincian belanja")
        print("3. Bayar")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            harga = float(input("Masukkan harga barang: "))
            jumlah = int(input("Masukkan jumlah barang: "))
            kasir.tambah_barang(nama_barang, harga, jumlah)
        
        elif pilihan == '2':
            kasir.tampilkan_rincian()
        
        elif pilihan == '3':
            kasir.tampilkan_rincian()
            uang_dibayar = float(input("Masukkan uang yang dibayar: "))
            kasir.bayar(uang_dibayar)
        
        elif pilihan == '4':
            print("Terima kasih, sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()