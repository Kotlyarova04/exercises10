class RomanNumber:
    decimal_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,'L': 50, 'XL': 40,'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, number):
        if isinstance(number, int):
            if self.is_int(number):
                self.int_value = number
                self.rom_value = RomanNumber.roman_number(self)
            else:
                self.int_value = None
                self.rom_value = None
                print('ошибка')
        elif isinstance(number, str):
            if self.is_roman(number):
                self.rom_value = number
                self.int_value = RomanNumber.decimal_number(self)
            else:
                self.rom_value = None
                self.int_value = None
                print('ошибка')
        else:
            self.rom_value = None
            self.int_value = None
            print('ошибка')


    @staticmethod
    def is_int(value):
        if isinstance(value, int):
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
        ss = self.int_value
        if ss is not None:
            while ss > 0:
                for i, r in self.decimal_dict.items():
                    while ss >= r:
                        roman += i
                        ss -= r
            return roman

    def __add__(self, other):
        result = self.int_value + other.int_value
        return RomanNumber(result)

    def __iadd__(self, other):
        self.int_value += other.int_value
        return RomanNumber(self.int_value)

    def __sub__(self, other):
        result = self.int_value - other.int_value
        if self.is_int(result):
            return RomanNumber(result)
        else:
            self.int_value = None
            print('ошибка')

    def __isub__(self, other):
        self.int_value += other.int_value
        self.rom_value = self.roman_number()
        if self.is_int(self.int_value):
            return RomanNumber(self.int_value)
        else:
            self.int_value = None
            print('ошибка')

    def __mul__(self, other):
        result = self.int_value * other.int_value
        return RomanNumber(result)

    def __truediv__(self, other):
        result = self.int_value/other.int_value
        if str(result)[-1] == '0':
            result = int(result)
        return RomanNumber(result)

    def __mod__(self, other):
        result = self.int_value% other.int_value
        if self.is_int(result):
            return RomanNumber(result)
        else:
            self.int_value = None
            print('ошибка')

    def __floordiv__(self, other):
        result = self.int_value // other.int_value
        if self.is_int(result):
            return RomanNumber(result)
        else:
            self.int_value = None
            print('ошибка')
    def __pow__(self, other):
        result = self.int_value ** other.int_value
        if self.is_int(result):
            return RomanNumber(result)
        else:
            self.int_value = None
            print('ошибка')

    def __imul__(self, other):
        result = self.int_value
        result = result * other.int_value
        return RomanNumber(result)

    def __itruediv__(self, other):
        self.int_value /= other.int_value
        self.rom_value = self.roman_number()
        if self.is_int(self.int_value):
            return RomanNumber(self.int_value)
        else:
            self.int_value = None
            print('ошибка')

    def __ifloordiv__(self, other):
        if self.is_int(self.int_value):
            self.int_value //= other.int_value
            self.rom_value = self.roman_number()
            return RomanNumber(self.int_value)
        else:
            self.int_value = None
            print('ошибка')

    def __imod__(self, other):
        self.int_value %= other.int_value
        self.rom_value = self.roman_number()
        if self.is_int(self.int_value):
            return RomanNumber(self.int_value)
        else:
            self.int_value = None
            print('ошибка')

    def __repr__(self):
        return f'{self.rom_value}'


a = RomanNumber('XI')
b = RomanNumber('VII')
c = a + b
print(c)
d = RomanNumber('XII')
print(c - d)
e = RomanNumber('XXXIV')
f = e * a
print(f)
g = f / b
print(g.rom_value)
print(f / RomanNumber('II'))
print(f // b)
print(f % b)
print(RomanNumber('II') ** RomanNumber('X'))
a -= b
print(a)
b += RomanNumber('XX')
print(b)
b /= RomanNumber('III')
print(b)
b *= a
print(b)
b /= RomanNumber('X')
print(b)
e //= RomanNumber('X')
print(e)
e %= RomanNumber('II')
print(e)
