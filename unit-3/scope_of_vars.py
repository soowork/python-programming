# global scope
num = 10 
'''
def change_num(num):
    # function scope
    num += 5
    print(f'inside function num is {num}')
    
# integer are passed by value - ie we pass a copy to the function
change_num(num)

print(f'outside function num is {num}')
'''

# but if I return it it works as I want 
def change_num(num):
    # function scope
    num += 5
    print(f'inside function num is {num}')
    return num 
    
# integer are passed by value - ie we pass a copy to the function
num = change_num(num)

print(f'outside function num is {num}')

# ======================================

nums = [1,2,3,4,5]

def change_nums(vals):
    for index in range(len(vals) - 1 ):
        vals[index] += 5
    print(f'inside the function vals is {vals}')

# lists are passed-by-reference (complex, bigger, passed by reference to avoid using all the memory)
change_nums(nums)

print(f'outside the function vals is {nums}')