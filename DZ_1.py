class Data:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Дата: {self.data}'

    @classmethod
    def number(cls, param):
        date = []
        for i in param.split('-'):
            date.append(int(i))
        (day, month, year) = date
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        if day > 0 and day <= 31:
            if month > 0 and month <= 12:
                if year > 0:
                    return f'Всё верно'
                else:
                    return f'Год неверный!'
            else:
                return f'Месяц неверный!'
        else:
            return f'День неверный!'


date = Data('01-12-2021')
d, m, y = date.number('01-12-2021')
print(date)
print(d, m, y)
print(date.validation(d, m, y))



