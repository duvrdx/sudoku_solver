class Table():
    # Size = N x N
    def __init__(self, n):
        self.size = n
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
    
    def get_size(self):
        return self.size

    def create_table(self):
        table = []

        for i in range(self.size):
            line = []
            for c in range(self.size):
                line.append(0)
            
            table.append(line)
        
        return table

    def resolve(self):
        # Algoritmo para resolução na vida real
        # 1 - Ver qual número falta em um grid N x N
        # 2 - Escolher uma posição vazia
        # 3 - Preposição 1: o número existe na mesma linha
        # 4 - Preposição 2: o número existe na mesma coluna
        # 5 - Caso não(Prep 1) e não(Prep 2): Coloca o número na posição, e repete o algoritmo
        # 6 - Caso não: escolhe outro número, e repete a partir do passo 3
        pass