# Task 1
# 1. Дан список случайных целых чисел. Замените все нечетные числа списка нулями. И выведете их количество
print('Task №1')

def odd(array):
    counter = 0
    for i in range(len(array)):
        if array[i] % 2 != 0:
            array[i] = 0
            counter += 1

    print('Список, после замены нечетных чисел - нулями:')
    print(array)
    print()
    print('Количество замененных чисел в списке:', counter)

from random import randint

lst = [randint(10, 1000) for _ in range(15)]
print(lst)
print()

odd(lst)
print()

# Task 2
# 2. Заполните список случайными числами и выполните реверс для части списка между элементами
# с индексами a и b (включая эти элементы)
print('Task №2')

def revert(array, a, b):
    first = a
    last = b
    for value in range(len(array[a:b + 1]) // 2):
        array[first], array[last] = array[last], array[first]
        first += 1
        last -= 1

    return print(values)

values = [randint(10, 100) for _ in range(18)]
print(values)

revert(values, 6, 9)
print()

# Task 3
# 3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
print('Task №3')

def square(side):
    perimeter = 4 * side
    square = side ** 2
    diagonal = 1.414 * side

    return print('Периметр:', perimeter, 'Площадь:', square, 'Диагональ квадрата:', diagonal)

square(75)
print()

# Task 4
# 4. Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое,
# и False - иначе.
print('Task №4')

def is_prime(integer):
    if integer == 0 or integer == 1:
        return print(False) #Числа "0" и "1" - не являются простыми числами, а относятся к другому классу чисел.
    countable = 0
    for value in range(1, integer // 2 + 1):
        if integer % value == 0:
            countable += 1
            if countable >= 2:
                return print(False)
    return print(True)


number = (randint(0, 1000))
print(number)
is_prime(number)