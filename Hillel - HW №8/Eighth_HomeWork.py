# Task 1
# 3. Реверс списка
#   Принцип алгоритма заключается в следующем: мы меняем местами 0-ый элемент с последним, 1-ый с предпоследним и д.т.
#   Итого количество таких обменов будет равно половине длины списка. Иначе элементы поменяются местами по-второму кругу
# и вернутся в первоначальное положение.

from random import randint

print('Task №1')

def revert(array):
    last = len(array) - 1
    for first in range(len(array) // 2):
        array[first], array[last] = array[last], array[first]
        last -= 1

    return print(values)

values = [randint(10, 100) for _ in range(12)]
print(values)

revert(values)
print()

# Task 2
# 8. Написать функцию `XOR_cipher`, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
# которая возвращает строку, зашифрованную путем применения операции XOR (битовое исключающее ИЛИ)
# над символами строки с ключом. Написать также функцию `XOR_uncipher`, которая по зашифрованной строке и ключу
# восстанавливает исходную строку.
print('Task №2')

def XOR_cipher(string, key):
    if type(key) != int:
        key = ord(key)

    list_of_symbols = []

    for symbol in string:
        value = str(ord(symbol) ^ key)
        list_of_symbols.append(value)

    encrypted_string = ' '.join(list_of_symbols)

    return print(encrypted_string)

def XOR_uncipher(string, key):
    if type(key) != int:
        key = ord(key)

    list_of_encrypted_symbols = string.split(' ')
    list_of_decrypted_symbols = []

    for symbol in list_of_encrypted_symbols:
        value = str(chr((int(symbol) ^ key)))
        list_of_decrypted_symbols.append(value)

    decrypted_string = ''.join(list_of_decrypted_symbols)

    return print(decrypted_string)

XOR_cipher('I\'m working as a QA Engineer in a French IT Company', '+')

print()

XOR_uncipher('''8518 8559 8546 8574 8569 8568 8502 8507 8502 8514 8574 8563 8502 8532 8563 8549 8546 8503 8502 8543 8502 
8563 8568 8572 8569 8559 8502 8565 8569 8562 8575 8568 8561 8502 8569 8568 8502 8546 8574 8567 8546 8502 8550 8548 
8569 8561 8548 8567 8571 8502 8570 8567 8568 8561 8547 8567 8561 8563 8503 8502 8491 8511''', '№')

# XOR_uncipher('98 12 70 11 92 68 89 64 66 69 76 11 74 88 11 74 11 122 106 11 110 69 76 66 69 78 78 89 11 66 69 11 74 11 109 89 78 69 72 67 11 98 127 11 104 68 70 91 74 69 82', '+')
print()

# Task 3
# Написать функцию для перевода десятичного числа в другую систему исчисления (2-36)
print('Task №3')

def number_system(decimal_value, convert):
    list_of_values_to_convert = []
    initial_value = decimal_value
    dict_of_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H',
                       18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
                       26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X',
                       34: 'Y', 35: 'Z'}
    while initial_value * convert ** 2 > convert:
        result = initial_value - (initial_value // convert) * convert
        if result >= 10:
            result = dict_of_letters[result]
        list_of_values_to_convert.append(str(result))
        initial_value //= convert

    list_of_values_to_convert.reverse()
    return print(''.join(list_of_values_to_convert))

number_system(961,2)
print()

# Task 4
# Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
# параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
# параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
# направление сдвига (по умолчанию влево (False)).
print('Task №4')

def cyclic_shift(value, shift = 1, direction = False):
    if shift < 0 or shift > len(str(value)):
        return print('Сдвиг не может быть отрицательным и сдвиг не может превышать количество цифр в value')

    elif shift == len(str(value)) or shift == 0:
        return print(value)

    if direction == True:
        number_of_digits_to_shift = 10 ** shift
        first_part = str(value // number_of_digits_to_shift)
        second_part = str(value % number_of_digits_to_shift)

        return print(int(second_part + first_part))
    else:
        number_of_digits_to_shift = 10 ** (len(str(value)) - shift)
        first_part = str(value // number_of_digits_to_shift)
        second_part = str(value % number_of_digits_to_shift)

        return print(int(second_part + first_part))

cyclic_shift(5687412560587, 3, False)