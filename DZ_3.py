class Cell:
    
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(f'Результат: {self.cell}')
        
    def make_order(self, cell_count):
        while self.cell > 0:
            for el in range(cell_count):
                print('*', end ='')
                self.cell -= 1
                if self.cell <= 0:
                    break
            print()

    def __add__(self, arg):
        return Cell(self.cell + arg.cell)
    
    def __sub__(self, arg):
        if (self.cell - arg.cell) > 0:
            return Cell(self.cell - arg.cell)
        else:
            return f'Результат меньше 0'
    
    def __mul__(self, arg):
        return Cell(self.cell * arg.cell)
    
    def __truediv__(self, arg):
        return Cell(self.cell // arg.cell)

cell_1 = Cell(12)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
cell_1.make_order(5)
