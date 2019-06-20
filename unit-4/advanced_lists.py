# list comprehension

nums = [1,2,4,5,9,11,16,18,22]

# create a new list with just the even numbers
new_nums = []
for num in nums:
    if num % 2 == 0:
        new_nums.append(num)

print('nums: ',nums)
print('newnums: ',new_nums)

# list comprehension
# [] means it will be a list 
# [ <result> <for loop>]
copy = [num for num in nums]
print('copy: ',copy)

square = [num*num for num in nums]
print('square: ',square)

# [ <RESULT> <LOOP> <CONDITION>]
evens = [num for num in nums if num % 2 == 0]
print('evens: ',evens)

# add in else
# create a new list with all fruits that have 4 letters
fruits = [ 'apple', 'kiwi', 'plum','banana', 'orange', 'pear', 'grapes']
four_letter_fruit = [ fruit for fruit in fruits if len(fruit)==4 ]

print('four_letter_fruit: ',four_letter_fruit)

# add in ELSE - list comprehension can only have an if and an else

# if num > 10, add 5, else subtract 5
# with an else [ <RESULT/CONDITION> <LOOP>]
modified = [num + 5 if num > 10 else num - 5 for num in nums]
print('modified: ',modified)

# there is also dictionary comprehension... figure that out 