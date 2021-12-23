class Warehouse:

    def __init__(self):
        self.__warehouse = {}
        self.__shop = {}
        self.date = date.today()

class OfficeEquipment:

    def __init__(self, name, quantity, price, serial_number, permission):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.serial_number = serial_number
        self.permission = permission

class Printer(OfficeEquipment):

    def __init__(self, name, quantity, price, serial_number, permission, print_speed, print_type):
        super().__init__(name, quantity, price, serial_number, permission)
        self.print_speed = print_speed
        self.print_type = print_type

class Scanner(OfficeEquipment):

    def __init__(self, name, quantity, price, serial_number, permission, sensor_type, scanner_type):
        super().__init__(name, quantity, price, serial_number, permission)
        self.sensor_type = sensor_type
        self.scanner_type = scanner_type

class Xerox(OfficeEquipment):

    def __init__(self, name, quantity, price, serial_number, permission, xerox_speed, scaling):
        super().__init__(name, quantity, price, serial_number, permission)
        self.xerox_speed = xerox_speed
        self.scaling = scaling

