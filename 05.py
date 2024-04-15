class RomanNumber:
    decimal_dict = {'M': 1000, 'D': 500, 'C': 100,'L': 50, 'X': 10, 'V': 5, 'I': 1}
    decimal_couple = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}

    def __init__(self, number):
        if self.is_int(number):
            self.int_value = number
        else:
            self.int_value = 'ошибка'

    @staticmethod
    def is_int(value):
        if 0 < int(value) < 4000:
                return True
        else:
            return False

    def roman_number(self):
        if self.int_value =='ошибка':
            return 'ошибка'
        roman = ''
        while self.int_value > 0:
            for num1, num2 in RomanNumber.decimal_dict.items():
                while self.int_value >= num2:
                    roman += num1
                    self.int_value -= num2
        return roman

    def __str__(self):
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