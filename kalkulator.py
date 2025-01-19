# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa membagi dengan nol"

# Menu utama
def main():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    
    # Meminta input dari pengguna
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    
    if pilihan in ['1', '2', '3', '4']:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        
        if pilihan == '1':
            print(f"{num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"{num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"{num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"{num1} / {num2} = {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid!")

# Menjalankan program
if __name__ == "__main__":
    main()