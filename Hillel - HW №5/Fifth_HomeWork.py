# Task №1
# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей (слева и справа),
# и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно
# соседей.

print('Task №1', '\n')

from random import randint

l = []

list_length = int(input('Введите длину списка:'))

while list_length < 3:
    print('Длина списка не может быть меньше 3 значений. Пожалуйста, введите длину списка от 3 значений!')
    list_length = int(input('Введите длину списка:'))

for _ in range(list_length):
    a = randint(0, 256)
    l.append(a)

print(l)

value = 1

for i in l:
    if value == len(l) - 1:
        print()
        break
    if l[value] > l[value - 1] and l[value] > l[value + 1]:
        print(l[value], end=' ')
        value += 1
    else:
        value += 1
print()

# Task №2
# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это
# сделать.
# - Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека
# в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
# - Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как
# у Пети, то он должен встать после них.

print('Task №2', '\n')

pupil_height = [randint(150, 200) for _ in range(int(input('Введите количество учеников в классе без Пети:')))]

print('Список роста учеников не включая Петю:', pupil_height)

petya_height = int(input('Введите рост Пети в диапазоне от 150 см до 200 см:'))

while petya_height < 150 or petya_height > 200:
    print('Рост Пети должен быть в диапазоне от 150 см до 200 см')
    petya_height = int(input('Введите рост Пети в диапазоне от 150 см до 200 см:'))

print('Рост Пети:', petya_height, '\n')

pupil_height.append(petya_height)
print('Список роста учеников, включая рост Пети:', pupil_height, '\n')

pupil_height.sort(reverse=True)
# print(pupil_height)

pupil_height.reverse()
#print(pupil_height)

x = pupil_height.index(petya_height)
# print(x)

y = len(pupil_height)
# print(y)

position_in_order = y - x

pupil_height.reverse()
print('Список роста учеников в порядке убывания:', pupil_height, '\n')
print('Номер места в строю для Пети:', position_in_order)
print()

# Task №3
# 11. Дан список из чисел и индекс элемента в списке `k`. Удалите из списка элемент с индексом `k`, сдвинув влево все
# элементы, стоящие правее элемента с индексом `k`.
#     a). Программа получает на вход список, затем число `k`. Программа сдвигает все элементы, а после этого удаляет
#     последний элемент списка при помощи метода `pop()` без параметров.
#     b). Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
#     Также нельзя использовать дополнительный список.
#     c). Также не следует использовать метод `pop(k)` с параметром.
#     d). Использовать оператор del НЕЛЬЗЯ!

print('Task №3', '\n')

list_length_third = [randint(-1000, 1000) for _ in range(int(input('Введите длину списка:')))]
print(list_length_third)

k = int(input('Введите индекс элемента, который должен быть удален из списка:'))

while k >= len(list_length_third) or k <= -len(list_length_third) - 1:
    print('Индекс должен находиться в диапозоне заданного списка')
    k = int(input('Введите индекс элемента, который должен быть удален из списка:'))

list_length_third[k] = 't'

list_length_third.remove('t')
print(list_length_third)

list_length_third.pop()
print(list_length_third)