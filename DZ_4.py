class Worker:
    
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        
    def get_full_name(self):
        print(self.name + ' ' + self.surname)
    
    def get_total_income(self):
        print(self._income.get('wage') + self._income.get('bonus'), 'руб.')

worker = Position('Иван', 'Петорв', 'Инженер-конструктор', 85000, 10000)
print(worker.name, worker.surname, worker.position)
worker.get_full_name()
worker.get_total_income()
