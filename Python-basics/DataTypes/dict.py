student = { 'name': 'arun' , 'age': 30, 'cources': ['math', 'english']}
# student['phone'] = '807783892902'
# print(type(student))
# print(student)
# print(student['name'])
# print(student.get('name'))
# print(student.get('invalidkey'))  ## It will give None as output
# print(student.get('invalidkey', 'Not found')) ## It will give 'Not found' as output

# type_op = print(student.get('phone', 'Not found')) ## It will give 'Not found' as output
# print(type(type_op))

# print(student.update({ 'name': 'abidf' , 'age': 78 })) ## It will returt None

# # correct way
# student.update({ 'name': 'abidf' , 'age': 78 }) ## It will returt None
# print(student)

# # del student['name']
# # print(student)

# print(student.pop('age'))
# print(student)

# print(len(student))

# print(student.keys())
# print(student.values())
# print(student.items())

for keysss in student: ## It will print only keys in the dict 
    print(keysss)

for keysss in student.items(): ## It will print only key and valude pair in the dict 
    print(keysss)

for keysss, valuess in student.items(): ## ## It will print only key and valude pair in the dict in different format
    print(keysss, valuess)