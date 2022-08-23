import imp
import os
import time
class Table():
    # Size = N x N
    def __init__(self):
        self.size = 9
        self.table = self.create_table()

    
    # Getters n' Setters
    def get_table(self):
        return self.table
    
    def get_positions(self, number):
        positions = []
        for pos_line, line in enumerate(self.table):
            for pos_item, item in enumerate(line):
                if item == number:
                    positions.append((pos_line, pos_item))
      
        return positions
    
    def get_number(self, position):
        return self.table[position[0]][position[1]]

    def set_number(self, position, number):
        self.table[position[0]][position[1]] = number

    # Methods
    def create_table(self):
        table = []

        for i in range(self.size):
            line = []
            for c in range(self.size):
                line.append(0)
            
            table.append(line)
        
        return table

    def table_to_string(self):
        string = ""
        for pl, line in enumerate(self.table):
            for pos, cell in enumerate(line):
                if (((pos + 1) % 3) == 0) and ((pos + 1) != 9):
                    string += f"{cell} | "
                else:
                    string += f"{cell} "
            if ((pl + 1) % 3) == 0 and ((pl + 1) != 9):
                string += "\n------X-------X------\n"
            else:
                string += "\n"

        return string

    def number_is_valid(self, r, c, k):
        not_in_row = k not in self.table[r]
        not_in_column = k not in [self.table[i][c] for i in range(0, self.size)]
        
        subgrid_rows_range = range(r//3*3, r//3*3+3)
        subgrid_cols_range = range(c//3*3, c//3*3+3)

        not_in_box = k not in [ self.table[i][j] for i in subgrid_rows_range for j in subgrid_cols_range] 

        return (not_in_row and not_in_column and not_in_box)

    def solve(self, r=0, c=0):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.table_to_string())
        if r == self.size:
            # Verificando se chegou na ultima linha
            return True
        elif c == self.size:
            # Verificando se chegou no ultimo item da coluna e descendo a linha
            return self.solve(r+1, 0)
        elif self.table[r][c] != 0:
            # Pulando celula caso já esteja preenchida
            return self.solve(r, c+1)
        else:
            # Testando todas as possibilidades de numero de 1 a 9
            for k in range(1, self.size + 1):
                if self.number_is_valid(r, c, k):
                    self.table[r][c] = k

                    if self.solve(r, c+1):
                        return True
                    self.table[r][c] = 0
            return False
        