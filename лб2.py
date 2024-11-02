from csv import reader
from random import randint

output = open('result.txt', 'w')

#строка > 30
count = 0
with open('books.csv', 'r') as csvfile:
    table  = reader(csvfile, delimiter=';')
    for row in table:
        if len(row[1]) > 30:
            count +=1
    print(f'Кол-во книг с названием длиннее 30 символов: {count}')
#поиск по автору
flag = 0
search  = input('Введите автора:')
with open('books.csv', 'r') as csvfile:
    table  = reader(csvfile, delimiter=';')
    for row in table:
        lower_case = row[4].lower()
        index = lower_case.find(search.lower())
        if index != -1:
            print(f'Автор: {row[3]} "{row[1]}"')
            flag +=1
    if flag == 0:
        print('Ничего не найдено :(')
    else:
        print(f'Найдено {flag} результатов.')
#генератор библиографических ссылок
with open('books.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    table1 = list(table)
    for i in range(20):
        index = randint(0, len(table1))
        print(f'{i+1}. {table1[index][3]}. {table1[index][1]}. Дата поступления: {table1[index][6]}')
        output.write(f'{i+1}. {table1[index][3]}. {table1[index][1]}. Дата поступления: {table1[index][6]}\n')

output.close()
