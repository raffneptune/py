# Program Absensi Sederhana

# Daftar nama siswa/pegawai
daftar_nama = ["Ali", "Budi", "Citra", "Dewi", "Eka"]

# Menyimpan data absensi
absensi = {}

# Fungsi untuk mencatat absensi
def catat_absensi():
    print("Daftar Nama:")
    for i, nama in enumerate(daftar_nama, 1):
        print(f"{i}. {nama}")

    for nama in daftar_nama:
        status = input(f"Apakah {nama} hadir? (y/n): ").strip().lower()
        if status == 'y':
            absensi[nama] = "Hadir"
        elif status == 'n':
            absensi[nama] = "Tidak Hadir"
        else:
            absensi[nama] = "Tidak Valid"
    
    print("\nAbsensi Hari Ini:")
    for nama, status in absensi.items():
        print(f"{nama}: {status}")

# Memulai pencatatan absensi
catat_absensi()