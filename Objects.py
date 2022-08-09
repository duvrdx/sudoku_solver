class Table():
    
    table = [[[None, None, None],[None, None, None],[None, None, None]],
             [[None, None, None],[None, None, None],[None, None, None]],
             [[None, None, None],[None, None, None],[None, None, None]],
             [[None, None, None],[None, None, None],[None, None, None]],
             [[None, None, None],[None, None, None],[None, None, None]],
             [[None, None, None],[None, None, None],[None, None, None]],
             [[None, None, None],[None, None, None],[None, None, None]],
             [[None, None, None],[None, None, None],[None, None, None]],
             [[None, None, None],[None, None, None],[None, None, None]]]
    solved = False

    def __init__(self):
        pass

    # position value was given in a tuple like
    # (grid, line, collum) -> (1, 2, 3)    
    def set_number(self, position, number):
        self.table[position[0]][position[1]][position[2]] = number
     
    def get_number(self, position):
        return self.table[position[0]][position[1]][position[2]]
    
    def get_positions(self, number):
        positions = []

        for pos_grid, grid in enumerate(self.table):
            for pos_line, lines in enumerate(grid):
                for pos_number, actual_number in enumerate(lines):
                    if number == actual_number:
                        positions.append((pos_grid, pos_line, pos_number))

        if positions != []:
            return positions

        return None


table = Table()
print(table.get_positions(None))