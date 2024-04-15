class RomanNumber:
    decimal_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_couple = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}

    def __init__(self, number):
        if self.is_roman(number):
            self.rom_value = number
        else:
            self.rom_value = 'ошибка'

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
        if self.rom_value == None:
            return 'ошибка'
        decimal_value = 0
        i = 0
        while i < len(self.rom_value):
            if i < len(self.rom_value) - 1 and self.rom_value[i:i + 2] in self.decimal_couple:
                decimal_value += self.decimal_couple[self.rom_value[i:i + 2]]
                i += 2
            else:
                decimal_value += self.decimal_dict[self.rom_value[i]]
                i += 1
        return decimal_value

    def __str__(self):
        return f'{self.rom_value}'



num_1 = RomanNumber('VI')
print(num_1.rom_value)
print(num_1.decimal_number())
print(num_1)
num_2 = RomanNumber('IIII')
print(num_2.rom_value)
num_3 = RomanNumber('DCCCXLI')
print(num_3.decimal_number())
num_4 = RomanNumber('QER2')
nums = []
nums.append(num_1)
nums.append(num_2)
nums.append(num_3)
nums.append(num_4)
print(nums)
print(RomanNumber.is_roman('MMMCMLXXXVI'))
print(RomanNumber.is_roman('MMMMLXXXVI'))
