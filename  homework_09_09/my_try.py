# side_a = float(input('Please enter side A: '))
# side_b = float(input('Please enter side B: '))
# side_c = float(input('Please enter side C: '))

# half_perimeter = (side_a + side_b + side_c) / 2

# triangle_area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5

# print(triangle_area)
user_name = input('Enter your name ')
user_surname = input('Enter your surname ')
year_of_birth = int(input('Enter your year of birth '))

current_year = 2022
# year_of_birth = 1986

age = current_year - year_of_birth
print(age)

#code_2 parts

code_1 = '354'
code_3 = 132
#[code_2 = ?]

# code_2 data

x = 152
y = 132
code_2 = round((x % y * 13) ** 0.5)
print(code_2)

secret_code = code_1 + '-' + str(code_2) + '-' + str(code_3)
print(secret_code)



# user_name = 'John'
# user_surname = 'Smith'
print('Hello ' + user_name + ' ' + user_surname + '. You are ' + str(age) +
      ' years old.')
print('Your secret code ' + secret_code + '.')

