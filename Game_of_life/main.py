from board import Board
import time


def main():
    user_rows = int(input("How many rows? "))
    user_columns = int(input("How many columns? "))

    game_of_life_board = Board(user_rows, user_columns)

    game_of_life_board.draw_board()

    while True:
        time.sleep(1 / 5)
        game_of_life_board.update_board()
        game_of_life_board.draw_board()

        alive_cells = game_of_life_board.count_alive_cells()
        generation = game_of_life_board.get_generation()

        print(f"Alive cells: {alive_cells}\nGeneration: {generation}")

        if alive_cells == 0:
            user_input = input("Restart? (y/n): ")
            if user_input == "y":
                game_of_life_board.restart()
            else:
                exit()


if __name__ == "__main__":
    main()
