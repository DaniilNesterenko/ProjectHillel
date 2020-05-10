from random import randint
from pprint import pprint

# Set

# Task 1
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
print('SET / # Task 1')
print(len(set([randint(1, 400) for _ in range(100)])))
print()


# Task 2
# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
print('SET / # Task 2')
print(len(set([randint(1, 56) for y in range(100)]) & set([randint(1, 56) for x in range(100)])))
print()

# Dict

# Task 1
# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз
# оно встречалось в этом тексте. Задачу необходимо решить с использованием словаря.
print('Dict / # Task 1')
print()

# Строка вырвана из романа А.С. Пушкина "Капитанская дочка"

a = '«Вот я вас! — закричал Иван Кузмич. — Ребята! стреляй!» Солдаты наши дали залп. Казак, державший письмо, зашатался и свалился с лошади; другие поскакали назад. Я взглянул на Марью Ивановну. Пораженная видом окровавленной головы Юлая, оглушенная залпом, она казалась без памяти. Комендант подозвал капрала и велел ему взять лист из рук убитого казака. Капрал вышел в поле и возвратился, ведя под уздцы лошадь убитого. Он вручил коменданту письмо. Иван Кузмич прочел его про себя и разорвал потом в клочки. Между тем мятежники, видимо, приготовлялись к действию. Вскоре пули начали свистать около наших ушей, и несколько стрел воткнулись около нас в землю и в частокол. «Василиса Егоровна! — сказал комендант. — Здесь не бабье дело; уведи Машу; видишь: девка ни жива ни мертва».'

# В данном задании считаю необходим сделать максимальное преобразование строки. А именно:
# Сделать преобразование строки к низкому регистру, т.к. к примеру, слова 'Солдат' и 'солдат' будут восприняты Питоном
# как два разных слова. Без данного преобразование, будет идти не верный подсчет слов.

a = a.capitalize()

a = a.replace(a[0], a[0].lower())

print(a)
print()

# Далее считаю необходимым сделать очистку строки от лишних символов, а именно таких как " . , : ; — ! ? « » "
# Так же в коде ниже присутсвует очистка от "двойного пробела"
# Данная очистка необходима, т.к. к примеру, слова 'солдат,' и 'солдат' будут восприняты Питоном
# как два разных слова.

