class GerbangTol:
    def __init__(self):
        self.antrian = []

    def tambah_antrian(self, kendaraan):
        """Menambah kendaraan ke antrian"""
        self.antrian.append(kendaraan)
        print(f"{kendaraan} ditambahkan ke antrian.")

    def proses_kendaraan(self):
        """Memproses kendaraan yang ada di antrian"""
        if self.antrian:
            kendaraan = self.antrian.pop(0)
            print(f"{kendaraan} sedang diproses.")
        else:
            print("Antrian kosong, tidak ada kendaraan yang diproses.")

    def tampilkan_antrian(self):
        """Menampilkan antrian kendaraan"""
        print("Antrian kendaraan saat ini:")
        for kendaraan in self.antrian:
            print(kendaraan)

class SistemTol:
    def __init__(self):
        # Tarif untuk masing-masing golongan kendaraan
        self.tarif = {
            "golongan_1": 5000,  # Golongan 1 (misalnya motor atau mobil kecil)
            "golongan_2": 10000, # Golongan 2 (misalnya truk kecil)
            "golongan_3": 15000, # Golongan 3 (misalnya truk besar)
        }

    def hitung_biaya(self, golongan, jarak):
        """Menghitung biaya tol berdasarkan golongan kendaraan dan jarak"""
        if golongan in self.tarif:
            biaya = self.tarif[golongan] * jarak
            print(f"Biaya tol untuk {golongan} dengan jarak {jarak} km adalah: {biaya} IDR")
        else:
            print("Golongan kendaraan tidak valid!")

# Program utama
def main():
    # Inisialisasi sistem tol dan gerbang tol
    sistem_tol = SistemTol()
    gerbang_tol = GerbangTol()

    # Menambah kendaraan ke antrian
    gerbang_tol.tambah_antrian("Mobil Kecil - Golongan 1")
    gerbang_tol.tambah_antrian("Truk Kecil - Golongan 2")
    gerbang_tol.tambah_antrian("Truk Besar - Golongan 3")
    
    # Menampilkan antrian kendaraan
    gerbang_tol.tampilkan_antrian()

    # Proses kendaraan pertama
    gerbang_tol.proses_kendaraan()

    # Menghitung biaya tol untuk kendaraan di antrian
    sistem_tol.hitung_biaya("golongan_1", 10)  # Misalnya jarak 10 km

if __name__ == "__main__":
    main()