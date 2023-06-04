from cell import Cell
from random import randint

class Board:
    def __init__(self, rows, colums):
        self.rows = rows
        self.columns = colums
        self.grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]

        self._gererate_board()

    def draw_board(self):
        print('\n' * 10)
        print('printing board')
        
        for row in self.grid:
            for column in row:
                print(column.get_print_character, end='')
            print()
    
    def _gererate_board(self):
        for row in self.grid:
            for column in row:
                chance_number = randint(0, 2)
                if chance_number == 1:
                    column.set_alive()


# #initial generation based on randomness.
# def _generate_board(self):
# #draw the board in the terminal
# def draw_board(self):
# #update for the next generation of cells
# def update_board(self):
# #find all the neighbours of a cell
# def find_neighbour(self,row,column):