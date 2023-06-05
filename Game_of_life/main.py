from board import Board

def main():
    user_rows = int(input('How many rows? '))
    user_columns = int(input('How many columns? '))

    game_of_life_board = Board(user_rows, user_columns)

    game_of_life_board.draw_board()

    user_action = ''
    while user_action != 'q':
        user_action = input('Press enten to add generation or q to quit: ')

        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()


if __name__ == '__main__':
    main()

# https://betterprogramming.pub/how-to-write-conwells-game-of-life-in-python-c6eca19c4676