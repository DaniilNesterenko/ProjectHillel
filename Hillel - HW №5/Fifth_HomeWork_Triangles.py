# Figure A
print('Figure A')
print()
rows = int(input('Введите высоту треугольника:'))
# print(rows)

cols = rows * 2 - 1
# print(cols)

counter_1 = (rows - 1) + 1
counter_2 = (rows - 1) - 1

for i in range(rows):
    print()
    counter_1 -= 1
    counter_2 += 1
    for j in range(cols):
        if counter_1 == j or counter_2 == j or i == rows - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print()

# Figure B
print('Figure B')
print()
rows = int(input('Введите высоту треугольника:'))
# print(rows)

cols = rows * 2 - 1
# print(cols)

counter_1 = (rows - 1) + 1
counter_2 = (rows - 1) - 1

for i in range(rows):
    print()
    counter_1 -= 1
    counter_2 += 1
    for j in range(cols):
        if counter_1 == j or counter_2 == j or counter_1 < j < counter_2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print()

# Figure C
print('Figure C')
print()
rows = int(input('Введите высоту фигуры:'))

while rows % 2 == 0:

    print('Фигура должна иметь нечетное значение высоты')
    rows = int(input('Введите высоту фигуры:'))

# print(rows)
cols = rows + 2
# print(cols)
rows += 2
counter_1 = (rows // 2 - 1) + 1
counter_2 = (rows // 2 - 1) - 1

for i in range(rows // 2):
    print()
    counter_1 -= 1
    counter_2 += 1
    for j in range(cols):
        if counter_1 == j or counter_2 == j or counter_1 < j < counter_2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
for i in range(rows // 2, rows - 2):
    print()
    counter_1 += 1
    counter_2 -= 1
    for j in range(cols):
        if counter_1 == j or counter_2 == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print()


# Figure D
print('Figure D')
print()
rows = int(input('Введите высоту фигуры:'))

while rows % 2 == 0:
    print('Фигура должна иметь нечетное значение высоты')
    rows = int(input('Введите высоту фигуры:'))

# print(rows)
cols = rows + 2
# print(cols)
rows += 2
counter_1 = (rows // 2 - 1) + 1
counter_2 = (rows // 2 - 1) - 1

for i in range(rows // 2):
    print()
    counter_1 -= 1
    counter_2 += 1
    for j in range(cols):
        if counter_1 == j or counter_2 == j or counter_1 < j < counter_2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
for i in range(rows // 2, rows - 2):
    print()
    counter_1 += 1
    counter_2 -= 1
    for j in range(cols):
        if counter_1 == j or counter_2 == j or j == rows // 2 - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
print()