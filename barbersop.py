import time

class Barbershop:
    def __init__(self):
        self.queue = []  # Antrian pelanggan
        self.is_open = True  # Status barbershop
    
    def buka_barbershop(self):
        print("Barbershop sedang buka, silakan masuk!")
    
    def tutup_barbershop(self):
        self.is_open = False
        print("Barbershop sudah tutup. Terima kasih sudah datang!")
    
    def tambah_pelanggan(self, nama):
        if self.is_open:
            self.queue.append(nama)
            print(f"{nama} telah masuk ke antrian.")
        else:
            print("Barbershop sudah tutup. Anda tidak bisa mendaftar.")
    
    def proses_pelanggan(self):
        if self.queue:
            pelanggan = self.queue.pop(0)
            print(f"Sedang melayani {pelanggan}...")
            time.sleep(2)  # Simulasi waktu pemotongan rambut
            print(f"{pelanggan} telah selesai dilayani.")
        else:
            print("Tidak ada pelanggan di antrian.")
    
    def tampilkan_antrian(self):
        if self.queue:
            print("Antrian pelanggan:")
            for i, pelanggan in enumerate(self.queue, start=1):
                print(f"{i}. {pelanggan}")
        else:
            print("Tidak ada pelanggan di antrian.")
    
def main():
    barbershop = Barbershop()
    barbershop.buka_barbershop()
    
    while True:
        print("\n--- Menu ---")
        print("1. Tambah Pelanggan")
        print("2. Proses Pelanggan")
        print("3. Lihat Antrian")
        print("4. Tutup Barbershop")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama pelanggan: ")
            barbershop.tambah_pelanggan(nama)
        
        elif pilihan == '2':
            barbershop.proses_pelanggan()
        
        elif pilihan == '3':
            barbershop.tampilkan_antrian()
        
        elif pilihan == '4':
            barbershop.tutup_barbershop()
            break
        
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini!")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()