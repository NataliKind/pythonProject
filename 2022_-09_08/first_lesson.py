
print(500)
print(type(500))  # integer (int)
print(help(500))

a = 500
print(a)
a = a + 200
print(a)

a = 500 # integer (int) целое число
b = 12.497695 #float (float) дробное число
print(b)
print(type(b))
print(a + b)

c = "Hello world!"   # srting (str) строка

# print(c)
# print(type('1234'))
#
# print(с + a)

d = True  # boolean (bool)
d2 = False
e = None  # nonetype

print(type(d))
print(type(e))

user_name = 'Tysik'
print('Hello' + user_name)
print('*' * 20)

# арифметические операторы
print(500 / 200)  # обычное деление
print(500 // 200)  # деление с округлением до целого числа "в пол"

print(100 % 30)  # 30 * 3 + 10  #остаток при делении
print(2 ** 10)  #возвеение в степень 2 в 10 степени
print(16 * 0.5) # извелечение квадратного корня

# последовательность операций как в математике. сначала в скобках, потом остальное
print(((10 - 5) * (2 % 3)) ** 0.5)

# операторы присвоения
# № хочу увеличить а на 200

print(a)
a += 200
print(a)

print(c)
c += 'Tysik'

# конвертация чисел
asdas = 100
asdas = None

print(float(a))
print(int(b))

print(int(float('13123.343')))
print(int('131231343'))
print(int(True))
print(int(False))

print(float(True))
print(float(False))

# print(int(None))

# конвертация в строку
print(str(d))
print(type(str(d)))

print(bool(0))
print(bool(1467953))

print(bool(''))
print(bool(False))
print(bool(' ')) # ввели пробел между кавычками - получили true
print(bool(None))

print('Hello', end='888') # - параметр метода end=. print - метод
print()
print('Natalya')
print('Hello again')

# new_a = a + str(234) + str(True)

print(123, 23.034, True, None, 'Hello', sep='')






user_name = input('Please enter your name: ') # всегда возвращает строку метод input
print('Hello' + user_name)


# узнать площадь треугольника

side_a = float(input('Please enter side A: '))
side_b = float(input('Please enter side B: '))
side_c = float(input('Please enter side C: '))

half_perimeter = (side_a + side_b + side_c) / 2
print(half_perimeter)

triangle_area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) *
(half_perimeter - side_c)) ** 0.5

print(triangle_area)

