class Vehicle:
    def __init__(self, model, price, stock):
        self.model = model
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Model: {self.model}, Harga: Rp{self.price}, Stok: {self.stock}")

    def update_stock(self, quantity):
        self.stock -= quantity
        if self.stock < 0:
            self.stock = 0

    def is_available(self, quantity):
        return self.stock >= quantity


class VehicleDealer:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, model, price, stock):
        vehicle = Vehicle(model, price, stock)
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        if not self.vehicles:
            print("Tidak ada kendaraan di diler.")
            return
        print("\nKendaraan yang Tersedia di Diler:")
        for idx, vehicle in enumerate(self.vehicles, 1):
            print(f"{idx}. ", end="")
            vehicle.display_info()

    def purchase_vehicle(self):
        self.display_vehicles()
        if not self.vehicles:
            return

        try:
            choice = int(input("\nPilih kendaraan (masukkan nomor): "))
            quantity = int(input("Berapa banyak yang ingin dibeli? "))
            
            selected_vehicle = self.vehicles[choice - 1]
            if selected_vehicle.is_available(quantity):
                total_price = selected_vehicle.price * quantity
                print(f"\nPembelian Sukses! Total Harga: Rp{total_price}")
                selected_vehicle.update_stock(quantity)
            else:
                print("\nStok tidak cukup.")
        except (ValueError, IndexError):
            print("\nPilihan tidak valid.")

def main():
    dealer = VehicleDealer()

    # Menambahkan beberapa kendaraan ke diler
    dealer.add_vehicle("Mobil Sedan", 300000000, 10)
    dealer.add_vehicle("Motor Sport", 100000000, 5)
    dealer.add_vehicle("Mobil SUV", 500000000, 3)

    while True:
        print("\n--- Menu Diler Kendaraan ---")
        print("1. Lihat kendaraan yang tersedia")
        print("2. Pembelian kendaraan")
        print("3. Keluar")
        
        try:
            choice = int(input("\nPilih menu: "))
            
            if choice == 1:
                dealer.display_vehicles()
            elif choice == 2:
                dealer.purchase_vehicle()
            elif choice == 3:
                print("Terima kasih telah mengunjungi diler kami!")
                break
            else:
                print("\nPilihan tidak valid.")
        except ValueError:
            print("\nMasukkan angka yang valid.")

if __name__ == "__main__":
    main()