# empty_list = []
# empty_list2 = () #этими способами можно создать пустой список
#
# print(bool(empty_list))
#

# world = 'world'
# filled_list = [1, 0.2, 'hello', [1, 2, [9, 8, 7, 6], 4, 5], world, True, None, True] #списки могут хранить в себе что угодно. всего элементов 8
# print(filled_list[3])
# print(type(filled_list[3]))

# courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'Literature']
# nums = [1, 5, 6, 8, 3, 4, 2]

#будем смотреть различные методы

# print(courses)
# courses.append('Art') #с помощью этого метода можно добавить в список элемент в конец списка
# print(courses)
# #courses.append(['Art', 'Biology'])
# courses.insert(1, 'Biology')

#метод добавления нескольких элементов списка
#courses.extend('hello')
# courses.extend(['Biology', 'Art'])

#как удалять
# courses.remove('Literature') #уаляет навсегда
# popped_item = courses.pop() #выкидываем по индексу( первый, последний или любой другой)
# courses.pop()
#
# print(courses)
#
# del courses[1]
# print(courses)

# методы сортировки

# courses.reverse()
# #print(course[::-1})
# courses.sort(reverse=True)
# nums.sort()
# print(nums)

# # не изменяет оригинал
# print(sorted(courses)) #возвращает список
# #print(reversed(courses))

#статистичексие методы
#
# print(min(courses))
# print(max(courses))
# print(sum(nums))

#метод для поиска чего-либо в списке
# print(courses.index('Literature'))
# print('13' in courses)
# lst_str = ', '.join(courses)
# print(lst_str)
# print(lst_str.split(', ')) #разбивает строку на список

# print(courses + nums)
# print(courses[0:2] + courses[-3:])

# courses2 = courses.copy()
# courses2[0] = 'Art'
# courses[1] = 'Biology'
# print(courses)
# print(courses2)
#
# print(courses)
# print()

# empty_tup = ()
# print(tipe(empty_tup))

# courses = ('History', 'Math', 'Literature', 'Physics', 'Programming', 'Literature')
# nums = (1, 5, 6, 8, 3, 4, 2)
#
# #print(courses.index('Math', 2, 5))
# print(courses.count('Literature'))
#
# print(list(courses))
#
# print(courses)
#
# print(courses + nums)

# courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Literature'}
# nums = {1, 5, 6, 8, 3, 4, 2}
#
# # empty_set = {1}
# # print(type(empty_set))
#
# a = courses.pop()
# print(a) #в случаййном порядке
#
# set1 = {'Math', 'History', 'Programming', 'Physics'}
# set2 = {'Math', 'Biololgy', 'Programming', 'Literature'}
#
# print(set2.intersection(set1))
#
# print(set1.difference(set2))
# print(set2.difference(set1))
#
# print(set1.union(set2))
# print(set1.update('Hello'))

#цикл FOR

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

test_lst = [[1, 2], [2, 3], [3, 4], [5, 6]]






#
# for num1 in numbers:
#         for num2 in numbers:
#             for num3 in numbers:
#                 for num4 in numbers:
#                     print(num1, num2, num3, num4)
# # odds = []
# evens = []
#
# for num in numbers:
#     if num % 2 == 1:
#         odds.append(num)
#     else:
#         evens.append(num)
#
# print(odds)
# print(evens)

