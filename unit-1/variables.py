def main():
    first_name = 'Sue'
    last_name = 'Work'
    full_name = first_name + ' ' + last_name

    print(full_name)

    # boolean variables
    has_child = True


def conditionals(grade):
    # given a range of grades from 0-100
    # if grade is between 80-100 print 'A'
    # if grade is between 60-79 print 'B'
    # if grade is between 50-59 print 'C'
    # if grade is 0-49 print 'F'
    if grade >= 80:
        print('A')
    elif grade >= 60:
        print('B') 
    elif grade >= 50:
        print('C')
    else:
        print('F')

def fizzbuzz():
    '''
    for the numbers 1 to 50 
    print 'fizz' if the number is a multiple of 3
    print 'buzz' if the number is a multiple of 5
    print 'fizzbuzz' if the number is a multiple of 15
    '''
    
    '''
    for i in range(1,51):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i) 
    '''

    # in this case we will never get fizzbuzz - because
    # it will be true for buzz 
    for i in range(1,51):
        if i % 5 == 0:
            print('buzz')
        elif i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)             



if __name__ == '__main__':
    fizzbuzz()





















