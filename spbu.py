def display_menu():
    print("Selamat datang di SPBU!")
    print("Pilih jenis bahan bakar:")
    print("1. Premium (Rp 10.000 per liter)")
    print("2. Pertalite (Rp 12.000 per liter)")
    print("3. Pertamax (Rp 15.000 per liter)")

def calculate_total_price(fuel_type, liters):
    price_per_liter = 0
    if fuel_type == 1:
        price_per_liter = 10000  # Harga Premium
    elif fuel_type == 2:
        price_per_liter = 12000  # Harga Pertalite
    elif fuel_type == 3:
        price_per_liter = 15000  # Harga Pertamax

    total_price = price_per_liter * liters
    return total_price

def main():
    display_menu()
    
    # Input pilihan bahan bakar
    try:
        fuel_type = int(input("Masukkan pilihan (1/2/3): "))
        if fuel_type not in [1, 2, 3]:
            print("Pilihan tidak valid.")
            return
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return

    # Input jumlah liter yang ingin dibeli
    try:
        liters = float(input("Masukkan jumlah liter: "))
        if liters <= 0:
            print("Jumlah liter harus lebih dari 0.")
            return
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return

    # Menghitung total harga
    total_price = calculate_total_price(fuel_type, liters)
    
    # Menampilkan struk pembayaran
    fuel_names = {1: "Premium", 2: "Pertalite", 3: "Pertamax"}
    print("\n--- STRUK PEMBAYARAN ---")
    print(f"Bahan Bakar: {fuel_names[fuel_type]}")
    print(f"Jumlah Liter: {liters} liter")
    print(f"Total Pembayaran: Rp {total_price:,.0f}")
    print("-------------------------")
    print("Terima kasih telah menggunakan layanan kami!")

if __name__ == "__main__":
    main()