# Task №2
# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.

file_w = open('Eleventh_HomeWork_Result_Task_№2.py',  'w', encoding='utf-8')

while True:

    string = input('Введите текст:')

    if string == '':
        file_w.close()
        break

    file_w.write(string)
    file_w.write('\n')