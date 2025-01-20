class Parkir:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.parkir = []

    def masuk_parkir(self, kendaraan):
        if len(self.parkir) < self.kapasitas:
            self.parkir.append(kendaraan)
            print(f"{kendaraan} berhasil masuk ke area parkir.")
        else:
            print("Parkir sudah penuh!")

    def keluar_parkir(self, kendaraan):
        if kendaraan in self.parkir:
            self.parkir.remove(kendaraan)
            print(f"{kendaraan} telah keluar dari area parkir.")
        else:
            print(f"{kendaraan} tidak ditemukan di parkir.")

    def status_parkir(self):
        if self.parkir:
            print("Kendaraan yang terparkir:")
            for kendaraan in self.parkir:
                print(kendaraan)
        else:
            print("Area parkir kosong.")

def main():
    kapasitas_parkir = int(input("Masukkan kapasitas parkir: "))
    parkir = Parkir(kapasitas_parkir)

    while True:
        print("\nPilih menu:")
        print("1. Masukkan kendaraan")
        print("2. Keluarkan kendaraan")
        print("3. Lihat status parkir")
        print("4. Keluar")
        
        pilihan = input("Pilihan Anda: ")
        
        if pilihan == '1':
            kendaraan = input("Masukkan nama kendaraan yang ingin parkir: ")
            parkir.masuk_parkir(kendaraan)
        elif pilihan == '2':
            kendaraan = input("Masukkan nama kendaraan yang ingin keluar: ")
            parkir.keluar_parkir(kendaraan)
        elif pilihan == '3':
            parkir.status_parkir()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem parkir!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()