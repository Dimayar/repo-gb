class Stationery:
    
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        return f'Запуск отрисовки.'
    

class Pen(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
            return f'Запуск отрисовки {self.title}'

class Pencil(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        return f'Запуск отрисовки {self.title}'
    
class Handle(Stationery):
    
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        return f'Запуск отрисовки {self.title}'

pen = Pen('ручкой')
penсil = Pencil('карандашом')
handle = Handle('маркером')
print(pen.draw())
print(penсil.draw())
print(handle.draw())
