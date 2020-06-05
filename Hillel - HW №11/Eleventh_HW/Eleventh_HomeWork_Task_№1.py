file_r = open('Students.py', encoding='utf-8')
file_w = open('Eleventh_HomeWork_Result_Task_№1.py',  'w', encoding='utf-8')

print('Студенты, чей средний балл меньше 5:')

average_rating_over_class = 0
average_rating_over_class_counter = 0

while True:

    res = file_r.readline()
    if res == '':
        break

    if res.find('\n') != -1:
        length_of_string = len(res)
        res = res[: length_of_string - 1]

    temporary_list = res.split(' ')

    rating_total = 0
    rating_number = 0

    for value in temporary_list[2:]:
        rating_total += int(value)
        rating_number += 1

    average_rating = round(rating_total / rating_number, 2)

    average_rating_over_class += average_rating
    average_rating_over_class_counter += 1

    if average_rating <= 5:
        print(temporary_list[0], temporary_list[1], average_rating)


    final_string_1 = temporary_list[1] + ' ' + temporary_list[0][0] + '.'

    while len(final_string_1) != 20:
        final_string_1 += ' '

    final_string = final_string_1 + str(average_rating)

    file_w.write(final_string)
    file_w.write('\n')

file_r.close()
file_w.close()

print()
print('Средний балл по классу:', round(average_rating_over_class / average_rating_over_class_counter, 2))