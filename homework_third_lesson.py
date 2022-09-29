string_1 = 'Hello bro'
print(string_1.replace('llo b', ''))
print(string_1[0:2] + string_1[-2:])

string_2 = 'jack Is My NAME'
#print(string_2.lower())
print(string_2.capitalize())

string_3 = "*Get rid of stars please*"
print(string_3.replace('*', '')) # удаляет/меняет смиволы где надо
print(string_3.strip('*')) #удаляет из начала символы

string_4 = "hello my name is jack"
print(string_4.capitalize().replace('jack', 'Jack'))

var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(var2.capitalize() + ', ' + var3.lower() + ' ' + var1.capitalize())

byte_string = b"\316\273"
print(byte_string.decode('utf8'))

# Write a code to return True if cost is greater than 500$
string_5 = "It cost me 1000.00$"
string_6 = string_5.replace('It cost me', '').replace('$', '')
price = float(string_6)
result = price > 500
print(result)

if float(string_5[-8:-1]) > 500:
    print('OK')
else:
    print('NOK')