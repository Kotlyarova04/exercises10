class RomanNumber:
    decimal_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                    'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, number):
        if isinstance(number, int):
            if self.is_int(number):
                self.int_value = number
                self.rom_value = RomanNumber.roman_number(self)
            else:
                self.int_value = None
                self.rom_value = None
                print('ошибка')
        else:
            if self.is_roman(number):
                self.rom_value = number
                self.int_value = RomanNumber.decimal_number(self)
            else:
                self.rom_value = None
                print('ошибка')

    @staticmethod
    def is_int(value):
        if 0 < value < 4000:
            return True
        else:
            return False

    @staticmethod
    def is_roman(value):
        count = 1
        for num in value:
            if num not in RomanNumber.decimal_dict:
                return False
        for i in range(len(value) - 1):
            if value[i] == value[i + 1]:
                count += 1
                if count > 3:
                    return False
            else:
                count = 1
        return True

    def decimal_number(self):
        decimal_value = 0
        i = 0
        if self.rom_value != None:
            while i < len(self.rom_value):
                if i < (len(self.rom_value) - 1) and self.rom_value[i:i + 2] in self.decimal_dict:
                    decimal_value += self.decimal_dict[self.rom_value[i:i + 2]]
                    i += 2
                else:
                    decimal_value += self.decimal_dict[self.rom_value[i]]
                    i += 1
            return decimal_value

    def roman_number(self):
        roman = ''
        ss = int(self.int_value)
        if ss is not None:
            while ss > 0:
                for i, r in self.decimal_dict.items():
                    while ss >= r:
                        roman += i
                        ss -= r
            return roman

    def __repr__(self):
        return f'{self.rom_value}'


num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))
