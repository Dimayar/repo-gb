class Car:
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def show_speed(self):
        return self.name, 'скорость:', self.speed
    
    def go(self):
        return  'машина', self.name, 'поехала'
    
    def stop(self):
        return  'машина', self.name, 'остановилась'
    
    def turn(self, i):
        if i == '<':
            return 'машина', self.name, 'повернула налево'
        elif i == '>':
            return 'машина', self.name, 'повернула направо'

class TownCar(Car):
    
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        print('Скорость', self.name, 'автомобиля:', self.speed)
        if self.speed > 60:
            return 'Скорость', self.name, 'превышена'

class WorkCar(Car):
    
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        print('Скорость', self.name, 'автомобиля:', self.speed)
        if self.speed > 40:
            return 'Скорость', self.name, 'превышена'
    
class SportCar(Car):
    
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
class PoliceCar(Car):
    
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
    def police(self):
        if self.is_police:
            return self.name,'Полиция'

citroen = TownCar(65, 'Серая', 'CITROEN', False)
bmw = SportCar(250, 'Голубая', 'BMW', False)
lada = WorkCar(100, 'Синяя', 'Лада', False)
honda = PoliceCar(120, 'Красная', 'HONDA', True)
print(citroen.go())
print(citroen.show_speed())
print(lada.turn('>'))
print(bmw.show_speed())
print(honda.police())
