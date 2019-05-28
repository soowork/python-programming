input_string = "the quick brown fox..."
#input_string = input("Please enter a word or phrase:")
reversed_str = ""
position = len(input_string)
'''
# works
# -----------------------------------
for i in range(0,position):
    reversed_str += input_string[position - ( i + 1 ):position-i]

print("input_string = " + input_string)
print("reversed = " + reversed_str)
# -------------------------------------

# also works - using range in a different way, and stepping through using -1
for i in range(position-1,-1,-1):
    reversed_str += input_string[i]

print("reversed = " + reversed_str)
print("input_string = " + input_string)
# ---------------------------------

# works
for elem in reversed(input_string):
    print(elem)
# ----------------------------------

'''

print("".join(reversed(input_string)))