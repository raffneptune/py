class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def __str__(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}"

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil ditambahkan.")

    def hapus_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul == judul:
                self.daftar_buku.remove(buku)
                print(f"Buku '{judul}' berhasil dihapus.")
                return
        print(f"Buku '{judul}' tidak ditemukan.")

    def tampilkan_buku(self):
        if len(self.daftar_buku) == 0:
            print("Tidak ada buku di perpustakaan.")
        else:
            print("Daftar Buku Perpustakaan:")
            for buku in self.daftar_buku:
                print(buku)

def menu():
    perpustakaan = Perpustakaan()

    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampilkan Daftar Buku")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            judul = input("Masukkan judul buku: ")
            penulis = input("Masukkan penulis buku: ")
            tahun_terbit = input("Masukkan tahun terbit buku: ")

            buku_baru = Buku(judul, penulis, tahun_terbit)
            perpustakaan.tambah_buku(buku_baru)

        elif pilihan == '2':
            judul = input("Masukkan judul buku yang akan dihapus: ")
            perpustakaan.hapus_buku(judul)

        elif pilihan == '3':
            perpustakaan.tampilkan_buku()

        elif pilihan == '4':
            print("Terima kasih! Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu()