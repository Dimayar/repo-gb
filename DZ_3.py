class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

 #   def mass(self):
 #       return self._length * self._width

class Mass(Road):
    def __init__(self, _length, _width, kg, thickness):
        super().__init__(_length, _width)
        self.kg = kg
        self.thickness = thickness

    def result(self):
        return self._length * self._width * self.kg * self.thickness

mas = Mass(20, 5000, 25, 0.005)
print(f'Масса асфальта: {mas.result()}')
