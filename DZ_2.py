from abc import ABC, abstractmethod

class Clothes(ABC):
    
    def __init__(self, param):
        self.param = param

    @abstractmethod    
    def method(self):
        pass

class Coat(Clothes):
    
    @property
    def method(self):
        return f'Площадь ткани для пальто: {round(self.param / 6.5 + 0.5, 2)}'
        
class Costume(Clothes):
    
    @property
    def method(self):
        return f'Площадь ткани для пкостюма: {2 * self.param + 0.3}'
        
class Result:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
        
    @property
    def total(self):
        return f'Общий расход ткани: {round(self.param_1 / 6.5 + 0.5, 2) + (2 * self.param_2 + 0.3)}'


coat = Coat(51)
costume = Costume(1.82)
result = Result(51, 1.82)
print(coat.method)
print(costume.method)
print(result.total)
