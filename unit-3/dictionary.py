student = {'name':'John', 'age':27, 'address': 'Toronto', 'hobby': 'pie eating'}

'''
print(student)
print(type(student))

# dictionaries can be used for fast lookup
print(student['address'])
'''

# iterate over a dictionary
# key, value are just strings - could be anything

# .items() gives you both
# .values() gives you values
# .keys() gives you just keys 
'''
for key,value in student.items():
    print(key,value)
    print(value)
    print(key)

for val in student.values():
    print(val)

for key in student.keys():
    print(key)
    '''

students = [{'name':'John', 'age':27 }, {'name':'Sue', 'age':51 },{'name':'Jane', 'age':19 }]

#print(students)
# each thing -- is a dictionary 

for student in students:
    if student['age'] < 20:
        print(student['name'],'is less than 20')
        print(student)



