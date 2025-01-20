import random

# Daftar kartu yang ada di dalam deck
deck = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
] * 4  # Empat set kartu untuk deck standar

# Fungsi untuk menghitung nilai kartu
def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11  # Untuk kesederhanaan, kita anggap Ace = 11, tidak memikirkan kemungkinan Ace = 1
    else:
        return int(card)

# Fungsi untuk membagikan kartu
def deal_card():
    card = random.choice(deck)
    deck.remove(card)  # Menghapus kartu yang sudah dibagikan dari deck
    return card

# Fungsi untuk menghitung nilai total kartu
def calculate_hand(hand):
    total = sum(card_value(card) for card in hand)
    return total

# Fungsi untuk bermain game sederhana
def start_game():
    print("Selamat datang di permainan Dealer Kartu!")

    # Membagikan dua kartu untuk pemain dan dealer
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Menampilkan kartu pemain dan satu kartu dealer
    print(f"Kartu Anda: {player_hand} dengan nilai {calculate_hand(player_hand)}")
    print(f"Kartu Dealer: {dealer_hand[0]} dan kartu tersembunyi")

    # Giliran pemain
    while calculate_hand(player_hand) < 21:
        action = input("Apakah Anda ingin 'Hit' atau 'Stand'? ").lower()
        if action == 'hit':
            player_hand.append(deal_card())
            print(f"Kartu Anda sekarang: {player_hand} dengan nilai {calculate_hand(player_hand)}")
        elif action == 'stand':
            break
        else:
            print("Pilihan tidak valid. Pilih 'Hit' atau 'Stand'.")

    # Cek apakah pemain melebihi 21
    if calculate_hand(player_hand) > 21:
        print(f"Nilai kartu Anda melebihi 21! Anda kalah!")
        return

    # Giliran dealer (dealer harus 'hit' sampai total nilai kartu >= 17)
    print(f"Kartu Dealer sekarang: {dealer_hand} dengan nilai {calculate_hand(dealer_hand)}")
    while calculate_hand(dealer_hand) < 17:
        print("Dealer memukul kartu...")
        dealer_hand.append(deal_card())
        print(f"Kartu Dealer sekarang: {dealer_hand} dengan nilai {calculate_hand(dealer_hand)}")

    # Tentukan pemenang
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    if dealer_total > 21:
        print("Dealer melebihi 21! Anda menang!")
    elif player_total > dealer_total:
        print("Anda menang!")
    elif player_total < dealer_total:
        print("Dealer menang!")
    else:
        print("Hasil seri!")

# Memulai permainan
start_game()