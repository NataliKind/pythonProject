# # #строки как отдельный тип данных
# #
# # string_sample1 = 'Hello world world'
# #                 #0123456789 отсчет начинается всегда с нуля. то есть,
# #                 #символов на самом деле 16, но при счете с 0 - будет 17
# #                 # -7-6-5-4-3-2-1 с конца берем срез
# # string_sample2 = 'first letteR is loWerCase'
# # string_sample3 = ' extra writespace string '
# # german_sample = 'der Fluß'
# #
# # #проверить длинну строки метод len(3462376583765)
# #
# # len('4365276527')
# # print(len('4365276527'))
# # print(len(string_sample1))
# # print(len(string_sample1[len(string_sample1) - 1]))
# # print(string_sample1[0:4]) #хотим сделать из массива выбрать данные. от 0 до 4 не включая 4
# # print(string_sample1[-5:-1]) #взять диапазон с конца. не включая -1. чтобы взять весть диапазон включая все символы - надо не указывать ничего
# # print(string_sample1[-5:])
# # print(string_sample1[:]) # [start : end]
# # print(string_sample1[0:10:2])
# # print(string_sample1[::-1]) #с шагом -1
# #
# # print(string_sample1)
# #
# # print(string_sample1[1]) #индексация строк
# #
# #
# # # целый арсенал для работы со строками. один из методов заглавные буквы и прописные - не одно и тоже.
# # # == - оператор сравнения
# #
# # print('A' == 'a')
# # print('A' > '1')
# # print('a' > '1')
# #
# # print(string_sample1.upper()) # это всё тип данных строка
# # print('srgugiuwhgwj'.upper())
# # print(string_sample1)
# #
# # # print(german_sample.upper())
# # # print(string_sample1.isupper()) #вернет true если строка в верхем регистра
# # #
# # # print('jfhkrghjrshgsA'.islower())
# # # print(german_sample.lower())
# # # print(german_sample.casefold()) #конвертация в альтернативный вид символов, которые имеют
# # #
# # # print(string_sample2.capitalize())
# # # print(string_sample2.title())
# # # print(string_sample2.istitle())
# # #
# # # print(string_sample3.strip(*))
# #
# # #может принимать аргументы, только в начале и в конце строки
# #
# #
# # #замена и удаление некоторых знакчений 'replace'
# #
# #
# # print(string_sample1.replace('world', 'planet', 1))
# #
# #
# #
# # #print(split())
# #
# # a, b, c = string_sample1.split()
# #
# #
# # print(string_sample1.count('world', 9, 15))
# #
# # print(string_sample1.find('world', 7)) #находим один раз слово которое встречается
# #
# # print('world' in string_sample1)
#
#
# salary = 2000
# sample_string = 'Johns salary is {1}, {2}, {0}' #метод формат
# print(sample_string.format(salary, 'one', 'two'))
#
# price_string = 'This {product:} costs {price:.2f} USD'
# print(price_string.format(product='computer', price=1231))
#
#
#
# name = 'Jack'
# surname = 'Smith'
# age = 20
#
# print(f'Hello {name} {surname}. You are {age} years old! Your {salary:.2f} EUR.')
#
# print('That\'s it')
# print(len('That\'s it'))
#
# print('Hello\nworld')
# print(r) #игнорирование всех способов форматирования
#

x = 9

if 10 > x > 2:
    print('YES')

if x > 3 and x < 10:
    print('YES')

if x > 3 or x < 10:
    print('YES')

if x > 3 and not x < 10:
    print('YES')

x = input('Enter name: ')
if x:
    print('Hello ' + x)

# x = 38803160272
#
# if len(x) == 11:
#     print(x)
# elif len(x) != 11:
#     if len(x) > 11:
#         print(x, 'is too long')
#     else:
#         print(x, 'is too short')
#     print('Try again!')
#
# # if x == 6:
#     print('x is 5')
# elif x != 100:
#     print('X is not 100')
# else:
#     print('All conditions are False!')
#
