# Очистка строки отсимвола " . "
if a.find('.') >= 0:
    v = a.find('.')
    new_string_1 = a[:v]

    x = a.find('.')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('.', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " , "
if a.find(',') >= 0:
    v = a.find(',')
    new_string_1 = a[:v]

    x = a.find(',')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find(',', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " : "
if a.find(':') >= 0:
    v = a.find(':')
    new_string_1 = a[:v]

    x = a.find(':')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find(':', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " ! "
if a.find('!') >= 0:
    v = a.find('!')
    new_string_1 = a[:v]

    x = a.find('!')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('!', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " ? "
if a.find('?') >= 0:
    v = a.find('?')
    new_string_1 = a[:v]

    x = a.find('?')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('?', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " — "
if a.find('—') >= 0:
    v = a.find('—')
    new_string_1 = a[:v]

    x = a.find('—')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('—', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " ; "
if a.find(';') >= 0:
    v = a.find(';')
    new_string_1 = a[:v]

    x = a.find(';')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find(';', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " « "
if a.find('«') >= 0:
    v = a.find('«')
    new_string_1 = a[:v]

    x = a.find('«')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('«', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " » "
if a.find('»') >= 0:
    v = a.find('»')
    new_string_1 = a[:v]

    x = a.find('»')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('»', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка от двойного пробела "  "
if a.find('  ') >= 0:
    v = a.find('  ')
    new_string_1 = a[:v]

    x = a.find('  ')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('  ', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

print(a)
print()

list_from_string = a.split(' ')
# print(list_from_string)
# print(len(list_from_string))

dictionary = dict.fromkeys(list_from_string)
# print(dictionary)

for i in dictionary:
    dictionary[i] = 0

for j in list_from_string:
    if j in dictionary:
        dictionary[j] += 1
    else:
        continue
pprint(dictionary)
print()

# Task 2
# Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите последнее.
print('Dict / # Task 2')
print()

# Текст вырван из романа А.С. Пушкина "Капитанская дочка"

a = '''
Комендант, Иван Игнатьич и я мигом очутились за крепостным валом; но обробелый гарнизон не тронулся. 
«Что ж вы, детушки, стоите? — закричал Иван Кузмич. — Умирать так умирать: дело служивое!» 
В эту минуту мятежники набежали на нас и ворвались в крепость. 
Барабан умолк; гарнизон бросил ружья; меня сшибли было с ног, но я встал и вместе с мятежниками вошел в крепость. 
Комендант, раненный в голову, стоял в кучке злодеев, которые требовали от него ключей. 
Я бросился было к нему на помощь: несколько дюжих казаков схватили меня и связали кушаками, приговаривая: 
«Вот ужо вам будет, государевым ослушникам!» Нас потащили по улицам; жители выходили из домов с хлебом и солью. 
Раздавался колокольный звон. Вдруг закричали в толпе, что государь на площади ожидает пленных и принимает присягу. 
Народ повалил на площадь; нас погнали туда же.
'''

a = a.capitalize()

a = a.replace(a[0], a[0].lower())

print(a)

# В данном задании добавлена очистка от "\n" перехода на след. строку. Т.к. по заданию дану, что текст записан в
# несколько строк. Это необходимо для корректного подсчета слов.

# Очистка строки отсимвола " . "
if a.find('.') >= 0:
    v = a.find('.')
    new_string_1 = a[:v]

    x = a.find('.')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('.', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " , "
if a.find(',') >= 0:
    v = a.find(',')
    new_string_1 = a[:v]

    x = a.find(',')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find(',', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " : "
if a.find(':') >= 0:
    v = a.find(':')
    new_string_1 = a[:v]

    x = a.find(':')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find(':', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " ! "
if a.find('!') >= 0:
    v = a.find('!')
    new_string_1 = a[:v]

    x = a.find('!')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('!', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " ? "
if a.find('?') >= 0:
    v = a.find('?')
    new_string_1 = a[:v]

    x = a.find('?')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('?', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " — "
if a.find('—') >= 0:
    v = a.find('—')
    new_string_1 = a[:v]

    x = a.find('—')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('—', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " ; "
if a.find(';') >= 0:
    v = a.find(';')
    new_string_1 = a[:v]

    x = a.find(';')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find(';', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " « "
if a.find('«') >= 0:
    v = a.find('«')
    new_string_1 = a[:v]

    x = a.find('«')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('«', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка строки отсимвола " » "
if a.find('»') >= 0:
    v = a.find('»')
    new_string_1 = a[:v]

    x = a.find('»')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('»', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка от двойного пробела "  "
if a.find('  ') >= 0:
    v = a.find('  ')
    new_string_1 = a[:v]

    x = a.find('  ')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('  ', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

# Очистка от перехода на следующую строку " \n "
if a.find('\n') >= 0:
    v = a.find('\n')
    new_string_1 = a[:v]

    x = a.find('\n')
    new_string_2 = ''
    b = x

    while x >= 0:
        x = a.find('\n', x + 1)
        if x == -1:
            new_string_2 += a[b + 1:]
        else:
            new_string_2 += a[b + 1:x]
            b = x

    a = new_string_1 + new_string_2
    # print(a)

print(a)

list_from_string = a.split(' ')
# print(list_from_string)

dictionary = dict.fromkeys(list_from_string)
# print(dictionary)

for i in dictionary:
    dictionary[i] = 0

for j in list_from_string:
    if j in dictionary:
        dictionary[j] += 1
    else:
        continue
print(dictionary)

pprint(dictionary)

countable = 0

for z in dictionary:
    if dictionary[z] >= countable:
        word = z
        countable = dictionary[z]
    else:
        continue
# Благодаря условию >= , происходит вывод последнего слова в словаря, в случае, если есть несколько слов, с одинаковым
# колиеством повторений.

print('Слово, которое встречается чаще всего:', word, '\nПовторяемость слова в тексте:', countable)