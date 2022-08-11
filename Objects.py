from typing import Integer, List


class Table():
    # Size = N x N
    def __init__(self, n):
        self.size = n
        self.table = self.create_table()
    
    # Getters n' Setters
    def get_table(self) -> List:
        return self.table
    
    def get_positions(self, number) -> List:
        positions = []
        for pos_line, line in enumerate(self.table):
            for pos_item, item in enumerate(line):
                if item == number:
                    positions.append((pos_line, pos_item))
      
        return positions
    
    def get_number(self, position) -> Integer:
        return self.table[position[0]][position[1]]
    
    def get_size(self) -> Integer:
        return self.size

    def create_table(self) -> List:
        table = []

        for i in range(self.size):
            line = []
            for c in range(self.size):
                line.append(0)
            
            table.append(line)
        
        return table

    def resolve(self) -> None:
        # to do
        pass