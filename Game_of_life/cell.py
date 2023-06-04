class Cell:
    def __init__(self):
        self._status = 'Dead'

    def set_dead(self):
        self._status = 'Dead'

    def set_alive(self):
        self._status = 'Alive'

    def is_alive(self):
        return self._status == 'Alive'
    
    def get_print_character(self):
        if self.is_alive():
            return 'O'
        return '*'

# #set status to dead
# def set_dead(self):
# #set status to alive
# def set_alive(self):
# #is the cell alive?
# def is_alive(self):
# #what the board should print.
# def get_print_character(self):