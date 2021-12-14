class Road:
    def __init__(self, _length, _width, kg, thickness):
        self._length = _length
        self._width = _width
        self.kg = kg
        self.thickness = thickness

    def result(self):
        return round(self._length * self._width * (self.kg / 1000) * self.thickness)


mas = Road(20, 5000, 25, 5)
print(f'Масса асфальта: {mas.result()} т.')