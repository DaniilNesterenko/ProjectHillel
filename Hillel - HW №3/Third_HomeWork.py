# Task 1

# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

# Например:
# 50      1 4 9 16 25 36 49
# 10      1 4 9
# 9       1 4 9
# 4       1 4
# 1       1
# 100     1 4 9 16 25 36 49 64 81 100
# 99      1 4 9 16 25 36 49 64 81
print('Task №1:')
n = int(input("Введите число n:"))
i = 1
print(n, end='\t')
while True:
    a = i ** 2
    if n < a:
        break
    print(a, end=' ')
    i +=1
print()

# Task 2

# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
# Выведите показатель степени и саму степень.
# Операцией возведения в степень, а так же функцией возведения в степень пользоваться НЕЛЬЗЯ!

# Например:
# 50          5 32            2 ** 5 = 32
# 10          3 8             2 ** 3 = 8
# 8           3 8             2 ** 3 = 8
# 7           2 4             2 ** 2 = 4
# 1           0 1             2 ** 0 = 1
# 2           1 2             2 ** 1 = 2
# 3           1 2             2 ** 1 = 2
# 4           2 4             2 ** 2 = 4
# 5           2 4             2 ** 2 = 4
# 100         6 64            2 ** 6 = 64
# 1025        10 1024         2 ** 10 = 1024
# 15431543    23 8388608      2 ** 23 = 8388608

print('Task №2:')
n = int(input("Введите натуральное число n:"))

while n <= 0:
    print("Введенное число не верно. Пожалуйста, введите число n >= 1")
    n = int(input("Введите натуральное число n:"))

if n == 1:
    c = 0
    a = 2 // 2
    print(n, '\t', c, a, '\t', '2 **', c, "=", a)

if n > 1:
    c = 1
    i = 1
    while True:
        a = 2 * i
        if n < 2 * (i*2):
            print(n, '\t', c, a, '\t', '2 **', c, "=", a)
            break
        i *= 2
        c += 1

# Task 3

# Программа запрашивает ввод последовательности целых чисел, пока не будет введён 0. Как только
# будет введён 0 (ноль), программа должна посчитать и вывести на экран:
# - количество введённых чисел (завершающий 0 не считается)
# - их сумму
# - среднее арифметическое (не считая завершающего числа 0)
# - определить максимальное и минимальное значение
# - определить количество чётных и не чётных элементов в последовательности

print('Task №3:')
input_number = int(input('Введите целое число:'))

input_number_count = 0
input_number_sum = 0
even_number_amount = 0
odd_number_amount = 0
maximum_value = input_number
minimum_value = input_number

while input_number != 0:

    if input_number > maximum_value:
        maximum_value = input_number
    elif input_number < minimum_value:
        minimum_value = input_number

    if input_number % 2 == 0:
        even_number_amount += 1
    else:
        odd_number_amount += 1

    input_number_count += 1
    input_number_sum += input_number

    input_number = int(input('Введите целое число:'))

print('Количество введных чисел:', input_number_count)
print('Сумма введных чисел:', input_number_sum)
print('Cреднее арифметическое введных чисел:', input_number_sum / input_number_count)
print('Количество четных введных чисел:', even_number_amount)
print('Количество не чётных введеных чисел:', odd_number_amount)
print('Максимальное значение:', maximum_value)
print('Минимальное значение:', minimum_value)