for x in range(0, 101):
    print(x, end=' ')
    if x % 15 == 0:
        print('fizzbuzz', end='')
    elif x % 3 == 0:
        print('fizz', end='')
    elif x % 5 == 0:
        print('buzz', end='')
    print()
# ---------------------------------------

for x in range(0, 101):
    if x % 3 == 0:
        print(x, end=' ')
        print('fizz')
    if x % 5 == 0:
        print(x, end=' ')
        print('buzz')
    if x % 15 == 0:
        print(x, end=' ')
        print('fizzbuzz')

# ----------------------------------------------

fizz = []
buzz = []
fizzbuzz = []

for x in range(0, 101):
    if x % 15 == 0:
        fizzbuzz.append(x)
    elif x % 3 == 0:
        fizz.append(x)
    elif x % 5 == 0:
        buzz.append(x)
print('fizz:', fizz)
print('buzz', buzz)
print('fizzbuzz', fizzbuzz)