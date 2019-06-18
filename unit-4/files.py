'''
name_file = open('names.txt')

print(name_file.read())

# file must be closed after use

name_file.close()
# ======================================


# write to a file
# 'w' will overwrite everything that was there 
# so this knocked out the names
name_file = open('names.txt','w')

name_file.write('Hello world!')
name_file.write('apple juice is delicious')
name_file.write('Have a nice day')

name_file.close()

name_file = open('names.txt')

print(name_file.read())

name_file.close()
# ======================================

# write to a file -- but this time append 
name_file = open('names.txt','a')

name_file.write('Hello world!')
name_file.write('apple juice is delicious')
name_file.write('Have a nice day')

name_file.close()

name_file = open('names.txt')

print(name_file.read())

name_file.close()
# ======================================

# using with
with open('names.txt','r') as text_file:
    lines = text_file.readlines()

print(lines)

for index, item in enumerate(lines):
    # this gets the last character (\n is one character)
    if(lines[index][-1] == '\n'):
        # get from the start to the second to last one
        lines[index] = lines[index][0:-1]

print(lines)
'''
# ================================================

# using with
with open('names.txt','r') as text_file:
    lines = text_file.readlines()
print(lines)

for index, item in enumerate(lines):
    lines[index] = lines[index].strip()

print(lines)
