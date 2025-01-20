class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Restoran:
    def __init__(self):
        self.menu = [
            Menu("Nasi Goreng", 25000),
            Menu("Mie Goreng", 20000),
            Menu("Sate Ayam", 30000),
            Menu("Ayam Penyet", 35000),
            Menu("Es Teh", 5000),
            Menu("Es Jeruk", 7000)
        ]
        self.pesanan = []

    def tampilkan_menu(self):
        print("\nMenu Restoran:")
        for idx, item in enumerate(self.menu, 1):
            print(f"{idx}. {item.nama} - Rp{item.harga}")

    def tambah_pesanan(self):
        self.tampilkan_menu()
        try:
            pilihan = int(input("\nPilih nomor menu untuk dipesan (0 untuk selesai): "))
            if pilihan == 0:
                return
            elif 1 <= pilihan <= len(self.menu):
                jumlah = int(input(f"Berapa banyak {self.menu[pilihan - 1].nama} yang ingin dipesan? "))
                self.pesanan.append((self.menu[pilihan - 1], jumlah))
                print(f"{jumlah} {self.menu[pilihan - 1].nama} ditambahkan ke pesanan.")
            else:
                print("Nomor menu tidak valid!")
        except ValueError:
            print("Input tidak valid!")

    def hitung_total(self):
        total = 0
        for item, jumlah in self.pesanan:
            total += item.harga * jumlah
        return total

    def tampilkan_pesanan(self):
        if not self.pesanan:
            print("\nBelum ada pesanan.")
        else:
            print("\nPesanan Anda:")
            for item, jumlah in self.pesanan:
                print(f"{item.nama} x {jumlah} - Rp{item.harga * jumlah}")
            print(f"Total Harga: Rp{self.hitung_total()}")

def main():
    restoran = Restoran()
    
    while True:
        print("\n-- Menu Utama --")
        print("1. Lihat Menu")
        print("2. Tambah Pesanan")
        print("3. Tampilkan Pesanan")
        print("4. Hitung Total")
        print("5. Keluar")
        
        try:
            pilihan = int(input("Pilih opsi (1-5): "))
            if pilihan == 1:
                restoran.tampilkan_menu()
            elif pilihan == 2:
                restoran.tambah_pesanan()
            elif pilihan == 3:
                restoran.tampilkan_pesanan()
            elif pilihan == 4:
                print(f"Total Harga: Rp{restoran.hitung_total()}")
            elif pilihan == 5:
                print("Terima kasih telah berkunjung!")
                break
            else:
                print("Opsi tidak valid!")
        except ValueError:
            print("Input tidak valid!")

if __name__ == "__main__":
    main()