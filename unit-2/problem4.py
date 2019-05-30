'''
calculation = input("what calculation would you like to do (add, sub, mult, div)? ")
num1 = int(input("what is number 1? "))
num2 = int(input("what is number 2? "))
result = 0 


# works
if calculation == "add":
    result = num1 + num2
elif calculation == "sub":
    result = num1 - num2
elif calculation == "mult":
    result = num1 * num2 
elif calculation == "div":
    result = num1 / num2
else:
    print("I did not understand your calculation choice!")
    result = "n/a"

print("result is =", result)
# ----------------------------------


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def div(a,b):
    return a / b

def mult(a,b):
    return a * b


if calculation == "add":
    print(add(num1,num2))
elif calculation == "sub":
    print(sub(num1,num2))
elif calculation == "mult":
    print(mult(num1,num2))
elif calculation == "div":
    print(div(num1,num2))
else:
    print("I did not understand your calculation choice!")

'''

# function with single argument
def print_msg(message):
    print(message)

# print_msg('It is only Wednesday!')

# functions that return a result
def square(val):
    return val * val

#print(square(5))
# -----------------------

def square2(val):
    result = val * val
    return result

answer = square2(10)
print(answer)
