class Kereta:
    def __init__(self, nama_kereta, tujuan, waktu_berangkat, kapasitas):
        self.nama_kereta = nama_kereta
        self.tujuan = tujuan
        self.waktu_berangkat = waktu_berangkat
        self.kapasitas = kapasitas
        self.terisi = 0

    def tampilkan_info(self):
        print(f"Nama Kereta: {self.nama_kereta}")
        print(f"Tujuan: {self.tujuan}")
        print(f"Waktu Berangkat: {self.waktu_berangkat}")
        print(f"Kapasitas: {self.kapasitas}")
        print(f"Terisi: {self.terisi}/{self.kapasitas}")
        print("")

    def pesan_tiket(self, jumlah_tiket):
        if self.terisi + jumlah_tiket <= self.kapasitas:
            self.terisi += jumlah_tiket
            print(f"Berhasil memesan {jumlah_tiket} tiket untuk {self.nama_kereta}.")
        else:
            print(f"Maaf, hanya tersisa {self.kapasitas - self.terisi} tiket untuk {self.nama_kereta}.")

class SistemKereta:
    def __init__(self):
        self.kereta_list = []

    def tambah_kereta(self, kereta):
        self.kereta_list.append(kereta)

    def tampilkan_jadwal(self):
        print("Jadwal Kereta:")
        for kereta in self.kereta_list:
            kereta.tampilkan_info()

    def pesan_tiket_kereta(self, nama_kereta, jumlah_tiket):
        for kereta in self.kereta_list:
            if kereta.nama_kereta == nama_kereta:
                kereta.pesan_tiket(jumlah_tiket)
                return
        print(f"Kereta dengan nama {nama_kereta} tidak ditemukan.")

def main():
    sistem_kereta = SistemKereta()

    # Menambahkan kereta ke sistem
    kereta1 = Kereta("Ekspres Jakarta", "Bandung", "10:00", 100)
    kereta2 = Kereta("Argo Bromo", "Surabaya", "15:00", 150)
    kereta3 = Kereta("Kelas Ekonomi", "Yogyakarta", "12:00", 200)

    sistem_kereta.tambah_kereta(kereta1)
    sistem_kereta.tambah_kereta(kereta2)
    sistem_kereta.tambah_kereta(kereta3)

    while True:
        print("\nMenu:")
        print("1. Tampilkan Jadwal Kereta")
        print("2. Pesan Tiket Kereta")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            sistem_kereta.tampilkan_jadwal()
        elif pilihan == "2":
            nama_kereta = input("Masukkan nama kereta yang ingin dipesan: ")
            jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
            sistem_kereta.pesan_tiket_kereta(nama_kereta, jumlah_tiket)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem kereta.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()