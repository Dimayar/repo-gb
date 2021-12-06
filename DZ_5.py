from functools import reduce

sum_all = reduce(lambda x, y: x * y, [i for i in range(100, 1001, 2)])
print('Результат вычисления произведения всех элементов списка: ', sum_all)
