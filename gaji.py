def hitung_gaji_pokok(gaji_pokok, tunjangan, potongan):
    gaji_total = gaji_pokok + tunjangan - potongan
    return gaji_total

def main():
    print("Program Perhitungan Gaji Karyawan")
    
    # Input data
    gaji_pokok = float(input("Masukkan gaji pokok: Rp "))
    tunjangan = float(input("Masukkan tunjangan: Rp "))
    potongan = float(input("Masukkan potongan: Rp "))
    
    # Menghitung gaji total
    gaji_total = hitung_gaji_pokok(gaji_pokok, tunjangan, potongan)
    
    # Menampilkan hasil
    print("\nRingkasan Gaji:")
    print(f"Gaji Pokok: Rp {gaji_pokok}")
    print(f"Tunjangan: Rp {tunjangan}")
    print(f"Potongan: Rp {potongan}")
    print(f"Gaji Total: Rp {gaji_total}")

if __name__ == "__main__":
    main()