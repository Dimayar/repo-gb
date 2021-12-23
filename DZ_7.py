class Complex:

    def __init__(self, real, imag):
        self.number = complex(real, imag)

    def __str__(self):
        return (f'Результат: {self.number.real} + {self.number.imag}j')

    def __add__(self, other):
        return Complex((self.number.real + other.number.real), (self.number.imag + other.number.imag))

    def __mul__(self, other):
        return Complex(((self.number.real * other.number.real) - (self.number.imag * other.number.imag)), 
                        ((self.number.real * other.number.imag) + (self.number.imag * other.number.real)))


complex_1 = Complex(5, 6)
complex_2 = Complex(5, 6)


print(complex_1 + complex_2)
print(complex_1 * complex_2)
