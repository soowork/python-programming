# use Try-Except to handle errors
val = 10 
guess = int(input('guess my secret number: '))

while guess != val:
    try:
        guess = int(input('guess my secret number (again): '))
    except:
        # an error happens
        print('you entered a bad value')



