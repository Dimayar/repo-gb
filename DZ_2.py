class DivisionNull:

    while True:
        try:
            numerator = int(input('Введите числитель: '))
            denominator = int(input('Введите знаменатель: '))
            result = numerator / denominator
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
        else:
            print(f"Результат: {result}")
            break
