# Fungsi untuk menampilkan papan permainan
def print_board(board):
    print("\n" + " | ".join(board[0:3]))
    print("-" * 5)
    print(" | ".join(board[3:6]))
    print("-" * 5)
    print(" | ".join(board[6:9]))
    print("\n")

# Fungsi untuk mengecek apakah pemain menang
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # baris
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # kolom
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Fungsi untuk mengecek apakah papan penuh
def is_board_full(board):
    return all(space != ' ' for space in board)

# Fungsi utama permainan
def play_game():
    board = [' ' for _ in range(9)]  # papan Tic Tac Toe kosong
    current_player = 'X'
    
    while True:
        print_board(board)
        
        # Meminta pemain untuk memilih posisi
        try:
            move = int(input(f"Player {current_player}, pilih posisi (1-9): ")) - 1
            if board[move] != ' ':
                print("Posisi sudah terisi, coba lagi.")
                continue
        except (ValueError, IndexError):
            print("Input tidak valid. Pilih angka antara 1-9.")
            continue
        
        # Menandai posisi dengan simbol pemain saat ini
        board[move] = current_player
        
        # Mengecek apakah pemain menang
        if check_win(board, current_player):
            print_board(board)
            print(f"Selamat! Pemain {current_player} menang!")
            break
        
        # Mengecek apakah papan penuh (seri)
        if is_board_full(board):
            print_board(board)
            print("Permainan berakhir dengan seri!")
            break
        
        # Ganti giliran pemain
        current_player = 'O' if current_player == 'X' else 'X'

# Memulai permainan
if __name__ == "__main__":
    play_game()