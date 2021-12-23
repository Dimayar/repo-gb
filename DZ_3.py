class ListNumber(Exception):

    my_list = []

    while True:
        try:
            text = input('Введите данные: ')
            if text == 'stop':
                print(f"Результат: {my_list}")
                break
            my_list.append(int(text))
            print(f"Введенные данные: {text}")
        except ValueError:
                print("Вы ввели не число!")
