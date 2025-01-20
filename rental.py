class RentalItem:
    def __init__(self, name, rate_per_hour):
        self.name = name
        self.rate_per_hour = rate_per_hour

    def calculate_cost(self, hours):
        return self.rate_per_hour * hours

class RentalSystem:
    def __init__(self):
        self.items = [
            RentalItem("Sepeda", 5000),
            RentalItem("Skuter", 10000),
            RentalItem("Mobil", 50000)
        ]

    def display_items(self):
        print("Barang yang tersedia untuk disewa:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - Rp{item.rate_per_hour} per jam")

    def rent_item(self):
        self.display_items()

        try:
            choice = int(input("Pilih barang yang ingin disewa (1/2/3): "))
            if choice < 1 or choice > len(self.items):
                print("Pilihan tidak valid!")
                return

            item = self.items[choice - 1]
            hours = int(input(f"Berapa jam Anda ingin menyewa {item.name}? "))
            total_cost = item.calculate_cost(hours)
            print(f"Total biaya untuk menyewa {item.name} selama {hours} jam adalah: Rp{total_cost}")
        
        except ValueError:
            print("Input tidak valid, pastikan Anda memasukkan angka.")

def main():
    rental_system = RentalSystem()

    while True:
        print("\nSelamat datang di sistem rental!")
        print("1. Sewa barang")
        print("2. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            rental_system.rent_item()
        elif choice == '2':
            print("Terima kasih telah menggunakan sistem rental!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()