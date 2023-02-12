def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-|-|-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-|-|-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def check_win(board):
    # Filas
    if board[0] == board[1] == board[2] != ' ':
        return True
    elif board[3] == board[4] == board[5] != ' ':
        return True
    elif board[6] == board[7] == board[8] != ' ':
        return True
    # Columnas
    elif board[0] == board[3] == board[6] != ' ':
        return True
    elif board[1] == board[4] == board[7] != ' ':
        return True
    elif board[2] == board[5] == board[8] != ' ':
        return True
    # Diagonales
    elif board[0] == board[4] == board[8] != ' ':
        return True
    elif board[2] == board[4] == board[6] != ' ':
        return True
    else:
        return False

def play_game():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 'X'
    while True:
        print(f"Turno del jugador {player}")
        display_board(board)
        move = int(input("Selecciona una posición (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = player
        else:
            print("Esa posición ya está ocupada. Selecciona otra.")
            continue
        if check_win(board):
            print(f"¡El jugador {player} ha ganado!")
            display_board(board)
            break
        if ' ' not in board:
            print("¡Empate!")
            display_board(board)
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

play_game()
