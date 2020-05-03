# Task 1
print('Task 1')
string = input('Пожалуйста, введите строку:')

# Выведите третий символ этой строки.
print('Третий символ строки:', string[2])

# Выведите предпоследний символ этой строки.
print('Предпоследний символ строки:', string[-2])

# Выведите первые пять символов этой строки.
print('Первые пять символов строки:', string[:5])

# Выведите всю строку, кроме последних двух символов.
length = len(string)
print('Строка, кроме последних двух символов:', string[: length - 2])

# Выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная
# с первого).
print('Все символы с четными индексами:', string[:: 2])

# Выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print('Все символы с нечетными индексами:', string[1:: 2])

# Выведите все символы в обратном порядке.
print('Все символы в обратном порядке:', string[:: -1])

# Выведите все символы строки через один в обратном порядке, начиная с последнего.
revert = string[:: -1]
print('Все символы строки через один в обратном порядке, начиная с последнего:', revert[:: 2])

# Выведите длину данной строки.
print('Длина данной строки:', length)
print()

# Task 2
# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения
# задачи функцию `count`
print('Task 2')
string_second = input('Пожалуйста, введите строку:')
number_of_spaces = string_second.count('  ')
number_of_tabs = string_second.count('\t')

while number_of_spaces >= 1 or number_of_tabs >= 1:
    print("Пожалуйста, разделяйте слова, используя только единичный пробел")
    string_second = input('Пожалуйста, введите строку:')
    number_of_spaces = string_second.count('  ')
    number_of_tabs = string_second.count('\t')

number_of_words = string_second.count(' ')
print('Количество слова в строке:', number_of_words + 1)
print()

# Task 3
# Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s` всех символов
# `ch`.Для решения можно использовать только функцию `find`(rfind), операторы  `if` и `for`(while).
print('Task 3')
s = input('Пожалуйста, введите строку:')
ch = input('Пожалуйста, введите символ, по которому необходимо выполнить поиск:')

found_symbol = s.find(ch)

if found_symbol == -1:
    print('Искомый символ отсутствует!')

while found_symbol >= 0:
    print('Индекс искомого символа в строке:', found_symbol)
    found_symbol = s.find(ch, found_symbol + 1)
print()

# Task 4
# Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.
print('Task 4')
initial_string = input('Введите строку, содержащую буквы "h":')
# print(initial_string)

if initial_string.count("h") == 0:
    print("Символы 'h' отсутствуют в строке!")

elif initial_string.count("h") <= 2:
    print(initial_string)

elif initial_string.count("h") > 2:
    first_value = initial_string.find('h')
    last_value = initial_string.rfind('h')

    first_part_of_string = initial_string[:first_value + 1]
    # print(first_part_of_string)

    middle_part_of_string = initial_string[first_value + 1:last_value]
    # print(middle_part_of_string)
    middle_part_of_string = middle_part_of_string.replace('h', 'H')
    # print(middle_part_of_string)

    last_part_of_string = initial_string[last_value:]
    # print(last_part_of_string)

    initial_string = first_part_of_string + middle_part_of_string + last_part_of_string
    print('Замененные символы появления буквы `h` на букву `H`, кроме первого и последнего вхождения:\n',initial_string)