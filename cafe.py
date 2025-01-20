class Cafe:
    def __init__(self):
        self.menu = {
            "Kopi": 15000,
            "Teh": 10000,
            "Espresso": 20000,
            "Cappuccino": 25000,
            "Kue": 12000
        }
        self.pesanan = {}

    def tampilkan_menu(self):
        print("\n--- Menu Kafe ---")
        for item, harga in self.menu.items():
            print(f"{item}: Rp {harga}")

    def tambah_pesanan(self):
        while True:
            self.tampilkan_menu()
            pesanan = input("\nMasukkan nama item yang ingin dipesan (ketik 'selesai' untuk mengakhiri): ").capitalize()
            if pesanan == 'Selesai':
                break
            elif pesanan in self.menu:
                jumlah = int(input(f"Berapa banyak {pesanan} yang ingin dipesan? "))
                if pesanan in self.pesanan:
                    self.pesanan[pesanan] += jumlah
                else:
                    self.pesanan[pesanan] = jumlah
                print(f"{jumlah} {pesanan} telah ditambahkan ke pesanan.")
            else:
                print("Item tidak ada dalam menu. Silakan coba lagi.")
    
    def hitung_total(self):
        total = 0
        for item, jumlah in self.pesanan.items():
            total += self.menu[item] * jumlah
        return total
    
    def tampilkan_pesanan(self):
        if not self.pesanan:
            print("\nTidak ada pesanan.")
        else:
            print("\n--- Pesanan Anda ---")
            for item, jumlah in self.pesanan.items():
                print(f"{item} x {jumlah} = Rp {self.menu[item] * jumlah}")
            print(f"\nTotal yang harus dibayar: Rp {self.hitung_total()}")

def main():
    cafe = Cafe()
    while True:
        print("\n--- Selamat Datang di Kafe! ---")
        print("1. Lihat Menu")
        print("2. Tambah Pesanan")
        print("3. Lihat Pesanan dan Total")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            cafe.tampilkan_menu()
        elif pilihan == "2":
            cafe.tambah_pesanan()
        elif pilihan == "3":
            cafe.tampilkan_pesanan()
        elif pilihan == "4":
            print("Terima kasih telah mengunjungi kafe kami. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()