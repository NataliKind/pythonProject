# # #функциональное программирование
# #
# # def no_parameter():
# #     return 'Hello world!'#возвращает значение
# #
# # # print(no_parameter())
# #
# # def double(number):
# #     return number * 2
# #
# # print(double(123))
# #
# # def four_times(number):
# #     return double(double(number))
# #
# # print(four_times(10))
# #
# # def say_hello(name, surname):
# #     return f'Hello {name} {surname}!'
# #
# # print(say_hello(input('Enter name: '), input('Enter surname:')))
# #
# # def square_list(numbers):
# #     res = []
# #     for num in numbers:
# #         res.append(num ** 2)
# #     return res
# # print(square_list(square_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 20])))
#
#
# #область видимости
# #
# # def area(a, b):
# #     global c
# #     c = 20
# #     return a * b * c
#
#
# #возмоности функций
#
# # def tester(a, b, c=1):
# #      return (a + b) * c
# #
# #  print(tester(5, 3))
# #  print(tester(5, 3, 2))
# #
# # def tester(a, b):
# #     if a > b:
# #         return a - b
# #     return b - a
# #
# # print(tester(5, 2))
# # print(tester(2, 5))
# #
# # def fizz_buzz(start, end):
# #     for num in range(start, end):
# #         if num % 15 == 0:
# #             print(num, 'FizzBuzz')
# #         elif num % 5 == 0:
# #             print(num, 'Buzz')
# #         elif num % 3 == 0:
# #             print(num, 'Fizz')
# #
# #
#
# # def tester(a, b, c=1)
# #     return a + b + c
#
# def sum_numbers(*args):
#     print(args)
#     res = 0
#     for num in args:
#         res += num
#     return res
#
# # lst = [1, 2, 3, 4, 5, 6, 2, 132, 545]
# # # lst = {'name': 'Jack', 'surname': 'smith'}
# # print(sum_numbers(*lst))
#
# import my_functions
# from my_functions import *
#
# def tester2(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
# tester2(name='Jack', surname='Smith', age=34, salary=1000)
#
# tester2(**emp_dict)
#
#
#
#
#
#
#
#
#
#
