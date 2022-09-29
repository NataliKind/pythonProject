
x = 5

student = {'name': 'Jack', 'age': 32, 'courses': ['Math', 'Art', 'Programming'],
           1: 'int_key', 0.2: 'float_key', x: 'variable', 'var_value': x, 'name2': 'Jack'}
print(student)

print(student['name'])

print(student.get('job', False))

print(student.get('courses')[0])

student['name'] = 'John'