import random

words = ['cat','superficial','organization','car','willow']
guess_limit = 3
guesses = 0 


object_word = words[random.randint(0,(len(words)-1))]
# shows this works
print(object_word)

dashes = ''

for i in range(0,len(object_word)):
    dashes += '-'

print(dashes)

'''
reversed_str = ""
position = len(input_string)

# works
# -----------------------------------
for i in range(0,position):
    reversed_str += input_string[position - ( i + 1 ):position-i]

print("input_string = " + input_string)
print("reversed = " + reversed_str)
'''


