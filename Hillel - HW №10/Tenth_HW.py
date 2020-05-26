from random import randint

def sort(array, sum):
    for k in range(len(sum) - 1):
        for l in range(len(sum) - 1 - k):
            if sum[l] > sum[l + 1]:
                sum[l], sum[l + 1] = sum[l + 1], sum[l]
                for m in range(len(array)):
                    array[m][l], array[m][l + 1] = array[m][l + 1], array[m][l]

    for counter in range(len(array)):
        if counter % 2 == 0:
            for o in range(len(array) - 1):
                for p in range(len(array) - 1 - o):
                    if array[p][counter] < array[p + 1][counter]:
                        array[p][counter], array[p + 1][counter] = array[p + 1][counter], array[p][counter]
        else:
            for o in range(len(array) - 1):
                for p in range(len(array) - 1 - o):
                    if array[p][counter] > array[p + 1][counter]:
                        array[p][counter], array[p + 1][counter] = array[p + 1][counter], array[p][counter]

    array.append(sum)


def display(list, cols):
    print('До сортировки:')

    for a in range(len(list)):
        for b in range(len(list)):
            print(list[a][b], end='\t')
        print()

    for u in range(len(cols)):
        print(cols[u], end='\t')

    print()

    sort(list, cols)
    print()

    print('После сортировки:')

    for a in range(len(list)):
        for b in range(len(list) - 1):
            print(list[a][b], end='\t')
        print()

M = int(input('Введите размер двухмерного массива MxM:'))
print()

lst = [[randint(1, 50) for i in range(M)] for j in range(M)]

sum_of_cols = [0 for _ in range(M)]

for x in range(len(lst)):
    for y in range(len(lst)):
        sum_of_cols[x] += lst[y][x]

display(lst, sum_of_cols)