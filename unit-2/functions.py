# function with multiple arguments
def greeting(name, job, hobby):
    # note f'' (f-string) is not available before 3.6
    print(f'Hello {name} your job is {job} and you like {hobby}')

#greeting('Sue','DB developer', 'pool')

'''
# -- works
def reverse_list(my_list):
    reversed_list = []
    # iterate over the list in reverse order
    for i in range(len(my_list)-1,-1,-1):
        # add each element to the new list 
        reversed_list.append(my_list[i])
    # return the reversed list
    return reversed_list 

answer = reverse_list(['apple','banana','cookie','dog'])
print(answer)
# --------------------


# works --------------------------------------------
def is_palindrome(word):
    #check if word is the same forwards and backwards
    position = len(word)
    reversed_word = ''
    for i in range(position-1, -1, -1):
        reversed_word += word[i]
    #return True if it is, False otherwise
    if word == reversed_word:
        return True
    else:  
        return False

# False
print('chickensoup')
print('is palindrome? ',is_palindrome('chickensoup'))

# True
print('racecar')
print('is palindrome? ',is_palindrome('racecar'))

# ----------------------------------------------------
'''

def is_palindrome(word):
    #check if word is the same forwards and backwards

    start = 0 
    last = len(word)-1
    # this also works (but I dislike it because it seems unclear)
    # start, last = 0, len(word) - 1

    while start <= last:  
        if start == last:
            # only one character - palindrome by definition
            result = True
            break
        elif word[start] == word[last]:
            result = True
            # keep going
            start += 1
            last -= 1
        else:
            result = False
            break

    return result

print('racecar')
print('is palindrome? ',is_palindrome('racecar'))

print('boo')
print('is palindrome? ',is_palindrome('boo'))

print('C')
print('is palindrome? ',is_palindrome('C'))

