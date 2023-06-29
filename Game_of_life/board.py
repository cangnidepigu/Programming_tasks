from cell import Cell
from random import randint

class Board:
    def __init__(self, rows, colums):
        self._rows = rows
        self._columns = colums
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]
        self._generation = 0
        
        self._gererate_board()

    def draw_board(self):
        print('\n' * 10)

        for row in self._grid:
            for column in row:
                print(column.get_print_character(), end='')
            print()

    def _gererate_board(self):
        for row in self._grid:
            if self._grid.index(row) > len(self._grid) / 2:
                for column in row:
                    if row.index(column) > len(row) / 2:
                        chance_number = randint(0, 2)
                        if chance_number == 1:
                            column.set_alive()

    def check_neighbour(self, check_row, check_columm):
        search_min = -1
        search_max = 2

        neighbour_list = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_columm + column

                valid_neighbour = True

                if neighbour_row == check_row and neighbour_column == check_columm:
                    valid_neighbour = False

                if neighbour_row < 0 or neighbour_row >= self._rows:
                    valid_neighbour = False

                if neighbour_column < 0 or neighbour_column >= self._columns:
                    valid_neighbour = False
        
                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])
        return neighbour_list

    def update_board(self):
        print('updating board')
        self._generation += 1

        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):

                check_neighbour = self.check_neighbour(row, column)

                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)
                
                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)
                
                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)
        
        print(f'Alive: {len(goes_alive)}')

        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()
    
    def count_alive_cells(self):
        return sum(1 for row in self._grid for column in row if column.is_alive())
    
    def get_generation(self):
        return self._generation
    
    def restart(self):
        self._generation = 0
        self.draw_board()