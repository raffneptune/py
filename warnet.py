import time

class Komputer:
    def __init__(self, nomor):
        self.nomor = nomor
        self.tersedia = True
        self.mulai_sewa = None
        self.durasi_sewa = 0

    def sewa(self):
        if self.tersedia:
            self.tersedia = False
            self.mulai_sewa = time.time()  # mencatat waktu mulai sewa
            print(f"Komputer {self.nomor} telah disewa.")
        else:
            print(f"Komputer {self.nomor} sedang disewa.")

    def selesai_sewa(self):
        if not self.tersedia:
            waktu_sewa = time.time() - self.mulai_sewa  # menghitung durasi sewa dalam detik
            self.durasi_sewa = waktu_sewa / 60  # durasi dalam menit
            biaya = self.durasi_sewa * 2000  # biaya sewa per menit misalnya 2000 IDR
            self.tersedia = True
            self.mulai_sewa = None
            print(f"Komputer {self.nomor} selesai disewa. Durasi: {self.durasi_sewa:.2f} menit.")
            print(f"Biaya yang harus dibayar: Rp {biaya:.2f}")
        else:
            print(f"Komputer {self.nomor} belum disewa.")

class Warnet:
    def __init__(self, jumlah_komputer):
        self.komputers = [Komputer(i) for i in range(1, jumlah_komputer + 1)]

    def tampilkan_komputer(self):
        print("Daftar Komputer:")
        for komputer in self.komputers:
            status = "Tersedia" if komputer.tersedia else "Sedang disewa"
            print(f"Komputer {komputer.nomor}: {status}")

    def sewa_komputer(self, nomor):
        if 1 <= nomor <= len(self.komputers):
            self.komputers[nomor - 1].sewa()
        else:
            print("Nomor komputer tidak valid!")

    def selesai_komputer(self, nomor):
        if 1 <= nomor <= len(self.komputers):
            self.komputers[nomor - 1].selesai_sewa()
        else:
            print("Nomor komputer tidak valid!")

def menu():
    warnet = Warnet(5)  # Misalkan ada 5 komputer di warnet
    while True:
        print("\n--- Menu Warnet ---")
        print("1. Tampilkan Daftar Komputer")
        print("2. Sewa Komputer")
        print("3. Selesai Sewa Komputer")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            warnet.tampilkan_komputer()
        elif pilihan == "2":
            nomor_komputer = int(input("Masukkan nomor komputer yang ingin disewa: "))
            warnet.sewa_komputer(nomor_komputer)
        elif pilihan == "3":
            nomor_komputer = int(input("Masukkan nomor komputer yang selesai disewa: "))
            warnet.selesai_komputer(nomor_komputer)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan warnet!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()