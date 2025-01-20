# Daftar film yang tersedia di bioskop
films = {
    1: {"judul": "Film A", "harga": 50000},
    2: {"judul": "Film B", "harga": 60000},
    3: {"judul": "Film C", "harga": 70000},
    4: {"judul": "Film D", "harga": 55000}
}

def show_films():
    print("Daftar Film yang Tersedia:")
    for key, value in films.items():
        print(f"{key}. {value['judul']} - Harga: Rp {value['harga']}")

def pilih_film():
    while True:
        try:
            pilihan = int(input("\nPilih film (1-4): "))
            if pilihan in films:
                return pilihan
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

def beli_tiket():
    show_films()
    pilihan = pilih_film()
    jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
    
    film_terpilih = films[pilihan]
    total_harga = film_terpilih["harga"] * jumlah_tiket
    
    print(f"\nTiket untuk film {film_terpilih['judul']} ({jumlah_tiket} tiket) berhasil dipesan.")
    print(f"Total harga: Rp {total_harga}")
    
    lagi = input("\nApakah Anda ingin membeli tiket lagi? (ya/tidak): ").strip().lower()
    if lagi == 'ya':
        beli_tiket()
    else:
        print("Terima kasih telah membeli tiket di bioskop kami!")

# Mulai program
beli_tiket()