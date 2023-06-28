from board import Board
import time

def main():
    user_rows = int(input('How many rows? '))
    user_columns = int(input('How many columns? '))

    game_of_life_board = Board(user_rows, user_columns)

    game_of_life_board.draw_board()

    while True:
        time.sleep(1 / 10)
        game_of_life_board.update_board()
        game_of_life_board.draw_board()


if __name__ == '__main__':
    main()