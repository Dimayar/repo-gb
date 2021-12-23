from datetime import date
from abc import ABC, abstractmethod

class Warehouse:

    def __init__(self):
        self.__warehouse = {}
        self.__shop = {}
        self.date = date.today()

    # Приём оргтехники на склад
    def to_warehouse(self, office_equipment):
        self.__warehouse.update({office_equipment.name: {'Количество': office_equipment.quantity,
        'Цена': office_equipment.price, 'Дата': self.date}})
        print(f'Получено на Склад магазина:  Модель - {office_equipment.name}, Количество - {office_equipment.quantity} шт, '
              f'Цена - {office_equipment.price} руб. Дата: {self.date}')

    # Приём оргтехники в магазин
    def in_subdivision(self, office_equipment):
        self.__shop.update({office_equipment.name: {'Количество': office_equipment.quantity,
                                                  'Цена': office_equipment.price, 'Дата': self.date}})
        print(f'Получено в Магазин:  Модель - {office_equipment.name}, Количество - {office_equipment.quantity} шт, '
              f'Цена - {office_equipment.price} руб. Дата: {self.date}')

class OfficeEquipment(ABC):

    def __init__(self, name, quantity, price, serial_number, permission):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.serial_number = serial_number
        self.permission = permission

    @abstractmethod
    def reception(self):
        pass

class Printer(OfficeEquipment):

    def __init__(self, name, quantity, price, serial_number, permission, print_speed, print_type):
        super().__init__(name, quantity, price, serial_number, permission)
        self.print_speed = print_speed
        self.print_type = print_type

    @property
    def reception(self):
        name = input('Введите модель принтера: ')
        while True:
            try:
                quantity = int(input('Введите количество: '))
            except ValueError:
                print("Вы ввели не число!")
            else:
                price = float(input('Введите цену: '))
                serial_number = input('Введите срийный №: ')
                permission = input('Введите разрешение: ')
                print_speed = int(input('Введите скорость печати: '))
                print_type = input('Введите тип принтера: ')
                print(f'Введенные данные: Модель: {name}, Количество: {quantity} шт, Цена: {price} руб, Серийный № {serial_number}, '
                    f'Разрешение: {permission} dpi, Скорость печати: {print_speed} л.м, Тип принтера: {print_type}')
                return Printer(name, quantity, price, serial_number, permission, print_speed, print_type)

class Scanner(OfficeEquipment):

    def __init__(self, name, quantity, price, serial_number, permission, sensor_type, scanner_type):
        super().__init__(name, quantity, price, serial_number, permission)
        self.sensor_type = sensor_type
        self.scanner_type = scanner_type

    @property
    def reception(self):
        name = input('Введите модель сканера: ')
        while True:
            try:
                quantity = int(input('Введите количество: '))
            except ValueError:
                print("Вы ввели не число!")
            else:
                price = float(input('Введите цену: '))
                serial_number = input('Введите срийный №: ')
                permission = input('Введите разрешение: ')
                sensor_type = input('Введите тип сенсора: ')
                scanner_type = input('Введите тип сканера: ')
                print(f'Модель: {name}, Количество: {quantity} шт, Цена: {price} руб, Серийный № {serial_number}, '
                    f'Разрешение: {permission} dpi, Тип сенсора: {sensor_type}, Тип сканера: {scanner_type}')
                return Printer(name, quantity, price, serial_number, permission, sensor_type, scanner_type)

class Xerox(OfficeEquipment):

    def __init__(self, name, quantity, price, serial_number, permission, xerox_speed, scaling):
        super().__init__(name, quantity, price, serial_number, permission)
        self.xerox_speed = xerox_speed
        self.scaling = scaling

    @property
    def reception(self):
        name = input('Введите модель ксерокса: ')
        while True:
            try:
                quantity = int(input('Введите количество: '))
            except ValueError:
                print("Вы ввели не число!")
            else:
                price = float(input('Введите цену: '))
                serial_number = input('Введите срийный №: ')
                permission = input('Введите разрешение: ')
                xerox_speed = int(input('Введите скорость печати: '))
                scaling = int(input('Введите увеличение: '))
                print(f'Модель: {name}, Количество: {quantity} шт, Цена: {price} руб, Серийный № {serial_number}, '
                    f'Разрешение: {permission} dpi, Скорость печати: {xerox_speed} л.м, Увеличение: {scaling}%')
                return Printer(name, quantity, price, serial_number, permission, xerox_speed, scaling)


printer = Printer('Canon PIXMA G5040', 6, 21990, 589647, '4800x1200', '13', 'Струйный')
scanner = Scanner('Fujitsu Fi-65F', 10, 31417, 296351, '600x600', 'CCD', 'Планшетный')
xerox = Xerox('Xerox', 12, 56200, 674235, '1200x1200', '40', '400')

warehouse = Warehouse()
warehouse.to_warehouse(printer.reception)
warehouse.to_warehouse(scanner.reception)
shop = Warehouse()
shop.in_subdivision(xerox.reception)