
def main():
    # Pick the players
    # Define the board
    # Determine if someone has won
    # If not, show board and get a play

    players = ["Pedro", "Guerreiro"]
    symbols = ["X", "O"]
    board = define_board(7, 6)
    show_board(board)
    rounds = 0
    active_player = 0
    winner = None

    while not winner:
        get_play(players[active_player], symbols[active_player], board)
        if winning(board):
            winner = players[active_player]
            print(f'Congratulations {winner}! You won!')
            show_board(board)
            break
        rounds += 1
        active_player = rounds % 2
        show_board(board)
        # print(rounds, winner, winning(board))


def define_board(columns, rows):
    game_board = []

    for col_num in range(0, columns):
        row = []
        for row_num in range(0, rows):
            row.append(None)
        game_board.append(row)
    return game_board


def show_board(board):
    for a in range(len(board[0])-1, -1, -1):
        print('| ', end="")
        for b in range(len(board)):
            symbol = board[b][a]
            print(symbol if symbol is not None else " ", end=" | ")
        print()


def get_play(player, symbol, board):
    play_col = 100
    print(f"{player}, it's your turn!")
    while play_col < 0 or play_col > 6:
        play_col = int(input(f"Please select a valid column number (1-7): "))
        play_col -= 1
        # print(play_col)
        # print(len(board))
        if not 0 <= play_col <= len(board)-1:
            print("That column is out of bounds!")
            continue
        elif board[play_col].count(None) < 1:
            print("That column is already full!")
            play_col = 10
            continue

    free_row = 6 - board[play_col].count(None)
    board[play_col][free_row] = symbol


def winning(board):
    win_comb = []

    # Gathering columns
    for a in range(len(board)):
        for b in range(len(board[a])-3):
            win_comb.append(board[a][b: b+4])

    # Gathering rows
    for a in range(len(board[0])):
        for b in range(len(board)-3):
            win_comb.append(board[b][a: a+4])

    # Gathering diagonals
    for a in range(len(board)-3):
        for b in range(len(board[a])-3):
            win_comb.append([board[a][b], board[a+1][b+1], board[a+2][b+2], board[a+3][b+3]])
            win_comb.append([board[a][b+3], board[a+1][b+2], board[a+2][b+1], board[a+3][b]])

    for cells in win_comb:
        symbol = cells[0]
        if symbol is not None and all(symbol == uno for uno in cells):
            return True
        else:
            return False



if __name__ == '__main__':
    main()
