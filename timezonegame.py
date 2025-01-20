import random
import time

# Database pengguna
users = {}

def register_user():
    """Fungsi untuk mendaftar pengguna baru"""
    name = input("Masukkan nama pengguna: ")
    if name in users:
        print(f"Pengguna dengan nama {name} sudah terdaftar.")
    else:
        users[name] = {'kredit': 0, 'permainan': []}
        print(f"Selamat datang, {name}! Akun Anda telah dibuat.")

def buy_credits(user_name):
    """Fungsi untuk membeli kredit"""
    try:
        credit_amount = int(input("Berapa banyak kredit yang ingin Anda beli? (1 kredit = 5000 IDR): "))
        users[user_name]['kredit'] += credit_amount
        print(f"{credit_amount} kredit telah ditambahkan ke akun Anda.")
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka yang valid.")

def play_game(user_name):
    """Simulasi bermain game"""
    if users[user_name]['kredit'] < 1:
        print("Anda tidak memiliki kredit cukup untuk bermain game. Silakan beli kredit terlebih dahulu.")
        return

    print("Pilih permainan yang ingin dimainkan:")
    print("1. Pac-Man (1 kredit)")
    print("2. Street Fighter (2 kredit)")
    print("3. Racing Game (3 kredit)")
    
    try:
        game_choice = int(input("Masukkan nomor permainan: "))
        if game_choice == 1 and users[user_name]['kredit'] >= 1:
            users[user_name]['kredit'] -= 1
            print("Anda sedang bermain Pac-Man! Semoga berhasil!")
        elif game_choice == 2 and users[user_name]['kredit'] >= 2:
            users[user_name]['kredit'] -= 2
            print("Anda sedang bermain Street Fighter! Bertarunglah dengan kuat!")
        elif game_choice == 3 and users[user_name]['kredit'] >= 3:
            users[user_name]['kredit'] -= 3
            print("Anda sedang bermain Racing Game! Gaspol!")
        else:
            print("Anda tidak memiliki kredit cukup untuk memilih permainan ini.")
            return
    except ValueError:
        print("Input tidak valid. Mohon masukkan nomor permainan yang benar.")
        return

    # Simulasi hasil permainan (acak)
    print("Memulai permainan...")
    time.sleep(2)  # Menunggu 2 detik untuk efek
    game_result = random.choice(["Menang", "Kalah"])
    print(f"Hasil permainan: {game_result}")
    users[user_name]['permainan'].append(game_result)

def check_balance(user_name):
    """Fungsi untuk mengecek saldo kredit pengguna"""
    print(f"Sisa kredit Anda: {users[user_name]['kredit']} kredit.")

def main():
    print("Selamat datang di Timezone Mall!")
    while True:
        print("\nMenu Utama:")
        print("1. Daftar pengguna baru")
        print("2. Beli kredit")
        print("3. Mainkan game")
        print("4. Cek saldo kredit")
        print("5. Keluar")
        
        try:
            choice = int(input("Pilih menu (1/2/3/4/5): "))
            if choice == 1:
                register_user()
            elif choice == 2:
                user_name = input("Masukkan nama pengguna untuk membeli kredit: ")
                if user_name in users:
                    buy_credits(user_name)
                else:
                    print("Pengguna tidak ditemukan. Silakan mendaftar terlebih dahulu.")
            elif choice == 3:
                user_name = input("Masukkan nama pengguna untuk bermain game: ")
                if user_name in users:
                    play_game(user_name)
                else:
                    print("Pengguna tidak ditemukan. Silakan mendaftar terlebih dahulu.")
            elif choice == 4:
                user_name = input("Masukkan nama pengguna untuk cek saldo: ")
                if user_name in users:
                    check_balance(user_name)
                else:
                    print("Pengguna tidak ditemukan. Silakan mendaftar terlebih dahulu.")
            elif choice == 5:
                print("Terima kasih telah bermain di Timezone Mall! Sampai jumpa lagi!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Input tidak valid. Pilih menu dengan benar.")

if __name__ == "__main__":
    main()